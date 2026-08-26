# SECCIÓN (a) v2 — CAPACIDADES, EQUIPOS Y RUTAS
Reescritura completa tras las correcciones del Owner. Pendiente de aprobación.

## a.0 — Tres niveles. El error de v1 fue confundirlos.

    CATÁLOGO DE CAPACIDADES     qué sabe hacer una organización ADS
    (kernel · fijo · reusable)  14 capacidades. No es un recorrido.
              |
              | materialización — sólo donde hay trabajo real
              v
    EQUIPOS VIVOS               capacidad + tablero + cola + memoria + agentes
    (proyecto · variable)       se materializan y se retiran
              |
              | composición — una por cada item, según su naturaleza
              v
    RUTAS                       grafo de valor: qué capacidades se activan,
    (item · única)              en qué orden, en paralelo o no, y POR QUÉ NO
                                las demás

v1 fusionó los tres niveles en una cadena de ocho paradas obligatorias. Eso obliga
a que una errata genere capa de Producto, Diseño y Uso Real aunque sea para decir
"no aplica": ceremonia sin valor, que es lo que este rediseño existe para eliminar.

REGLA DE CATEGORÍA (sustituye a "sombreros, no saltos", derogada):
No existe "la cadena". Existe un catálogo, y un enrutador que compone una ruta por
item. Saltarse una capacidad no es un defecto — no dejar escrito por qué se saltó,
sí. La traza la escribe el enrutador UNA VEZ al componer la ruta, no cada capacidad
saltada por separado.

## a.1 — Qué es una capacidad (ficha del catálogo)

Once campos. Sin los once es una etiqueta y el kernel DEBE rechazarla.

  MISIÓN          una frase: qué falta si esto no existe
  CAPA DE VALOR   qué añade al item que no traía al entrar   ← su razón de ser
  ENTRADA         qué acepta y en qué estado mínimo
  SALIDA          qué deja escrito cuando añade su capa
  GATE            lista COMPROBABLE que debe cumplirse para que el item cambie
                  de estado y salga de su custodia. No es un juicio: es una lista.
                  Si hiciera falta juicio, ese juicio es otra capacidad activada,
                  no una aprobación oculta.
  RESULTADOS      cuáles de los cuatro (a.2) puede emitir y con qué autoridad
  MEMORIA PROPIA  su fuente de verdad persistente en el repo
  TABLERO         su fichero de estado, legible por el Owner sin herramienta (a.8)
  MÉTODO          procedimiento interno; puede tener subcircuitos propios
  CHECKPOINT      en qué punto de su propio MÉTODO se quedó con cada item que tiene
                  a medias, persistido de forma que un agente nuevo lo retome sin
                  que el Owner tenga que resumir nada (a.9)
  AUTORIDAD       qué decide sola · qué escala · sobre qué tiene veto
  OWNER           en qué nivel de los tres de a.7 opera, y con qué criterio escrito

CUSTODIA (regla que hace legibles los tableros):
Un item está en custodia de exactamente UNA estación en cada momento. Los servicios
se consultan SIN transferir custodia — por eso varias consultas pueden correr en
paralelo. Un item aparece como `custodia` en un solo tablero y como `consulta` en
los tableros de los servicios que lo atienden.

## a.2 — Los cuatro resultados (v1 sólo tenía uno y estaba mal)

Cuando una capacidad termina con un item emite exactamente uno:

1. CAPA AÑADIDA   añadió su capa. El GATE decide si el item puede cambiar de estado.
                  Capa y gate son cosas distintas: la capa es lo producido, el gate
                  es la condición de entrega.
2. DEVOLUCIÓN     una capa anterior es insuficiente. Vuelve a la capacidad concreta,
                  nombrando qué falta. Sujeta al freno numérico de a.6.
3. BLOQUEO        no puede avanzar: depende de algo que aún no existe (decisión,
                  dato, otro item). DEBE nombrar qué lo desbloquearía.
4. CANCELACIÓN    este item no merece seguir fabricándose. Motivos legítimos: el
                  problema se disolvió, el anclaje reveló que ya está resuelto, la
                  relación coste/valor se invirtió, lo sustituye otro item.
                  Autoridad: PRD y DSP cancelan por sí solas items de naturaleza
                  interna; toda cancelación de algo que el Owner pidió explícitamente
                  se propone y la decide él. Cancelar SIEMPRE deja motivo escrito;
                  un item cancelado no se borra.

APARCADO NO ES UN RESULTADO. Es ortogonal: lo declara el Owner (o DSP por
instrucción suya). Un item aparcado conserva custodia y todas sus capas intactas.
REGLA DURA: el sistema NO DEBE proponer desaparcar, cerrar ni "limpiar" un item
aparcado por antigüedad. Un item puede quedar aparcado indefinidamente. Es un
resultado normal del sistema, no una anomalía.

## a.3 — EL CATÁLOGO · 14 capacidades

### ESTACIONES — toman custodia del item y le añaden capa

PRD · PRODUCTO — intención y criterio de éxito
  Para quién, qué cambia, qué queda fuera, qué haría que esto fuera un fracaso
  aunque funcione, relación con la definición de éxito del Owner (K0.13).
  En un GAP: aquí el hueco pasa de "falta algo" a resultado definido con criterio
  de terminado. Es el procedimiento estándar de gaps que hoy no existe.
  Se activa SÓLO si el item afecta al producto. Un bug interno no la activa.
  Autoridad: alcance rutinario sola; escala alcance relevante y prioridad
  estratégica. Cancela items internos.

DIS · DISEÑO — forma
  Dos niveles simultáneos y ambos exigibles: funcional/experiencia (flujo, estados,
  información, densidad, accesibilidad, fluidez percibida) y estética/dirección de
  arte (identidad, carácter, capacidad de sorprender).
  Condición de entrada: consultar la memoria de diseño. Salida obligatoria: memoria
  actualizada con lo decidido Y con lo descartado y su porqué.
  Subcircuitos propios: DIS/Fundación · DIS/Reconstrucción · DIS/Evolución.
  Veto sobre soluciones técnicas que degraden la forma sin agotar alternativas.

ARQ · ARQUITECTURA — encaje y plan técnico
  Cómo entra en lo que ya hay; RADIO DE IMPACTO MEDIDO, no estimado; contratos que
  cambian; alternativas con coste; ADR cuando proceda; descomposición en paquetes
  con orden y dependencias. También hace el diagnóstico en rutas de defecto.
  Devuelve a DIS sólo trayendo alternativas de forma, nunca sólo la negativa.

CON · CONSTRUCCIÓN — la implementación y sus tests
  NO redecide capas anteriores. Si descubre que una está mal, DEVUELVE.
  Implementar sobre una capa que sabe mal es el fallo característico de esta
  estación. Sin autoridad sobre forma ni intención.

VER · VERIFICACIÓN — dosier de evidencia
  No emite un sí/no: produce un artefacto que viaja hacia adelante. Revisión
  independiente de quien construyó (G13 deja de ser proporcional al riesgo y pasa
  a ser estructura por defecto de esta capacidad), tests, regresión incluida la
  visual, seguridad cuando aplica, presupuestos, y evidencia JUZGABLE POR UN HUMANO:
  capturas, grabaciones, comparativas, estados extremos (vacío, error, carga,
  mínimo, máximo). Veto sobre entrega mientras haya evidencia en rojo.

ENT · ENTREGA Y OPERACIÓN — realidad operativa   [capacidad nueva, error 4]
  El cambio existe fuera del entorno de desarrollo y se ha OBSERVADO comportarse.
  Integración de ramas y paquetes, migraciones, despliegue (preview/staging/
  dispositivo), smoke tests, publicación (materia reservada al Owner, G05),
  observación de logs y métricas durante una ventana declarada, rollback, y la
  confirmación de que funciona en el entorno real.
  Autoridad: rollback por decisión propia, sin consultar, ante señal en rojo.

  POR QUÉ ESTACIÓN Y NO PARTE DE PLT: PLT construye y posee la maquinaria (CI,
  entornos, scripts, observabilidad) — capacidad con backlog propio, sin custodia.
  ENT opera esa maquinaria sobre un item concreto y SÍ toma custodia. Fundirlas
  mete en una sola cola el trabajo de infraestructura y el trabajo por item, y uno
  de los dos siempre pierde. Además el rollback es una decisión de nivel item: debe
  pertenecer a quien tiene la custodia, no a quien mantiene el pipeline.

USO · USO REAL — juicio
  Prepara el item para que el Owner lo pruebe con el mínimo set-up (hereda G36
  íntegro: cola priorizada, plan de validación único, orden por coste de set-up,
  estado preparado de antemano), recoge la reacción y la convierte en salida
  estructurada: aceptado · rechazado · nueva dirección (G51) · item nuevo.
  SE ACTIVA SÓLO cuando hay algo que únicamente el Owner puede juzgar.

APR · APRENDIZAJE — criterio
  Convierte el recorrido en cambio de criterio: ledgers (G52), promoción de
  aprendizaje a regla, memoria de diseño y memorias de equipo actualizadas,
  candidatos a UPSTREAM (K0.12), ajuste de la propia ruta por defecto si el
  recorrido reveló una composición mal definida, y los items nuevos que nacen del
  uso real, que entrega a DSP para su encuadre.

### SERVICIOS — se consultan sin transferir custodia

INV · INVESTIGACIÓN Y EVIDENCIA
  Preguntas falsables, spikes contra el entorno real, freshness (G22+G33).
  Autoridad: puede declarar que una decisión NO puede tomarse todavía.
DOM · DOMINIO Y DATOS
  Modelo, vocabulario compartido, contratos de datos, reversibilidad de esquemas.
  Veto sobre lo que rompa el modelo o la recuperabilidad.
SEG · SEGURIDAD Y PRIVACIDAD
  G27 + G28 + cumplimiento declarado. Veto duro, no negociable.
PLT · PLATAFORMA
  Build, CI, entornos, tooling, observabilidad, aislamiento multiagente.
  Con cola y backlog propios: la fábrica es un producto con sus items.

### SISTEMA — trabajan sobre la fábrica, no sobre el producto

SIS · INGENIERÍA DEL SISTEMA
  Dueña del sistema operativo: memoria en bloques, EL DISPATCHER COMO SOFTWARE,
  plantillas uniformes, catálogo de capacidades, composiciones por defecto, prueba
  de conformidad de una organización instalada, enrutamiento de modelos,
  rendimiento de equipos, revisión de plantilla y regla de retirada (G52).
  FUNCIÓN COHERENCIA DOCUMENTAL: valida estructura, frescura, enlaces y coherencia
  del corpus. NO escribe contenido por nadie: cuando encuentra un documento
  huérfano o caduco, crea un item y lo enruta a quien posee esa capa.
  Va aquí y no en APR porque el sujeto de APR es el CRITERIO (qué aprendimos cambia
  qué decidimos), mientras que estructura, frescura y enlaces son propiedades de los
  ARTEFACTOS del sistema — misma naturaleza que plantillas, tableros y dispatcher.
  Además es comprobación mayoritariamente automatizable, que es el modo de SIS, y
  parte natural de la prueba de conformidad que SIS ya ejecuta.

DSP · DESPACHO   (absorbe Encuadre — decisión A1 del Owner)
  Implementación: SOFTWARE/RUNTIME primero (el dispatcher), propiedad de SIS. Un
  supervisor —agente o el Owner— interviene sólo en excepciones: item estancado,
  contradicción de estado, ruta que hay que recomponer.
  Cuatro funciones:
   · ENCUADRE  el item pasa de frase suelta a ficha persistente: id, enunciado de
     una línea de lo que de verdad se pide, naturaleza, y DOSIER DE ANCLAJE —
     qué sistemas/módulos/agentes YA implementados tocan esto · qué decisiones
     previas lo gobiernan · qué aprendizajes vigentes aplican · si duplica un item
     abierto · QUÉ NO EXISTE TODAVÍA Y SE CREÍA QUE SÍ.
     Se apoya en el ÍNDICE DE LO EXISTENTE, memoria propia de DSP.
   · ENRUTAMIENTO  compone la ruta y escribe la traza de a.5
   · ESTADO  reconstruye el estado al abrir, contrasta lo declarado contra la
     realidad del repo, resuelve inconsistencias, mantiene la coherencia global de
     los tableros. Responde a "Continúa".
   · SUPERVISIÓN  detecta estancados, aplica el freno de a.6, escala
  Autoridad: total sobre el ORDEN y la RUTA. Ninguna sobre el contenido de ninguna
  capa. Cancela items internos duplicados.
  Poner Encuadre aquí lo REFUERZA, no lo debilita: el índice de anclaje es lo que
  el enrutador necesita de todos modos para detectar duplicados y componer rutas.
  Pasa de usarse en una estación a usarse en TODOS los items.

## a.4 — Materialización y retirada (error 6)

El kernel define CAPACIDADES. El proyecto materializa EQUIPOS.

MATERIALIZAR una capacidad = darle tablero, cola, memoria viva y agentes declarados.
  Señal de materialización: el enrutador necesita activar una capacidad que no tiene
  equipo. Esa necesidad ES el disparador. No se materializa "por si acaso".
RETIRAR: un equipo materializado cuyo tablero no ha tenido movimiento durante dos
  auditorías es candidato a desmaterializarse (regla de retirada de G52).
  SU MEMORIA PERSISTE. Las memorias no mueren; los equipos sí.

Ejemplos, para que la regla se vea:
  DOM en PesquerApp (ERP con stock, trazabilidad y tenancy) → se materializa como
      equipo propio desde el principio, con dominio grande y vivo.
  DOM en un proyecto sin dominio complejo → puede no materializarse nunca.
  DSP y SIS → materializadas siempre. Sin ellas no hay sistema operativo.

## a.5 — Composición de rutas (la corrección central)

### Gramática (para que la ruta sea verificable, no prosa)
  A → B    secuencia
  A ∥ B    en paralelo
  A ⇄ B    revisión cruzada: producen y se critican mutuamente antes de cerrar
  A ⊳ B    A desbloquea B: el resultado de A es condición de entrada de B, que
           puede estar ya preparado esperándolo
  [A si X] condicional, con la condición escrita

### Tipos de proceso y su composición POR DEFECTO
La composición por defecto es un punto de partida del kernel/pack, no una obligación.
El enrutador puede apartarse de ella dejando el motivo.

  FEA  feature / capacidad nueva
       PRD → DIS → ARQ → CON ∥[DOM,SEG si tocan] → VER → ENT → USO → APR
  GAP  hueco entre lo implementado y lo pretendido
       PRD → [DIS si tiene superficie] → ARQ → CON → VER → ENT → [USO si observable] → APR
  DEF  defecto / bug
       ARQ(diagnóstico) → CON → VER → ENT → [USO si lo reportó el Owner] → [APR si revela criterio]
  INC  incidente en uso real
       ENT(contención/rollback) → ARQ(diagnóstico) → CON → VER → ENT → APR (obligatorio)
  INV  investigación / pregunta abierta
       INV → [PRD o ARQ según destino] → APR
  DEU  deuda técnica / refactor
       ARQ → CON → VER → ENT → APR
  DEP  actualización de dependencia
       SEG ∥ PLT → CON → VER → ENT
  AUD  auditoría de proyecto existente
       INV ∥ DOM ∥ SEG ∥ DIS/Reconstrucción → PRD → APR
  DIR  cambio de dirección (G51)
       PRD ∥ DIS → ARQ(radio de impacto) → OWNER OBLIGATORIO → CON → VER → ENT → USO → APR
  SIS  evolución del propio sistema o del kernel
       SIS → CON → VER → APR

Nótese: DEF no activa PRD ni DIS. DEP no activa ninguna de las dos. AUD no activa
CON. Ninguna ruta es la de otra. Eso es la corrección.

### Traza obligatoria — sustituye a "sombreros, no saltos"
El enrutador escribe en la ficha del item, al componer y en cada recomposición:

  RUTA
  compuesta: <fecha> por DSP · tipo: DEF
  activadas:     ARQ(diagnóstico) → CON → VER → ENT
  no activadas:
    PRD — no altera alcance ni criterio de éxito: corrige comportamiento ya
          especificado en FEA-009
    DIS — sin superficie de interfaz: el fallo es de cálculo en capa de dominio
    USO — no observable por el Owner; la evidencia de VER basta
  recomposiciones: <fecha> ARQ pidió añadir PRD — el "bug" era un gap de alcance

REGLA: activar de más deja traza igual que activar de menos. Una ruta que activa una
capacidad que no cambió nada es una señal del modo de fallo (b) de a.6.
REGLA: cualquier capacidad puede pedir a DSP recomponer la ruta, dejando el motivo.
Esto sustituye al "escalado automático" de G34 en una forma trazable.

## a.6 — El freno: dos modos de fallo simétricos (sustituye a K0.9)

K0.9 declaraba un único modo de fallo —"la organización documenta sobre sí misma y
no compila nunca"— y con él justificaba todos los timeboxes y presupuestos. Se
sustituye por dos, ambos vigilados, ninguno subordinado al otro.

MODO (a) — FRAGMENTACIÓN SIN SISTEMA        [el problema real hoy]
  Muchos agentes, documentos y circuitos descoordinados; trabajo que duplica lo ya
  implementado; memoria perdida entre sesiones; el Owner reexplicando contexto.
  Señales: items que al anclarse resultan duplicados · la misma decisión tomada dos
  veces con resultado distinto · el Owner reescribiendo cómo guiar la conversación.
  Mecanismos: Encuadre obligatorio con dosier de anclaje · índice de lo existente ·
  fuente única por item · tableros legibles sin traducción.

MODO (b) — AUTORREFERENCIA SIN PRODUCTO     [el riesgo simétrico de construir esto]
  El sistema dedica más esfuerzo a organizarse a sí mismo que a producir resultados.
  Señales: rutas que activan capacidades que no cambiaron nada · devoluciones
  repetidas entre el mismo par · capacidades materializadas sin cola · proporción
  de items de tipo SIS frente a items de producto.
  MECANISMO NUMÉRICO, no interpretable:

    LÍMITE DE DEVOLUCIONES = 2 entre el mismo par de capacidades sobre el mismo item.
    La 1ª devolución es información: la capa estaba incompleta.
    La 2ª es desacuerdo: no se han puesto de acuerdo en qué falta.
    LA 3ª NO SE EJECUTA. El item no rebota otra vez.
    DSP lo detiene y escala CON LAS DOS POSTURAS ENFRENTADAS ESCRITAS:
    qué sostiene cada capacidad y por qué. A DSP si es problema de ruta;
    al Owner si es desacuerdo de fondo.
    PROHIBIDO: una tercera revisión muda, o que una capacidad ceda en silencio.

  Otros mecanismos: regla de retirada de G52 aplicada a capacidades materializadas ·
  la traza de ruta obligatoria en ambos sentidos.

## a.7 — Intervención del Owner: tres niveles con criterio escrito (error 5)

v1 ponía "Owner obligatorio" fijo en tres estaciones para todo item. Eso reproduce el
cuello de botella con más pasos de por medio. Se sustituye por:

  OBLIGATORIO   al FUNDAR o CAMBIAR DIRECCIÓN de producto o diseño (conecta con G51,
                no es mecanismo nuevo) · decisiones estratégicas · materias reservadas
                (G05) · lo difícilmente reversible con impacto significativo
  OPCIONAL /    cuando el item EXTIENDE UN PATRÓN YA APROBADO. Va a la cola de
  ACUMULADA     validación por lotes (G36); no detiene el item
  NINGUNA       mantenimiento, bugs internos, trabajo rutinario ya autorizado

### Criterio escrito y comprobable de "extiende un patrón ya aprobado"
Mismo patrón que G53 resolvió con premium_areas: declarado, finito, comprobable.
Sin esto, la ambigüedad vuelve por la puerta de atrás.

Un PATRÓN APROBADO es un artefacto declarado, no una impresión. Vive en la memoria
de diseño (patrones de forma) o en CONVENTIONS (patrones de ingeniería):

  PATRÓN: <nombre>
  Aprobado:   <fecha> · por el item/AT que lo aprobó
  Alcance:    a qué se aplica y a qué NO
  Criterios comprobables: <lista — si el item los cumple todos, lo extiende>
  Caduca:     condición que lo reabre

TEST: un item extiende un patrón aprobado si y sólo si
  (1) existe una entrada de patrón VIGENTE cuyo alcance lo cubre, Y
  (2) el item cumple TODOS sus criterios comprobables, Y
  (3) no introduce ningún elemento fuera del alcance declarado.
Si falla cualquiera de los tres → Owner obligatorio.

Consecuencia deliberada: la PRIMERA instancia de cualquier cosa es siempre Owner
obligatorio, y su aprobación CREA el patrón. Es D10 del pack-design-led ("una
pantalla llevada al final, aceptada por el Owner, convertida en el listón")
generalizada a todo el sistema. Fusión con lo existente, no sistema paralelo.

## a.8 — LOS TABLEROS: el estado ES el repositorio

Requisito del Owner: abrir el repo y leer el estado real, sin informe intermedio.

### Dos ficheros, una sola verdad
  estado/items/<ID>.md      LA FICHA. Fuente de verdad del item: naturaleza,
                            enunciado, prioridad, estado, ruta y su traza, custodia,
                            capas añadidas, historial.
  estado/equipos/<CAP>.md   EL TABLERO. Proyección editable de lo que ese equipo
                            tiene ahora, con puntero a cada ficha.

REGLA DE FUENTE ÚNICA: no hay dos fuentes. Hay una FUENTE (la ficha) y una
PROYECCIÓN EDITABLE (el tablero). Editar el tablero es una forma legítima de dar una
orden — el Owner puede cambiar una prioridad ahí mismo — y DSP la propaga a la ficha
en la siguiente reconciliación. Lo que NUNCA ocurre es que las dos diverjan en
silencio: toda divergencia queda registrada como inconsistencia resuelta.

### Formato: tabla Markdown de columnas fijas. Idéntico en los 14 equipos.
Legible en crudo, parseable sin ambigüedad si se respeta: orden de columnas fijo ·
sin `|` en el contenido (usar `·`) · vacío = `—` · fechas ISO · prefijo tipado en la
última columna. Todo campo que no quepa en una línea vive en la ficha, no aquí.

    # TABLERO — DIS · Diseño
    > Proyección de estado/items/. Fuente: la ficha. Reconcilia: DSP.
    > actualizado: 2026-08-25

    | item | estado | prio | actúa | espera desde | necesita para avanzar |
    |---|---|---|---|---|---|
    | [GAP-014](../items/GAP-014.md) | aparcado | normal | owner | 2026-08-19 | aparcado por: atención en FEA-021 · reactiva: "retoma el gap" |
    | [FEA-021](../items/FEA-021.md) | en curso | urgente | dis/critico | 2026-08-25 | 2ª dirección explorada y comparada |
    | [FEA-009](../items/FEA-009.md) | bloqueado | normal | inv | 2026-08-22 | bloqueo: latencia real sin medir · desbloquea: SPIKE-03 |
    | [DEF-102](../items/DEF-102.md) | consulta | normal | dis | 2026-08-24 | opinión sobre estado vacío · custodia: CON |

Micro-gramática de la última columna, tipada:
  `bloqueo: <qué falta> · desbloquea: <item o decisión>`
  `aparcado por: <motivo> · reactiva: <señal>`
  `custodia: <CAP>`   (filas de consulta en tableros de servicio)
  sin prefijo: lo que falta para cerrar la capa

### Vocabulario de estados (transiciones completas → sección b)
  propuesto · en curso · esperando-owner · bloqueado · aparcado · devuelto ·
  cancelado · cerrado

  BLOQUEADO   no puede avanzar: depende de algo que aún no existe
  APARCADO    SÍ podría avanzar; el Owner ha decidido centrar la atención en otra
              cosa. Decisión de prioridad, no imposibilidad. Conserva custodia y
              todas sus capas intactas.
  Un item aparcado o bloqueado NO consume capacidad ni frena a ningún otro.

### Prioridad: es del Owner
  urgente · normal · fondo        por defecto: normal
  `normal` significa "avanza a su ritmo", NO "cuanto antes".
  REGLA DURA: el sistema NO DEBE marcar `urgente` por su cuenta. Sólo el Owner.
  Se cambia en lenguaje natural o editando el tablero directamente.

### Concurrencia: es el modo normal, no la excepción
Items en custodia de equipos distintos avanzan de forma independiente por defecto.
Sólo se serializa cuando hay dependencia declarada entre items o conflicto de
escritura sobre la misma fuente de verdad (G17). Lanzar un gap y luego un feature
debe dejar ambos progresando.

### DSP no traduce
Preguntar a DSP "qué tiene cada equipo" DEBE devolver el contenido de los tableros,
no una síntesis. Si la respuesta de DSP difiere de los ficheros, es un defecto de
reconciliación, no una interpretación.

## a.9 — CHECKPOINT: en qué punto exacto del método se quedó el equipo

El TABLERO resuelve DÓNDE está un item. No resuelve EN QUÉ PUNTO de su trabajo
interno se quedó el equipo con él. Son cosas distintas y hacen falta las dos.

CHECKPOINT ≠ APARCADO.
  APARCADO   es prioridad: el item podría avanzar, el Owner atiende otra cosa.
  CHECKPOINT es posición dentro del método propio del equipo. Existe igual si el
             item está activo, aparcado, bloqueado o esperando en cola.

### Obligación
Toda capacidad con MÉTODO conversacional o iterativo con el Owner —DIS de forma
característica, pero también PRD, INV, USO y cualquier otra que delibere— DEBE
persistir su checkpoint como parte de su capa en curso. Para las demás es DEBERÍA.

CUÁNDO SE ESCRIBE: al cerrar cada paso del método, NO al terminar la sesión.
Esta regla es deliberada: si sólo se escribiera al final, una conversación cortada
en seco no dejaría nada. Escribiendo por paso, un corte abrupto pierde como mucho
un paso.

### Formato — vive en la ficha del item, bajo la capa de esa capacidad

    CHECKPOINT — DIS · GAP-014
    actualizado: 2026-08-25T18:40
    método:   DIS/Evolución · paso 2 de 5 (COMPARAR)
    resuelto: · dirección A (densidad alta, lista) descartada — no aguanta el
                texto largo del nombre de lote
              · paleta: se reutiliza el patrón "tabla operativa" (aprobado 2026-07-30)
    abierto:  ¿la fila expandible sustituye al detalle o convive con él?
              ← pregunta viva dirigida al Owner
    siguiente: explorar la 2ª dirección (detalle lateral) y compararla contra D3
    falta para cerrar la capa:
              · 2ª dirección explorada · comparación escrita · memoria de diseño
                actualizada
    contexto vivo: <enlaces a lo consultado — NUNCA copias del diálogo>

Reglas:
1. NO es una transcripción. Enlaces a fuentes, no copias. Un checkpoint que crece
   con cada turno de conversación es un log, y los logs no se releen.
2. `siguiente` es UNA acción concreta, no un área. "Seguir con el diseño" no es un
   checkpoint válido.
3. Un checkpoint desactualizado —la capacidad siguió trabajando y no lo escribió—
   es un defecto del sistema, no una omisión menor.
4. Escribir el checkpoint es parte del GATE DE SUSPENSIÓN, no del gate de
   terminación. Un equipo no puede soltar un item a medias sin dejarlo.

### PRUEBA DE REANUDACIÓN (criterio de corrección, comprobable)
Un checkpoint es correcto si y sólo si:

  el Owner abre un chat COMPLETAMENTE NUEVO, con un agente que no vio la
  conversación original, dice "retoma GAP-014 con Diseño", y ese agente continúa
  EXACTAMENTE desde el punto donde se cortó — sin reiniciar el método del equipo
  desde cero y sin pedirle al Owner que resuma lo ya hablado.

Si el agente nuevo necesita preguntar algo que ya se habló, el checkpoint estaba
mal escrito. Es un criterio verificable, no una aspiración: SIS puede probarlo.

### Relación con el tablero (sin duplicar)
La columna `necesita para avanzar` del tablero es la PROYECCIÓN EN UNA LÍNEA del
campo `siguiente` del checkpoint. El checkpoint completo vive sólo en la ficha.
DSP mantiene la correspondencia; no hay dos verdades.

### Relación con DSP
"Retoma el item X con [equipo]", en lenguaje natural, es una entrada de la función
ESTADO de DSP: localiza la ficha, carga el checkpoint de esa capacidad, y devuelve
el control a esa capacidad en su paso. No es un comando ni requiere sintaxis.

## a.10 — Derogaciones y ajustes sobre el kernel 1.3.0

  DEROGADAS   G11 (13 cajas de capacidades) → a.1-a.4
              G12 (orquestación sin tecnología) → DSP + SIS + sección (g)
              K0.9 (modo de fallo único) → a.6
  SUSTITUIDAS G14 → SIS · G07 embudo → protocolo de a.7, se cierra en (d)
              G26 JOURNAL narrativo → fichas + tableros
              G32 "debe existir un task system" → a.8, ya concreto
              G08 estado ejecutivo redactado → los tableros, leídos tal cual
  AJUSTADAS   G13 deja de ser proporcional al riesgo: es estructura por defecto de VER
              G34 escalado automático → recomposición de ruta trazada (a.5)
              G52 regla de retirada → se aplica a capacidades materializadas (a.4)
  PREVISTAS   G24 · G34 vía rápida · G53 → secciones (e), (f), (h)

NOTA SOBRE (e): esta corrección resuelve DE FACTO buena parte de la pregunta de la
vía rápida — una errata es un DEF con ruta `CON → VER`, compuesta por el mismo
enrutador y con la misma traza. No es un carril aparte. NO lo doy por cerrado: lo
confirmo contigo en la sección (e).

## a.11 — Decisiones abiertas de esta sección

B1  ENT como estación propia y no como parte de PLT. Justificado en a.3. ¿Lo apruebas?
B2  Coherencia documental en SIS y no en APR. Justificado en a.3. ¿Lo apruebas?
B3  Límite de devoluciones = 2 (dijiste 2-3). Elegí 2: la 1ª es información, la 2ª
    desacuerdo, la 3ª bucle. ¿2 o 3?
B4  Modo de fallo (b): ¿quieres un segundo indicador numérico —proporción de items
    tipo SIS frente a items de producto, con techo declarado— o te basta el límite
    de devoluciones? No lo decido solo porque es precisamente inventar mecanismo.
B5  Formato de tablero: tabla Markdown de 6 columnas con micro-gramática tipada.
    Alternativa que descarté: bloque YAML por entrada — parseo trivial, pero 20
    items x 8 campos = 160 líneas y dejas de poder escanearlo. ¿De acuerdo?
B6  La ficha del item: aquí defino los campos de ESTADO y el CHECKPOINT. El formato
    de las CAPAS TERMINADAS que cada capacidad escribe dentro es la sección (c).
    ¿Correcto?
B7  Checkpoint obligatorio en capacidades conversacionales (DIS, PRD, INV, USO) y
    DEBERÍA en el resto. ¿O lo quieres obligatorio en las catorce?
