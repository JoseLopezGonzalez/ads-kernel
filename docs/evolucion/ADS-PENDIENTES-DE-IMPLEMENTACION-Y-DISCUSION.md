# ADS — Pendientes de implementación y discusión tras F2

> **Estado:** documento vivo de trabajo con el Owner.  
> **Fecha de apertura:** 2026-08-27.  
> **Base revisada:** `redesign/kernel-2.0@a224c36ae4dde1e58158ce860f4875a3b8cb2b8a`.  
> **No es todavía especificación normativa ni autoriza a implementar automáticamente sus propuestas.**

## 1. Por qué existe este documento

ADS NEXT ordenó estudiar proyectos reales —principalmente PesquerApp—, extraer lo que funcionaba,
contrastarlo con ADS y después diseñar e implementar las mejoras que merecieran incorporarse.

El trabajo no llegó todavía a esa última parte completa:

```text
F0  baseline y mapa                         terminada
F1  minería de PesquerApp                   terminada: 29 candidatos
F2  contraste contra ADS                    terminada: veredictos y problemas registrados
M   mandato multi-repositorio               implementado de forma extraordinaria
F3  síntesis de los candidatos              NO iniciada
F4  arquitectura integrada                  NO iniciada
F5  enmiendas y contratos                   NO iniciada
F6  descomposición e implementación         NO iniciada
```

Por tanto, **la minería sí se realizó, pero la mayoría de sus conclusiones todavía no se ha
convertido en arquitectura ni implementación**. El mandato multi-repositorio interrumpió el paso
de F2 a F3 y resolvió principalmente la relación `producto != repositorio` y el gobierno Git
multi-source.

La corrección técnica de F2 que está ejecutándose actualmente es otro frente: debe arreglar los
defectos del tooling y del corpus multi-repo, pero no sustituye F3–F6 ni debe incorporar en silencio
los asuntos de este documento.

## 2. Qué sí quedó incorporado

- Un ADS Project gobierna un producto, no un repositorio.
- Un único control repo contiene gobierno, estado, PROFILE, kernel, packs y decisiones.
- `SOURCES.toml` declara las fuentes y componentes del producto.
- Los repositorios técnicos conservan Git, CI y despliegue independientes.
- Los paquetes declaran las fuentes que leen y escriben.
- Un item puede producir cambios en varias fuentes.
- `integration-set` representa las revisiones probadas conjuntamente.
- C6 define producto, fuente, componente y workspace.
- C7 distribuye las responsabilidades Git y evita cerrar con integración parcial.

Esto resuelve P-04 en su parte arquitectónica. No resuelve el resto de ADS NEXT.

## 3. Corrección técnica de F2 actualmente en curso

Debe mantenerse separada de la ampliación conceptual posterior. Incluye, al menos:

- seguridad de rutas reales y enlaces simbólicos;
- prohibición de fuentes dentro de `ads/` y de repositorios anidados;
- ausencia de efectos laterales ante un manifiesto inválido;
- redacción de secretos en todas las salidas;
- soporte correcto de remotes SSH;
- normalización conservadora de identidad Git;
- validación robusta de tipos e identificadores TOML;
- coherencia de rama inicial `main`;
- barrido de restos del modelo proyecto = repositorio;
- pruebas adversariales que demuestren cada corrección;
- retirada o corrección de afirmaciones de evidencia no demostradas.

**Estado:** en implementación por otro agente. No ampliar su alcance sin decisión expresa.

---

# BLOQUE A — Macrocircuitos de instalación, adopción y evolución

## 4. Proyecto nuevo: instalación y especialización

El Circuito 0 define el bootstrap de la organización, pero debe comprobarse si cubre de forma
suficientemente operativa todo lo necesario para un producto nuevo:

- creación del ADS Project;
- elaboración conversacional del PROFILE;
- selección y composición de packs;
- creación de adaptadores por entorno agentic;
- definición de repositorios o fuentes iniciales;
- compilación real de `AGENTS.md`;
- creación del estado persistido;
- preparación de CI, herramientas y permisos;
- certificación de que el sistema puede iniciar y recuperar una sesión mínima.

Debe decidirse si esto continúa siendo una única variante de Circuito 0 o si necesita un
macrocircuito de instalación explícito anterior a C0.

### 4.1. Recorrido regulado actualmente

La ruta A de `START_HERE.md` regula hoy este recorrido manual:

1. ejecutar `tooling/new-project.sh <producto> <blueprint>`;
2. obtener un workspace que no es Git y, dentro de él, un repositorio de control `ads/`;
3. crear y publicar el remoto de `ads/`;
4. declarar las fuentes técnicas en `SOURCES.toml`, que puede estar inicialmente vacío;
5. ejecutar `workspace.py check`, `init` y `status`;
6. completar `PROFILE.md` conversacionalmente;
7. obtener aprobación del Owner sobre éxito, riesgos, timebox y decisiones fuertes, provisionales
   o abiertas;
8. completar `PROJECT.md` con kernel, packs, extensiones y overrides;
9. entregar `BOOTSTRAP_PROMPT.md` al agente principal;
10. ejecutar C0 y demostrar sus diez entregables antes de comenzar a construir producto.

El repositorio de control debe contener la verdad organizativa y transversal. Los repositorios de
código son fuentes hermanas con Git, CI y despliegue propios.

### 4.2. Faseado actual después de la instalación

```text
PREPARACIÓN MANUAL
    creación de workspace, control repo, fuentes, PROFILE y PROJECT
        ↓
C0 · BOOTSTRAP ORGANIZATIVO
    organización, AGENTS, estado, memoria, tareas, documentación, Git y CI mínima
        ↓
C1 · DISCOVERY / DEFINITION
    producto, dominio, diseño, arquitectura, riesgos e investigación
        ↓
C2 · ENGINEERING BOOTSTRAP
    stack validado, repositorios técnicos, entornos, CI/CD, pruebas e integración
        ↓
C3 · PRODUCT BUILD
    construcción normal del producto
        ↓
C4 · CONTINUOUS EVOLUTION
    operación, mantenimiento, aprendizaje y adaptación
```

C0 está expresado mediante prompt, entregables y gate G22. C1–C4 existen como macrofases, pero
los gates C1→C2 y C2→C3 no están definidos canónicamente por el kernel: deben diseñarse durante el
bootstrap y aprobarse para cada producto.

### 4.3. Participantes actuales y carencias

- El **Owner** define y aprueba perfil, decisiones fuertes, riesgos y criterios de éxito.
- El **agente principal** ejecuta manualmente el bootstrap.
- **DSP** y **SIS** son las capacidades permanentes previstas para dirección y conformidad.
- **ENC** transforma la intención del Owner en entrada estructurada.
- PRD, INV, DOM, DIS, ARQ, SEG, PLT, VER, ENT, USO y otras capacidades se activan según el trabajo.

Todavía faltan para considerar este circuito completo:

- un método canónico ejecutable de instalación y C0, no sólo prosa y prompt;
- gates mínimos comunes para C1→C2 y C2→C3;
- runtime que conduzca y persista el recorrido;
- certificación estructural, operativa, integrada y de reanudación;
- prueba de que un agente nuevo puede retomar el producto sin contexto conversacional;
- separación formal entre instalar, adoptar, migrar y actualizar.

### 4.4. Recorrido candidato que deberá discutirse

Sin aprobar todavía su forma definitiva, el circuito de proyecto nuevo debería poder materializar:

```text
N0  Crear y publicar el control repo y el workspace
N1  Elaborar y aprobar PROFILE
N2  Elegir topología de fuentes, packs, extensiones y adaptadores
N3  Ejecutar C0 y dejar organización, estado, memoria y herramientas
N4  Certificar instalación y reanudación
N5  Ejecutar Discovery suficiente para producto, dominio y diseño
N6  Ejecutar Engineering Bootstrap con evidencia real
N7  Superar el gate «listo para construir» y entrar en C3
```

El objetivo no es llenar documentación antes de aprender, sino dejar explícito qué está decidido,
qué debe investigarse y qué evidencia autoriza cada transición.

### 4.5. Principio aceptado: ADS debe distribuirse preestructurado

Se acepta como dirección de diseño:

> **Una instalación no debe volver a diseñar ADS. Debe materializar una organización ya completa,
> descubrir el producto, rellenar sus huecos, especializarla y certificarla.**

El trabajo universal y determinista debe resolverse una vez dentro de la distribución de ADS. C0 no
debe pedir a cada agente que vuelva a redactar agentes, skills, prompts, carpetas, circuitos,
checkpoints, contratos, documentación y adaptadores desde cero.

La instalación debe partir de un blueprint de control repo sustancialmente completo, con campos
obligatorios, opcionales y pendientes explícitos. En un producto nuevo esos huecos se completan
mediante definición y descubrimiento; en uno existente se completan mediante inventario,
reconstrucción y contraste con su realidad.

### 4.6. Capas que deben separarse

| Capa | Momento de construcción | Responsabilidad |
|---|---|---|
| ADS canónico | En `ads-kernel` y su proceso de release | Capacidades, roles, métodos, procesos, circuitos, contratos, schemas, plantillas, validadores, blueprints y compiladores |
| Blueprint de proyecto | Antes de cualquier instalación real | Estructura completa del control repo y huecos tipados para especialización |
| Especialización del producto | Durante instalación o adopción | Identidad, fuentes, stack, arquitectura, dominio, diseño, riesgos, reglas, equipos y overrides reales |
| Proyección por entorno agentic | Al compilar o actualizar | Archivos e integraciones que Claude, Codex, Cursor, Copilot, Gemini u otros entornos puedan consumir |
| Estado operativo | Durante el trabajo | Items, paquetes, dossiers, checkpoints, evidencia, memoria y siguiente acción |

Una posible separación física, todavía no cerrada, sería:

```text
ADS DISTRIBUTION
├── catálogo canónico de capacidades, agentes y roles
├── métodos, procesos, circuitos y gates
├── contratos, schemas y plantillas
├── blueprints
├── adaptadores
├── compiladores
└── validadores

ADS PROJECT
├── PROFILE, PROJECT y SOURCES
├── especializaciones y overrides
├── estado, memoria y trabajo vivo
├── dossiers y documentación global
└── proyecciones generadas para cada entorno agentic
```

### 4.7. Contenido que debe venir preparado

La distribución debería poder materializar sin rediseño por proyecto:

- estructura de directorios y fuentes canónicas;
- PROFILE, PROJECT y SOURCES con schemas y campos guiados;
- estado, memoria, items, paquetes, rutas, handoffs y checkpoints;
- iniciativa amplia y dossier vivo;
- tipos de trabajo, contratos, gates y criterios de evidencia;
- circuitos de instalación, adopción, migración y actualización;
- certificación y mecanismo `doctor` o equivalente;
- catálogo completo de capacidades, agentes, roles y responsabilidades;
- métodos, prompts base y skills base;
- agentes permanentes y agentes activables;
- reglas Git y multi-repositorio;
- blueprints, adaptadores, compiladores y validadores;
- plantillas documentales y documentación de operación.

### 4.8. Contenido que sólo puede completarse al conocer el producto

Debe permanecer abierto, pero estructurado y validable:

- identidad, propósito, usuarios y definición de éxito;
- repositorios, fuentes, componentes e integraciones;
- arquitectura, dominio, datos y sistema de diseño reales;
- stack, comandos de build, pruebas, despliegue y operación;
- seguridad, permisos, regulación, restricciones y riesgos;
- decisiones fuertes, provisionales y todavía abiertas;
- backlog, ideas, gaps, deuda, incidentes e investigación;
- especializaciones, capacidades y skills propias del producto;
- herramientas y adaptadores realmente disponibles;
- gates particulares justificados por el riesgo del producto.

La distribución prepara los recipientes, contratos, métodos y validación; la instalación aporta la
verdad específica sin inventarla.

### 4.9. Catálogo completo frente a equipo activo

ADS debe traer definidos todos los agentes, capacidades, roles, métodos y prompts que forman su
catálogo soportado. Esto no obliga a inyectarlos todos en cada sesión.

Debe diferenciarse:

1. **catálogo completo disponible** en el control repo o distribución;
2. **equipo mínimo permanente** necesario para gobernar el sistema;
3. **agentes activados por el trabajo actual**;
4. **especialistas derivados del producto**.

La dirección candidata mantiene DSP y SIS de forma permanente, activa ENC ante entrada del Owner y
carga el resto según ruta, proceso y riesgo. De esta forma, la estructura queda preparada sin
sobrecargar contexto ni crear un equipo ficticiamente activo.

La composición exacta del equipo mínimo continúa pendiente de decisión y prueba real.

### 4.10. Fuente canónica y adaptadores para cada modelo

No deben mantenerse manualmente organizaciones independientes en `AGENTS.md`, `CLAUDE.md`, reglas
de Cursor, Copilot, Gemini u otros formatos. Esto produciría deriva entre instrucciones.

Debe existir una única definición canónica:

```text
DEFINICIÓN CANÓNICA ADS
        +
ESPECIALIZACIÓN DEL PRODUCTO
        ↓
COMPILADOR DE ADAPTADORES
        ↓
AGENTS.md · CLAUDE.md · reglas Cursor · Copilot · Gemini · otros soportados
```

Cada proyección generada debe registrar, como mínimo:

- versión de ADS;
- versión del adaptador;
- revisión de la especialización;
- origen canónico;
- aviso de archivo generado;
- huella que permita detectar edición manual o deriva.

Las particularidades persistentes deben editarse en configuración u overrides canónicos y después
recompilarse, no introducirse de forma divergente en cada archivo generado.

No se promete soporte certificado para cualquier modelo existente. Debe mantenerse una matriz:

| Nivel | Significado |
|---|---|
| Soportado | Adaptador probado y certificado |
| Compatible | Proyección disponible sin certificación integral |
| Genérico | Sólo recibe el contrato e instrucciones universales |
| Desconocido | Requiere diseñar o actualizar un adaptador |

La instalación detectará los entornos presentes y materializará únicamente las proyecciones
necesarias. La primera lista de entornos soportados continúa pendiente de decidirse y verificarse.

### 4.11. Consecuencia para C0

C0 mezcla actualmente instalación universal y especialización. La arquitectura futura debe mover a
la distribución todo lo genérico y determinista. C0 debería concentrarse en:

1. descubrir o definir el producto;
2. completar los campos variables;
3. seleccionar packs, extensiones y capacidades;
4. activar adaptadores y equipo necesario;
5. compilar las proyecciones agentic;
6. validar estructura, operación y reanudación;
7. obtener las aprobaciones del Owner.

Por tanto, el agente no crea ADS durante C0: **especializa y verifica una instalación previamente
materializada**.

## 5. Adopción de ADS en un producto existente

El repositorio contiene una ruta manual en `START_HERE.md`, pero **no existe todavía un
macrocircuito operativo completo** con método, estados, equipos, gates, handoffs y evidencia.

La adopción debe poder analizar:

- todos los repositorios y componentes;
- código, documentación e historial Git;
- CI, despliegue, entornos y observabilidad;
- arquitectura y stack reales;
- workflows, skills, prompts, agentes y herramientas existentes;
- decisiones documentadas y decisiones implementadas sin documentar;
- trabajo abierto, abandonado, duplicado o ya resuelto;
- riesgos, restricciones, deuda, fallos e integraciones;
- conocimiento local que merece conservarse.

### 5.1. Lo que la ruta actual permite realmente

La ruta B de `START_HERE.md` sólo regula una base manual:

1. crear un workspace y un repositorio de control `ads/` separados;
2. mover o clonar manualmente los repositorios existentes como fuentes hermanas;
3. declararlos en `SOURCES.toml`;
4. ejecutar `workspace check` y `ads_lint`;
5. pedir a un agente que lea código, documentación e historial Git sin modificar el producto;
6. completar `PROFILE.md` clasificando decisiones como fuertes, provisionales o no registradas;
7. añadir a C0 una lista de decisiones implementadas pero nunca documentadas;
8. continuar con el bootstrap general.

Para migrar un antiguo ADS monorrepositorio se limita a crear el nuevo control repo, copiar
PROFILE/PROJECT y gobierno, retirar del repositorio técnico kernel, packs y organización, y declarar
ese repositorio como fuente.

Esto instala la topología multi-repositorio, pero no demuestra una adopción completa del producto.
No hay todavía un procedimiento canónico que extraiga, reconcilie, migre, limpie y certifique toda
la realidad preexistente.

### 5.2. Diferencia entre lo operativo y lo ordenado por ADS NEXT

El Owner Brief sí exige investigar, según sea aplicable:

- documentación, código e historial;
- issues, tareas, tableros e ideas;
- CI/CD, pruebas, despliegue, bases de datos y migraciones;
- arquitectura, integraciones, seguridad y operación;
- agentes, skills, prompts, reglas, workflows y herramientas;
- decisiones, convenciones y conocimiento tácito;
- bugs, backlog, deuda, investigación y trabajo incompleto, abandonado o desplegado parcialmente.

También exige preservar procedencia, no convertir mecánicamente todo lo anterior en items ADS y no
reemplazar una buena solución existente sólo para homogeneizar. Estas exigencias son normativas o
directivas, pero todavía no están materializadas como fases, estados, checkpoints, handoffs,
plantillas, validadores y gates de adopción.

### Resultado mínimo de la adopción

Antes de que ADS gobierne activamente el producto debe existir un baseline con evidencia que
responda:

- qué existe y qué no;
- qué funciona, qué está roto y qué está incompleto;
- qué está desplegado;
- qué decisiones gobiernan realmente el producto;
- qué contradicciones y riesgos existen;
- qué especialización necesita el proyecto;
- qué mecanismos anteriores se conservan, se adaptan o se retiran.

### Conversión del trabajo preexistente

No se convierte mecánicamente cada issue, TODO o nota en item ADS. Cada elemento pasa por ENC y
puede resultar ser:

- observación;
- nota;
- idea inmadura;
- decisión;
- duplicado;
- trabajo ya resuelto;
- FEA, GAP, DEF, INC, INV, DEU, DEP, AUD, DIR o SIS;
- material que debe conservarse sin crear trabajo;
- material que debe retirarse.

Siempre debe conservarse su procedencia.

### Recorrido conceptual candidato

```text
INVENTARIO
   ↓
BASELINE CON EVIDENCIA
   ↓
CONSERVACIÓN Y CLASIFICACIÓN
   ↓
PROFILE + PACKS + ADAPTADORES + SOURCES
   ↓
INSTALACIÓN DE LA ORGANIZACIÓN
   ↓
CONVERSIÓN SELECTIVA DEL TRABAJO EXISTENTE
   ↓
CERTIFICACIÓN OPERATIVA
   ↓
ENTRADA EN EL MACROCIRCUITO REAL DEL PRODUCTO
```

Un producto existente puede incorporarse directamente a Discovery, Engineering Bootstrap,
Product Build o Evolución Continua. ADS no debe fingir que vuelve a empezar desde cero.

### Decisión pendiente

Elegir entre:

1. un macrocircuito nuevo `ADOPCIÓN`;
2. una variante formal de Circuito 0 para productos existentes;
3. una iniciativa amplia que componga procesos `AUD + INV + SIS + PLT + PRD + ARQ`, con gate
   propio de adopción.

La solución puede reutilizar procesos existentes; no debe crearse automáticamente un tipo de
proceso nuevo.

### 5.3. Propuesta pendiente: iniciativa y macrocircuito de adopción

La visión candidata es tratar la adopción como una **iniciativa amplia con dossier vivo** que
compone procesos existentes y posee un gate propio. Un producto existente puede encontrarse ya en
C2, C3 o C4; ADS no debe degradarlo ficticiamente a un proyecto vacío.

| Fase | Trabajo principal | Participantes principales | Resultado/gate |
|---|---|---|---|
| A0 · Apertura y protección | Abrir iniciativa, fijar alcance, fuentes, revisiones y modo inicialmente no destructivo | Owner, DSP, SIS, PLT | Perímetro y checkpoint inicial aprobados |
| A1 · Topología | Crear/publicar `ads/`, declarar fuentes, comprobar identidad, remotos, ramas y permisos | PLT | Workspace reproducible |
| A2 · Inventario | Examinar código, docs, Git, arquitectura, dominio, UI/UX, datos, CI/CD, pruebas, agentes, skills, backlog y operación | INV, ARQ, DOM, DIS, SEG, ENT, VER, PLT | Inventario con procedencia |
| A3 · Baseline | Clasificar qué funciona, está roto, incompleto, desplegado, obsoleto, duplicado o no verificado | SIS, INV, ARQ, VER, Owner | Verdad inicial aprobada |
| A4 · Conocimiento | Separar verdad global, verdad acoplada al código, duplicados, contradicciones y material obsoleto | SIS, especialistas, Owner | Mapa de conservación y migración |
| A5 · Especialización | Crear o adaptar PROFILE, PROJECT, packs, capacidades, agentes, skills, adaptadores, contratos, estado y memoria | SIS, DSP, ENC, PRD, Owner | ADS específico del producto |
| A6 · Reconstrucción | Documentar producto, arquitectura, dominio, datos, seguridad, operación, UI/UX y sistema de diseño reales | PRD, ARQ, DOM, DIS, USO, SEG, ENT | Baselines especializados y gaps explícitos |
| A7 · Trabajo vivo | Recuperar issues, TODO, ideas, bugs, deuda, auditorías, ramas y tareas; deduplicar y clasificar | ENC, DSP y especialistas | Backlog ADS con procedencia |
| A8 · Limpieza | Retirar copias organizativas y verdades paralelas sólo tras migrar y verificar | PLT, SIS, VER; autoriza Owner | Fuentes limpias con rollback |
| A9 · Certificación | Probar estructura, tooling, integración, seguridad, entrada de trabajo y reanudación | SIS, PLT, VER, SEG, DSP, ENC | Certificación por niveles |
| A10 · Preparación | Resolver bloqueos y determinar la macrofase real del producto | Owner y responsables anteriores | Gate «ahora puedes empezar a programar» |

Esta tabla no aprueba todavía nuevos tipos de proceso. Las etiquetas A0–A10 describen fases de una
composición coordinada; cada fase puede ejecutar procesos ADS existentes mediante paquetes e items.

### 5.4. Reparto candidato de responsabilidades

- **Owner:** aprueba baseline, contradicciones relevantes, decisiones fuertes, migraciones
  destructivas, dirección de producto/diseño y gate final.
- **ENC:** captura la intención y clasifica el trabajo histórico; evita copiar tareas mecánicamente.
- **DSP:** dirige orden, dependencias, handoffs, checkpoints y siguiente acción global.
- **SIS:** comprueba conformidad de la instalación, contratos y fuentes canónicas.
- **PLT:** materializa repositorios, workspace, herramientas, CI, adaptadores y reconstrucción.
- **INV:** realiza minería amplia de evidencia, historial, soluciones y conocimiento.
- **ARQ:** reconstruye arquitectura, dependencias y radio de impacto real entre fuentes.
- **DOM:** reconstruye dominio, reglas, datos y migraciones.
- **DIS/Reconstrucción:** extrae la UI/UX y el sistema de diseño que ya existen antes de proponer
  cambios.
- **PRD:** reconstruye propósito, usuarios, alcance, comportamiento y éxito del producto.
- **SEG:** revisa seguridad, privacidad, permisos y secretos.
- **ENT:** reconstruye despliegue, operación, entornos e integraciones reales.
- **USO:** contrasta el comportamiento con uso real cuando sea posible.
- **VER independiente:** prueba evidencias y certificación sin confiar sólo en quien instaló.
- **APR:** promueve a conocimiento reusable los aprendizajes demostrados.
- **CON:** no debería modificar producto durante la fase de observación, salvo tooling o
  experimentos expresamente autorizados; la construcción normal comienza tras el gate.

### 5.5. Clasificación obligatoria de la documentación

La aspiración de reunir toda la verdad del producto en ADS necesita esta distinción:

| Clase | Ubicación canónica |
|---|---|
| Gobierno, PROFILE, PROJECT, estado, items, rutas, paquetes, memoria, ADR globales, contratos maestros, kernel, packs y organización global | Control repo `ads/` |
| Producto, arquitectura transversal, dominio global, experiencia y sistema de diseño maestros | Control repo `ads/` |
| README de build, instrucciones de desarrollo de un componente, migraciones, configuración, CI local, API o documentación generada/acoplada al código | Fuente técnica correspondiente |
| Contenido que afecta a ambos niveles | Una única fuente canónica y referencias desde el otro nivel |
| Copias, contradicciones y material obsoleto | Resolver, archivar o eliminar después de demostrar sustitución |

Por tanto, **no debe trasladarse literalmente toda la documentación al control repo**. Debe moverse
la verdad global; la documentación cuya utilidad depende del código debe permanecer junto a él.

### 5.6. Reglas de seguridad para migrar y limpiar

- No borrar agentes, skills, prompts, documentación, issues ni backlogs al descubrirlos.
- Registrar fuente, ruta, revisión, identidad y relación antes de transformar cada pieza.
- Importar, referenciar o reemplazar primero; validar después; retirar al final.
- Separar la limpieza en commits revisables por fuente.
- Mantener rollback y evidencia de que existe una fuente canónica sustituta.
- Comprobar build, pruebas, CI, despliegue y comportamiento agentic tras cada retirada.
- No convertir cada elemento histórico en trabajo actual: debe pasar por ENC/anclaje.
- Preservar las soluciones existentes que funcionan; envolverlas o adaptarlas antes de sustituirlas
  sólo por uniformidad.

### 5.7. Reconstrucción de producto, UI/UX y sistema de diseño

En un producto existente no debe crearse automáticamente un sistema de diseño desde cero. El
procedimiento candidato es:

1. inventariar pantallas, flujos, componentes, tokens, patrones, accesibilidad y estados;
2. extraer el sistema de diseño de facto presente en producto y código;
3. identificar inconsistencias, excepciones y deuda;
4. separar con claridad «sistema vigente» de «sistema deseado»;
5. documentar el baseline con evidencia;
6. crear DIR, GAP, FEA, AUD o INV para los cambios que merezcan trabajo;
7. someter la dirección futura a aprobación del Owner.

La misma lógica se aplica a arquitectura, dominio, stack y operación: descubrir y evaluar antes de
rediseñar.

### 5.8. Conversión del trabajo histórico

Cada issue, TODO, rama, nota, auditoría, idea o gap debe recorrer:

```text
IDENTIFICACIÓN Y PROCEDENCIA
        ↓
DEDUPLICACIÓN Y CONTRASTE CON EL PRODUCTO REAL
        ↓
CLASIFICACIÓN POR ENC
        ↓
CONVERSIÓN SELECTIVA EN ITEM ADS
        ↓
AGRUPACIÓN EN INICIATIVA/DOSSIER Y PRIORIZACIÓN
        ↓
ESTADO, EVIDENCIA Y SIGUIENTE ACCIÓN
```

Los resultados posibles incluyen evidencia, decisión histórica, observación, idea inmadura,
duplicado, asunto ya resuelto o un tipo de trabajo ADS. El origen nunca debe desaparecer.

### 5.9. Gate candidato «Ahora puedes empezar a programar»

El gate de adopción debería exigir, como mínimo:

- fuentes identificadas y revisiones verificadas;
- baseline aceptado;
- material organizativo y agentic clasificado;
- PROFILE y PROJECT aprobados;
- arquitectura, dominio, producto, diseño, pruebas, seguridad y operación suficientemente conocidos;
- backlog anterior clasificado y con procedencia;
- verdades canónicas definidas y duplicados relevantes resueltos;
- agentes, skills, adaptadores, CI y validadores probados;
- limpieza efectuada de forma verificable y reversible;
- riesgos e incógnitas restantes transformados en trabajo explícito;
- reanudación satisfactoria por un agente sin contexto conversacional;
- certificación de SIS, PLT y VER, con SEG cuando corresponda;
- aprobación final del Owner.

El gate no debe exigir una enciclopedia antes de permitir código. Debe demostrar que lo necesario
para cambiar el producto con seguridad está conocido y que lo desconocido está identificado,
clasificado y bloquea sólo cuando su riesgo lo exige.

### 5.10. Persistencia entre chats y agentes

Toda la adopción debe estar gobernada por una iniciativa amplia y un dossier vivo, no por la memoria
de un chat. Ese dossier debe contener:

- objetivo, alcance y fuentes/revisiones;
- fase actual y checkpoint;
- inventario y baseline;
- hallazgos, contradicciones y decisiones;
- migraciones realizadas y retiradas pendientes;
- items, paquetes y procesos relacionados;
- evidencias y criterios de gate;
- riesgos, bloqueos y aprobación del Owner;
- siguiente acción exacta y condiciones de cierre.

Cada agente debe leerlo, reclamar un paquete acotado, registrar evidencia, actualizar su checkpoint
y dejar una siguiente acción reanudable. Terminar un paquete no equivale a cerrar la adopción.

El ADS actual posee paquetes y checkpoints, pero todavía no una coordinación superior plenamente
implementada. Esta necesidad enlaza directamente con el **BLOQUE C — Unidad amplia de trabajo y
dossier vivo**.

### 5.11. Principio aceptado: documentación viva global del producto

Se acepta que el control repo ADS debe contener la documentación viva que **define, explica y
dirige el producto completo**, incluyendo producto, diseño, arquitectura, dominio, tecnologías,
entornos, despliegue, calidad, seguridad, operación y evolución.

La salvedad de C6 sobre documentación local no excluye estos documentos. Sólo reserva para cada
fuente técnica la documentación cuya utilidad depende estrechamente de su código. El control repo
debe mantener el mapa global, la dirección, las reglas, las decisiones y los enlaces canónicos.

La documentación debe permitir que un agente sin contexto conversacional responda:

- qué producto es, para quién existe y qué problema resuelve;
- qué existe realmente y qué está desplegado;
- hacia dónde se dirige cada área y por qué;
- cómo está diseñado y construido;
- qué tecnologías, entornos e integraciones utiliza;
- cómo se desarrolla, valida, despliega, opera y recupera;
- qué decisiones, restricciones, riesgos y excepciones gobiernan;
- qué está aprobado, qué es provisional y qué no está demostrado.

### 5.12. Cuatro vistas que no deben confundirse

Para producto, diseño, arquitectura, dominio, tecnología, seguridad y operación deben distinguirse:

| Vista | Pregunta |
|---|---|
| Baseline actual | ¿Qué existe y funciona realmente hoy? |
| Dirección | ¿Hacia dónde queremos evolucionar y por qué? |
| Sistema, principios o reglas | ¿Qué patrones, límites y criterios deben respetarse? |
| Decisiones | ¿Por qué se eligió, cambió o exceptuó algo concreto? |

Un documento puede agrupar varias vistas en proyectos pequeños, pero debe mantenerlas
semánticamente separadas. Una arquitectura objetivo no puede presentarse como implementada; una
convención accidental no puede presentarse como principio aprobado.

### 5.13. Familias documentales canónicas

Estas son familias lógicas. El blueprint puede compactarlas o expandirlas según tamaño, riesgo y
naturaleza del producto.

| Familia | Contenido gobernante | Aplicación inicial |
|---|---|---|
| Mapa documental | Índice, fuentes canónicas, responsables, estado, relaciones y documentos locales | Obligatoria |
| Identidad y dirección de producto | Visión, propósito, usuarios, valor, alcance, no-alcance, éxito y evolución | Obligatoria |
| Baseline funcional | Capacidades, comportamiento, flujos, estados, permisos y límites reales | Obligatoria |
| Usuarios y experiencia | Perfiles, necesidades, journeys, investigación, usabilidad y accesibilidad | Según producto, normalmente obligatoria si tiene interacción humana |
| Dirección de diseño | Personalidad, principios, referencias, lenguaje visual, UX, responsive y anti-patrones | Obligatoria cuando existe interfaz o experiencia diseñada |
| Sistema de diseño | Tokens, componentes, variantes, estados, patrones, accesibilidad y vínculo con código | Condicional por interfaz y madurez |
| Dominio y glosario | Conceptos, entidades, estados, reglas, cálculos, eventos, invariantes y vocabulario | Obligatoria |
| Arquitectura actual | Contexto, componentes, fuentes, dependencias, flujos, fronteras, persistencia y despliegue | Obligatoria |
| Dirección arquitectónica | Principios, propiedades objetivo, límites, evolución, deuda y arquitectura deseada | Obligatoria |
| Tecnologías y entorno de desarrollo | Stack, lenguajes, frameworks, servicios, versiones, herramientas, requisitos e instrucciones | Obligatoria |
| Datos | Modelo, propiedad, fuentes de verdad, calidad, retención, migración, privacidad y recuperación | Condicional por complejidad de datos |
| Integraciones | Sistemas externos, contratos, autenticación, datos, errores, límites, versiones y pruebas | Condicional |
| Dirección de ingeniería | Convenciones, repositorios, dependencias, compatibilidad, revisión, releases y deuda | Obligatoria |
| Calidad y pruebas | Estrategia, niveles, entornos, datos, regresión, rendimiento, accesibilidad y gates | Obligatoria |
| Seguridad, privacidad y cumplimiento | Amenazas, activos, permisos, secretos, regulación, controles e incidentes | Obligatoria, con profundidad proporcional al riesgo |
| Despliegue, entornos y operación | CI/CD, entornos, configuración, infraestructura, observabilidad, rollback y continuidad | Obligatoria |
| Decisiones | Contexto, opciones, resolución, consecuencias, evidencia y revisión | Obligatoria |
| Riesgos, restricciones y deuda estratégica | Riesgos, limitaciones, supuestos, dependencias críticas y decisiones temporales | Obligatoria |
| Dirección y evolución | Situación, prioridades, iniciativas, hitos, aplazamientos y rumbo aprobado | Obligatoria |

### 5.14. Contenido mínimo por familia

#### Producto y experiencia

- visión, propósito, problema y propuesta de valor;
- usuarios, actores, permisos y contextos de uso;
- alcance, no-alcance y definición de éxito;
- capacidades y comportamiento actual;
- journeys, flujos, estados y excepciones;
- principios de producto y experiencia;
- métricas y evidencia de uso cuando exista;
- dirección futura y preguntas abiertas.

`PROFILE` debe conservar la síntesis operativa y enlazar a la documentación desarrollada. No debe
mantenerse una segunda verdad contradictoria.

#### Dirección de diseño y sistema de diseño

- personalidad y sensaciones que debe transmitir;
- principios y objetivos UX;
- referencias aprobadas y rechazadas con motivo;
- lenguaje visual, composición, jerarquía y densidad;
- color, tipografía, iconografía, ilustración y movimiento;
- responsive, plataformas y accesibilidad;
- tokens, grids, espaciado, bordes, elevación y escalas;
- componentes, variantes, estados, formularios, tablas, navegación y feedback;
- patrones de carga, vacío, error, permisos y confirmación;
- vínculo entre especificación y componentes implementados;
- sistema vigente, sistema deseado, excepciones y deuda.

#### Dominio y datos

- glosario canónico;
- entidades, relaciones, estados y ciclos de vida;
- reglas, invariantes, cálculos, eventos y excepciones;
- propiedad y fuentes de verdad de los datos;
- clasificación, sensibilidad, retención y borrado;
- sincronización, migraciones, trazabilidad, analítica y recuperación;
- decisiones y gaps del modelo.

#### Arquitectura e integraciones

- contexto del sistema y fronteras del producto;
- aplicaciones, servicios, componentes y repositorios;
- responsabilidades, dependencias y flujos;
- persistencia, comunicaciones y contratos;
- integraciones externas, autenticación, límites, errores y reintentos;
- arquitectura desplegada por entorno;
- restricciones y puntos críticos;
- arquitectura objetivo y camino de evolución;
- deuda, excepciones y decisiones relacionadas.

### 5.15. Tecnologías, herramientas e instrucciones de desarrollo

El control repo debe ofrecer una visión profesional y reproducible de:

- lenguajes, frameworks, runtimes, bases de datos, colas, servicios y proveedores;
- versiones soportadas, restricciones y política de actualización/EOL;
- motivo y estado de cada elección: vigente, provisional, heredada o en retirada;
- herramientas de desarrollo, gestores de paquetes y generadores;
- sistemas operativos y dependencias necesarias;
- variables de entorno y configuración, sin almacenar secretos;
- acceso y permisos necesarios;
- preparación de una máquina o entorno de agente;
- arranque del producto completo y orden de sus componentes;
- comandos coordinados de build, lint, pruebas y ejecución;
- datos y servicios locales de desarrollo;
- diferencias entre desarrollo, pruebas, staging y producción;
- resolución de problemas comunes;
- enlaces a las instrucciones técnicas detalladas de cada fuente.

El documento global explica el stack completo y cómo cooperan sus piezas. Cada fuente conserva los
comandos y detalles íntimamente acoplados a su implementación. ADS debe poder comprobar que los
enlaces y comandos declarados siguen siendo válidos.

### 5.16. Despliegue, entornos y operación

La documentación global debe cubrir:

- mapa de entornos y finalidad de cada uno;
- componentes desplegados, ubicación, versión y dependencias;
- infraestructura y servicios gestionados;
- pipelines de CI/CD y condiciones de promoción;
- configuración por entorno y gestión de secretos;
- migraciones, orden de despliegue y compatibilidad;
- instrucciones de release, rollback y recuperación;
- smoke tests y verificaciones posteriores;
- dominios, certificados, redes y permisos relevantes;
- observabilidad, logs, métricas, trazas y alertas;
- backups, restauración, continuidad y objetivos operativos;
- responsables, escalado, soporte e incidentes;
- diferencias entre estado diseñado, configurado y realmente desplegado.

Los runbooks exclusivos de un servicio pueden vivir en su fuente, pero el producto debe tener un
mapa operativo global y una ruta reproducible que los enlace. Un cambio de despliegue que afecte al
producto completo debe actualizar la documentación global y no sólo el README de un repositorio.

### 5.17. Calidad, seguridad y decisiones

La estrategia de calidad debe definir qué significa calidad para el producto, criticidad, tipos de
prueba, datos y entornos de validación, regresión, rendimiento, accesibilidad, evidencia y gates.

Seguridad debe recoger amenazas, activos, roles, autenticación, autorización, secretos, privacidad,
regulación, dependencias, respuesta a incidentes, controles y riesgos aceptados.

Debe existir un único contrato de decisión aplicable a producto, diseño, dominio, arquitectura,
tecnología, seguridad y operación. Cada registro debe contener contexto, opciones, decisión, motivo,
consecuencias, evidencia, responsables, fecha, estado, ámbito y condición de revisión.

### 5.18. Núcleo obligatorio y documentación condicional

El contrato documental mínimo debe exigir en todo producto:

1. mapa documental;
2. identidad y dirección de producto;
3. baseline funcional;
4. dominio y glosario;
5. arquitectura actual y dirección arquitectónica;
6. tecnologías e instrucciones de desarrollo;
7. dirección de ingeniería;
8. calidad y pruebas;
9. seguridad y riesgos;
10. despliegue, entornos y operación;
11. decisiones;
12. dirección de evolución y gaps documentales.

Se activan según el producto: UX e investigación, dirección visual, sistema de diseño, arquitectura
de datos detallada, integraciones, cumplimiento regulatorio, modelo de amenazas avanzado,
observabilidad, continuidad, analítica, dispositivos, internacionalización o gobierno de IA.

«No aplicable» debe ser una evaluación registrada, no una ausencia silenciosa. El blueprint puede
materializar plantillas completas o slots declarados por el manifiesto, evitando archivos vacíos sin
propósito.

### 5.19. Estados, procedencia y vigencia

Cada documento gobernante debe declarar:

- estado: no evaluado, observado, provisional, aprobado, necesita revisión o sustituido;
- ámbito y fuente canónica;
- capacidad o responsable;
- última verificación real, no sólo última edición;
- fuentes, entornos y revisiones examinadas;
- decisiones, items y dossiers relacionados;
- lagunas y contradicciones conocidas;
- eventos que obligan a revisarlo.

Las afirmaciones reconstruidas durante una adopción deben distinguir si fueron observadas,
inferidas, tomadas de documentación anterior, confirmadas por uso, aprobadas por el Owner o siguen
sin verificar.

### 5.20. Eventos que deben actualizar documentación

Las rutas ADS deben incorporar actualización documental cuando ocurra, entre otros:

- cambio fuerte de producto o diseño;
- nueva pantalla, flujo, componente o patrón;
- cambio de arquitectura, tecnología o dependencia estructural;
- nueva fuente, integración, entorno o proveedor;
- modificación de datos, migraciones o reglas de dominio;
- cambio de CI/CD, despliegue, configuración u operación;
- cambio de seguridad, permisos, secretos o regulación;
- incidente, aprendizaje de uso o auditoría;
- release relevante, ADR aprobada o cierre de iniciativa;
- divergencia detectada entre documentación, código y despliegue.

DSP debe incluir la revisión en la ruta y el gate; cada especialista mantiene su área; SIS comprueba
conformidad y fuentes canónicas; VER contrasta afirmaciones críticas.

### 5.21. Extracción y reconstrucción durante la adopción

El recorrido A0–A10 debe:

1. localizar todos los documentos y artefactos existentes;
2. contrastarlos con código, pantallas, historial, CI, entornos y despliegues;
3. clasificar fuente canónica, documento local, evidencia, copia, contradicción u obsolescencia;
4. separar baseline actual, dirección deseada, reglas y decisiones;
5. reconstruir los documentos globales ausentes;
6. extraer producto, dominio, arquitectura, tecnologías, UI/UX y sistema de diseño de facto;
7. reconstruir desarrollo, entornos, despliegue y operación reales;
8. presentar al Owner las direcciones o decisiones que no puedan demostrarse;
9. crear gaps para lo desconocido;
10. retirar documentos antiguos sólo cuando exista sustituto verificado y rollback.

### 5.22. Ubicación global y documentación local

| Contenido | Fuente canónica |
|---|---|
| Dirección de producto, diseño, arquitectura, tecnología, calidad, seguridad y operación | Control repo ADS |
| Baseline global, mapa de componentes, entornos, integraciones y despliegue | Control repo ADS |
| Decisiones globales, riesgos, evolución, dossiers y evidencia transversal | Control repo ADS |
| Instalación y comandos exactos de un componente | Su fuente técnica, enlazada desde ADS |
| API o documentación generada desde código | Su fuente técnica |
| Migración concreta, configuración local, CI propia o runbook exclusivo | Su fuente técnica, promoviendo a ADS cualquier impacto global |

Debe existir una sola verdad por asunto. El control repo no copiará documentación local sólo para
centralizarla; la enlazará, gobernará su existencia y promoverá sus consecuencias globales.

### 5.23. Contrato o manifiesto documental

ADS necesita un contrato verificable que declare:

- familias aplicables, obligatorias, condicionales y no aplicables;
- documentos o secciones que las materializan;
- fuente canónica y enlaces locales;
- responsables y capacidades;
- estado, evidencia y última verificación;
- triggers y frecuencia de revisión;
- relaciones entre documentos, decisiones, items, fuentes y dossiers;
- gaps y excepciones aprobadas.

SIS debería poder detectar documentos ausentes, duplicados, sin responsable, obsoletos, no
verificados o con enlaces rotos; direcciones sin aprobación; baselines presentados como objetivos;
y cambios relevantes que no actualizaron la documentación afectada.

La forma física exacta —un manifiesto específico, metadata distribuida o ambos— queda pendiente de
diseño. El contrato común debe permitir una presentación compacta en productos pequeños y una
estructura expandida en productos grandes o regulados.

### 5.24. Responsabilidad documental por capacidad

- **PRD:** identidad, dirección de producto, alcance, usuarios y baseline funcional.
- **DIS:** experiencia, dirección de diseño, sistema de diseño y accesibilidad.
- **DOM:** dominio, reglas, glosario, datos y eventos.
- **ARQ:** arquitectura actual, dirección, componentes, dependencias e integraciones.
- **PLT:** tecnologías, entorno de desarrollo, repositorios, herramientas, CI/CD e infraestructura.
- **ENT:** despliegue, entornos, operación, observabilidad, releases y recuperación.
- **VER:** estrategia de calidad, pruebas, evidencia y vigencia contrastada.
- **SEG:** seguridad, privacidad, cumplimiento, permisos y amenazas.
- **ENC:** captura y anclaje de nuevas direcciones o decisiones del Owner.
- **DSP:** inclusión de actualización documental en rutas, handoffs y gates.
- **SIS:** contrato documental, conformidad, duplicidades y auditoría de vigencia.
- **Owner:** aprobación de direcciones, decisiones fuertes, riesgos aceptados y excepciones.

La responsabilidad no implica que una capacidad escriba aislada: debe usar evidencia de código,
fuentes, otros especialistas, uso real y decisiones del Owner.

## 6. Migración desde una versión anterior de ADS

Debe distinguirse de adoptar un producto sin ADS. Debe cubrir:

- disposición antigua de un solo repositorio;
- separación del control repo y las fuentes;
- conservación de PROFILE, decisiones, documentación y memoria;
- migración de estado persistido;
- reemplazo de mecanismos retirados;
- tratamiento de overrides y forks locales;
- compatibilidad con items y paquetes en curso;
- validación y rollback de la migración.

## 7. Actualización de ADS en proyectos ya instalados

Principio aceptado:

> **Detectar automáticamente; actualizar conscientemente.**

Debe existir un ciclo equivalente a:

```text
versión instalada
   ↓
versión candidata detectada
   ↓
comparación comprensible
   ↓
impacto y compatibilidad en este producto
   ↓
plan de migración
   ↓
aplicación controlada
   ↓
certificación
   ↓
rollback disponible
```

La actualización debe considerar kernel, packs, skills, adaptadores, tooling, runtime, esquemas,
estado, PROFILE, overrides, personalizaciones, documentación generada y trabajo en curso.

Debe decidirse si se expresa con procesos existentes —por ejemplo SIS, DEP y PLT— o necesita una
composición de macrocircuito propia. No se creará un proceso nuevo sólo por comodidad nominal.

---

# BLOQUE B — Certificación de una instalación ADS

## 8. Lo que SIS/Conformidad cubre actualmente

SIS es el propietario conceptual correcto de la conformidad. El método existente comprueba:

- validadores del corpus;
- extensiones de kernel, packs y PROFILE;
- duplicación de fuentes de verdad;
- documentos sin consumidor operativo;
- correspondencia entre pruebas, estado declarado y evidencia;
- enrutamiento de hallazgos a su capacidad propietaria.

Esto demuestra principalmente **conformidad estructural del corpus**.

## 9. Lo que todavía no demuestra

No basta para afirmar que ADS está completamente instaurado y operativo. Falta demostrar que:

- un agente nuevo puede iniciar ADS sin contexto oral;
- el adaptador de cada entorno agentic funciona;
- los repositorios y fuentes son accesibles con los permisos correctos;
- el agente entiende dónde puede leer y escribir;
- ENC puede recibir una expresión mínima;
- DSP/runtime puede crear y persistir un item mínimo;
- puede escribirse y recuperarse un checkpoint;
- `Continúa` puede reanudar sin pedir un resumen al Owner;
- los comandos reales del producto funcionan;
- CI, validadores y tooling son ejecutables;
- no existen copias divergentes entre núcleo, adaptadores y skills;
- un trabajo multi-source mínimo puede verificarse como conjunto;
- un fallo de instalación puede diagnosticarse y revertirse.

## 10. Propuesta de certificación por niveles

| Nivel | Qué autoriza a afirmar |
|---|---|
| **Estructural** | Los archivos, contratos y referencias necesarios existen y son coherentes. |
| **Operativo** | Una sesión nueva puede arrancar, interpretar el proyecto y persistir/recuperar un checkpoint. |
| **Integrado** | Fuentes, herramientas, CI, permisos y adaptadores funcionan en el entorno real. |
| **Completo** | Runtime, despacho, reanudación, concurrencia, integración y recuperación están demostrados. |

No debe declararse un nivel superior por argumento ni porque pase el nivel anterior.

## 11. Participantes de la certificación

| Capacidad | Responsabilidad |
|---|---|
| **SIS/Conformidad** | Posee el contrato, ejecuta la auditoría estructural y emite el estado de conformidad. |
| **PLT** | Comprueba instalación física, repositorios, comandos, herramientas, CI y adaptadores. |
| **VER independiente** | Ejecuta la prueba de humo sin haber participado en la instalación y produce el dosier. |
| **SEG** | Revisa permisos, secretos y exposición cuando exista superficie sensible. |
| **ENC + DSP/runtime** | Demuestran entrada, persistencia, despacho y reanudación mínima. |

SIS debe ser propietario, pero no puede ser el único productor y único crítico de su propia
instalación.

## 12. Gate obligatorio de certificación

Debe ejecutarse al menos:

- al cerrar Circuito 0;
- al cerrar una adopción;
- al cerrar una migración desde ADS anterior;
- tras una actualización relevante de kernel, packs o esquemas;
- tras cambiar runtime o adaptador principal;
- cuando una auditoría detecte deriva entre fuentes de verdad.

Salida requerida: **dosier de certificación**, con nivel alcanzado, evidencia, elementos no
comprobados, limitaciones y rollback.

---

# BLOQUE C — Unidad amplia de trabajo y dosier vivo

## 13. Necesidad aceptada, diseño pendiente

Está aceptada la necesidad de una unidad persistente superior al paquete y capaz de agrupar
varios items relacionados. Todavía no tiene nombre, esquema, propietario, gate ni implementación.

No debe diseñarse sólo para features. Casos de uso:

- feature grande;
- auditoría extensa;
- adopción o migración de ADS;
- nueva lógica de negocio;
- cambio arquitectónico amplio;
- cambio de dirección;
- investigación compleja;
- programa de seguridad;
- integración externa;
- transformación de datos;
- evolución importante del propio ADS;
- cualquier trabajo que atraviese varios items, procesos, repositorios o releases.

## 14. Relación con las unidades existentes

```text
UNIDAD AMPLIA — nombre pendiente
├── intención o pregunta global
├── dosier vivo
├── decisiones, contratos, riesgos y evidencia
├── ITEM-1 · un proceso ADS
│   └── paquetes ejecutables
├── ITEM-2 · otro proceso ADS
│   └── paquetes ejecutables
└── ITEM-N
    └── source changes e Integration Sets
```

- La unidad amplia coordina y conserva sentido global.
- El item sigue representando un resultado concreto y tiene exactamente un proceso.
- El paquete sigue siendo la unidad de custodia y ejecución.
- El source change sigue siendo la mutación Git en una fuente.
- El Integration Set sigue representando la combinación verificada.

La unidad amplia **no sustituye ni debilita los paquetes**.

## 15. Dossier vivo

Debe ser índice y memoria, no una copia de todas las fuentes.

### Antes

- por qué existe;
- resultado o pregunta global;
- alcance y fuera de alcance;
- riesgos y alternativas;
- dependencias;
- contratos previstos;
- impacto esperado.

### Durante

- decisiones tomadas y sustituidas;
- cambios de alcance;
- items y paquetes derivados;
- componentes y fuentes afectados;
- versiones de contratos;
- bloqueos;
- evidencia;
- estado de integración.

### Después

- qué terminó existiendo realmente;
- qué fue descartado o retirado;
- decisiones finales;
- commits, Integration Sets y releases;
- evidencia final;
- deuda o trabajo derivado;
- aprendizaje.

Las decisiones permanecen en ADR o en su fuente canónica; los contratos en su fuente; el estado en
los items; la evidencia en sus artefactos. El dossier los enlaza y explica la relación.

## 16. Activación: evitar burocracia

Debe activarse sólo cuando exista al menos una señal objetiva de entidad suficiente. Criterios
candidatos para discutir:

- requiere varios items;
- atraviesa varios procesos;
- afecta a varios componentes o repositorios;
- tiene varias decisiones o contratos relevantes;
- dura varias sesiones o releases;
- necesita memoria propia para conservar el sentido global;
- su cierre no puede explicarse mediante un único item;
- el Owner necesita seguirlo como una unidad;
- requiere coordinación continuada entre varias capacidades.

Un bug pequeño, una dependencia rutinaria o una feature localizada deben continuar usando solamente
item y paquetes.

## 17. Decisiones pendientes sobre esta unidad

1. Nombre: `iniciativa`, `expediente`, `programa`, `workstream` u otro.
2. Si es un nuevo tipo canónico o una composición de artefactos existentes.
3. Quién puede crearla y cerrarla.
4. Si tiene propietario global propio o deriva de los items.
5. Si admite items con distintos propietarios y procesos.
6. Si puede contener otras unidades amplias o se prohíbe la anidación.
7. Dónde vive físicamente el dossier.
8. Cómo se calcula su estado global.
9. Qué gate permite cerrarla.
10. Cómo se representa en el estado ejecutivo del Owner.
11. Cómo evita duplicar las fuentes canónicas de los items.
12. Qué umbral exacto activa su creación.

---

# BLOQUE D — Problemas de PesquerApp aún sin sintetizar

## 18. P-01 · Adaptadores sin contrato

ADS exige neutralidad de proveedor, pero el adaptador que traduce perfiles ADS a Claude, Codex,
Cursor, Gemini u otro entorno:

- no es tipo canónico;
- no tiene propietario;
- no tiene gate;
- no lo produce ninguna ruta;
- no se crea al instalar;
- no tiene prueba de humo obligatoria;
- no declara de forma canónica comandos, permisos, capacidades y degradaciones.

Debe diseñarse el contrato del adaptador y su relación con C6/C7, PLT, SIS y PROFILE.

## 19. P-02 · Conocimiento externo incorporado

No existe posición clara para skills de terceros, presets o doctrinas externas. Debe gobernarse:

- origen;
- versión;
- hash o integridad;
- licencia;
- autoridad y precedencia;
- actualización;
- retirada;
- diferencias frente a las reglas del proyecto.

No debe confundirse con una posible capa de conocimiento propio reutilizable.

## 20. P-03 · Calidad persistente por área del producto

ADS mide avance de items, pero no conserva bien cómo evoluciona la calidad de un área funcional a
lo largo del tiempo.

### 20.1. Dirección aceptada: sistema permanente de auditoría y mejora

Se acepta que ADS necesita un **sistema permanente de aseguramiento, auditoría y mejora continua**.
No debe depender de que el Owner recuerde qué bloque pedir, qué especialidad revisar, qué findings
quedaron pendientes o cuándo volver a auditar.

`AUD` seguirá representando una auditoría concreta. Por encima debe existir un subsistema que
gobierne:

- universo auditable;
- dimensiones de calidad aplicables;
- cobertura y vigencia;
- planificación por eventos, riesgo y recurrencia;
- ejecución especializada;
- findings y causas raíz;
- campañas de corrección;
- verificación independiente;
- prevención de regresión;
- reauditoría.

No se aprueba automáticamente una capacidad nueva. La solución candidata compone SIS, DSP, ENC,
AUD, especialistas, CON, VER y APR, integrada con runtime, CI, documentación, items, paquetes,
dossiers y gates.

### 20.2. Problema que debe eliminar

El recorrido manual actual convierte al Owner en planificador y memoria del control de calidad:

1. el Owner sospecha qué revisar;
2. solicita una auditoría y delimita el bloque;
3. el agente genera gaps o findings;
4. el Owner revisa y ordena correcciones;
5. debe recordar lo que quedó atrás;
6. debe decidir cuándo y dónde volver a auditar.

El sistema futuro debe poder responder por sí mismo:

> ¿Qué existe en el producto, qué dimensiones le aplican, qué nunca fue auditado, qué auditoría ha
> caducado, qué findings siguen abiertos, qué se está corrigiendo y cuándo volverá a revisarse?

### 20.3. Universo auditable

Debe inventariar, según el producto:

- aplicaciones, repositorios, fuentes y componentes;
- módulos, áreas funcionales, pantallas, flujos y formularios;
- componentes visuales y patrones;
- servicios, APIs, integraciones y contratos;
- entidades, reglas, datos y migraciones;
- entornos, pipelines, infraestructura y despliegues;
- documentación, decisiones y baselines;
- agentes, skills, prompts, reglas y workflows.

Las dimensiones candidatas incluyen:

- producto y funcionalidad;
- UI, UX, diseño visual y sistema de diseño;
- responsive y accesibilidad;
- arquitectura y calidad de código;
- dominio y datos;
- seguridad, privacidad y cumplimiento;
- rendimiento y resiliencia;
- pruebas y regresión;
- dependencias y supply chain;
- integraciones;
- CI/CD, despliegue, observabilidad y recuperación;
- documentación y conformidad ADS.

No se audita todo contra todo. PROFILE, SOURCES, arquitectura, riesgos y tipo de activo determinan
qué celdas son aplicables, obligatorias, opcionales o no aplicables.

### 20.4. Matriz viva de cobertura

La pieza central debe cruzar objeto y dimensión:

| Objeto | Dimensión | Estado | Última revisión | Revisión examinada | Findings | Próxima revisión |
|---|---|---|---|---|---|---|
| Formularios web | Diseño | Verificado | Fecha | `frontend@rev` | 0 abiertos | Tras nuevo formulario |
| Checkout | Accesibilidad | Findings abiertos | Fecha | `web@rev` | 3 | Tras corrección |
| API pedidos | Seguridad | Nunca auditado | — | — | — | Prioridad alta |
| Despliegue backend | Recuperación | Obsoleto | Fecha | `backend@rev` | 2 | Inmediata |

Estados mínimos candidatos:

- no aplicable;
- nunca auditado;
- planificado;
- en curso;
- auditado parcialmente;
- findings sin clasificar;
- corrección pendiente;
- corregido sin verificar;
- verificado;
- excepción aceptada;
- obsoleto por cambios;
- reauditoría vencida.

Cada registro debe conservar alcance, profundidad, método, evidencia, auditor, verificador,
revisiones de fuentes, confianza, findings, caducidad y trigger de reapertura. La cobertura queda
obsoleta si cambia el objeto, su estándar o una dependencia relevante.

### 20.5. Catálogos sistemáticos por especialidad

Cada especialidad debe combinar:

- controles universales;
- controles derivados del PROFILE y riesgos;
- dirección y reglas aprobadas del producto;
- lecciones de auditorías e incidentes;
- controles particulares del tipo de activo.

La auditoría de diseño y armonía debe revisar, entre otros:

- alturas, tamaños, padding y alineación de inputs;
- espaciado y ritmo;
- tipografía, color, radios, iconografía y elevación;
- botones y estados hover, focus, disabled, loading y error;
- labels, ayudas, validación y feedback;
- formularios, tablas, modales, navegación y cabeceras;
- estados vacío, carga, error y permisos;
- responsive, densidad, consistencia entre pantallas;
- uso de componentes y tokens canónicos;
- excepciones al sistema de diseño.

UX y accesibilidad deben revisar flujos, orden de pasos, prevención y recuperación de errores,
teclado, foco, contraste, lectores de pantalla, etiquetas, tamaños táctiles, feedback y coherencia
entre plataformas.

Arquitectura y código deben revisar responsabilidades, fronteras, acoplamiento, duplicidad,
dependencias, complejidad, código muerto, errores, configuración, observabilidad, mantenibilidad,
compatibilidad, rendimiento y deuda. Deben existir catálogos equivalentes para dominio, datos,
seguridad, pruebas, despliegue, operación y documentación.

Las listas orientan cobertura; no sustituyen juicio profesional ni evidencia.

### 20.6. Planificación autónoma y recurrente

El sistema debe generar auditorías sin petición expresa del Owner.

#### Por eventos

- creación o modificación de módulo, pantalla, flujo, formulario o componente;
- nueva regla de dominio, fuente, integración o tecnología;
- cambio de arquitectura, datos, permisos o despliegue;
- actualización crítica de dependencia;
- cierre de feature o iniciativa;
- incidente o regresión;
- preparación y publicación de release.

#### Por riesgo y recurrencia

La cadencia depende de criticidad y cambio: seguridad, dependencias, accesibilidad, rendimiento,
arquitectura, deuda, coherencia visual, documentación, recuperación y conformidad ADS pueden tener
frecuencias distintas.

#### Por envejecimiento

El runtime debe detectar áreas nunca auditadas, parciales, vencidas o invalidadas por cambios, y
proponer o abrir el trabajo correspondiente según la política autorizada.

### 20.7. Ciclo integral

```text
INVENTARIO Y COBERTURA
        ↓
AUDITORÍA ESPECIALIZADA
        ↓
FINDINGS + CAUSAS RAÍZ
        ↓
CLASIFICACIÓN Y PRIORIZACIÓN
        ↓
CAMPAÑA DE CORRECCIÓN
        ↓
VERIFICACIÓN INDEPENDIENTE
        ↓
REGLA, TEST, COMPONENTE O GATE PREVENTIVO
        ↓
ACTUALIZACIÓN DE REGISTROS Y REAUDITORÍA
```

Una auditoría no termina al producir un informe. Debe registrar alcance y exclusiones, cubrir las
celdas aplicables, producir evidencia y findings, agrupar causas raíz, convertir el resultado en
trabajo o excepción, programar la corrección y dejar próxima revisión.

### 20.8. Clasificación y tratamiento de findings

| Hallazgo | Tratamiento candidato |
|---|---|
| Comportamiento incorrecto | DEF |
| Incumplimiento de un estándar aprobado | DEF o GAP según contrato y estado real |
| Refactorización o mantenibilidad | DEU o trabajo técnico equivalente |
| Mejora funcional nueva | FEA |
| Ausencia o cambio de dirección | DIR |
| Incertidumbre | INV |
| Seguridad o privacidad | SEG |
| Problema sistémico de ADS/organización | SIS |
| Documento desactualizado | Corrección documental vinculada |
| Duplicado | Vincular; no crear trabajo paralelo |

AUD detecta; ENC clasifica y ancla; DSP organiza. No todo finding es un GAP ni toda observación debe
convertirse en item.

### 20.9. Corregir causas raíz

Los hallazgos repetidos deben agruparse por causa, alcance y solución sistémica. Veinte inputs con
alturas distintas no deberían producir veinte reparaciones independientes si la causa es la
ausencia o incumplimiento de un componente canónico.

El recorrido correcto sería:

1. confirmar o definir la dirección de diseño;
2. documentar tokens, medidas, estados y excepciones;
3. corregir el componente o primitiva raíz;
4. migrar implementaciones paralelas;
5. revisar todas sus apariciones;
6. añadir control visual o automatizado;
7. actualizar sistema de diseño y cobertura;
8. verificar transversalmente antes de cerrar.

El mismo principio se aplica a arquitectura, seguridad, pruebas, documentación y despliegue.

### 20.10. Auditoría de cada bloque nuevo

La definición de terminado de una feature, módulo, componente o integración debe activar su
cobertura mínima. Según el tipo puede incluir funcionalidad, diseño, UX, responsive, accesibilidad,
permisos, errores, pruebas, documentación, rendimiento, seguridad, despliegue u operación.

Los controles se distribuyen entre:

- validación durante el paquete;
- CI y análisis automático;
- revisión antes de merge;
- gate previo al despliegue;
- smoke test posterior;
- auditorías periódicas o transversales.

El Owner no debe pedir de nuevo las dimensiones previsibles de cada bloque.

### 20.11. Prevenir la repetición

Principio aceptado:

> **Lo que se encuentra una vez se corrige; lo que puede repetirse se convierte, cuando sea
> razonable, en regla, componente, test, validador, skill o gate.**

| Defecto | Prevención posible |
|---|---|
| Inputs con alturas distintas | Componente canónico, tokens y regresión visual |
| Colores o espaciados arbitrarios | Tokens y lint |
| Componente sin estados obligatorios | Contrato y pruebas |
| Dependencia arquitectónica prohibida | Regla automática de dependencias |
| API sin tratamiento de error | Contrato y test |
| Problema recurrente de accesibilidad | Lint, test y auditoría especializada |
| Documento obsoleto | Trigger y gate documental |
| Despliegue sin rollback | Gate de release |
| Secreto en código | Escaneo automático |

APR debe promover aprendizajes demostrados. La automatización no sustituye auditorías semánticas,
visuales o de uso que requieren juicio.

### 20.12. Autonomía con límites

El sistema puede inventariar, auditar, registrar y clasificar de forma autónoma dentro de su
política. La corrección depende del riesgo:

| Nivel | Autorización candidata |
|---|---|
| Mecánico y bajo riesgo | Ejecutable dentro de campaña preautorizada, con pruebas |
| Corrección local sin cambio funcional | Ejecutable con verificación independiente |
| Refactorización transversal | Requiere plan y radio de impacto |
| Cambio de UX, producto o arquitectura | Requiere dirección aprobada |
| Seguridad, datos o comportamiento crítico | Revisión especializada y gate; posible Owner |

El Owner aprueba política de calidad, tolerancia, prioridades, excepciones, campañas mayores y
cambios de dirección; no cada padding ni reparación mecánica.

### 20.13. Estado y documentación viva

No debe descansar en informes Markdown aislados. Necesita estado estructurado del que puedan
generarse vistas humanas:

- registro del universo auditable;
- plan y calendario por triggers;
- matriz de cobertura;
- registro de findings;
- registro de causas raíz;
- campañas y paquetes de corrección;
- ledger de verificación;
- excepciones, responsable, motivo y caducidad;
- baselines de calidad por área;
- historial y próxima auditoría.

Cada finding debe enlazar objeto, dimensión, evidencia, causa, gravedad, item, estado, responsable,
fuentes/revisiones y fecha. Los documentos legibles deben generarse o sincronizarse desde ese estado
para no crear otra memoria manual obsoleta.

### 20.14. Responsabilidades

| Participante | Responsabilidad |
|---|---|
| SIS | Contrato de cobertura, conformidad y estado global |
| DSP | Planificación, recurrencia, campañas, dependencias y trabajo huérfano |
| ENC | Clasificación y anclaje de findings |
| AUD y especialistas | Ejecución de auditorías con método y evidencia |
| DIS | Diseño, UX, sistema de diseño y accesibilidad |
| ARQ | Arquitectura, dependencias y deuda estructural |
| DOM | Dominio, reglas y datos |
| SEG | Seguridad, privacidad y cumplimiento |
| PLT/ENT | Tooling, CI/CD, infraestructura, despliegue y operación |
| CON | Reparaciones autorizadas |
| VER independiente | Confirmación de corrección, alcance y evidencia |
| APR | Conversión de recurrencias en prevención reusable |
| Owner | Política, riesgo, excepciones y direcciones importantes |

### 20.15. Condiciones de cierre

Una auditoría sólo se cierra cuando:

- cubrió todo el alcance o justificó cada exclusión;
- registró findings y evidencia;
- no dejó críticos sin clasificar;
- cada pendiente tiene item, responsable, campaña o excepción;
- registra revisiones examinadas y vigencia;
- dejó trigger o fecha de reauditoría.

Un finding sólo se cierra cuando:

- la corrección existe y fue probada;
- se verificó independientemente;
- se revisó el radio de impacto;
- se actualizó documentación y cobertura;
- se añadió prevención cuando era razonable.

`corregido` y `verificado` deben ser estados distintos. Un finding aplazado permanece visible con
responsable, motivo y fecha de revisión.

### 20.16. Ejemplo operativo: formulario nuevo

1. una feature introduce un formulario;
2. ADS registra pantalla, flujo y componentes afectados;
3. activa diseño, UX, accesibilidad, funcionalidad, permisos, errores y pruebas;
4. validadores revisan tokens y componentes;
5. DIS inspecciona coherencia visual;
6. se encuentran alturas distintas en inputs;
7. se identifica el componente compartido como causa raíz;
8. ENC genera una corrección agrupada;
9. CON corrige componente y usos;
10. VER revisa todos los formularios afectados;
11. se añade regresión visual o regla preventiva;
12. se actualizan sistema de diseño, findings y cobertura;
13. la celda se reabre automáticamente si cambia la primitiva.

### 20.17. Decisiones de diseño todavía pendientes

- representación canónica del universo, objetos y áreas auditables;
- esquema exacto de matriz de cobertura y caducidad;
- si este subsistema tiene nombre y contrato propios sin crear nueva capacidad;
- catálogo mínimo de dimensiones y checks por tipo de activo;
- política inicial de recurrencia y riesgo;
- límites exactos de corrección preautorizada;
- relación entre findings, items, causas raíz, campañas y dossier vivo;
- qué vistas se generan para agentes y para el Owner;
- qué parte vive en runtime, CI, documentos o estado estructurado;
- cómo se evita que el propio registro se convierta en burocracia obsoleta.

## 21. P-04 · Gobierno Git

Arquitectónicamente abordado mediante C7 e Integration Set. Pendiente de demostrar en runtime y en
un producto real:

- ramas abandonadas visibles;
- trazabilidad item/paquete/commit/PR/despliegue;
- integración parcial;
- recuperación multi-source;
- responsabilidad por cada operación Git.

## 22. P-05 · Posible capa de conocimiento propio compartido

Pregunta deliberadamente deferida: conocimiento válido en varios proyectos propios pero no
necesariamente universal ni propio de una clase técnica.

No debe diseñarse una capa nueva hasta disponer de evidencia independiente de otro proyecto maduro.

## 23. P-06 · Deriva entre núcleo y adaptadores

La regla de fuente única existe, pero no hay validador que detecte duplicaciones y divergencias en
un proyecto instalado entre:

- núcleo neutral;
- adaptadores;
- skills;
- memorias;
- instrucciones por herramienta.

PesquerApp demostró la deriva en más de una ocasión. Hace falta una comprobación operativa.

## 24. P-07 · Material normativo en voz del Owner

No existe ubicación ni tratamiento formal para documentos del Owner que son normativos pero no
pueden reescribirse al lenguaje canónico del kernel.

Actualmente requieren exclusiones manuales y pueden quedar en lugares sin convención. Debe
definirse:

- dónde viven;
- qué autoridad tienen;
- cómo se enlazan;
- qué validaciones se les aplican;
- cómo originan una enmienda o decisión sin convertirse en corpus operativo.

---

# BLOQUE E — Mejoras concretas extraídas de PesquerApp

## 25. Mejoras de pack y tooling pendientes de síntesis

- Herramienta reproducible para capturar y comparar estados visuales cargando/esqueleto bajo las
  mismas condiciones.
- Gancho Git con degradación explícita cuando el entorno no puede ejecutarlo.
- Mapa por adaptador de qué consume, qué comandos usa y qué puede escribir cada herramienta.
- Prueba de humo en una sesión nueva después de instalar o cambiar un adaptador.
- Vendorado controlado de skills externas con procedencia e integridad.
- Detección de ramas o trabajo Git abandonado sin integrar.
- Fronteras de escritura entre distintos entornos agentic que trabajan sobre el mismo producto.

Estas piezas deben contrastarse en F3 antes de decidir si pertenecen a kernel, pack, PROFILE,
adaptador, tooling o runtime.

---

# BLOQUE F — Simplificación y control de complejidad

## 26. Auditoría subtractiva

### 26.1. Principio aceptado: eficiencia sin degradación

ADS debe auditar su coste, contexto y complejidad, pero la optimización no puede significar
implementaciones rápidas, básicas o meramente funcionales.

> **ADS optimiza recursos sin reducir el estándar profesional. Si faltan créditos, tiempo o
> capacidad, deja un estado seguro y continúa después; no degrada silenciosamente el resultado.**

El objetivo no es minimizar tokens aislados, sino obtener el mejor resultado profesional con el
menor desperdicio total. Deben incluirse planificación, investigación, agentes, implementación,
pruebas, auditoría, correcciones, reintentos, contexto repetido, intervención del Owner, defectos y
retrabajo.

Una ejecución más larga distribuida en varios días es preferible a cerrar en una sesión un resultado
mediocre. El presupuesto puede alargar el calendario; no rebaja el gate.

### 26.2. Contrato de calidad

La calidad por defecto debe ser producción profesional:

- arquitectura mantenible;
- diseño y UX de alto nivel;
- implementación coherente y no genérica;
- pruebas y evidencia suficientes;
- documentación viva;
- seguridad y operación proporcionales al riesgo;
- verificación independiente cuando proceda;
- ausencia de «básico pero funcional» como cierre final.

Debe diferenciarse:

| Modalidad | Resultado permitido |
|---|---|
| Investigación o spike | Evidencia temporal; no apta para promoción directa |
| Prototipo | Sirve para decidir; no equivale a implementación final |
| Implementación profesional | Código, diseño, pruebas, documentación, integración y verificación de producción |

Un prototipo o spike no asciende a producto porque compile o parezca funcional. Cualquier reducción
del nivel de calidad requiere decisión explícita del Owner.

### 26.3. Coste por resultado aceptado y verificado

La unidad de análisis no debe ser «tokens para generar código», sino recursos hasta alcanzar un
resultado aceptado, integrado y verificado.

Un modelo fuerte que resuelve correctamente un problema complejo puede ser más eficiente que varios
modelos económicos cuyo resultado exige replanificación y retrabajo. Toda comparativa debe incluir
el coste posterior y los defectos escapados.

### 26.4. Auditoría empírica del propio ADS

ADS debe medir periódicamente:

- capacidades, agentes, roles y skills disponibles y activados;
- procesos, rutas, handoffs y gates;
- documentos, plantillas, prompts y adaptadores;
- items, paquetes y dossiers creados por resultado;
- tamaño y composición del contexto;
- lecturas repetidas y contenido duplicado;
- llamadas y modelos utilizados;
- coordinación y trabajo administrativo;
- tiempo, créditos y recursos;
- intervención y seguimiento exigidos al Owner;
- calidad final, defects, reaperturas y retrabajo;
- éxito de reanudación por otro agente.

No debe optimizarse sobre intuiciones ni sobre el número bruto de archivos. Debe probarse en
productos y escenarios reales.

### 26.5. Prueba de utilidad de cada pieza

Una capacidad, rol, skill, documento, gate, handoff o registro debe justificar que:

- evita errores o reduce riesgo;
- mejora calidad o especialización;
- reduce retrabajo;
- preserva conocimiento o reanudación;
- automatiza trabajo;
- aporta evidencia necesaria;
- habilita una capacidad que de otro modo se perdería.

Si sólo añade contexto, mantenimiento o pasos, debe evaluarse su fusión, generación automática,
carga bajo demanda, simplificación o retirada. No se elimina una función sólo por consumir tokens:
primero debe demostrarse que queda cubierta de forma igual o mejor.

Antes de crear una pieza nueva debe intentarse expresarla con lo existente. La regla inversa también
aplica: no se fusionan conceptos realmente distintos sólo para reducir el recuento.

### 26.6. Catálogo completo y contexto selectivo

El control repo puede contener la organización completa, pero cada ejecución debe recibir únicamente:

- objetivo y alcance actuales;
- contexto del item y paquete;
- decisiones y documentos aplicables;
- fuentes, componentes y revisiones necesarias;
- método y especialistas requeridos;
- restricciones, riesgos y criterios de cierre;
- checkpoint y evidencia previa relevante.

No debe cargar automáticamente todo el catálogo de agentes, skills, métodos, documentos, historial,
backlog y dossiers.

```text
CATÁLOGO COMPLETO DISPONIBLE
        ↓
RUTA + ITEM + PAQUETE ACTUAL
        ↓
CONTEXTO MÍNIMO SUFICIENTE
        ↓
AMPLIACIÓN PROGRESIVA POR NECESIDAD
```

El agente debe poder ampliar contexto cuando detecte incertidumbre. Contexto selectivo no significa
contexto insuficiente.

### 26.7. Skills y herramientas de contextualización

ADS debe investigar, evaluar e integrar skills y herramientas ya probadas —incluyendo **Caveman o
equivalentes**— que reduzcan el coste de comprender un proyecto sin perder precisión.

Las familias candidatas incluyen:

- índices semánticos y estructurales del repositorio;
- mapas de arquitectura, símbolos y dependencias;
- recuperación selectiva de fragmentos relevantes;
- resúmenes incrementales con procedencia;
- memoria y checkpoints compactos;
- detección de cambios por hash o revisión;
- caché de análisis todavía vigente;
- mapas de documentación y fuentes canónicas;
- herramientas de impacto y alcance;
- navegación asistida por AST, símbolos, tipos o grafo;
- compresión de contexto verificable;
- skills especializadas para stack, diseño, seguridad, pruebas y operación.

No se adopta una herramienta sólo porque prometa ahorrar tokens. Cada candidato debe declarar:

- problema que resuelve;
- modelos y entornos compatibles;
- coste de instalación, indexación y mantenimiento;
- precisión y pérdidas de contexto;
- procedencia y posibilidad de verificar lo recuperado;
- privacidad y tratamiento del código;
- frescura ante cambios;
- impacto real en tokens, calidad y retrabajo;
- degradación y fallback si deja de estar disponible.

El resultado de una skill o índice es ayuda de recuperación, no nueva fuente de verdad. Debe enlazar
al código o documento original y permitir que el agente amplíe la lectura cuando la decisión lo
requiera.

### 26.8. Estrategia de contexto del producto

El control repo debería poder mantener, derivar o generar:

- mapa del producto y de sus fuentes;
- índices de componentes, dominio, arquitectura, tecnologías y documentación;
- relaciones entre items, decisiones, código y despliegues;
- paquetes de contexto por capacidad y tipo de trabajo;
- deltas desde la última revisión conocida;
- resúmenes con revisión de origen y caducidad;
- contexto de reanudación independiente del chat.

Los artefactos derivados deben ser regenerables y no duplicar autoridad. Cuando cambian las fuentes,
el sistema debe invalidar únicamente los índices o resúmenes afectados.

### 26.9. Enrutamiento de modelos por juicio y riesgo

| Trabajo | Estrategia candidata |
|---|---|
| Arquitectura, diseño, síntesis y decisiones complejas | Modelo de alta capacidad |
| Auditoría semántica, visual o de uso | Especialista y modelo con capacidad suficiente |
| Cambio mecánico bien definido | Modelo eficiente con validación |
| Clasificación masiva | Modelo eficiente, muestreo y escalado |
| Investigación ambigua | Modelo fuerte o escalado automático |
| Verificación crítica | Independencia y capacidad suficiente |

No se asigna un modelo inferior sólo para cumplir un presupuesto. Debe existir escalado ante
incertidumbre, registro del modelo ejecutor/verificador y medición del retrabajo causado por el
enrutamiento.

### 26.10. Delegación y tamaño de paquetes

Más agentes no equivale a más profesionalidad. Una delegación debe aportar especialización,
paralelización real, independencia, aislamiento útil de contexto o reducción demostrable de riesgo.

Los paquetes demasiado grandes saturan contexto; los demasiado pequeños multiplican arranques,
lecturas, commits, handoffs e integración. DSP debe ajustar tamaño y delegación según complejidad,
fuentes, riesgo, capacidad del modelo, coherencia necesaria y posibilidad de checkpoint seguro.

### 26.11. Reutilización sin duplicidad

Debe priorizarse:

- fuente canónica única;
- referencias en lugar de copias;
- resúmenes derivados con procedencia;
- lectura incremental por cambios;
- hashes y revisiones;
- índices y mapas;
- compilación de instrucciones;
- checkpoints compactos;
- evidencia enlazada;
- reutilización de auditorías mientras conserven vigencia.

Un agente no debería releer el corpus completo si sólo han cambiado decisiones o componentes
identificables, pero tampoco confiar en un resumen obsoleto para una decisión crítica.

### 26.12. Automatización determinista

Schemas, enlaces, formato, dependencias, duplicidades, tokens de diseño, componentes prohibidos,
tests, secretos, cobertura, divergencia documental, Git, fuentes, versiones y configuración deben
automatizarse cuando pueda hacerse de manera fiable.

La IA debe reservarse preferentemente para juicio, diseño, interpretación, creatividad,
arquitectura, contradicciones y casos no reducibles a reglas.

### 26.13. Métricas equilibradas

No debe existir una única puntuación de eficiencia que incentive recortar calidad.

| Dimensión | Ejemplos |
|---|---|
| Calidad | Aceptación, defects escapados, reaperturas, coherencia visual, cobertura, evidencia y estabilidad |
| Recursos | Tokens por resultado verificado, llamadas, modelos, contexto, tiempo, créditos y herramientas |
| Complejidad | Agentes, handoffs, pasos, gates, documentos, items y mantenimiento de estado |
| Retrabajo | Correcciones, trabajo descartado, decisiones revertidas e intervención del Owner |
| Robustez | Reanudación, determinismo, recuperación, trazabilidad y coherencia multi-repo |

Una optimización sólo se acepta si reduce recursos o complejidad sin empeorar el contrato de calidad.

### 26.14. Banco de escenarios

La auditoría debe ejecutar casos representativos:

1. instalación en proyecto nuevo;
2. adopción de producto existente;
3. feature multi-repositorio;
4. corrección de defecto;
5. refactorización;
6. diseño e implementación de interfaz;
7. auditoría visual;
8. cambio arquitectónico;
9. release y despliegue;
10. pausa y reanudación con otro agente.

Se comparan calidad, coste, contexto, modelos, agentes, handoffs, intervención, retrabajo, defects y
reanudación antes y después de cada optimización.

### 26.15. Fases candidatas de la auditoría del ADS

```text
E0  Baseline de calidad, coste y complejidad
E1  Mapa de contexto, agentes, skills, documentos y rutas
E2  Duplicidades, sobreorganización y trabajo administrativo
E3  Evaluación de herramientas de contexto y banco de escenarios
E4  Propuestas de optimización
E5  Comparación antes/después
E6  Aceptación sólo con no degradación demostrada
E7  Presupuestos, alertas y regresión de eficiencia
E8  Reauditoría tras cambios relevantes del kernel o ecosistema
```

La unidad amplia, la certificación, el sistema documental, la auditoría continua y los
macrocircuitos deben pasar esta prueba antes de considerarse estabilizados.

### 26.16. Presupuesto como ritmo

ADS debe permitir definir créditos o uso máximos por sesión/día, modelos autorizados, umbrales de
pausa y operaciones que no deben empezar sin poder dejarse seguras.

Al aproximarse al límite debe:

1. completar una unidad segura;
2. probar y verificar lo alcanzado;
3. persistir estado, evidencia y revisiones;
4. dejar la siguiente acción exacta;
5. pausar sin declarar terminación;
6. continuar cuando existan recursos.

No debe omitir pruebas, documentación o diseño; usar un modelo insuficiente; reducir alcance
silenciosamente; ni presentar trabajo parcial como terminado.

### 26.17. Protección específica del diseño profesional

Una interfaz no se considera profesional porque compile. Según el alcance debe atravesar dirección
de diseño, referencias, exploración, sistema de diseño, propuesta, implementación, comparación
visual, armonía, responsive, accesibilidad, uso y corrección.

Si no existen recursos para completar el recorrido, se deja parcial y reanudable. La optimización no
puede volver a producir interfaces genéricas o pobres como consecuencia de recortar razonamiento,
iteración o crítica visual.

### 26.18. Evitar optimización y auditoría infinitas

El propio sistema de auditoría continua debe deduplicar findings, agrupar causas raíz, priorizar por
riesgo, reutilizar evidencia vigente, automatizar checks y reservar capacidad para construir
producto. No debe crear bucles de auditoría sobre auditoría ni trabajo administrativo sin impacto.

La auditoría del ADS también necesita stop conditions: se detiene cuando alcanza evidencia
suficiente para una decisión, no cuando ha consumido todas las variantes posibles.

### 26.19. Responsabilidades

| Participante | Responsabilidad |
|---|---|
| SIS | Contrato de complejidad, contexto y conformidad |
| DSP | Eficiencia de rutas, delegación, paquetes y carga contextual |
| ARQ | Arquitectura organizativa del propio ADS |
| PLT | Telemetría, herramientas, índices, compilación y caché |
| INV | Investigación y comparación de Caveman, skills y alternativas |
| VER | Demostrar que la calidad no disminuye |
| APR | Aprender de costes, defectos, reanudación y recurrencias |
| AUD | Ejecutar auditorías del ADS y de sus optimizaciones |
| Owner | Fijar suelo de calidad y autorizar degradaciones excepcionales |

### 26.20. Principios no negociables

1. calidad profesional por defecto;
2. no optimizar tokens de forma aislada;
3. medir coste total hasta resultado verificado;
4. no usar modelos insuficientes para tareas de juicio;
5. catálogo completo con contexto selectivo y ampliable;
6. aprovechar skills y herramientas probadas con evaluación empírica;
7. automatizar lo mecánico y reservar IA para juicio;
8. simplificar sólo con evidencia de no degradación;
9. pausar antes que entregar un resultado mediocre;
10. no presentar trabajo parcial como terminado;
11. exigir el mismo gate de calidad después de reducir costes;
12. preservar procedencia y acceso a las fuentes originales.

### 26.21. Decisiones todavía pendientes

- suite inicial de escenarios y métricas de no degradación;
- formato y granularidad de la telemetría de tokens/modelos/contexto;
- presupuestos configurables y política de pausa/reanudación;
- catálogo inicial de skills y herramientas de context engineering a evaluar;
- criterios de adopción, actualización y retirada de Caveman o equivalentes;
- estrategia de índices, caché, hashes, resúmenes y recuperación por fuente;
- política exacta de enrutamiento y escalado de modelos;
- límites para fan-out de agentes y tamaño de paquetes;
- quién puede aprobar una optimización del kernel;
- cómo probar diseño profesional sin reducirlo a métricas mecánicas.

### 26.22. Principio aceptado: corpus final limpio

Al terminar F3–F6 y antes de declarar estable o publicar la nueva versión, ADS debe quedar **limpio
de los documentos y artefactos utilizados únicamente para investigarlo o implementarlo**.

No deben permanecer en el HEAD estable, salvo que se hayan convertido en una fuente canónica real:

- prompts de implementación ya consumidos;
- planes temporales;
- informes intermedios;
- contrastes y matrices de trabajo agotadas;
- documentos de ideas ya resueltas;
- copias de mensajes del Owner;
- handoffs históricos;
- checkpoints de iniciativas cerradas;
- evidencias generadas que deban vivir como artefactos de CI;
- borradores, versiones paralelas y archivos «final-v2»;
- documentación de migración que ya no tenga consumidores soportados.

Git, commits, tags, releases y ramas históricas conservan la trazabilidad. No debe crearse un
directorio `archive/` dentro de la distribución sólo para desplazar allí el ruido.

### 26.23. Clasificación obligatoria antes de retirar

Cada artefacto temporal debe terminar en una de estas salidas:

| Resultado | Acción |
|---|---|
| Regla o contrato vigente | Integrar en kernel, pack, schema o documentación canónica |
| Decisión vigente | Registrar en el sistema canónico de decisiones |
| Capacidad, método o tooling útil | Integrar, probar y asignar propietario |
| Idea todavía válida pero no implementada | Convertir en item/dossier o incluirla en el único ledger de evolución |
| Evidencia de prueba | Conservar sólo donde el contrato de evidencia lo exija; preferentemente CI/release |
| Historia ya consumida | Conservar mediante Git y retirarla del HEAD |
| Duplicado, borrador u obsoleto | Eliminar tras comprobar referencias |

No se borra una idea importante para limpiar: primero se promueve a la fuente correcta. Tampoco se
mantiene un documento entero porque contenga una única conclusión útil.

### 26.24. Un único registro de evolución como máximo

El corpus estable puede mantener, como máximo, un documento conciso —nombre por decidir, por
ejemplo `EVOLUTION.md` o `CHANGELOG.md`— para:

- resumir cambios relevantes por versión;
- enlazar decisiones canónicas y migraciones;
- indicar ideas importantes expresamente diferidas;
- conservar procedencia mínima de grandes iniciativas;
- dirigir al historial Git o release correspondiente.

Ese documento es un ledger e índice, no un almacén de informes ni una segunda fuente de verdad. No
debe copiar contratos, decisiones, backlog o documentación vigente que ya tienen ubicación
canónica.

Las ideas pendientes con entidad suficiente deben vivir como trabajo estructurado; el ledger sólo
mantiene una referencia breve.

### 26.25. Gate de higiene del corpus

Antes del cierre de la actualización debe ejecutarse:

1. inventario de todos los documentos y artefactos no ejecutables;
2. declaración de autoridad, propietario, consumidor y ciclo de vida;
3. promoción de conclusiones vigentes a fuentes canónicas;
4. conversión de pendientes reales en items o dossiers;
5. consolidación del único ledger de evolución;
6. retirada de temporales, copias, archivos agotados y evidencia no versionable;
7. comprobación de enlaces y referencias entrantes/salientes;
8. validación de que tooling, tests y documentación no dependan de lo retirado;
9. prueba de navegación por un agente nuevo;
10. validadores completos, árbol Git limpio y release/tag recuperable.

El gate debe fallar si existe un documento sin consumidor, propietario o justificación vigente; si
una norma sólo vive en material temporal; si quedan verdades duplicadas; o si el índice documental
presenta archivos ya retirados.

### 26.26. Criterio de limpieza correcto

«Limpio» no significa reducir documentación gobernante. El sistema documental del producto,
kernel, contratos, métodos, plantillas, decisiones, tests y manuales vigentes permanecen porque son
parte de ADS.

Lo que se elimina es el **andamiaje de construcción ya consumido**. El HEAD estable debe explicar
cómo funciona ADS y cómo usarlo, no obligar a reconstruir la historia de su implementación para
descubrir qué documentos siguen vigentes.

Responsabilidad candidata:

- **SIS:** inventario, autoridad, duplicidades y gate de corpus;
- **APR:** promoción de aprendizajes antes de retirar material;
- **DSP/ENC:** resolución de ideas y trabajo todavía abierto;
- **PLT:** referencias, tooling, CI, artefactos y limpieza física;
- **VER independiente:** demuestra que el corpus sigue completo y navegable;
- **Owner:** aprueba el destino de ideas relevantes y el cierre final.

---

# BLOQUE G — Orden de trabajo propuesto cuando se autorice

## 27. No saltar directamente a implementar

```text
F3  SÍNTESIS
    comparar todos los candidatos y problemas; resolver relaciones y contradicciones

F4  ARQUITECTURA INTEGRADA
    decidir conceptos, autoridad, fuentes únicas, procesos, gates y migración

F5  ENMIENDAS Y CONTRATOS
    modificar la normativa únicamente por la vía autorizada

F6  DESCOMPOSICIÓN E IMPLEMENTACIÓN
    crear items trazables, pruebas negativas, tooling, documentación y piloto
```

## 28. Bloques de implementación previsibles

1. Macrocircuitos de proyecto nuevo, adopción, migración y actualización.
2. Contrato de instalación y certificación operativa.
3. Contrato de adaptadores y prueba de humo.
4. Unidad amplia y dossier vivo.
5. Calidad persistente por área, si la síntesis la aprueba.
6. Gobierno de conocimiento externo.
7. Validador de deriva núcleo/adaptadores.
8. Ubicación y autoridad de documentos del Owner.
9. Mejoras concretas de packs y tooling.
10. Auditoría empírica de calidad/coste y estrategia de context engineering, skills e índices.
11. Consolidación y gate final de higiene del corpus.
12. Runtime mínimo y primer piloto real.

## 29. Criterio de cierre de esta iniciativa de actualización

No se considerará completada únicamente porque existan documentos o validadores estructurales.
Debe demostrarse, al menos, que:

- se instala ADS en un proyecto nuevo;
- se adopta en un producto existente multi-repositorio sin perder su historia;
- se actualiza una instalación conservando overrides y estado;
- una sesión nueva supera la prueba de humo;
- un trabajo amplio mantiene dossier, items y paquetes sin duplicación;
- una feature transversal atraviesa varias fuentes y converge;
- un agente distinto reanuda por checkpoint;
- SIS emite una certificación con evidencia independiente;
- el Owner puede conocer estado, decisiones pendientes, riesgos y resultado sin gestionar detalles
  técnicos;
- el piloto real identifica qué debe simplificarse o retirarse.

---

# BLOQUE H — Preguntas para continuar la discusión con el Owner

## 30. Asuntos todavía por decidir

- Nombre y naturaleza de la unidad amplia.
- Si adopción es macrocircuito propio o variante de C0.
- Diferencia exacta entre instalación, adopción, migración y actualización.
- Nivel mínimo de certificación necesario para empezar a trabajar.
- Qué pruebas de humo deben realizarse en Claude, Codex y otros entornos.
- Cómo debe ver el Owner una iniciativa amplia y su dossier.
- Cuándo se crea automáticamente la unidad amplia y cuándo requiere decisión.
- Si el dossier se organiza con estructura flexible o con secciones canónicas mínimas.
- Relación entre dossier vivo y calidad persistente por área.
- Alcance del runtime mínimo que debe construirse antes del piloto.
- Qué proyecto se utilizará para cada prueba real.
- Si la adopción se aprueba como iniciativa amplia que compone procesos existentes y posee fases
  A0–A10, o si esas fases deben tener otra representación.
- Qué mínimo documental exacto permite superar «ahora puedes empezar a programar» sin convertir la
  adopción en documentación infinita.
- Qué partes del baseline de arquitectura, dominio, producto y diseño son obligatorias en todos los
  proyectos y cuáles dependen de riesgo y naturaleza.
- Qué protocolo técnico autoriza cada retirada de documentación, agentes, skills o backlog antiguo.
- Quién puede declarar que un sistema de diseño existente está suficientemente reconstruido.
- Qué parte del catálogo canónico se copia físicamente a cada control repo y qué parte se referencia
  desde la distribución, sin comprometer autonomía ni reproducibilidad.
- Qué capacidades forman exactamente el equipo mínimo permanente además de DSP y SIS, y bajo qué
  condición se activa ENC.
- Qué entornos agentic integran la primera matriz soportada, compatible o genérica y qué pruebas
  debe superar cada adaptador.
- Si el contrato documental se materializa con un manifiesto central, metadata en cada documento o
  una combinación de ambos.
- Qué blueprint documental compacto, estándar o regulado se genera según el perfil del producto.
- Qué criterios y eventos determinan que un documento está vigente, necesita revisión o bloquea un
  gate.
- Qué parte de las instrucciones coordinadas de desarrollo/despliegue se ejecutará y verificará
  automáticamente desde el control repo.
- Qué representación canónica tendrá el universo auditable y su matriz objeto × dimensión.
- Qué política de riesgo, recurrencia, caducidad y reapertura gobernará las auditorías continuas.
- Qué reparaciones mecánicas pueden ejecutarse dentro de campañas preautorizadas y cuáles requieren
  dirección, gate u Owner.
- Cómo se representan causas raíz, findings, campañas, prevención y verificación sin duplicar
  items, paquetes ni dossiers.
- Qué skills y herramientas de contextualización —Caveman o equivalentes— integran el banco de
  candidatos y con qué pruebas se aceptan o rechazan.
- Qué métricas demuestran que una reducción de tokens, modelos, agentes o contexto no degrada
  arquitectura, diseño, implementación, documentación ni verificación.
- Qué presupuestos actúan sólo sobre el ritmo y qué protocolo obliga a pausar con checkpoint seguro.
- Qué límites de fan-out, tamaño de paquete y carga contextual deben derivarse de pilotos reales.
- Nombre y contrato del único ledger de evolución que puede permanecer en el corpus estable.
- Qué evidencias deben conservarse en Git/release/CI y cuáles deben retirarse del HEAD.

## 31. Registro de cambios de este documento

| Fecha | Cambio |
|---|---|
| 2026-08-27 | Versión inicial: fases pendientes, macrocircuitos, certificación, unidad amplia, dossier vivo, P-01–P-07, mejoras concretas y orden de trabajo. |
| 2026-08-27 | Ampliación de los circuitos de proyecto nuevo y adopción: recorrido regulado actual, fases candidatas N0–N7 y A0–A10, actores, migración documental, reconstrucción UI/UX, trabajo histórico, gate de preparación y persistencia multichat. |
| 2026-08-27 | Principio aceptado de distribución preestructurada: capas canónica, blueprint, especialización, proyección agentic y estado; catálogo frente a equipo activo; generación de AGENTS/CLAUDE/reglas mediante adaptadores; y reducción de C0 a especialización y certificación. |
| 2026-08-27 | Sistema documental vivo aceptado: familias de producto, experiencia, diseño, dominio, arquitectura, tecnologías, desarrollo, calidad, seguridad, despliegue, entornos y operación; separación baseline/dirección/reglas/decisiones; extracción en adopción; responsabilidades, vigencia y contrato documental verificable. |
| 2026-08-27 | P-03 ampliado como sistema permanente de auditoría y mejora: universo auditable, matriz de cobertura, recurrencia autónoma, catálogos especializados, findings y causas raíz, campañas de corrección, prevención, verificación independiente y reauditoría. |
| 2026-08-27 | Auditoría subtractiva ampliada a calidad/coste/contexto del ADS: calidad profesional no negociable, coste total por resultado verificado, contexto progresivo, skills y herramientas como Caveman a evaluar, enrutamiento de modelos, banco de escenarios, presupuestos como ritmo y simplificación sólo sin degradación. |
| 2026-08-27 | Principio de corpus final limpio: promoción de contenido vigente, retirada del andamiaje temporal, trazabilidad mediante Git, un único ledger conciso de evolución y gate obligatorio de higiene antes del release estable. |
