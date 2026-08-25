# SECCIÓN (a) v4 — CAPACIDADES, EQUIPOS, PAQUETES Y ESTADO

Rediseño del kernel ADS. Reescritura tras las correcciones del Owner sobre v3
(C1-C4 y correcciones 1-10). v3 conservada como superada.
Estado: **pendiente de aprobación**. No pasar a la sección (b) sin ella.

---

## a.0 — Tres niveles

```text
CATÁLOGO DE CAPACIDADES     qué sabe hacer una organización ADS
(kernel + packs + profile)  14 base, extensible. No es un recorrido.
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
**APR no es un trámite universal.** El cierre de un item ejecuta una comprobación
-`learning_candidate: none | <enlace>`- que **NO** requiere crear un paquete APR. APR se
materializa y recibe paquete cuando existe **señal real**: un aprendizaje candidato, un
incidente, una revisión de circuito o una promoción. Una entrada forzada contamina el
ledger con falsa autoridad (G52). *Dónde se ejecuta esa comprobación se decide en (b).*

### Servicios — se consultan sin tomar custodia del paquete que consultan

| | capacidad | nota |
|---|---|---|
| **INV** | Investigación y evidencia | spikes contra entorno real, freshness (G22+G33). Puede declarar que una decisión **no puede tomarse todavía** |
| **DOM** | Dominio y datos | modelo, vocabulario, contratos, reversibilidad de esquemas. **Veto** sobre lo que rompa el modelo o la recuperabilidad |
| **SEG** | Seguridad y privacidad | G27 + G28 + cumplimiento declarado. **Veto duro**, no negociable |
| **PLT** | Plataforma | build, CI, entornos, tooling, observabilidad, aislamiento multiagente. Cola y backlog propios |

### Dos modos de participación, no dos clases de capacidad

"Estación" y "servicio" describen el **modo habitual** de una capacidad, no una frontera
ontológica inmutable. Cualquier capacidad opera en dos modos, **sin duplicarse en el
catálogo**:

```text
MODO consulta        aporta resultado sin custodiar el paquete principal.
                     Varias consultas corren en paralelo sobre el mismo paquete.
MODO trabajo propio  recibe un paquete hijo sustantivo, CON custodia, gate, estado
                     y checkpoint propios. Un spike de INV o una migración de
                     contratos de DOM viven aquí.
```

El modo lo fija DSP al crear el paquete y queda declarado en él.

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

## a.4 — Materialización, extensión y retirada

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

### El catálogo es extensible

Las 14 son el **catálogo base**, no un catálogo universal cerrado. *"Reusable"* no puede
acabar significando *"sólo sirve para los tipos de proyecto previstos hoy"*: ML y
evaluación de modelos, hardware, contenido, cumplimiento regulatorio especializado,
datos científicos, localización u operaciones industriales pueden necesitar capacidades
propias.

```text
CATÁLOGO BASE DEL KERNEL     capacidades universales · 14 · códigos reservados
EXTENSIONES DE PACK          capacidades propias de una CLASE de proyecto
EXTENSIONES DE PROFILE       excepcionales y específicas de UN proyecto (K0.7)
```

Toda capacidad añadida cumple **exactamente el mismo contrato**: los doce campos de a.1,
las pruebas de conformidad de a.12, y las reglas de materialización y retirada de arriba.
Una extensión que no los cumpla **DEBE** ser rechazada por el instalador.

**Colisión de identificador.** El kernel reserva los catorce códigos de tres letras. Toda
extensión declara su código con prefijo obligatorio de espacio de nombres:

```text
kernel      DIS · ARQ · CON …             reservados, no sombreables
pack        <pack>:<COD>   p. ej.  ml:EVA · hw:LAB · loc:I18N
profile     local:<COD>
```

Con prefijo obligatorio la colisión es **imposible por construcción**, y una extensión
**NO PUEDE** sombrear una capacidad del kernel.

**Colisión de autoridad.** Una capacidad añadida:

1. **NO PUEDE** reclamar veto sobre una materia ya vetada por una capacidad del kernel,
   salvo override declarado en el PROFILE (K0.7) con justificación escrita.
2. **NO PUEDE** ser propietario global de un tipo de proceso del kernel salvo que el pack
   declare esa composición explícitamente.
3. Si dos extensiones reclaman la misma materia, el PROFILE **DEBE** arbitrar en la
   instalación. Sin arbitraje declarado, la prueba T18 falla y la organización no es
   conforme.

---

## a.5 — Propiedad global, custodia de paquetes y paralelismo

v2 decía "un item está en custodia de exactamente una estación" y a la vez permitía
paralelismo. Era contradictorio. Se separan dos niveles distintos:

```text
NIVEL 1 · PROPIEDAD GLOBAL DEL ITEM
  Un único equipo responde de extremo a extremo por el avance general y por la
  coherencia semántica del resultado. No es quien más trabaja: es quien responde.

NIVEL 2 · CUSTODIA DEL PAQUETE
  Cada paquete tiene exactamente un equipo responsable vigente.
  Varios paquetes del mismo item PUEDEN estar simultáneamente en equipos distintos.
```

### Propietario global

- **Regla de asignación:** es la capacidad **cuya capa define el resultado del item**.
  DSP lo asigna al encuadrar, desde la composición por defecto del tipo, y queda escrito.
- Siempre es una capacidad en **modo trabajo propio**, nunca en modo consulta. Para items
  de tipo `SIS`, es SIS.
- **Puede cambiar** durante el recorrido, sólo por decisión de DSP y con traza (un `DEF`
  que resulta ser un `GAP` traslada la propiedad de ARQ a PRD).
- **NO DEBE** declarar el item cerrado porque su parte terminó. Cierra cuando todos los
  paquetes tienen gate cumplido o resultado declarado.
- **No tiene autoridad sobre las capas de otros.** Si dos capas son incompatibles, abre
  un desacuerdo; **no arbitra**.
- La asignación concreta por tipo de proceso se cierra en la sección (b).

### El propietario global NO es un integrador manual universal

Responder por el resultado **no** significa combinar a mano cada paquete cuando la
integración es mecánica. Cuatro cosas distintas:

| función | quién |
|---|---|
| **Responsabilidad global** del resultado | propietario global |
| **Integración técnica automatizable** — ramas, artefactos, estados, vistas | DSP / runtime |
| **Integración semántica** — ¿las capas dicen lo mismo? ¿el conjunto es coherente? | propietario global |
| **Arbitraje de desacuerdos** | nadie en silencio — por autoridad, ver abajo |

DSP integra lo mecánico; el propietario global responde por lo semántico. **Ninguno de
los dos decide en silencio materias cuya autoridad pertenece a otra capacidad.** DSP sabe
qué **no** puede integrar mecánicamente porque el paquete declara `afecta_decisiones`.

### El paquete y lo que declara

```text
PAQUETE  <ITEM-ID>/<nn>
  capacidad responsable   una y sólo una, vigente
  modo                    consulta | trabajo propio
  objetivo                qué debe quedar hecho
  contexto mínimo         ENLACES a fuentes, nunca copias
  nivel de calidad exigido
  capa · gate · estado · checkpoint · v     propios

  DECLARACIÓN DE ACOPLAMIENTO      (nombres definitivos en la sección (g))
  escribe_ficheros:   qué artefactos físicos modifica
  afecta_contratos:   qué contratos, endpoints, esquemas o APIs toca
  afecta_decisiones:  sobre qué decisiones ejerce autoridad
  depende_de:         qué paquetes y decisiones necesita cerrados
  based_on:           fuentes y VERSIONES de las que parte
  integra_en:         dónde y cómo vuelve su resultado
```

### Condición de paralelismo — compuesta, no `escribe` disjunto

> **Corrección de v3.** *"Paralelo si y sólo si `escribe` es disjunto"* era falso: dos
> paquetes pueden tocar ficheros distintos y decidir cosas incompatibles sobre el mismo
> contrato, componente, concepto de dominio, endpoint, migración o dirección visual.
> `escribe` disjunto evita conflictos **físicos**, no **semánticos**.

Dos paquetes se despachan en paralelo sólo si se cumplen **las seis**:

```text
[ ] no existe dependencia de salida entre ellos
[ ] sus escrituras físicas son disjuntas, o están aisladas
[ ] no poseen autoridad concurrente sobre la misma decisión
[ ] no modifican contratos compartidos de forma incompatible
[ ] sus versiones de entrada (based_on) son compatibles
[ ] existe una estrategia explícita de integración
```

Si falla cualquiera, DSP **secuencia o exige coordinación explícita**; no paraleliza a
ciegas. Esto instrumenta G17 en lugar de dejarlo a criterio.

### Conflictos entre paquetes

| tipo | detección | resolución |
|---|---|---|
| **Físico** — mismos artefactos | al despachar, por la condición compuesta | DSP secuencia. El segundo se recompone sobre el resultado del primero. Nunca merge silencioso de decisiones. |
| **Semántico** — dos capas incompatibles | al despachar, por `afecta_contratos` y `afecta_decisiones`; si escapa, al integrar | El propietario global **no decide en silencio**: abre desacuerdo con las dos posturas escritas. Si una capacidad tiene **veto** en esa materia, se aplica el protocolo de veto. Si no hay veto: a DSP si es problema de ruta, al Owner si es de fondo. |

> Nadie declara completado el proceso global porque terminó su parte. Los desacuerdos se
> registran y escalan según autoridad; **nunca se resuelven en silencio**.

### Contrato de veto *(obligatorio para toda capacidad con veto)*

Decir "el veto manda" no basta. Toda capacidad con veto —DIS, DOM, SEG, VER y cualquier
extensión— **DEBE** declarar los seis campos:

```text
MATERIA          sobre qué exactamente puede vetar, y sobre qué NO
EVIDENCIA MÍNIMA qué debe aportar para que el veto sea válido
EFECTO           qué ocurre operativamente al aplicarse
LEVANTAMIENTO    quién puede levantarlo, o declararlo NO LEVANTABLE
APELACIÓN        cómo se impugna una aplicación incorrecta
COLISIÓN         qué ocurre ante dos vetos incompatibles
```

Alcances, para fijar el registro (las políticas detalladas se cierran donde corresponda):

- **SEG** puede impedir una vulneración de seguridad o privacidad. **No** puede decidir
  dirección de producto.
- **DOM** puede impedir corrupción de datos o pérdida de recuperabilidad. **No** puede
  imponer una preferencia arquitectónica cualquiera.
- **DIS** puede impedir que se degrade una dirección aprobada **sin haber explorado
  alternativas**. **No** puede ignorar una imposibilidad física demostrada.
- **VER** bloquea el tránsito con evidencia en rojo. **No** redefine el criterio que
  verifica — ese criterio pertenece a PRD o a DIS.

**Regla de colisión de vetos:** dos vetos incompatibles **NO se arbitran entre las
capacidades**. Escalan al Owner con ambas materias y ambas evidencias escritas. Excepción
única: si uno de los dos es **no levantable por regla dura del kernel** (G27), ese
prevalece y el otro paquete se recompone.

> **Un veto sin su evidencia mínima declarada no es un veto: es una opinión, y no detiene
> nada.**

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

## a.9 — Estado persistido: propiedad, órdenes y concurrencia

Requisito del Owner: **el estado operativo ES los ficheros del repo**, legibles
directamente, sin informe intermedio.

### Lo que queda aprobado en (a): seis invariantes

La **disposición física concreta** —cuántos ficheros, cómo se fragmentan, transacciones,
event log y recuperación— pertenece a la sección **(g)**. Lo que (a) fija es el contrato
que esa disposición **DEBE** cumplir:

```text
I1  PROPIEDAD INEQUÍVOCA     cada parte del estado tiene una autoridad y un ejecutor
                             de mutación identificados. Sin campos de dueño ambiguo.
I2  ESCRITORES CONTROLADOS   ningún campo canónico admite dos ejecutores concurrentes.
I3  PAQUETES FRAGMENTABLES   el estado se divide por unidad de custodia, de modo que
                             trabajos independientes no compitan por el mismo recurso.
I4  VISTAS COMPLETAS         existen artefactos derivados, persistentes, deterministas
    DERIVADAS                y legibles sin herramienta, que muestran el todo.
I5  SIN DUPLICIDAD           ningún dato editable existe en dos sitios a la vez. Lo
    EDITABLE                 derivado no es editable como estado — ver canal de órdenes.
I6  CONCURRENCIA Y           ambas comprobables por prueba, no por argumento (a.12).
    RECUPERACIÓN VERIFICABLES
```

### Autoridad no es lo mismo que escritor

> **Corrección de v3.** Decir *"el Owner es el escritor único de `02-control.md`"*
> confundía autoridad semántica con el proceso que escribe bytes.

```text
AUTORIDAD DEL CAMPO   Owner              quién tiene derecho a decidirlo
ORIGEN DEL COMANDO    edición directa · lenguaje natural · instrucción reconocida
EJECUTOR DE MUTACIÓN  DSP / runtime      quién escribe realmente
ACTOR ATRIBUIDO       Owner              a quién se imputa el cambio
```

Toda mutación conserva, sin excepción: **quién la ordenó · quién la aplicó · sobre qué
versión · mediante qué evento.**

| clase de campo | autoridad | ejecutor de mutación |
|---|---|---|
| Canónico global del item | DSP | DSP / runtime |
| Canónico del paquete | la capacidad con custodia | esa capacidad |
| Control del Owner — prioridad, aparcado | **Owner** | **DSP / runtime** |
| Derivado — vistas, tableros | nadie: se regenera | DSP / runtime |

El Owner **PUEDE** escribir bytes editando el tablero, pero eso **nunca es una escritura
canónica**: es la **emisión de una orden**. La mutación canónica siempre la ejecuta el
runtime. Así I2 se mantiene aunque el Owner tenga las manos en el fichero.

### Diseño candidato de disposición *(preferido, no contrato — se cierra en (g))*

```text
estado/
├─ items/<ITEM-ID>/
│  ├─ 00-encuadre.md      autoridad DSP        id · enunciado · naturaleza · anclaje
│  ├─ 01-ruta.md          autoridad DSP        ruta · traza · grafo · propietario global
│  ├─ 02-control.md       autoridad OWNER      prioridad · aparcado · motivo · reactivador
│  ├─ 03-integracion.md   autoridad PROPIETARIO GLOBAL   estado global · capas · desacuerdos
│  ├─ paq/<nn>-<CAP>.md   autoridad LA CAPACIDAD CON CUSTODIA
│  └─ vista.md            DERIVADO             el item entero en un fichero legible
└─ tableros/<CAP>.md      DERIVADO             la cola de ese equipo
```

**Derivado no significa efímero.** Vistas y tableros son ficheros reales, versionados en
git, legibles sin herramienta. Significa: **regeneración determinista** — mismo estado
canónico produce bytes idénticos.

### Determinismo: fuera la volatilidad ajena a las entradas

> **Corrección de v3.** El ejemplo llevaba `generado: 2026-08-25T19:04`. Con hora de
> pared, dos regeneraciones del mismo estado producen bytes distintos y **T03 falla por
> construcción.**

```text
PROHIBIDO en un artefacto derivado: hora de pared, duración, número de ejecución,
                                    identidad del proceso, cualquier telemetría.
OBLIGATORIO:  source_revision: <hash del estado canónico del que deriva>
PERMITIDO:    una fecha DERIVADA del último evento canónico incluido
```

La telemetría de ejecución vive fuera del artefacto determinista.

> **Regla anticircularidad:** `source_revision` hashea **únicamente ficheros canónicos**,
> nunca derivados. Si incluyera los derivados, regenerar cambiaría el hash del que la
> regeneración depende y el determinismo sería imposible por construcción.

### El tablero: zona derivada + canal de órdenes

> **Corrección de v3.** *"DSP es el único escritor del tablero, luego cualquier diff es
> una orden"* no se sostiene: el Owner **puede** editar el tablero, luego hay dos
> escritores físicos sobre el mismo fichero. Y `mtime` no resuelve máquinas distintas,
> commits remotos, rebase, ni una edición hecha entre la lectura y la escritura.

El requisito de poder editar desde el tablero se conserva. Se hace **visible y fácil**
separando dos zonas dentro de la misma experiencia:

```markdown
# TABLERO — DIS · Diseño
<!-- source_revision: 9f3c1a7 -->

## ÓRDENES        ← escribe aquí. DSP nunca borra una orden no consumida.
- [ ] FEA-021/02  prio: urgente
- [ ] GAP-014     aparcar: "centro la atención en FEA-021"  reactiva: "retoma el gap"

## COLA           ← derivado de source_revision. Se regenera; editar aquí no manda.
| paquete | estado | prio | actúa | espera desde | necesita para avanzar | v |
|---|---|---|---|---|---|---|
| [GAP-014/01](../items/GAP-014/paq/01-DIS.md) | aparcado | normal | owner | 2026-08-19 | aparcado por: atención en FEA-021 · reactiva: "retoma el gap" | 7 |
| [FEA-021/02](../items/FEA-021/paq/02-DIS.md) | en curso | urgente | dis/critico | 2026-08-25 | 2ª dirección explorada y comparada | 3 |
```

**Ciclo de consumo de órdenes** — cumple los siete requisitos exigidos:

```text
1 LEER        DSP lee el fichero completo y calcula el hash de su contenido, H0
2 DETECTAR    órdenes no consumidas `- [ ]`   MÁS   diff de la zona COLA contra lo
              que regeneraría a partir de source_revision
3 ELEVAR      toda diferencia hallada en COLA se ELEVA a la zona ÓRDENES como
              `- [?] interpretado: prio de FEA-021/02 → urgente. Confirma o borra.`
              DSP NUNCA regenera encima de una diferencia sin elevarla antes.   (req 1)
4 VALIDAR     ¿campo de autoridad del Owner? ¿la base de la orden sigue vigente? (req 2)
              Si la base cambió → CONFLICTO: `- [!]` con AMBAS intenciones escritas;
              ni se aplica ni se borra.                                         (req 6)
5 REGISTRAR   la orden válida se persiste como EVENTO —id · autor Owner · base ·
              ejecutor DSP— ANTES de tocar el estado canónico.                  (req 3)
6 APLICAR     el evento se aplica al campo canónico. Idempotente por id.        (req 4)
7 MARCAR      la orden pasa a `- [x] <event-id>`
8 REGENERAR   COLA se regenera y el fichero se escribe con COMPARE-AND-SWAP sobre
              el hash de CONTENIDO H0. Si cambió, se descarta y se repite todo.  (req 5)
```

**Recuperación** (req 7): la propia línea de orden es el registro write-ahead. Al
reiniciar, DSP encuentra cada orden en el estado en que quedó —`- [ ]` sin evento, evento
registrado con la línea aún sin marcar, o ya `- [x]`— y **converge sin inventar estado**,
porque aplicar un evento por id dos veces es una no-operación.

**Compare-and-swap sobre hash de contenido, nunca `mtime`.** Los casos distribuidos —dos
máquinas, commits remotos, rebase— se resuelven porque cada orden lleva su base: una
orden cuya base ya no existe tras un rebase se marca `- [!]` y **no se aplica**.

**Editar una celda derivada por costumbre nunca pierde la intención ni gana en silencio**:
el paso 3 la eleva a orden y se la devuelve al Owner para que confirme.

**Contradicción detectada al aplicar y resuelta aquí:** la zona ÓRDENES la escribe el
Owner y la zona COLA es derivada. Si T03 comparase **el fichero completo**, la presencia
de órdenes lo haría fallar aunque el generador fuese perfectamente determinista. Por
tanto: **T03 compara la zona derivada, no el fichero entero.** Esto es un argumento a
favor de separar el canal de órdenes en un fichero propio (sidecar) al cerrar (g) — con
sidecar, T03 vuelve a ser una comparación de fichero completo.

> **El soporte físico del tablero NO queda cerrado en (a).** Lo aprobado es el contrato:
> legibilidad sin herramienta · uniformidad entre equipos · zona derivada determinista ·
> canal de órdenes visible que nunca se sobrescribe. Si en (g) resulta mejor fragmentar
> por fila, usar un índice compilado o un sidecar de comandos, el contrato se mantiene.

### Atomicidad entre ficheros canónicos

Una sola transición puede tener que tocar paquete, ruta, integración, control, evento y
vistas. **Git no convierte una secuencia de escrituras en una transacción**: si el proceso
muere a mitad, el estado queda parcialmente aplicado.

> **Requisito de (a):** toda transición multiarchivo **DEBE** ser **recuperable e
> idempotente**. El runtime **DEBE** poder detectar una operación incompleta y terminarla
> o revertirla **sin inventar estado**.

El mecanismo —event sourcing, write-ahead log, manifest transaccional, commits atómicos
u otro— se decide en **(g)**.

### Prueba de concurrencia

Escrituras sobre unidades de custodia distintas no colisionan por diseño (I3):

```text
agente A  → paquete FEA-021/02          unidad distinta
agente B  → paquete GAP-014/01          unidad distinta
Owner     → zona ÓRDENES del tablero de DIS
DSP       → zona COLA del mismo tablero, con CAS sobre hash de contenido
```

El único fichero con dos escritores físicos es el tablero, y ahí el ciclo de órdenes con
elevación previa más CAS garantiza que ninguna orden se pierde ni se sobrescribe.

> **T02 no se declara superada por argumento: se declara superada cuando la prueba pasa**,
> incluido el caso del Owner editando prioridad mientras DSP regenera ese mismo tablero.

Casos residuales, nombrados:

1. **Dos agentes sobre el mismo paquete** — prohibido por custodia única. Es un defecto de
   despacho, no un conflicto a fusionar.
2. **Dos instancias de DSP** — el runtime **DEBE** garantizar un solo ejecutor de
   mutaciones (lock real o proceso único). Requisito del runtime, se implementa en (g).

### Forma de la zona COLA

Orden de columnas fijo · sin `|` en el contenido, usar `·` · vacío = `—` · fechas ISO ·
prefijo tipado en `necesita`: `bloqueo: … · desbloquea: …` / `aparcado por: … · reactiva:
…` / `custodia: <CAP>` / sin prefijo = lo que falta para cerrar la capa. Lo que no quepa
en una línea vive en el paquete.

### Estados — PROVISIONALES, se cierran en (b)

```text
propuesto · en curso · consulta · esperando-owner · bloqueado · aparcado ·
devuelto · cancelado · cerrado
```

Esta lista **no es definitiva**. Faltan distinciones por resolver en (b): `listo` ·
`esperando capacidad` · `esperando dependencia` · `esperando Owner` · `activo` ·
`suspendido`. v3 usaba además "en cola", que no figuraba en la lista — inconsistencia
registrada.

Lo que **sí queda aprobado** es la distinción semántica:

```text
BLOQUEADO  no puede avanzar: depende de algo que aún no existe
APARCADO   SÍ podría avanzar; el Owner ha decidido centrar la atención en otra cosa.
           Decisión de prioridad, no imposibilidad. Conserva custodia y capas.

Un item aparcado o bloqueado NO consume capacidad ni frena a ningún otro.
```

### Prioridad

```text
urgente · normal · fondo          por defecto: normal
`normal` significa "avanza a su ritmo", NO "cuanto antes".
REGLA DURA: el sistema NO DEBE marcar `urgente` por su cuenta. Sólo el Owner.
Se cambia en lenguaje natural o por orden desde el tablero.
```

### Concurrencia: es el modo normal

Paquetes en custodia de equipos distintos avanzan de forma independiente por defecto.
Sólo se serializa cuando falla alguna de las seis condiciones de a.5. Lanzar un gap y
después un feature debe dejar ambos progresando.

---

## a.10 — CHECKPOINT

El tablero resuelve **dónde** está un paquete. No resuelve **en qué punto del método
interno** se quedó el equipo con él.

> **CHECKPOINT ≠ APARCADO.** Aparcado es prioridad. Checkpoint es posición dentro del
> método propio del equipo — existe igual si el paquete está activo, aparcado, bloqueado
> o en cola. *(La lista formal de estados es provisional: ver a.9.)*

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

T02 CONCURRENCIA     (a) Dos agentes en dos paquetes del mismo equipo, DSP regenerando
                         y el Owner aparcando uno → cero cambios perdidos.
                     (b) EL OWNER EDITA PRIORIDAD EN EL TABLERO MIENTRAS DSP REGENERA
                         ESE MISMO TABLERO → la orden no se pierde, no se sobrescribe
                         y queda atribuida al Owner.                        [corregida]

T03 DETERMINISMO     Regenerar DOS VECES sin cambios en el estado canónico y comparar
                     BYTES DE LA ZONA DERIVADA. Ningún artefacto derivado contiene hora
                     de pared ni telemetría. `source_revision` hashea sólo ficheros
                     canónicos, nunca derivados.                            [corregida]

T04 PROPIEDAD        Ningún campo canónico admite dos ejecutores de mutación. Toda
                     mutación registra quién la ordenó, quién la aplicó, sobre qué
                     versión y mediante qué evento.                         [corregida]

T05 TRAZA DE RUTA    Todo item tiene `activadas` y `no activadas` con motivo escrito.

T06 FRENO PAR        La 3ª devolución entre el mismo par no se ejecuta; existe el
                     registro con las dos posturas enfrentadas.

T07 FRENO CICLO      Un rebote repetido de 3 o más capacidades se detecta y se detiene.

T08 RACHA SIS        El 3er item SIS consecutivo no se despacha si hay item de producto
                     listo, salvo excepción declarada. Todo item SIS enlaza su
                     justificación de producto.

T09 CHECKPOINT       Ningún paquete suspendido sin checkpoint, o con `not_required` sin
                     motivo. Todo checkpoint tiene `based_on` con versiones.

T10 APARCADO         Ningún item aparcado cerrado, desaparcado ni "limpiado" por
                     antigüedad.

T11 SÍNTESIS         Toda afirmación de una vista derivada enlaza su origen y es
                     comprobable leyendo los ficheros canónicos.

T12 SIN EQUIPOS      Ningún equipo materializado sin cola durante dos auditorías.
    VACÍOS

T13 PATRONES         Todo patrón vigente declara clase, alcance, criterios comprobables
                     y condición de caducidad.

T14 ROLLBACK         Todo rollback autónomo ejecutado cumplía los cinco requisitos y
                     dejó evento y evidencia.

T15 CONFLICTO        Ningún conflicto de decisión entre paquetes resuelto sin desacuerdo
                     registrado con las dos posturas.

T16 PARALELISMO      Dos paquetes escriben FICHEROS DIFERENTES pero alteran el MISMO
    SEMÁNTICO        contrato semántico → DSP detecta que no son paralelizables, o
                     exige coordinación explícita.                              [nueva]

T17 RECUPERACIÓN     El proceso se interrumpe DESPUÉS de modificar el estado canónico y
                     ANTES de regenerar las vistas. Al reiniciar, DSP detecta la
                     transición incompleta y converge al MISMO resultado que una
                     ejecución sin interrupción.                                [nueva]

T18 EXTENSIONES      Toda capacidad añadida por pack o profile cumple los doce campos,
                     usa prefijo de espacio de nombres, y no reclama veto ni propiedad
                     global en colisión sin arbitraje declarado en el PROFILE.  [nueva]

T19 VETOS            Toda capacidad con veto declara sus seis campos de contrato. Un
                     veto sin evidencia mínima declarada no detiene nada.       [nueva]

T20 APR NO TRÁMITE   Existen items cerrados SIN paquete APR, con `learning_candidate:
                     none` registrado. APR sólo recibe paquete ante señal real. [nueva]
```

---

