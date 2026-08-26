# ADS — Arquitectura multi-repositorio elegida y mandato de implementación

**Estado:** APROBADO PARA IMPLEMENTACIÓN  
**Ámbito:** ADS Kernel 2.0  
**Decisión:** un producto ADS puede estar compuesto por múltiples repositorios Git independientes, gobernados por un único repositorio ADS de producto.  
**Prioridad:** estructural. Esta decisión sustituye la suposición histórica `ADS PROJECT = repositorio de código`.

---

## 0. Propósito de este documento

Este documento fija la arquitectura elegida para que ADS pueda gobernar un único producto cuyo código esté distribuido entre varios repositorios Git independientes.

No es una propuesta para seguir investigando alternativas. La decisión de arquitectura descrita aquí está tomada y debe implementarse en ADS Kernel.

El objetivo práctico es que el Owner pueda abrir **un único proyecto ADS** y trabajar con cualquier agente compatible —local o remoto— sobre frontend, backend, móvil, infraestructura u otros componentes del producto sin:

- cambiar manualmente de repositorio;
- trasladar información entre chats;
- redactar handoffs manuales entre frontend y backend;
- reconstruir el contexto del producto para cada repositorio;
- duplicar PROFILE, memoria, decisiones, arquitectura o contratos;
- convertir los repositorios de código en una organización ADS independiente cada uno.

La unidad organizativa es el **producto ADS**.

Los repositorios Git son únicamente unidades físicas de código, historial, integración y despliegue.

---

# 1. Decisión principal

## 1.1. Nueva relación fundamental

ADS debe adoptar como propiedad estructural:

```text
PRODUCTO
    !=
REPOSITORIO GIT
```

y:

```text
ADS PROJECT
    !=
REPOSITORIO DE CÓDIGO
```

La relación elegida es:

```text
PRODUCTO
│
└── ADS PROJECT
    │
    ├── repositorio ADS de control
    │
    ├── componentes lógicos
    │
    └── fuentes/repositorios técnicos
```

Ejemplo:

```text
LA PESQUERAPP
│
├── pesquerapp-ads
│
│   ├── ADS
│   ├── PROFILE
│   ├── estado
│   ├── items
│   ├── decisiones
│   ├── arquitectura global
│   ├── dominio
│   ├── contratos
│   ├── documentación transversal
│   └── composición del producto
│
├── pesquerapp-frontend
│   └── código Next.js
│
├── pesquerapp-backend
│   └── código Laravel
│
└── pesquerapp-mobile
    └── código de la aplicación móvil
```

Todos ellos son repositorios Git independientes.

No existe un repositorio Git padre que contenga técnicamente a los demás.

La relación entre ellos la conoce y gobierna ADS.

---

# 2. Principio de diseño

La arquitectura debe separar tres problemas que anteriormente podían confundirse:

## 2.1. Identidad y gobierno del producto

Responde a:

> ¿Dónde vive la organización ADS y cuál es la fuente de verdad del producto?

Respuesta:

> En un repositorio ADS de control independiente de los repositorios técnicos.

---

## 2.2. Composición del producto

Responde a:

> ¿Cómo sabe ADS qué repositorios y componentes forman parte del producto?

Respuesta:

> Mediante un manifiesto declarativo, versionado y machine-readable dentro del repositorio ADS.

---

## 2.3. Materialización del workspace

Responde a:

> ¿Dónde aparecen físicamente esos repositorios para que un agente pueda utilizarlos?

Respuesta:

> En un workspace de producto donde el repositorio ADS y los repositorios técnicos aparecen como repositorios hermanos.

La materialización puede realizarse con repos ya clonados en local o clonándolos/preparándolos en un entorno remoto.

---

# 3. Topología elegida

## 3.1. Workspace local

La disposición local conforme a ADS será:

```text
<workspace-del-producto>/
│
├── ads/
│   └── .git/
│
├── frontend/
│   └── .git/
│
├── backend/
│   └── .git/
│
└── mobile/
    └── .git/
```

El directorio exterior:

```text
<workspace-del-producto>/
```

NO es un repositorio Git.

Es únicamente el contenedor físico del producto.

Cada hijo mantiene su propio `.git`.

---

## 3.2. Convención local

ADS debe establecer como convención normal:

```text
<workspace>/
    ads/
    <source-1>/
    <source-2>/
    ...
```

El repositorio de control debe materializarse localmente como:

```text
ads/
```

salvo que una integración técnica externa obligue justificadamente a usar otra ruta.

Los repositorios técnicos tendrán rutas locales declaradas en el manifiesto del producto.

La flexibilidad arbitraria de rutas no es un objetivo.

Las rutas predecibles son deliberadas porque reducen:

- configuración;
- errores;
- contexto para los agentes;
- código especial;
- diferencias local/cloud;
- dificultad de recuperación;
- dependencia de un proveedor concreto.

---

# 4. El repositorio ADS de control

## 4.1. Qué es

El repositorio ADS es el repositorio de gobierno y coordinación del producto.

Es el punto de entrada normal para cualquier trabajo gobernado por ADS.

Conceptualmente:

```text
repo ADS
    =
sistema operativo de desarrollo del producto
```

No es:

```text
repo ADS
    =
otro componente técnico del producto
```

---

## 4.2. Qué debe vivir aquí

Como mínimo, el repositorio ADS es la autoridad para:

- kernel vendorizado;
- packs;
- PROFILE;
- PROJECT;
- AGENTS compilado;
- memoria del proyecto;
- decisiones;
- ADR;
- arquitectura global;
- modelo de dominio transversal;
- requisitos;
- investigación;
- items;
- rutas;
- packages;
- checkpoints;
- estado global;
- contratos compartidos;
- evidencias de integración;
- documentación transversal;
- composición de fuentes/repositorios;
- relación entre componentes;
- integración entre componentes;
- estado ejecutivo;
- trazabilidad de cambios multi-repo.

---

## 4.3. Qué NO debe vivir aquí

El repositorio ADS no debe absorber el código de producto solamente para simplificar la coordinación.

No debe contener como código versionado:

- frontend;
- backend;
- aplicación móvil;
- servicios independientes;
- infraestructura que ya tenga su propio ciclo de vida;
- artefactos técnicos que deban desplegarse desde sus propios repositorios.

Tampoco debe contener clones Git de los repositorios técnicos en su interior.

Debe evitarse:

```text
ads/
├── .git/
└── workspace/
    ├── frontend/.git/
    └── backend/.git/
```

como topología ADS estándar.

La forma estándar es de hermanos:

```text
workspace/
├── ads/.git/
├── frontend/.git/
└── backend/.git/
```

---

# 5. No usar submodules como arquitectura ADS

La solución elegida NO depende de:

- Git submodules;
- Git subtree;
- monorepo;
- nested Git;
- sincronización manual de copias;
- una herramienta propietaria de un proveedor de agentes.

Los submodules pueden ser una herramienta válida en otros productos, pero ADS no los necesita para representar la composición del producto.

ADS debe distinguir:

```text
relación lógica de producto
```

de:

```text
relación Git padre/hijo
```

La composición debe estar expresada en ADS, no delegada en mecanismos Git que añadan fricción operacional.

---

# 6. Fuente de verdad de la composición

## 6.1. Nuevo manifiesto obligatorio

Debe crearse un manifiesto machine-readable en la raíz del repositorio ADS:

```text
SOURCES.toml
```

`SOURCES.toml` será la fuente de verdad para:

- fuentes Git externas;
- identidad remota;
- ruta de materialización;
- relación entre fuentes y componentes.

No debe duplicarse su contenido semántico en `PROJECT.md`, `PROFILE.md`, `AGENTS.md` ni otros documentos.

Los demás documentos pueden enlazar o explicar el manifiesto.

---

## 6.2. Por qué TOML

Se elige TOML porque:

- es legible por humanos;
- es suficientemente simple;
- admite comentarios;
- es estable para configuración;
- Python moderno puede leerlo mediante biblioteca estándar (`tomllib`);
- evita introducir PyYAML u otra dependencia sólo para interpretar el manifiesto;
- es más cómodo de revisar que JSON.

No debe incorporarse una dependencia externa únicamente para leer `SOURCES.toml`.

---

# 7. Modelo de `SOURCES.toml`

## 7.1. Versión inicial

Formato base:

```toml
schema = 1

[workspace]
layout = "siblings"

[[sources]]
id = "frontend"
remote = "https://github.com/organizacion/pesquerapp-frontend.git"
path = "frontend"

[[sources]]
id = "backend"
remote = "https://github.com/organizacion/pesquerapp-backend.git"
path = "backend"

[[sources]]
id = "mobile"
remote = "https://github.com/organizacion/pesquerapp-mobile.git"
path = "mobile"

[[components]]
id = "web"
source = "frontend"
path = "."
kind = "frontend"

[[components]]
id = "api"
source = "backend"
path = "."
kind = "backend"

[[components]]
id = "mobile"
source = "mobile"
path = "."
kind = "mobile"
```

---

# 8. Semántica del manifiesto

## 8.1. `schema`

Obligatorio.

Permite evolucionar el formato sin interpretación ambigua.

Versión inicial:

```toml
schema = 1
```

---

## 8.2. `[workspace]`

Versión inicial:

```toml
[workspace]
layout = "siblings"
```

Sólo se implementará inicialmente:

```text
siblings
```

No introducir opciones sin una necesidad real.

El soporte de otras topologías podrá añadirse en versiones futuras sin romper el modelo lógico.

---

## 8.3. `sources`

Una `source` representa una fuente física versionada.

En la primera implementación será normalmente un repositorio Git.

Campos obligatorios:

```text
id
remote
path
```

### `id`

Identificador estable dentro de ADS.

Ejemplos:

```text
frontend
backend
mobile
infra
shared
```

No debe depender del nombre local exacto del repositorio.

---

### `remote`

Identidad Git remota canónica de la fuente.

Ejemplo:

```text
https://github.com/organizacion/pesquerapp-backend.git
```

La identidad real de la fuente es el remoto, no la ruta local.

ADS debe soportar al menos remotos Git normales mediante HTTPS y SSH.

No deben almacenarse credenciales en el manifiesto.

Ejemplos prohibidos:

```text
https://usuario:token@github.com/...
```

```text
https://TOKEN@...
```

---

### `path`

Ruta relativa al workspace de producto donde debe materializarse la fuente.

Ejemplo:

```toml
path = "backend"
```

Produce:

```text
<workspace>/backend
```

No es identidad.

Es materialización.

ADS debe rechazar:

- rutas absolutas;
- rutas que escapen del workspace mediante `..`;
- rutas duplicadas;
- `ads` como ruta de una fuente técnica;
- rutas que colisionen entre sí.

---

# 9. Componentes no son repositorios

Esta distinción debe quedar expresamente incorporada al kernel.

```text
COMPONENTE
    != necesariamente
REPOSITORIO
```

Un componente es una unidad lógica/técnica del producto.

Una source es una unidad física de versionado/materialización.

Esto permite soportar con el mismo modelo:

## 9.1. Multi-repo

```text
frontend component → frontend repo
backend component  → backend repo
```

## 9.2. Monorepo técnico

```text
web component → app repo /apps/web
api component → app repo /apps/api
```

## 9.3. Híbrido

```text
web      → product repo /apps/web
api      → product repo /apps/api
mobile   → mobile repo
infra    → infra repo
```

ADS no debe introducir una regla `1 componente = 1 repo`.

---

# 10. Modelo de `components`

Campos iniciales:

```text
id
source
path
kind
```

`kind` debe ser descriptivo, no una enumeración cerrada rígida.

Ejemplo:

```toml
[[components]]
id = "api"
source = "backend"
path = "."
kind = "backend"
```

El kernel puede utilizar packs/capacidades para especialización.

`kind` no debe convertirse en una nueva taxonomía burocrática.

---

# 11. Workspace root

## 11.1. Resolución estándar

Cuando el repositorio ADS está materializado como:

```text
/producto/ads
```

el workspace root es:

```text
/producto
```

Por tanto:

```text
ADS_ROOT       = /producto/ads
WORKSPACE_ROOT = /producto
```

y:

```text
source.path = "backend"
```

resuelve a:

```text
/producto/backend
```

---

## 11.2. Restricción de seguridad

Toda resolución de rutas debe comprobar que el destino final continúa bajo `WORKSPACE_ROOT`.

Nunca debe permitirse que un manifiesto haga:

```toml
path = "../../otro-proyecto"
```

ni que un symlink permita salir silenciosamente del workspace sin control.

---

# 12. Materialización local

## 12.1. Regla principal

En local, si los repositorios ya existen correctamente dentro del workspace:

> ADS debe reutilizarlos.

No debe volver a clonarlos.

No debe crear copias temporales innecesarias.

No debe descargar el repositorio en cada sesión.

---

## 12.2. Caso normal

```text
la-pesquerapp/
├── ads/
├── frontend/
├── backend/
└── mobile/
```

Al iniciar una sesión:

1. ADS localiza `SOURCES.toml`.
2. Determina `WORKSPACE_ROOT`.
3. Comprueba las fuentes necesarias.
4. Verifica que los directorios existentes sean repos Git.
5. Comprueba que sus remotos correspondan con los declarados.
6. Entrega al agente únicamente los directorios necesarios para el trabajo.

---

# 13. Materialización remota/cloud

El modelo lógico no cambia.

El mismo:

```toml
remote = "..."
path = "..."
```

debe permitir materializar:

```text
/workspace/
├── ads/
├── frontend/
├── backend/
└── mobile/
```

en una VM, container, sandbox o entorno cloud.

---

## 13.1. Dos modos remotos compatibles

ADS debe permitir conceptualmente:

### A. El proveedor ya materializa múltiples repositorios

Ejemplo conceptual:

```text
Cursor/Claude/otro proveedor
    ↓
clona ADS + frontend + backend
    ↓
ADS valida el workspace
```

### B. Sólo está disponible el repositorio ADS

```text
proveedor
    ↓
clona ADS
    ↓
ADS lee SOURCES.toml
    ↓
clona las sources requeridas
```

El kernel no debe asumir que siempre ocurrirá A ni siempre B.

---

# 14. Compatibilidad con agentes

La arquitectura debe ser **provider-neutral**.

El contrato de ADS es:

> El agente recibe el repositorio ADS como contexto principal y las rutas de las sources requeridas como directorios adicionales de lectura/escritura.

Ejemplos de adaptación actuales:

```text
Claude Code
    ADS como cwd
    + additional directories

Cursor
    workspace multi-root / multi-repo

Codex
    ADS como proyecto/carpeta primaria
    + repos técnicos como carpetas adicionales cuando el entorno lo soporte

Gemini
    ADS
    + include-directories / workspace directories
```

Estos son adaptadores de entorno.

NO son semántica del kernel.

ADS no debe quedar acoplado a flags concretos de Claude, Cursor, Codex o Gemini.

---

# 15. Denominador común portable

El soporte multi-repo del kernel debe basarse sólo en:

```text
filesystem
+
directorios
+
Git
+
shell/proceso
+
credenciales aportadas por el entorno
```

Una integración de proveedor puede mejorar la experiencia, pero la arquitectura base debe seguir funcionando sin ella.

---

# 16. Nuevo principio operativo: entrada por ADS

Todo trabajo gobernado por ADS debe iniciarse desde el repositorio ADS del producto o desde un runtime que cargue explícitamente ese ADS Project.

La ruta normal será:

```text
abrir repo ADS
    ↓
expresar intención del Owner
    ↓
ADS determina el item/ruta/package
    ↓
ADS determina componentes/sources afectados
    ↓
materializa/verifica dichas sources
    ↓
habilita el contexto necesario al agente
    ↓
trabaja sobre uno o varios repos técnicos
    ↓
integra resultados en el estado global
```

---

# 17. Trabajo directo en un repo técnico

Abrir únicamente:

```text
pesquerapp-backend
```

y modificarlo sin cargar el ADS Project debe considerarse:

```text
trabajo fuera de ADS
```

No es necesario impedirlo técnicamente.

Git sigue perteneciendo a sus propietarios.

Pero ADS no debe fingir que ese trabajo siguió:

- sus gates;
- sus rutas;
- sus decisiones;
- sus contratos;
- su estado;
- su trazabilidad.

No debe duplicarse todo ADS dentro del backend sólo para intentar evitar esta posibilidad.

---

# 18. No duplicar ADS en las sources

Los repositorios técnicos NO deben recibir copias de:

- PROFILE;
- PROJECT;
- estado global;
- items;
- memoria;
- ADR globales;
- contratos maestros;
- kernel;
- packs;
- AGENTS global;
- documentación organizativa.

La regla de una fuente de verdad continúa siendo obligatoria:

> Una verdad vive en un lugar. Los demás elementos la referencian.

---

# 19. Documentación técnica local

La separación anterior no significa que un repositorio técnico deba carecer absolutamente de documentación.

Puede conservar documentación **code-adjacent** cuya utilidad depende directamente del código, por ejemplo:

- README de construcción;
- instrucciones de desarrollo del componente;
- documentación de migrations;
- documentación generada desde el código;
- configuración de CI;
- deployment específico del componente;
- notas que deban versionarse exactamente con esa implementación.

Pero deben vivir en ADS, de forma preferente, los documentos de producto y coordinación transversal:

- decisiones de producto;
- arquitectura global;
- contratos entre componentes;
- requisitos;
- investigación;
- estado;
- planificación;
- memoria;
- integración.

---

# 20. Scope de sources para items, rutas y packages

La identidad de un item no depende de un repositorio.

Un item puede afectar a:

```text
frontend
+
backend
+
mobile
```

sin dejar de ser un solo item.

Esto debe quedar reflejado en la especificación normativa.

---

# 21. Packages multi-repo

Un package es una unidad de trabajo y custodia.

No debe imponerse:

```text
1 package = 1 repo
```

porque un repositorio es una frontera física, no necesariamente la frontera correcta del trabajo.

Un package debe poder declarar:

```text
read_sources
write_sources
```

Ejemplo:

```yaml
read_sources:
  - frontend
  - backend

write_sources:
  - frontend
  - backend
```

El formato real deberá adaptarse al formato de packages existente.

No se introduce YAML como nuevo formato obligatorio por este ejemplo.

---

## 21.1. Regla por defecto

El DSP debe preferir el scope mínimo que mantenga el trabajo coherente.

Si una operación puede realizarse con:

```text
write_sources = [frontend]
```

no debe autorizar escritura en todo el producto.

Pero si una unidad coherente necesita modificar frontend y backend conjuntamente, ADS debe permitirlo.

No debe fragmentarse artificialmente sólo porque existan dos repositorios.

---

# 22. Lectura y escritura son permisos distintos

Una source puede necesitarse sólo como contexto.

Ejemplo:

```text
Package: adaptar frontend a API existente

read:
    backend

write:
    frontend
```

El agente puede inspeccionar el backend para confirmar:

- endpoint;
- tipos;
- validaciones;
- nombres;
- contrato real;

sin recibir autoridad para modificarlo.

Esto reduce errores y superficie de cambio.

---

# 23. Contratos transversales

Los contratos entre componentes son conceptos globales del producto.

Su fuente de verdad debe estar en el repositorio ADS cuando no exista una razón técnica fuerte para que una herramienta concreta necesite materializarlos junto al código.

Ejemplos:

- OpenAPI;
- JSON Schema;
- GraphQL schema;
- protobuf;
- contratos de eventos;
- contratos de integración;
- tipos compartidos conceptuales;
- consumer/provider compatibility.

ADS debe distinguir:

```text
CONTRATO
```

de:

```text
IMPLEMENTACIÓN DEL CONTRATO
```

y de:

```text
EVIDENCIA DE COMPATIBILIDAD
```

---

# 24. Contract-first para cambios transversales

Cuando un cambio frontend/backend depende de una interfaz nueva o modificada, la ruta debe poder establecer primero la decisión contractual.

Ejemplo:

```text
ITEM-123
    ↓
contrato API v4 aprobado/versionado
    ↓
frontend implementa contra v4
backend implementa v4
    ↓
verificación conjunta
```

Los dos agentes no deben inventar independientemente el JSON y resolver discrepancias al final.

---

# 25. Git sigue siendo independiente por source

Cada source mantiene:

- su repositorio;
- su historial;
- su rama principal;
- sus branches;
- sus commits;
- sus PR;
- su CI;
- sus tags;
- su despliegue.

ADS no debe intentar crear un falso commit atómico que abarque varios repositorios.

Git no ofrece un commit físico multi-repo.

---

# 26. Atomicidad lógica de producto

En un cambio transversal puede existir:

```text
frontend commit AAA
backend  commit BBB
mobile   commit CCC
```

ADS debe poder afirmar:

> AAA + BBB + CCC constituyen la combinación que ha sido integrada/verificada para este item.

Esto es una **atomicidad lógica ADS**, no una atomicidad Git.

---

# 27. Integration Set

Debe incorporarse al modelo operativo el concepto de **Integration Set**.

Un Integration Set representa una combinación exacta de revisiones de sources que ha sido candidata o probada conjuntamente.

Ejemplo conceptual:

```text
Integration Set: IS-142

item:
  ITEM-123

sources:
  frontend:
    commit: AAA
    pr: 301

  backend:
    commit: BBB
    pr: 812

contract:
  api-contract: v4

verification:
  frontend: PASS
  backend: PASS
  integration: PASS
  e2e: PASS
```

El formato físico final debe respetar las convenciones de ADS y no crear duplicación.

---

# 28. Objetivos de Integration Set

Debe permitir responder con evidencia:

- ¿qué frontend fue probado con qué backend?;
- ¿qué commits componían el candidato?;
- ¿qué contratos estaban vigentes?;
- ¿qué migrations intervenían?;
- ¿qué CI pasó?;
- ¿qué E2E pasó?;
- ¿qué combinación se desplegó?;
- ¿qué combinación debe restaurarse si se revierte el producto?

---

# 29. Integration Set no es Release

Deben distinguirse:

```text
Integration Set
    =
combinación exacta evaluada

Release
    =
decisión de publicar/desplegar una combinación
```

Un Integration Set puede validarse y no desplegarse.

Un despliegue puede además ser independiente por componente.

---

# 30. Merge multi-repo

ADS no debe prometer que los merges de varios repos sean físicamente atómicos.

Si un item necesita merge de frontend y backend:

```text
PR frontend
PR backend
```

ADS los considera miembros del mismo cambio lógico.

Si sólo uno se fusiona por un fallo:

```text
estado global = integración parcial
```

No:

```text
estado global = terminado
```

El runtime/ENT debe poder:

- continuar la convergencia;
- bloquear publicación;
- ejecutar compensación;
- revertir cuando corresponda.

---

# 31. Revisión de G29 / gobierno Git

Las reglas Git del kernel deben actualizarse para eliminar cualquier semántica implícita:

```text
un item
→ una branch
→ un PR
```

como relación universal.

La relación correcta será:

```text
item/package
    ↓
0..N source changes
    ↓
cada source:
    branch/worktree
    commits
    push
    PR
    CI
    ↓
Integration Set / convergencia ADS
```

`main` continúa representando el último estado integrado/aceptado **de cada source**.

El estado del producto se calcula en ADS.

---

# 32. Branches y worktrees

Cada source puede utilizar branch/worktree/sandbox independiente.

Para un cambio multi-repo:

```text
frontend:
    branch feat/item-123

backend:
    branch feat/item-123
```

pueden compartir un identificador lógico, aunque sean branches Git distintas.

No debe asumirse que los nombres tienen que ser idénticos si una plataforma exige otra convención.

La asociación vive en ADS.

---

# 33. Trazabilidad de source changes

Un package/checkpoint/handoff que escriba sobre una source debe poder registrar al menos:

- source id;
- branch/ref si existe;
- commit SHA cuando haya commit;
- PR si existe;
- estado de push;
- evidencia de CI disponible;
- dirty state sólo cuando sea necesario para recuperación.

Para varios repositorios, la colección es 0..N.

---

# 34. Recuperación

La recuperación de una sesión multi-repo no puede depender sólo de “abre la branch”.

ADS debe saber:

```text
item
package
sources implicadas
refs/commits
contrato vigente
último evento significativo
siguiente acción
```

Los checkpoints actuales deben ampliarse para poder referenciar múltiples sources y sus revisiones.

---

# 35. `based_on`

La regla existente de `based_on` se conserva y gana importancia.

Cuando un trabajo depende de otra source, debe poder expresarse, por ejemplo:

```text
based_on:
    backend@<sha>
    api-contract@v4
```

No se debe copiar el contenido del backend al checkpoint.

Se referencia la fuente/version exacta.

---

# 36. Nuevo tooling mínimo de workspace

Debe incorporarse una herramienta provider-neutral en:

```text
tooling/workspace.py
```

Debe usar, en la medida de lo posible, sólo Python stdlib y Git CLI.

No crear una dependencia de Node, Docker o un SDK de proveedor para esta función.

---

# 37. Comandos mínimos

La interfaz exacta puede afinarse durante implementación, pero debe cubrir como mínimo:

```text
python3 tooling/workspace.py check
python3 tooling/workspace.py init
python3 tooling/workspace.py status
```

y selección de sources:

```text
python3 tooling/workspace.py init frontend backend
```

Sin ids:

```text
init
```

significa todas las sources declaradas.

---

# 38. `workspace check`

Debe validar como mínimo:

- existe `SOURCES.toml`;
- schema soportado;
- layout soportado;
- ids válidos y únicos;
- paths válidos y únicos;
- no hay path `ads`;
- no hay escape del workspace;
- remotes válidos;
- no hay credenciales embebidas;
- componentes referencian sources existentes;
- paths de componentes no escapan de la source;
- las sources materializadas son repos Git;
- el remote de la source corresponde con el manifest;
- no se está confundiendo otro repo con la source esperada.

Debe distinguir:

```text
ERROR
WARN
INFO
```

---

# 39. Normalización de remotes

ADS debe reconocer como identidad equivalente, cuando proceda:

```text
https://github.com/org/repo.git
git@github.com:org/repo.git
ssh://git@github.com/org/repo.git
```

si apuntan inequívocamente al mismo repositorio.

No debe depender de una comparación textual ingenua.

La primera implementación puede soportar normalización conservadora de GitHub y una normalización genérica para URLs Git.

Ante ambigüedad, debe fallar de forma segura.

---

# 40. `workspace init`

Comportamiento:

```text
para cada source solicitada:
    si no existe:
        git clone remote path
    si existe y es la source correcta:
        reutilizar
    si existe pero no es repo Git:
        ERROR
    si existe pero su identidad remota no coincide:
        ERROR
```

No debe:

- borrar carpetas;
- resetear cambios;
- hacer checkout destructivo;
- hacer pull forzado;
- sobrescribir trabajo existente.

---

# 41. `workspace status`

Debe ofrecer una vista compacta por source:

```text
SOURCE     PATH       PRESENT  BRANCH      HEAD       DIRTY  REMOTE
frontend   frontend   yes      feat/x      a1b2c3d    no     ok
backend    backend    yes      main        e4f5g6h    yes    ok
mobile     mobile     no       -           -          -      -
```

La presentación humana puede variar.

Debe existir también una salida machine-readable cuando sea necesaria para runtime/agentes, preferentemente JSON mediante opción explícita.

Ejemplo:

```text
--json
```

---

# 42. No hacer sync implícito

`workspace init` no debe convertirse en:

```text
git pull todos los repos
```

La actualización de refs y branches pertenece al trabajo Git correspondiente.

Preparar un workspace y sincronizar un trabajo son operaciones distintas.

Esto evita alterar silenciosamente repositorios con trabajo local.

---

# 43. Materialización selectiva

Aunque en un equipo local normal sea razonable tener todas las sources clonadas, ADS debe permitir que un entorno cloud materialice sólo las necesarias.

Ejemplo:

```text
item de frontend puro
    ↓
ADS + frontend

cambio transversal
    ↓
ADS + frontend + backend
```

Esto reduce tiempo, superficie y consumo.

---

# 44. Contexto mínimo para el agente

Tener cuatro repositorios disponibles NO debe significar cargar cuatro repositorios completos en contexto.

ADS debe aplicar:

```text
necesidad
    ↓
componentes afectados
    ↓
sources necesarias
    ↓
read/write scope
    ↓
contexto mínimo
```

El runtime debe evitar búsquedas indiscriminadas por todo el workspace cuando el scope sea conocido.

---

# 45. Nuevo bootstrap de proyectos

El bootstrap actual debe cambiar.

La creación de un proyecto ADS ya NO debe generar:

```text
../mi-proyecto/
    ADS + código futuro
```

como raíz Git del producto.

Debe generar:

```text
../mi-proyecto/
└── ads/
    ├── .git/
    ├── PROJECT.md
    ├── PROFILE.md
    ├── SOURCES.toml
    ├── BOOTSTRAP_PROMPT.md
    ├── kernel/
    ├── packs/
    ├── docs/
    └── tooling/
```

`../mi-proyecto/` será el workspace.

`../mi-proyecto/ads/` será el repo Git creado por ADS.

---

# 46. `new-project.sh`

`tooling/new-project.sh` debe actualizarse para:

1. crear el directorio de workspace;
2. crear dentro `ads/`;
3. instalar allí kernel/packs/docs/tooling;
4. crear `SOURCES.toml`;
5. inicializar Git únicamente en `ads/`;
6. realizar el commit semilla únicamente en `ads/`;
7. presentar al Owner el siguiente paso correctamente;
8. no crear repositorios técnicos ficticios.

Resultado:

```text
Proyecto 'mi-proyecto' creado

workspace:
    ../mi-proyecto/

ADS control repo:
    ../mi-proyecto/ads/
```

---

# 47. Repositorio remoto del ADS Project

El primer remoto que se crea/pushea es el repositorio ADS.

Ejemplo:

```text
pesquerapp-ads
```

Los repos técnicos son registrados posteriormente en `SOURCES.toml`.

El bootstrap no debe asumir que todos existan ya.

---

# 48. Proyecto nuevo con sources vacías

Debe ser válido iniciar con:

```toml
schema = 1

[workspace]
layout = "siblings"
```

sin ninguna source técnica aún.

Circuito 0 puede decidir posteriormente la arquitectura física y añadir las sources necesarias.

Esto es especialmente importante para productos nuevos.

---

# 49. Adopción de proyecto existente

La actual ruta de adopción que copia ADS dentro de un repositorio de código debe retirarse como ruta normal.

NO:

```text
cd backend-existente
cp kernel ...
```

La nueva adopción debe ser:

```text
workspace/
├── ads/
└── repo-existente/
```

ADS se instala en su propio repo y registra el repo existente como una source.

---

# 50. Adopción multi-repo

Ejemplo:

Situación inicial:

```text
~/dev/
├── pesquerapp-front/
├── pesquerapp-api/
└── pesquerapp-mobile/
```

Objetivo:

```text
~/dev/la-pesquerapp/
├── ads/
├── frontend/
├── backend/
└── mobile/
```

La documentación de adopción debe explicar una transición segura.

No debe mover/renombrar repos automáticamente de forma destructiva sin aprobación explícita.

Puede permitirse clonar nuevas copias en la topología conforme si resulta más seguro.

---

# 51. Migración de proyectos ADS 1-repo existentes

Debe documentarse una ruta de migración para proyectos creados con el modelo anterior:

```text
repo/
├── kernel/
├── PROFILE
└── código
```

La migración conceptual es:

```text
workspace/
├── ads/
└── app/
```

donde:

- la organización ADS y documentación global pasan a `ads`;
- el código continúa o se extrae a `app`;
- `SOURCES.toml` registra `app`.

Dado que ADS 2.0 todavía está en evolución, no debe mantenerse una compatibilidad compleja que perpetúe la arquitectura antigua.

Debe priorizarse una migración clara.

---

# 52. PROJECT

`PROJECT.md` debe seguir siendo el binder humano del ADS Project.

Debe actualizarse para declarar explícitamente:

```text
Este repositorio es el control plane versionado del producto.
Los repositorios técnicos se declaran en SOURCES.toml.
```

No debe copiar en una tabla todas las URLs de `SOURCES.toml`.

Puede enlazar:

```text
Composición técnica del producto: `SOURCES.toml`
```

---

# 53. PROFILE

El PROFILE continúa siendo uno por producto.

NO:

```text
PROFILE frontend
PROFILE backend
PROFILE mobile
```

Sí:

```text
LA PESQUERAPP
    └── PROFILE único
```

El PROFILE puede registrar diferencias importantes entre componentes si afectan a objetivos, riesgos o restricciones, pero no se fragmenta por repositorio.

---

# 54. DSP

Debe dejarse explícito en la semántica del DSP:

- existe un único DSP por ADS Project;
- DSP razona sobre el producto completo;
- source/repo es una dimensión de ejecución;
- DSP puede componer rutas que atraviesen múltiples sources;
- DSP puede asignar read/write source scope a packages;
- la falta de una source bloquea sólo los packages que la requieren.

---

# 55. ENT

ENT debe ser capaz de integrar un cambio lógico con contribuciones de múltiples repositorios.

Debe responsabilizarse conceptualmente de:

- verificar convergencia de source changes;
- comprobar Integration Set;
- coordinar migraciones;
- ejecutar o solicitar integración/E2E;
- manejar integración parcial;
- preparar release/rollback cuando corresponda.

No debe asumir que “merge del PR” significa “producto integrado”.

---

# 56. PLT

PLT debe tratar el workspace multi-repo como infraestructura de desarrollo.

Ámbitos posibles:

- preparación de repos;
- CI cruzada;
- caches;
- entornos;
- servicios de desarrollo;
- observabilidad;
- aislamiento;
- worktrees/sandboxes;
- materialización cloud.

La semántica del producto continúa fuera de PLT.

---

# 57. SIS / runtime futuro

El runtime futuro debe consumir una abstracción tipo:

```text
ADS Project
    + Source Manifest
    + Source Scope
```

y resolverla hacia el proveedor actual.

No debe codificar el producto en términos de:

```text
Cursor workspace
```

o:

```text
Claude --add-dir
```

Esos son adapters.

---

# 58. AGENTS compilado

`AGENTS.md` debe incluir la regla operativa, sin duplicar el manifest:

- este es el control repo;
- las sources se resuelven mediante `SOURCES.toml`;
- todo trabajo debe determinar scope;
- no asumir que el repo actual contiene el código;
- no modificar sources no autorizadas;
- no copiar estado global a repos técnicos;
- validar workspace antes de actuar cuando el package dependa de sources.

La lista concreta de repos no debe quedar hard-coded en AGENTS si ya vive en `SOURCES.toml`.

---

# 59. START_HERE

`START_HERE.md` requiere una revisión estructural.

Debe dejar de explicar:

```text
crea mi-proyecto
cd mi-proyecto
añade remote
```

como si ADS y código fueran el mismo repo.

Debe explicar:

```text
mi-proyecto/
    ads/
    sources...
```

y separar:

1. crear ADS Project;
2. publicar el repo ADS;
3. declarar sources;
4. materializar workspace;
5. completar PROFILE;
6. bootstrap/circuitos.

---

# 60. BOOTSTRAP_PROMPT

El bootstrap debe enseñar al agente que:

- está en un repo ADS de control;
- el código puede vivir fuera del cwd;
- debe leer `SOURCES.toml`;
- no debe inventar que una source no existe sólo porque no esté dentro de `ads/`;
- puede comprobar/materializar las sources;
- debe construir conocimiento global desde todos los componentes pertinentes;
- las decisiones y documentación global se escriben en ADS.

En adopción de producto existente, el agente debe inspeccionar las sources registradas.

---

# 61. Validadores

`ads_lint.py` y/o validadores relacionados deben incorporar:

- presencia de `SOURCES.toml` en proyectos nuevos;
- schema válido;
- referencias de componentes;
- consistencia de estructura;
- enlaces/documentos actualizados;
- ausencia de reglas contradictorias del viejo modelo.

El lint normativo no debe requerir que todas las sources estén físicamente presentes para validar documentación estática.

Para eso existe:

```text
workspace check
```

Debe separarse:

```text
validez del ADS Project
```

de:

```text
disponibilidad del workspace actual
```

---

# 62. Validación estática vs operacional

Ejemplo:

```text
ads_lint
    SOURCES.toml bien formado
    referencias correctas
    corpus consistente

workspace check
    frontend está clonado
    backend remote correcto
    mobile falta
```

Esto permite validar el repositorio ADS en CI aunque los repos técnicos privados no estén disponibles.

---

# 63. Errores de workspace

Casos que deben tratarse explícitamente:

## Source ausente

```text
frontend: present
backend: missing
```

Un trabajo frontend puro puede continuar.

Un package que requiera backend debe quedar bloqueado por dependencia de materialización.

---

## Directorio ocupado por repo incorrecto

```text
backend/
    origin = otro-proyecto
```

ERROR.

No clonar encima.

No resetear.

No cambiar automáticamente el remote.

---

## Source dirty

No es automáticamente error.

Debe reportarse.

La política de aislamiento del package decide cómo proceder.

Nunca destruir cambios locales.

---

## Source sin remote

Si el manifest exige una identidad remota y el repo existente no puede demostrarse equivalente:

ERROR o bloqueo seguro.

---

## Remote inaccesible

No invalida el ADS Project.

Bloquea la materialización de esa source.

El error debe identificar:

- source;
- remote;
- operación fallida;

sin exponer secretos.

---

# 64. Credenciales

ADS no gestiona secretos Git dentro de `SOURCES.toml`.

Autenticación procede de:

- SSH agent;
- credential manager;
- token del entorno;
- integración cloud;
- GitHub App;
- provider runtime.

El kernel sólo declara identidad.

---

# 65. Clone URLs

El manifiesto debe aceptar una URL Git canónica.

No añadir simultáneamente, salvo necesidad demostrada:

```text
github_slug
ssh_url
https_url
api_url
```

porque serían datos duplicados.

Un adapter puede derivar lo que necesite de la identidad remota o resolverlo mediante proveedor.

---

# 66. Coste y rendimiento

La implementación debe respetar:

```text
repos disponibles
    !=
repos cargados enteros en contexto
```

El mero hecho de materializar varias sources no autoriza al agente a leerlas indiscriminadamente.

El source scope debe usarse para minimizar:

- búsqueda;
- tokens;
- I/O;
- preparación de entornos;
- pruebas innecesarias.

---

# 67. Cloud: no clonar todo obligatoriamente

Una plataforma remota debe poder materializar:

```text
ADS + sources requeridas
```

en lugar de todo el producto si el scope está determinado.

Pero también debe poder materializar todo mediante:

```text
workspace init
```

cuando resulte más simple o sea necesario para integración.

---

# 68. Reutilización local

Una vez materializado:

```text
workspace/
├── ads/
├── frontend/
└── backend/
```

las sesiones futuras deben reutilizarlo.

No debe existir un coste de clone por conversación.

---

# 69. Reutilización cloud

ADS no debe exigir una estrategia concreta de cache.

Si el proveedor mantiene snapshots, caches o entornos reutilizables, el adapter puede aprovecharlos.

Si no, `workspace init` debe poder reconstruir el workspace desde Git.

Esto da portabilidad.

---

# 70. Reproducibilidad

La composición viva dice:

```text
qué sources pertenecen al producto
```

No es suficiente para decir:

```text
qué revisiones exactas forman un estado integrado
```

Por ello la composición (`SOURCES.toml`) y el Integration Set son conceptos distintos.

---

# 71. No fijar SHAs en `SOURCES.toml` para el trabajo normal

`SOURCES.toml` no debe convertirse en un archivo de submodules manual.

No debe requerir actualizar un SHA cada vez que frontend avanza.

Su misión es identidad/composición.

Las revisiones exactas verificadas pertenecen al estado de integración.

---

# 72. Separación de verdades

Debe quedar explícito:

```text
SOURCES.toml
    qué sources/componentes forman el producto

Git de cada source
    historial y estado de código

estado ADS
    qué trabajo está ocurriendo

Integration Set
    qué revisiones exactas se verificaron juntas

contratos
    qué interfaz debe cumplirse
```

Ninguna de estas piezas debe intentar sustituir a todas las demás.

---

# 73. Experiencia del Owner

La arquitectura sólo es correcta si el Owner puede trabajar así:

```text
abre ADS
```

y después:

> Añade X al producto.

No debe necesitar decir:

> ahora ve al backend

ni:

> copia este MD al frontend

ni:

> recuerda que en el otro chat decidimos...

ni:

> abre esta branch

ni:

> dime qué commit tengo que pasar al otro agente.

ADS debe resolver la distribución técnica.

---

# 74. Ejemplo completo — feature frontend + backend

Owner:

> Quiero que al crear un cliente podamos registrar también su idioma preferido.

ADS:

1. crea/actualiza un item global;
2. identifica web + API;
3. inspecciona contrato actual;
4. decide si hace falta cambio contractual;
5. crea la decisión/contrato global si corresponde;
6. materializa frontend/backend;
7. entrega ambos como contexto;
8. package(s) modifican las implementaciones;
9. ejecuta tests por source;
10. ejecuta verificación de contrato;
11. crea commits/branches/PR por source;
12. registra los source changes;
13. genera/actualiza Integration Set;
14. ejecuta integración/E2E;
15. cierra el item sólo cuando el estado global sea coherente.

El Owner no realiza ningún handoff manual.

---

# 75. Ejemplo — frontend con backend sólo como lectura

Owner:

> Corrige el formulario porque no está interpretando bien la respuesta de la API.

Scope:

```text
frontend:
    write

backend:
    read
```

El agente inspecciona el backend para comprobar la respuesta real.

Sólo modifica frontend.

---

# 76. Ejemplo — source no disponible

Package:

```text
write:
    frontend
    backend
```

Workspace:

```text
frontend = OK
backend = missing
```

ADS:

```text
package bloqueado:
    source requerida "backend" no materializada
```

Puede intentar `workspace init backend`.

Si falla por autenticación:

```text
bloqueo operacional recuperable
```

No debe inventar el contrato ni continuar a ciegas.

---

# 77. Ejemplo — despliegue independiente

Supongamos:

```text
frontend AAA
backend BBB
```

han sido verificados juntos.

Backend se despliega primero.

ADS puede registrar:

```text
backend deployed BBB
frontend pending AAA
```

El producto está en una transición de deployment.

No debe declararse una release global completa hasta cumplir la política correspondiente.

---

# 78. Qué debe cambiar en el corpus actual

El agente implementador debe buscar y corregir sistemáticamente todas las suposiciones de:

```text
"el repo"
"este repositorio contiene el proyecto"
"cd tu-proyecto-existente y copia ADS"
"una branch/PR por tarea"
"ficheros del repo" como único carrier físico
```

cuando semánticamente deban pasar a:

```text
ADS Project
control repo
source
workspace
source changes
```

No realizar reemplazos mecánicos de texto sin comprender cada contexto.

---

# 79. Ficheros conocidos que deben revisarse

Como mínimo:

```text
START_HERE.md
tooling/new-project.sh
kernel/PROJECT_TEMPLATE.md
kernel/PROFILE_TEMPLATE.md
kernel/BOOTSTRAP_PROMPT.md
kernel/KERNEL.md
kernel/operativo/00-INDICE.md
kernel/operativo/capacidades/DSP/...
kernel/operativo/capacidades/ENT/...
kernel/operativo/capacidades/PLT/...
kernel/operativo/capacidades/SIS/...
kernel/operativo/plantillas/CHECKPOINT.md
docs/rediseno/a-CAPACIDADES-APROBADA.md
docs/rediseno/b-RECORRIDO-APROBADA.md
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
validadores
tests
documentación de evolución afectada
```

El agente debe realizar búsqueda global para localizar otros puntos afectados.

Esta lista no es exhaustiva.

---

# 80. Actualización de “estado = ficheros del repo”

La expresión histórica:

```text
el estado operativo son los ficheros del repo
```

debe reinterpretarse formalmente.

La verdad persistente global continúa siendo directamente legible y versionable, pero “repo” pasa a significar:

```text
repositorio ADS de control
```

para el estado global.

El código y sus revisiones viven en sus sources.

Un estado global puede referenciar SHAs en otras sources sin copiar su contenido.

---

# 81. Regla de autoridad

La autoridad debe quedar así:

```text
CONTROL REPO
    verdad de organización/producto

SOURCE REPOS
    verdad de sus implementaciones

RUNTIME
    estado operacional efímero cuando exista

INTEGRATION SET
    evidencia versionada de composición verificada
```

Un futuro runtime no debe sustituir silenciosamente la verdad durable del control repo.

---

# 82. Cambios a plantillas

Deben existir plantillas/ejemplos para:

- `SOURCES.toml`;
- source scope de package;
- source changes;
- Integration Set;
- checkpoint multi-source cuando proceda.

No crear plantillas redundantes si el mismo formato puede servir para varios casos.

---

# 83. Cambios a compilación

Si AGENTS se compila desde kernel + packs + PROFILE:

- la compilación debe conocer que existe `SOURCES.toml`;
- puede incluir instrucciones operativas derivadas;
- no debe incrustar una copia completa del manifiesto;
- un cambio de URLs/repos no debe requerir editar manualmente AGENTS.

---

# 84. Cambios a CI del ADS Project

La CI del control repo debe poder:

- validar corpus;
- validar `SOURCES.toml`;
- validar documentación;
- ejecutar tests de tooling;
- no necesitar credenciales a todos los repos técnicos para validaciones estáticas.

Los tests integrados multi-repo pertenecen a pipelines que dispongan de las sources necesarias.

---

# 85. Pruebas automatizadas de `workspace.py`

Deben añadirse tests sin depender de GitHub real.

Usar repositorios Git temporales/local bare cuando sea posible.

Casos mínimos:

1. manifest vacío válido;
2. una source válida;
3. varias sources válidas;
4. clone de source ausente;
5. reutilización de source existente;
6. path duplicado;
7. id duplicado;
8. `../` escape;
9. ruta absoluta;
10. path reservado `ads`;
11. remote equivocado;
12. directorio no Git;
13. repo dirty no destruido;
14. source inexistente remota;
15. componente con source inexistente;
16. component path fuera de source;
17. normalización HTTPS/SSH donde aplique;
18. `status --json`;
19. selección de source en `init`;
20. ejecución desde subdirectorio del control repo si se decide soportarla.

---

# 86. Prueba end-to-end del bootstrap

Un test debe verificar:

```text
new-project.sh demo
```

produce:

```text
demo/
└── ads/
    ├── .git/
    ├── SOURCES.toml
    ├── PROJECT.md
    ├── PROFILE.md
    ├── kernel/
    └── ...
```

y que:

```text
demo/
```

no sea repo Git.

---

# 87. Prueba de adopción conceptual

Debe existir fixture/documentación verificable con:

```text
workspace/
├── ads/
├── frontend/
└── backend/
```

donde frontend/backend sean repos independientes y `workspace check` los reconozca correctamente.

---

# 88. No añadir infraestructura innecesaria

Esta implementación NO autoriza a crear ahora:

- servidor central ADS;
- base de datos;
- registry propio;
- daemon;
- broker;
- cola;
- API cloud;
- servicio Git;
- lock service;
- submodule manager;
- monorepo tooling.

La primera implementación debe resolver la semántica y la materialización reproducible con archivos + Git + tooling ligero.

---

# 89. No resolver problemas futuros por anticipado

No implementar ahora, salvo que sea estrictamente necesario:

- sincronización distribuida;
- atomic commits multi-repo;
- mirrors;
- checkout parcial avanzado;
- virtual filesystems;
- federación de ADS Projects;
- dependencia entre productos ADS;
- registry global de componentes;
- GitHub-only orchestration;
- multi-cloud execution.

El diseño actual debe permitirlos sin necesitarlos.

---

# 90. Compatibilidad monorepo/híbrida

Aunque la motivación inicial sea multi-repo, la abstracción `component -> source + path` debe evitar que ADS quede encerrado en:

```text
1 repo = 1 component
```

No es necesario desarrollar tooling específico de monorepo complejo en esta iteración.

Sólo evitar una restricción conceptual que obligue a romper el esquema después.

---

# 91. Source scope y permisos

El runtime/agente debe tratar:

```text
read_sources
write_sources
```

como declaración de alcance.

No es un sistema de seguridad duro por sí mismo.

Pero adapters compatibles deben usarlo para limitar carpetas editables cuando sea posible.

---

# 92. Unavailable source y fault recovery

La source ausente debe ser un fallo explícito y recuperable.

ADS debe conservar suficiente contexto para reanudar cuando vuelva a estar disponible.

No debe obligar a reiniciar el item desde cero.

---

# 93. Cambio de remote

Si una source migra de:

```text
org-a/backend
```

a:

```text
org-b/backend
```

el cambio ocurre una vez en:

```text
SOURCES.toml
```

Las referencias por `source id = backend` continúan siendo estables.

Esta es otra razón para no usar la URL como identificador lógico en items/packages.

---

# 94. Renombrado de ruta local

Si:

```text
path = "backend"
```

cambia a:

```text
path = "api"
```

la identidad de source continúa siendo:

```text
id = backend
remote = ...
```

Los items no deben romperse porque cambie una ruta local.

---

# 95. Eliminación de source

Eliminar una source del producto es una decisión de composición.

No debe implicar borrar automáticamente el repositorio local.

ADS actualiza su manifest y deja de considerarlo parte del producto.

El borrado físico necesita una acción explícita distinta.

---

# 96. Alta de nueva source

Debe ser posible añadir:

```text
infra
```

modificando `SOURCES.toml`, validando y materializando.

No debe requerir reinstalar ADS.

---

# 97. Cambios normativos

La documentación normativa debe declarar como principios:

### N1

Un ADS Project representa un producto/sistema, no un repositorio.

### N2

Un ADS Project tiene un único control repo.

### N3

El control repo es la autoridad organizativa global.

### N4

El producto puede tener 0..N sources.

### N5

Una source es una ubicación física versionada.

### N6

Un componente lógico referencia una source y path.

### N7

Componente y source no tienen cardinalidad 1:1 obligatoria.

### N8

El workspace local estándar utiliza repos hermanos.

### N9

La identidad de una source no depende de su ruta local.

### N10

El estado global no se copia en las sources.

### N11

Un item/package puede atravesar múltiples sources.

### N12

Git permanece independiente por source.

### N13

La integración multi-repo es lógica y evidenciada, no un commit Git ficticio.

### N14

El kernel es provider-neutral.

---

# 98. Invariantes

La implementación debe poder comprobar o preservar:

```text
I1. Existe una única fuente de verdad para la composición.
I2. Ninguna source técnica necesita contener ADS para participar.
I3. Un workspace puede reconstruirse a partir del control repo + Git remotes.
I4. Una source existente nunca se destruye para "arreglar" el workspace.
I5. El mismo modelo sirve local y cloud.
I6. El Owner no actúa como mensajero entre repos.
I7. El agente recibe sólo el scope necesario.
I8. Los cambios Git continúan siendo propios de cada repo.
I9. ADS puede recuperar qué revisiones se probaron juntas.
I10. Ninguna integración de proveedor se convierte en requisito del kernel.
```

---

# 99. Criterios de aceptación funcionales

La implementación no se considera terminada hasta demostrar:

## CA-1

Se puede crear un ADS Project nuevo y el resultado es:

```text
workspace/ads
```

en lugar de un único repo mezclado.

## CA-2

El control repo puede declarar frontend y backend mediante `SOURCES.toml`.

## CA-3

Con ambos ya clonados como hermanos, `workspace check` los detecta sin volver a clonarlos.

## CA-4

Con backend ausente, `workspace init backend` puede materializarlo.

## CA-5

Una source con remote equivocado produce error seguro.

## CA-6

Un repo dirty no pierde cambios.

## CA-7

Un component puede apuntar a un path dentro de una source.

## CA-8

Dos components pueden apuntar a la misma source.

## CA-9

La documentación deja de enseñar la adopción copiando ADS dentro del repo técnico.

## CA-10

PROFILE sigue siendo único por producto.

## CA-11

DSP/routes/packages pueden expresar scope multi-source.

## CA-12

Checkpoint puede registrar múltiples revisiones de sources.

## CA-13

Existe representación de Integration Set.

## CA-14

G29 no presupone una única branch/PR global.

## CA-15

Los validadores del kernel pasan.

## CA-16

Los tests de workspace pasan sin red externa.

## CA-17

No se introduce dependencia obligatoria de Cursor, Claude, Codex, Gemini o GitHub.

---

# 100. Criterios de aceptación de experiencia

Un agente nuevo que sólo abra:

```text
workspace/ads
```

debe poder descubrir sin información oral adicional:

1. que está ante un ADS control repo;
2. cuál es el producto;
3. qué sources existen;
4. dónde deberían estar localmente;
5. cómo comprobarlas;
6. cómo materializar las ausentes;
7. qué componentes viven en ellas;
8. dónde vive la documentación global;
9. que no debe copiar ADS en las sources;
10. que un cambio puede afectar varias sources.

---

# 101. Criterio de éxito principal

El caso que debe guiar toda la implementación es:

> El Owner inicia una conversación desde el ADS Project y pide una feature transversal. El sistema puede inspeccionar y modificar frontend y backend, conservar una única decisión/contrato/estado, producir los cambios Git necesarios en cada repositorio y verificar el conjunto sin que el Owner tenga que trasladar contexto manualmente entre repositorios o chats.

Si esto requiere que el Owner sea mensajero, la implementación ha fallado aunque todos los archivos de configuración sean técnicamente correctos.

---

# 102. Antiobjetivos

La implementación se considera desviada si termina creando cualquiera de estos modelos:

```text
ADS frontend
ADS backend
ADS mobile
```

como organizaciones completas independientes que después deban sincronizarse.

También es desviación:

```text
copiar PROFILE en cada repo
```

```text
copiar memoria en cada repo
```

```text
usar submodules sólo para conseguir que el agente vea varios repos
```

```text
hacer que Git sea el coordinador del producto
```

```text
obligar al Owner a abrir varios chats
```

```text
acoplar el kernel a un proveedor concreto
```

---

# 103. Relación con proyectos simples

Incluso si un producto sólo tiene un repositorio de código, el modelo conceptual nuevo será:

```text
workspace/
├── ads/
└── app/
```

Esto mantiene una arquitectura uniforme.

No deben mantenerse dos semánticas fundamentales:

```text
si 1 repo → ADS dentro del código
si varios → ADS separado
```

porque volvería a introducir bifurcaciones en todo el kernel.

---

# 104. Impacto de compatibilidad

Esta decisión cambia el layout histórico del bootstrap.

Por tanto debe tratarse como un cambio estructural visible de ADS 2.0.

El agente implementador debe:

- revisar VERSION/changelog conforme a las reglas existentes;
- registrar la decisión;
- documentar migración;
- actualizar tests;
- eliminar contradicciones del corpus.

No debe mantener compatibilidad accidental con instrucciones obsoletas si ello debilita la nueva arquitectura.

---

# 105. Registro de decisión

Debe añadirse o actualizarse el ADR/registro normativo correspondiente con una decisión equivalente a:

```text
ADS PROJECT ≠ GIT REPOSITORY

Se adopta un control repo ADS independiente y un workspace de repos hermanos.
La composición se declara mediante SOURCES.toml.
Los repos técnicos continúan independientes.
```

Debe incluir las razones:

- multi-repo es normal en productos reales;
- repos pueden usar stacks diferentes;
- pueden tener despliegues independientes;
- agentes modernos pueden trabajar con múltiples carpetas/repos;
- la coordinación global no requiere fusionar físicamente los repos;
- separar gobierno de código reduce duplicación;
- mantiene un único contexto y estado;
- evita que el Owner sea el canal de integración.

---

# 106. Decisiones expresamente cerradas por este documento

Quedan cerradas para esta implementación:

### D1 — Home global

**Repositorio ADS independiente.**

### D2 — Source of truth global

**Repositorio ADS.**

### D3 — Composición

**Manifiesto versionado `SOURCES.toml`.**

### D4 — Materialización local

**Workspace con repos hermanos.**

### D5 — Identidad de source

**Remote Git canónico + source id estable.**

### D6 — Submodules

**No forman parte de la arquitectura base.**

### D7 — Trabajo multi-repo

**Un item/package puede abarcar múltiples sources.**

### D8 — Estado global

**No se duplica por repo.**

### D9 — Integración

**Integration Set con revisiones exactas.**

### D10 — Provider model

**Adapters sobre un contrato de filesystem/Git.**

---

# 107. Decisiones que permanecen abiertas fuera de este alcance

Este documento NO cierra detalles no necesarios para implementar la arquitectura base, por ejemplo:

- formato final del runtime distribuido;
- sistema de locks multi-agente;
- scheduler;
- colas;
- servicio cloud ADS;
- estrategia universal de release;
- política detallada de despliegues parciales;
- almacenamiento externo de eventos;
- mirrors;
- provider adapters completos.

Si durante la implementación aparece una de estas cuestiones, no debe utilizarse como excusa para retrasar el soporte base multi-repo.

---

# 108. Orden recomendado de implementación

El agente puede adaptar el orden si encuentra dependencias reales, pero debe cubrir todo el alcance.

## Paso A — Corpus y modelo

1. registrar decisión;
2. introducir source/component/workspace/integration-set en normativa;
3. eliminar equivalencia proyecto=repo.

## Paso B — Manifest

1. crear plantilla `SOURCES.toml`;
2. implementar parser/validator;
3. tests.

## Paso C — Workspace tooling

1. resolución root;
2. check;
3. init;
4. status;
5. JSON output;
6. tests locales con repos temporales.

## Paso D — Bootstrap

1. modificar `new-project.sh`;
2. crear `workspace/ads`;
3. actualizar output;
4. tests.

## Paso E — Operación

1. DSP;
2. packages/source scope;
3. checkpoints;
4. ENT;
5. Git governance;
6. Integration Set.

## Paso F — Documentación

1. START_HERE;
2. adopción;
3. bootstrap prompt;
4. PROJECT;
5. PROFILE;
6. AGENTS compilation;
7. ejemplos.

## Paso G — Conformance

1. búsqueda global de contradicciones;
2. validators;
3. tests completos;
4. lint;
5. enlaces;
6. versión.

---

# 109. Regla para el agente implementador

No debe limitarse a editar los ficheros enumerados en este documento.

Debe inspeccionar todo el branch y localizar dependencias semánticas de la suposición anterior.

Debe preguntarse en cada caso:

> ¿Este texto/código presupone que el ADS Project y el repo de código son la misma cosa?

Si sí, debe corregirlo de forma coherente con esta arquitectura.

---

# 110. Regla de simplicidad

Ante dos implementaciones equivalentes, elegir la que:

- tenga menos fuentes de verdad;
- menos configuración;
- menos archivos manuales;
- menos dependencias;
- menos provider-specific code;
- menos pasos para el Owner;
- sea más fácil de reconstruir desde Git.

No crear abstracciones adicionales sólo porque puedan ser útiles en el futuro.

---

# 111. Regla de no duplicación

No mantener simultáneamente:

```text
SOURCES.toml
+
lista equivalente en PROJECT.md
+
lista equivalente en AGENTS.md
+
lista equivalente en runtime config
```

`SOURCES.toml` es autoridad.

Las demás representaciones deben:

- referenciarla;
- derivarse;
- o ser cache efímera.

---

# 112. Regla de trazabilidad

Todo cambio multi-repo debe poder llegar finalmente a una cadena conceptual:

```text
Owner intent
    ↓
item
    ↓
route/package
    ↓
source changes
    ↓
commits/PR
    ↓
Integration Set
    ↓
verification
    ↓
release/deployment si existe
```

El usuario no tiene que operar esta cadena manualmente.

---

# 113. Regla de independencia de chat

El estado necesario para continuar un cambio multi-repo debe sobrevivir al cierre de la conversación.

No es aceptable que:

```text
el backend sabía X sólo porque estaba en otro chat
```

Todo conocimiento durable relevante debe estar:

- en una fuente global;
- en una decisión;
- en un contrato;
- en el estado;
- en un checkpoint;
- o referenciado mediante versión.

---

# 114. Resultado esperado tras la implementación

ADS debe poder representar de forma natural:

```text
LA PESQUERAPP
│
└── ADS PROJECT
    │
    ├── PROFILE único
    ├── DSP único
    ├── memoria única
    ├── decisiones globales
    ├── contratos globales
    ├── items/rutas/packages
    │
    └── SOURCES.toml
        │
        ├── frontend → Git repo A
        ├── backend  → Git repo B
        └── mobile   → Git repo C
```

En local:

```text
la-pesquerapp/
├── ads/
├── frontend/
├── backend/
└── mobile/
```

En cloud:

```text
workspace/
├── ads/
├── frontend/
├── backend/
└── mobile/
```

La topología física puede ser reconstruida.

La organización lógica es la misma en ambos casos.

---

# 115. Mandato final de implementación

El agente encargado de aplicar este documento debe:

1. leer el corpus actual de ADS Kernel antes de modificarlo;
2. tratar este documento como la decisión aprobada para multi-repo;
3. implementar la arquitectura de control repo + sibling workspace;
4. crear `SOURCES.toml` como fuente de verdad de composición;
5. implementar tooling mínimo de materialización/validación;
6. modificar bootstrap y adopción;
7. adaptar PROFILE/PROJECT/BOOTSTRAP/AGENTS;
8. adaptar DSP, packages, checkpoints y Git governance;
9. incorporar Integration Set;
10. actualizar normativa y documentación;
11. localizar y resolver todas las contradicciones del viejo modelo;
12. añadir tests;
13. ejecutar todos los validadores existentes y nuevos;
14. no introducir dependencias o servicios innecesarios;
15. no convertir la solución en Git submodules;
16. no duplicar ADS dentro de los repos técnicos;
17. no acoplar ADS a Cursor, Claude, Codex, Gemini o GitHub;
18. conservar la filosofía de una fuente de verdad;
19. conservar trazabilidad y recuperación;
20. dejar el branch en un estado coherente, verificable y documentado.

La implementación no termina cuando existe `SOURCES.toml`.

Termina cuando **todo ADS entiende que un producto es superior a sus repositorios físicos y puede operar sobre ellos como una única organización de desarrollo**.

---

# 116. Test mental final

Antes de considerar el trabajo cerrado, comprobar:

> Si mañana La Pesquerapp tiene frontend Next.js, backend Laravel, app móvil y repositorio de infraestructura, ¿puedo clonar/abrir sólo su repo ADS, reconstruir el workspace, pedir una feature transversal y dejar que ADS coordine todo sin que el Owner transporte contexto manualmente entre repos?

Si la respuesta no es claramente **sí**, todavía quedan cambios por implementar.

---

**Fin de la decisión.**
