# ADS — Ideas consolidadas y cuestiones abiertas tras la evolución NEXT

> Estado: documento de trabajo del Owner.
>
> Este archivo **no es una especificación cerrada** ni autoriza a implementar automáticamente
> todos sus puntos. Recoge ideas consolidadas, necesidades detectadas y cuestiones que deben
> investigarse o diseñarse antes de materializarlas.

---

# 1. Objetivo de este documento

Durante la evolución de ADS han aparecido varias necesidades que deben incorporarse al análisis
global del sistema:

- simplificación y optimización del propio ADS;
- actualización controlada de ADS en proyectos que ya lo utilizan;
- tratamiento especial de trabajos de gran alcance que necesitan algo más que tasks/packages;
- coordinación real de productos compuestos por varios repositorios;
- contratos compartidos entre componentes;
- integración y verificación a nivel de producto, no sólo de repositorio.

Una cuestión queda **expresamente abierta y bloqueada para implementación**:

> **Cómo materializar un único proyecto ADS cuando el producto está repartido entre varios repositorios.**

No debe resolverse apresuradamente ni dejarse a una implementación automática sin una fase previa
de investigación, comparación de alternativas y decisión del Owner.

---

# 2. Auditoría de simplificación y optimización de ADS

ADS debe ser capaz de auditar no sólo su corrección, sino también su complejidad.

La conformidad del sistema debería buscar:

- erratas;
- referencias rotas;
- incongruencias;
- contradicciones;
- duplicaciones;
- redundancias;
- fuentes de verdad duplicadas;
- protocolos que aportan poca garantía respecto a su coste;
- roles, métodos, gates, documentos o estados sin consumidor real;
- mecanismos históricos sustituidos pero todavía presentes;
- complejidad accidental;
- pasos que puedan eliminarse sin perder garantías;
- piezas que puedan fusionarse sin mezclar responsabilidades realmente distintas.

Principio:

> Antes de crear un nuevo concepto, protocolo, documento, rol, gate o mecanismo, ADS debe comprobar
> si puede expresarse correctamente mediante algo que ya existe.

La regla inversa también aplica:

> No se deben fusionar conceptos diferentes únicamente para reducir el número de piezas.

La auditoría debe ser **substractiva**: encontrar cosas que retirar, fusionar, simplificar o reemplazar.

---

# 3. Actualización de ADS en proyectos ya instalados

Cada proyecto debe conocer y fijar la versión de ADS que utiliza.

Es legítimo que distintos proyectos estén temporalmente en versiones diferentes:

```text
Proyecto A → ADS X
Proyecto B → ADS Y
Proyecto C → ADS Z
```

No se pretende que todos consuman automáticamente el estado más reciente de `ads-kernel`.

Principio provisional:

> **Detectar automáticamente; actualizar conscientemente.**

Una actualización de ADS no equivale a copiar archivos encima.

Debe existir un ciclo equivalente a:

```text
versión instalada
      ↓
versión disponible
      ↓
comparación
      ↓
impacto sobre este proyecto
      ↓
compatibilidad
      ↓
plan de migración
      ↓
aplicación
      ↓
validación
      ↓
rollback posible
```

Debe analizar como mínimo:

- kernel;
- packs;
- skills;
- adaptadores;
- tooling;
- runtime;
- schemas;
- estado persistido;
- PROFILE;
- overrides;
- personalizaciones locales;
- documentación generada;
- mecanismos retirados;
- compatibilidad con procesos en curso.

Debe estudiarse si la actualización ADS dentro de un proyecto puede representarse mediante
procesos/capacidades existentes —por ejemplo DEP/PLT/SIS— en lugar de crear automáticamente un
nuevo tipo de proceso.

---

# 4. Unidad de trabajo superior a task/package

Se detecta la necesidad de una unidad persistente que represente **trabajos de entidad suficiente
como para necesitar memoria, documentación, coordinación y evolución propias**.

No debe diseñarse exclusivamente para features.

Debe servir para cualquier trabajo que, por tamaño, duración, alcance o transversalidad, necesite
algo más que un paquete/tarea aislado.

Ejemplos:

- feature grande;
- nueva lógica de negocio;
- auditoría extensa;
- migración importante;
- cambio de arquitectura;
- cambio de dirección amplio;
- investigación compleja;
- programa de seguridad;
- integración externa importante;
- transformación de datos;
- adopción de ADS;
- evolución relevante del propio sistema;
- iniciativas que agrupen varios items/packages relacionados.

Nombre definitivo: **pendiente**.

Conceptualmente:

```text
UNIDAD DE TRABAJO AMPLIA
        │
        ├── intención / pregunta / resultado
        ├── memoria viva
        ├── decisiones
        ├── documentación
        ├── artefactos
        ├── contratos
        ├── riesgos
        ├── items
        ├── packages
        ├── evidencias
        └── cierre
```

No debe convertirse en una nueva capa burocrática para trabajos pequeños.

Su activación debe depender de criterios de alcance/impacto/complejidad.

---

# 5. Dossier vivo de trabajos de gran alcance

Cuando la unidad anterior se active, debe existir documentación persistente asociada al trabajo.

No significa crear diez `.md` obligatorios por cada iniciativa.

Principio:

> La documentación debe actuar como índice y memoria de fuentes únicas, no como una colección de
> copias del mismo contenido.

Ejemplo conceptual:

```text
docs/<unidad>/<id>/
    README / INDEX
    producto
    dominio
    arquitectura
    contratos
    decisiones
    integración
    validación
    cierre
```

La estructura exacta debe poder variar según el tipo de trabajo.

Debe conservar:

### Antes
- por qué existe;
- resultado perseguido;
- alcance;
- fuera de alcance;
- riesgos;
- alternativas;
- dependencias;
- contratos previstos;
- impacto.

### Durante
- decisiones tomadas;
- cambios de alcance;
- versiones de contratos;
- items/packages derivados;
- componentes afectados;
- bloqueos;
- evidencia;
- estado de integración.

### Después
- qué terminó existiendo realmente;
- decisiones finales;
- commits/releases relacionados;
- evidencia;
- deuda o trabajo derivado;
- aprendizaje.

---

# 6. Feature grande como caso particular

El proceso `FEA` sigue representando correctamente la intención de añadir una nueva capacidad.

No se propone necesariamente crear otro proceso para “feature grande”.

Lo que cambia es el **radio de impacto y la forma de ejecución**.

Una FEA podría activar la unidad superior cuando:

- introduce lógica de negocio relevante;
- toca varios componentes;
- toca varios repositorios;
- necesita nuevas entidades;
- necesita migraciones;
- introduce contratos entre componentes;
- cambia un flujo principal;
- tiene riesgos relevantes;
- necesita múltiples capacidades coordinadas;
- dura lo suficiente como para necesitar memoria propia.

El feature no debe desaparecer al descomponerse en tasks.

Debe seguir existiendo como unidad coherente que permita saber meses después:

- qué se quería;
- qué se decidió;
- qué se construyó;
- qué componentes participaron;
- cómo se integró;
- cómo se verificó;
- en qué release llegó.

---

# 7. Proyecto ADS no debe equivaler a repositorio Git

Principio conceptual consolidado:

> **Un producto puede estar repartido entre varios repositorios y seguir siendo un único proyecto ADS.**

Ejemplo:

```text
                 PRODUCTO
                    │
               PROYECTO ADS
                    │
      ┌─────────────┼─────────────┐
      │             │             │
   frontend       backend       mobile
   repo A         repo B        repo C
```

Frontend y backend no deben tratarse como dos organizaciones ADS aisladas si forman un único producto.

La organización común debe compartir, cuando corresponda:

- Owner;
- ENC;
- PRD;
- DSP;
- arquitectura;
- dominio;
- investigación;
- seguridad;
- integración;
- verificación;
- memoria;
- decisiones;
- items;
- unidades amplias de trabajo;
- contratos entre componentes;
- estado global.

Cada componente puede necesitar especialización técnica distinta.

Ejemplo:

```text
CON/frontend
CON/backend
CON/mobile
```

o cualquier diseño mejor que se determine posteriormente.

---

# 8. Problema real que debe resolver el modelo multi-repo

El flujo manual habitual hoy puede ser:

```text
front analiza feature
→ determina qué necesita del back
→ Owner cambia al repo backend
→ vuelve a explicar el contexto
→ backend implementa
→ genera .md para informar al front
→ Owner vuelve al frontend
→ aparecen diferencias
→ endpoint inexistente
→ JSON distinto
→ suposiciones incompatibles
→ vuelta al backend
```

Problemas:

- el Owner actúa como mensajero;
- cada repo desarrolla una versión distinta de la feature;
- se copia contexto;
- aparecen alucinaciones sobre APIs;
- los contratos no son fuentes únicas;
- frontend y backend pueden asumir formas diferentes;
- cada repositorio puede cerrar “su parte” aunque la feature no funcione integrada;
- la documentación de handoff envejece;
- el historial del feature queda repartido.

ADS debe eliminar esta coordinación manual.

---

# 9. Contratos compartidos entre componentes

Un trabajo que cruza componentes necesita establecer contratos comunes antes de que cada parte
implemente independientemente su interpretación.

Ejemplo conceptual:

```text
necesidad de producto
       ↓
modelo / dominio
       ↓
contrato compartido versionado
       ↓
 ┌─────┴─────┐
 ↓           ↓
backend    frontend
 ↓           ↓
 └─────┬─────┘
       ↓
integración real
```

Los packages de distintos componentes deberían declarar la versión del contrato en la que se basan.

Ejemplo:

```text
based_on:
  api-contract: v3
```

Si el contrato cambia, el sistema debe poder identificar qué trabajo queda afectado.

Cuando sea posible, el contrato debe ser ejecutable/verificable:

- OpenAPI;
- JSON Schema;
- protobuf;
- GraphQL schema;
- tipos compartidos;
- contract tests;
- interfaces u otros mecanismos adecuados.

No se impone una tecnología universal.

Principio:

> Un `.md` escrito por backend para “explicarle” al frontend lo que hizo no debe ser el mecanismo
> normal de coordinación.

---

# 10. Integración como obligación global

No basta con que cada repositorio pase sus propias pruebas.

Una unidad multi-componente debe demostrar que sus componentes funcionan **juntos**.

Debe existir evidencia equivalente a un manifest o conjunto de integración:

```text
Trabajo: FEA-XXX

frontend:
  commit: ...

backend:
  commit: ...

mobile:
  commit: ...

contrato:
  versión: ...

migraciones:
  ...

entorno:
  ...

e2e:
  PASS
```

La feature/iniciativa no debe considerarse cerrada únicamente porque cada repositorio tenga su
implementación local completada.

---

# 11. Un solo ADS por producto multi-repo

Dirección conceptual preferida:

- un PROFILE de producto;
- una identidad ADS;
- una versión ADS instalada;
- un estado global;
- un DSP;
- un mapa de items;
- una memoria común;
- decisiones comunes;
- contratos comunes;
- componentes/repositorios registrados.

No se desea:

```text
ADS frontend
ADS backend
ADS mobile
```

funcionando como tres organizaciones independientes que luego intentan sincronizarse.

---

# 12. CUESTIÓN ABIERTA CRÍTICA — Materialización del proyecto multi-repo

**NO IMPLEMENTAR TODAVÍA.**

La dirección conceptual anterior está aceptada, pero no está decidido **cómo se materializa físicamente
y operacionalmente**.

Preguntas abiertas:

- ¿Dónde vive el PROFILE global?
- ¿Dónde vive el estado del runtime?
- ¿Dónde vive la documentación transversal?
- ¿Dónde viven los contratos?
- ¿Existe un repositorio de control independiente?
- ¿Existe un workspace local por encima de los repos?
- ¿Existe un “meta-repo”?
- ¿Se usa Git submodules, subtree, manifests o nada de eso?
- ¿Cómo se clona un proyecto completo?
- ¿Cómo accede un agente a varios repos simultáneamente?
- ¿Cómo funciona con Claude Code, Codex, Cursor y Gemini?
- ¿Cómo se mantienen permisos por repositorio?
- ¿Cómo trabaja un package que modifica dos repos?
- ¿Debe dividirse siempre en packages por repo?
- ¿Cómo se realiza un commit o PR coordinado multi-repo?
- ¿Qué significa rollback de una feature distribuida?
- ¿Cómo se vinculan releases de frontend y backend?
- ¿Cómo funciona CI global?
- ¿Dónde se ejecutan tests E2E?
- ¿Cómo se despliega una unidad coherente?
- ¿Cómo se adopta ADS en un producto que ya tiene repos separados?
- ¿Cómo se evita crear una nueva fuente de verdad fuera de los repos?
- ¿Cómo se evita que el control-plane sea un nuevo repositorio que también derive?
- ¿Qué ocurre si uno de los repos está inaccesible?
- ¿Cómo se representa un monorepo en el mismo modelo sin duplicar conceptos?
- ¿Cómo se soportan productos híbridos: monorepo + repos externos?
- ¿Cómo se versiona la composición del producto?
- ¿Qué herramienta conoce la correspondencia entre componentes, commits y releases?

Esta cuestión debe investigarse en profundidad antes de elegir una solución.

---

# 13. Alternativas que deben compararse antes de decidir

Como mínimo investigar:

1. repositorio de coordinación/control-plane separado;
2. workspace local no versionado que agrupa repos;
3. meta-repo con manifests;
4. monorepo;
5. Git submodules;
6. Git subtree;
7. multi-root workspaces;
8. manifests declarativos que apuntan a repos externos;
9. runtime central con repos como recursos externos;
10. combinación de las anteriores.

No se debe seleccionar una por familiaridad.

Comparar:

- fuente de verdad;
- simplicidad;
- experiencia del agente;
- experiencia del Owner;
- Git;
- CI/CD;
- atomicidad;
- PR;
- rollback;
- releases;
- trazabilidad;
- permisos;
- trabajo local;
- trabajo en cloud;
- compatibilidad multi-provider;
- recuperación ante fallo;
- escalabilidad;
- lock-in;
- adopción de proyectos existentes.

---

# 14. Instrucción para futuras implementaciones

Hasta que el Owner cierre la decisión multi-repo:

> Se pueden diseñar contratos y abstracciones que reconozcan `proyecto != repositorio`, pero no se
> debe imponer una materialización física definitiva de la unión entre repositorios.

Cualquier implementación provisional debe:

- ser reversible;
- no bloquear alternativas;
- no convertir una hipótesis en contrato permanente;
- registrar explícitamente que la materialización multi-repo sigue abierta.

---

# 15. Estado de las ideas

| Tema | Estado |
|---|---|
| auditoría substractiva/simplificación | dirección aceptada; diseñar con ADS existente |
| actualización ADS → proyectos | necesidad aceptada; política “detectar automáticamente, actualizar conscientemente” como base |
| unidad superior a task/package | necesidad aceptada; nombre/contrato por diseñar |
| dossier vivo | dirección aceptada; evitar documentación duplicada |
| FEA grande | tratar como FEA con ejecución ampliada salvo evidencia contraria |
| proyecto ≠ repositorio | principio aceptado |
| un ADS por producto multi-repo | dirección preferida |
| contratos compartidos | necesidad aceptada |
| integración global | necesidad aceptada |
| materialización física multi-repo | **ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO** |
