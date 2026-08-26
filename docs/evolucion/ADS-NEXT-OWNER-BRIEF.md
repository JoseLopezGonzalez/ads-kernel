# ADS NEXT — Directiva maestra del Owner

**Estado:** directiva de evolución del sistema  
**Ámbito:** repositorio `ads-kernel` y ecosistema ADS  
**Naturaleza:** visión, requisitos y criterios del Owner. **No es una especificación técnica cerrada.**  
**Objetivo:** llevar ADS desde su estado actual a una plataforma sólida, instalable, acumulativa y multiagente para crear, gobernar, evolucionar y mantener proyectos reales de software.

---

## 1. Propósito de esta directiva

ADS ya define una organización de trabajo para agentes de IA: capacidades, equipos, roles, agentes, métodos, procesos, rutas, paquetes, handoffs, memoria, gates, autoridad, aprendizaje y coordinación.

La siguiente evolución debe conservar esa base, pero ampliar el alcance del sistema.

La intención del Owner es que ADS deje de entenderse únicamente como un «sistema operativo de agentes» y pase a funcionar como una **base integral para proyectos de software desarrollados principalmente por agentes de IA bajo gobierno humano**.

ADS debe ayudar no sólo a decidir **quién hace qué**, sino también a establecer y gobernar de forma coherente:

- la estructura inicial de un proyecto;
- la organización agentic del proyecto;
- la documentación persistente;
- el conocimiento reutilizable;
- las skills y herramientas disponibles;
- los agentes y roles especializados necesarios;
- el gobierno del repositorio Git del proyecto real;
- el trabajo concurrente de varios agentes;
- la calidad y verificación;
- la integración y entrega;
- la incorporación de proyectos ya existentes;
- la actualización del propio ADS en proyectos ya instalados;
- la extracción de conocimiento desde proyectos reales para mejorar ADS;
- la evolución de ADS mediante sus propios procesos;
- y la continuidad del trabajo sin depender de un chat concreto, una sesión o un proveedor de IA.

Esta directiva expresa **qué debe ser capaz de conseguir ADS**. El sistema y los agentes que lo evolucionen deben determinar la arquitectura concreta adecuada después de estudiar el estado actual, las restricciones existentes, los proyectos reales disponibles y la evidencia acumulada.

---

# 2. Principio rector

La experiencia deseada es ésta:

> El Owner expresa intención, prioridades, restricciones y decisiones que realmente le corresponden. ADS se ocupa de transformar esa intención en trabajo persistente, coordinado, verificable y recuperable, utilizando los agentes, herramientas, conocimiento y procesos adecuados sin obligar al Owner a convertirse en gestor de tareas, Git, sesiones, prompts o coordinación interna.

El sistema debe ser capaz de trabajar durante meses o años sobre un proyecto sin que su continuidad dependa de recordar lo que ocurrió en conversaciones antiguas.

Nada crítico debe existir únicamente en el contexto de una conversación.

---

# 3. Principios que no deben perderse durante la evolución

La siguiente versión puede modificar profundamente la arquitectura actual si existe una razón sólida, pero debe conservar los principios que dan sentido a ADS.

## 3.1 El Owner gobierna por intención

El Owner no debe actuar como scheduler manual de agentes.

No debería tener que decidir normalmente:

- qué agente trabaja ahora;
- qué rama debe crear;
- cuándo hacer un commit;
- cómo dividir internamente una tarea;
- qué documentación actualizar;
- qué revisor llamar;
- cuándo realizar un handoff;
- qué modelo concreto usar para un trabajo rutinario.

Sí deben seguir siendo materia del Owner las decisiones de producto, alcance, prioridades reales, dinero, publicación, riesgos materiales, cuestiones legales, privacidad relevante, monetización y decisiones difíciles de revertir cuando corresponda.

## 3.2 La organización es independiente de los agentes concretos

Un rol o una responsabilidad no debe depender de una instancia concreta de Claude, Codex, Gemini, Cursor u otro proveedor.

Los agentes son recursos temporales que ocupan roles.

La memoria, la autoridad, los contratos y el estado deben sobrevivir al agente que los ejecutó.

## 3.3 Productor y crítico deben poder ser independientes

Cuando una entrega requiera juicio independiente, quien produce no debe poder certificarse a sí mismo simplemente porque sea el mismo agente o modelo disponible.

## 3.4 Evidencia antes que afirmación

ADS debe distinguir entre:

- algo diseñado;
- algo implementado;
- algo ejecutado;
- algo probado;
- algo observado en condiciones reales;
- algo aprendido a partir de esa evidencia.

No debe declarar como comprobado lo que sólo existe como documentación o intención.

## 3.5 Fuente única de verdad

Una misma decisión o estado no debe mantenerse manualmente en varios lugares sin una razón explícita.

El sistema debe saber qué artefacto es autoridad para cada materia.

## 3.6 Persistencia y recuperación

Todo trabajo importante debe poder reanudarse después de:

- cerrar el chat;
- cambiar de agente;
- cambiar de modelo;
- cambiar de proveedor;
- reiniciar el equipo;
- interrumpir un proceso durante días;
- o sustituir por completo la herramienta agentic utilizada.

## 3.7 El sistema no debe crecer sin control

Más agentes, más roles, más skills y más documentación no son automáticamente una mejora.

ADS debe conservar mecanismos para retirar, fusionar, sustituir o degradar piezas que no demuestren valor.

---

# 4. Ampliación de la visión de ADS

ADS debe evolucionar hacia una plataforma con varias responsabilidades relacionadas pero separadas.

No se impone desde esta directiva una estructura final concreta. La arquitectura actual `KERNEL + PACK + PROFILE` puede mantenerse, ampliarse o refinarse si el análisis demuestra que se necesita otra capa.

Sin embargo, el diseño final debe ser capaz de representar al menos estas categorías de conocimiento:

## 4.1 Reglas universales de ADS

Lo que debe funcionar igual en prácticamente cualquier proyecto:

- autoridad;
- coordinación;
- memoria;
- handoffs;
- estado;
- procesos;
- evidencia;
- aprendizaje;
- concurrencia;
- recuperación;
- gobierno del Owner;
- etc.

## 4.2 Conocimiento por clase de proyecto

Por ejemplo:

- aplicaciones web;
- aplicaciones móviles;
- Wear OS;
- APIs;
- servicios backend;
- herramientas CLI;
- otros tipos futuros.

Este conocimiento puede corresponder a los PACKS actuales o a su evolución.

## 4.3 Conocimiento reutilizable propio de nuestra forma habitual de construir

Existe una clase de conocimiento que no necesariamente es universal para toda la industria, pero que puede ser válido para muchos de nuestros proyectos.

Ejemplos:

- stacks tecnológicos habituales;
- librerías preferentes cuando no existe una razón para usar otra;
- convenciones comunes;
- patrones de arquitectura recurrentes;
- sistemas de autenticación habituales;
- enfoque de diseño moderno de interfaces;
- componentes y patrones de UI;
- tablas, formularios, filtros, búsqueda, navegación, estados vacíos, carga y error;
- shadcn/ui o soluciones equivalentes cuando proceda;
- estrategias de testing;
- observabilidad;
- despliegues;
- documentación;
- tooling;
- integración agentic.

ADS debe estudiar si esta materia necesita una capa conceptual propia —por ejemplo blueprint, baseline, preset, distribución u otro concepto— en lugar de forzarla dentro del KERNEL, de un PACK genérico o del PROFILE de cada proyecto.

**El nombre y la implementación de esa posible capa no están decididos por esta directiva.**

## 4.4 Conocimiento específico de un proyecto

Cada proyecto debe poder tener:

- sus decisiones propias;
- sus excepciones;
- sus skills específicas;
- sus agentes o roles específicos cuando estén justificados;
- sus reglas de dominio;
- sus herramientas;
- sus entornos;
- sus restricciones;
- su arquitectura;
- su documentación;
- su perfil de validación;
- su memoria.

Lo específico de un proyecto no debe contaminar automáticamente ADS global.

---

# 5. Minería de proyectos reales para mejorar ADS

## 5.1 Esta operación es distinta de instalar ADS en un proyecto existente

Este punto es fundamental.

El Owner dispone de proyectos de software ya desarrollados o en desarrollo que contienen experiencia real acumulada.

Antes de cerrar el rediseño de la siguiente generación de ADS, deben estudiarse esos proyectos como **fuentes de conocimiento para mejorar `ads-kernel`**.

El flujo conceptual es:

```text
PROYECTOS REALES EXISTENTES
          ↓
ANÁLISIS Y EXTRACCIÓN
          ↓
CONOCIMIENTO CANDIDATO
          ↓
COMPARACIÓN CON ADS
          ↓
CLASIFICACIÓN / CRÍTICA / EVIDENCIA
          ↓
MEJORAS DEL KERNEL, PACKS, SKILLS, ADAPTADORES, MÉTODOS, ETC.
```

Esto NO es el proceso mediante el cual posteriormente esos proyectos adoptarán ADS.

Son dos operaciones distintas:

```text
MINERÍA:    proyecto real → conocimiento → ADS
ADOPCIÓN:   ADS → proyecto existente
```

Ambas deben existir, pero nunca confundirse.

## 5.2 Qué debe estudiarse

La minería no debe limitarse a buscar carpetas llamadas `skills` o `agents`.

Los agentes investigadores deben reconstruir **cómo funciona realmente cada proyecto y cómo se ha trabajado en él**.

Como mínimo deben buscar y analizar cuando exista:

- `AGENTS.md`;
- `CLAUDE.md`;
- reglas de Cursor;
- instrucciones para Codex u otros entornos;
- skills;
- subagentes;
- agentes especializados;
- prompts persistentes;
- scripts;
- hooks;
- GitHub Actions y otros workflows;
- convenciones Git;
- estrategia de ramas;
- uso de worktrees;
- PR y revisión;
- CI/CD;
- testing;
- auditorías;
- seguridad;
- documentación de arquitectura;
- ADR;
- journals;
- documentación de producto;
- sistemas de tareas;
- gestión de backlog;
- mecanismos de recuperación de contexto;
- formas de dividir trabajo entre agentes;
- mecanismos de verificación independientes;
- sistemas de revisión visual;
- diseño y UX;
- herramientas de navegador;
- manejo de bases de datos y migraciones;
- depuración;
- despliegues;
- observabilidad;
- gestión de errores;
- mecanismos anti-deriva;
- automatizaciones;
- integraciones externas;
- patrones repetidos aunque nunca hayan sido formalizados como «método» o «circuito».

## 5.3 Descubrimiento de sistemas implícitos

El análisis debe ser semántico, no únicamente documental.

Si en un proyecto existe repetidamente un patrón del tipo:

```text
implementación
→ revisión independiente
→ ejecución en navegador/dispositivo
→ comparación visual
→ corrección
→ nueva validación
→ registro
```

el sistema debe ser capaz de identificarlo como un posible método o circuito, aunque nunca exista un fichero que lo nombre de esa forma.

Debe buscar especialmente:

- trabajo repetido manualmente;
- instrucciones que aparecen varias veces;
- mecanismos creados para evitar errores recurrentes;
- revisiones que siempre se realizan de una determinada forma;
- herramientas creadas porque los agentes fallaban sin ellas;
- decisiones que se repiten entre proyectos;
- skills que han demostrado valor;
- skills que resultaron inútiles;
- patrones de coordinación entre agentes;
- mecanismos para reducir pérdida de contexto;
- soluciones que sean mejores que las equivalentes actuales de ADS.

## 5.4 Registro de candidatos con procedencia

Nada extraído debe incorporarse silenciosamente.

Cada candidato debe conservar procedencia suficiente para saber:

- de qué proyecto salió;
- dónde se encontró;
- qué problema resolvía;
- cómo funciona;
- qué evidencia de uso existe;
- cuántas veces se utilizó si puede determinarse;
- si funcionó o generó retrabajo;
- con qué parte de ADS se solapa;
- si contradice alguna regla existente;
- su aplicabilidad estimada;
- el destino candidato dentro de ADS;
- la decisión final: incorporar, fusionar, adaptar, investigar o descartar.

Una representación conceptual podría contener campos similares a:

```text
Candidato:       ...
Origen:          ...
Fuentes:         ...
Problema:        ...
Mecanismo:       ...
Evidencia:       ...
Aplicabilidad:   ...
Solapamiento:    ...
Contradicciones: ...
Destino posible: ...
Decisión:        ...
Motivo:          ...
```

La estructura definitiva debe decidirla ADS.

## 5.5 No obligar a que todo encaje en la arquitectura actual

Éste es otro requisito fundamental.

Los proyectos reales deben utilizarse también para cuestionar el modelo actual.

Si aparece una idea valiosa que no cabe correctamente en:

- una capacidad;
- un rol;
- una skill;
- un método;
- un PACK;
- un proceso;
- o cualquiera de las categorías actuales,

no debe deformarse para hacerla caber.

Debe considerarse la posibilidad de que revele una categoría, capa o contrato que ADS no haya previsto.

---

# 6. Circuito de adopción de ADS en un proyecto existente

Este circuito es posterior y distinto de la minería descrita anteriormente.

ADS debe poder incorporarse a un proyecto real que ya tenga meses o años de historia sin tratarlo como si estuviera vacío.

La adopción debe construir una representación fiable del proyecto antes de asumir su gobierno.

## 6.1 Fuentes que deben poder analizarse

Según disponibilidad:

- código actual;
- estructura del repositorio;
- documentación;
- historial Git;
- ramas;
- tags y releases;
- PR;
- issues;
- TODO;
- comentarios relevantes;
- CI/CD;
- tests;
- arquitectura existente;
- base de datos;
- migraciones;
- despliegue;
- errores conocidos;
- backlog externo;
- skills;
- agentes;
- prompts;
- reglas;
- workflows;
- herramientas;
- decisiones registradas;
- decisiones inferibles a partir de la implementación;
- convenciones de hecho;
- trabajos incompletos;
- funcionalidades abandonadas;
- deuda técnica;
- bugs conocidos;
- investigaciones pendientes.

## 6.2 Resultado esperado de la adopción

Antes de empezar a gobernar activamente el proyecto, ADS debe poder establecer un baseline que responda, con evidencia razonable:

- qué existe realmente;
- qué está terminado;
- qué está parcialmente implementado;
- qué está pendiente;
- qué está roto;
- qué está desplegado;
- qué decisiones gobiernan actualmente el proyecto;
- qué decisiones están implementadas pero nunca se documentaron;
- qué elementos se contradicen;
- qué trabajo pendiente existe;
- qué elementos son duplicados;
- qué riesgos y restricciones existen;
- qué partes del conocimiento local deben conservarse;
- qué especialización necesita ese proyecto.

## 6.3 Conversión del trabajo existente al modelo ADS

El sistema no debe convertir mecánicamente cada issue, TODO o nota en un item ADS.

Debe pasar el contenido por el equivalente del circuito de entrada y anclaje para determinar qué representa realmente.

Un elemento antiguo puede ser:

- una observación;
- una decisión;
- una idea inmadura;
- un duplicado;
- algo ya resuelto;
- un defecto;
- una capacidad nueva;
- una expectativa incumplida;
- una investigación;
- deuda técnica;
- una dependencia;
- un cambio de dirección;
- un incidente;
- algo que debe descartarse.

La adopción debe preservar procedencia y trazabilidad.

## 6.4 Creación del PROFILE y especialización del proyecto

ADS debe tener un circuito, metodología y criterios explícitos para construir los artefactos específicos de un proyecto.

No debe limitarse a rellenar manualmente una plantilla.

El sistema debe estudiar lo que existe y, con intervención del Owner sólo donde sea necesaria, derivar o proponer:

- PROFILE;
- decisiones fuertes;
- decisiones provisionales;
- riesgos centrales;
- entorno real de validación;
- restricciones;
- arquitectura conocida;
- stack;
- capacidades activables;
- skills específicas;
- agentes o roles específicos si aportan valor;
- herramientas;
- reglas del proyecto;
- convenciones;
- documentación;
- mecanismos de testing;
- mecanismos de despliegue;
- integraciones;
- criterios de calidad;
- cualquier otra especialización necesaria.

Las piezas específicas deben crearse siguiendo contratos ADS, no mediante prompts improvisados que queden fuera del sistema.

## 6.5 El proyecto puede traer una base sólida propia

Si el proyecto ya contiene una buena solución, ADS no debe sustituirla por una versión inferior sólo por homogeneizar.

Debe poder:

- reconocerla;
- evaluarla;
- conservarla;
- envolverla en contratos ADS;
- documentarla;
- adaptarla cuando sea necesario;
- y registrar las diferencias frente a los defaults de ADS.

---

# 7. Proyecto nuevo: instalación y especialización

En un proyecto nuevo ADS debe poder crear una base coherente desde el principio.

La instalación no debería significar únicamente «copiar unos `.md`».

Debe establecer de forma reproducible todo lo necesario para que la organización pueda empezar a trabajar y continuar trabajando.

Según el diseño definitivo, esto puede incluir:

- identidad y versión ADS instalada;
- kernel;
- packs;
- posible blueprint/base reutilizable;
- PROFILE inicial;
- estructura persistente de estado;
- documentación;
- memoria;
- agentes/roles;
- skills;
- herramientas;
- adaptadores para el entorno agentic;
- Git;
- CI mínima;
- validadores;
- hooks;
- convenciones;
- entorno de trabajo concurrente;
- integración con runtime;
- comandos o interfaz para el Owner.

Debe existir una definición verificable de **«ADS está instalado correctamente»**.

---

# 8. Git y versionado del PROYECTO REAL

Este apartado se refiere al repositorio del producto donde ADS trabaja, **no al repositorio `ads-kernel`**.

ADS debe gobernar Git como parte de la operación normal de la organización.

El Owner no debería tener que administrar manualmente el repositorio para que los agentes puedan trabajar.

## 8.1 Materias que deben quedar gobernadas

El diseño debe definir claramente responsabilidades, autoridad, métodos, gates y evidencia para:

- estrategia de ramas;
- creación y retirada de ramas;
- worktrees u otros mecanismos de aislamiento;
- trabajo concurrente de múltiples agentes;
- relación entre paquete ADS y espacio de trabajo Git;
- commits;
- mensajes de commit;
- granularidad de commits;
- trazabilidad entre item/paquete/decisión y commit;
- push;
- PR;
- revisión;
- checks obligatorios;
- integración;
- orden de integración;
- merges;
- rebases cuando sean apropiados;
- resolución de conflictos;
- prevención de sobrescrituras entre agentes;
- recuperación de trabajo parcial;
- cherry-picks cuando procedan;
- hotfixes;
- tags;
- releases del producto;
- rollback;
- ramas abandonadas;
- limpieza;
- protección de `main` u otras ramas relevantes;
- correspondencia entre versión desplegada y commit real.

## 8.2 Propiedad clara

La solución no debe repartir estas responsabilidades de forma ambigua entre PLT, ENT, DSP, CON u otras capacidades.

Puede existir un contrato transversal o una distribución explícita de responsabilidades, pero debe haber una respuesta inequívoca para cada operación Git:

- quién la solicita;
- quién la ejecuta;
- quién puede bloquearla;
- quién verifica el resultado;
- qué evidencia queda;
- qué ocurre si falla.

## 8.3 Git debe ser parte de la memoria operativa

ADS debería poder responder preguntas como:

- ¿qué cambios de código ejecutaron este item?;
- ¿qué paquetes todavía tienen ramas no integradas?;
- ¿qué versión contiene esta decisión?;
- ¿quién revisó este cambio?;
- ¿qué release introdujo este comportamiento?;
- ¿qué commit está desplegado ahora?;
- ¿qué trabajo quedó abandonado sin integrar?;

sin reconstruirlo manualmente desde un chat.

---

# 9. Entornos agentic y neutralidad de proveedor

ADS debe ser utilizable con:

- Claude Code;
- OpenAI Codex;
- Cursor Agents;
- Gemini y sus herramientas agentic;
- y proveedores futuros.

## 9.1 Núcleo neutral

Las responsabilidades, contratos, procesos y memoria de ADS no deben estar definidos en términos de un proveedor concreto salvo cuando una capacidad sea explícitamente específica de dicho proveedor.

## 9.2 Adaptadores

La neutralidad conceptual debe convertirse en neutralidad práctica.

Debe estudiarse una arquitectura de adaptadores que traduzca la organización ADS a las capacidades reales de cada entorno.

Por ejemplo, cuando proceda:

```text
ADS role / skill / tool / memory / permission
                  ↓
            adapter layer
       ┌──────────┼───────────┐
       ↓          ↓           ↓
 Claude Code    Codex       Cursor ...
```

Cada adaptador puede conocer:

- formato de agentes;
- formato de skills;
- instrucciones persistentes;
- herramientas disponibles;
- aislamiento;
- subagentes;
- límites de contexto;
- permisos;
- ejecución de comandos;
- mecanismos de continuación;
- diferencias de capacidades.

Las capacidades especiales de un proveedor pueden aprovecharse sin convertirlas en requisitos universales del kernel.

## 9.3 Degradación explícita

Si una función ADS requiere una capacidad que un entorno no tiene, debe quedar claro:

- si puede degradarse;
- cómo se degrada;
- qué garantías se pierden;
- o si esa configuración no puede ejecutar correctamente ese rol/proceso.

---

# 10. Skills, agentes y especialización reutilizable

ADS debe evolucionar de un catálogo principalmente abstracto de roles y métodos hacia una plataforma que pueda incorporar conocimiento operativo más concreto cuando demuestre valor.

## 10.1 Skills

Debe existir una forma clara de distinguir entre:

- skill universal;
- skill por tipo de proyecto;
- skill por stack;
- skill por proveedor agentic;
- skill específica de un proyecto.

Las skills deben tener:

- propósito;
- propietario;
- condiciones de uso;
- entradas;
- salidas;
- herramientas necesarias;
- evidencia esperada;
- compatibilidad;
- versión o mecanismo equivalente cuando sea necesario;
- aprendizaje de uso;
- criterios de retirada.

## 10.2 Agentes especializados

No todo conocimiento concreto necesita crear un agente permanente.

ADS debe decidir cuándo una responsabilidad justifica:

- una nueva capacidad;
- un rol;
- una skill;
- una extensión de método;
- una herramienta;
- un gate;
- un agente temporal;
- o simplemente documentación de conocimiento.

## 10.3 Aprovechar experiencia existente

La minería de proyectos debe utilizarse para descubrir skills, agentes y mecanismos ya probados y decidir dónde pertenecen.

No se debe reconstruir desde cero lo que ya se ha demostrado útil en un proyecto real sin una razón.

---

# 11. Base tecnológica y patrones comunes

ADS debe investigar cuánto conocimiento tecnológico reutilizable conviene incorporar.

El objetivo no es congelar todos los proyectos en el mismo stack.

El objetivo es evitar que cada proyecto vuelva a descubrir desde cero soluciones que ya conocemos bien.

## 11.1 Ejemplo: web apps modernas

En muchos proyectos web puede ser razonable partir de una base moderna de:

- sistema de componentes;
- tokens;
- layout;
- responsive;
- accesibilidad;
- tablas;
- formularios;
- filtros;
- búsqueda;
- navegación;
- estados de carga/error/vacío;
- feedback;
- overlays;
- modales/drawers;
- dashboards;
- diseño de densidad;
- comportamiento móvil;
- testing visual;
- etc.

Cuando tecnologías como shadcn/ui, Tailwind, Radix u otras sean una elección habitual, ADS debe poder contener conocimiento experto para utilizarlas correctamente sin elevarlas necesariamente a ley universal.

## 11.2 Defaults con salida explícita

La existencia de una base preferente no debe impedir elegir otra tecnología cuando el proyecto lo necesite.

Debe existir una diferencia clara entre:

- default probado;
- decisión fuerte;
- restricción;
- recomendación;
- excepción del proyecto.

---

# 12. Aprendizaje: proyecto → ADS

ADS debe convertir experiencia real en conocimiento reutilizable.

El flujo actual de aprendizaje debe ampliarse y materializarse de forma clara:

```text
experiencia de proyecto
       ↓
evidencia
       ↓
aprendizaje local
       ↓
candidato reutilizable
       ↓
APR / crítica / clasificación
       ↓
SIS
       ↓
mejora de ADS
```

No todo aprendizaje debe subir a ADS.

Debe poder terminar en:

- PROJECT;
- PROFILE;
- skill local;
- blueprint/base común;
- PACK;
- KERNEL;
- adaptador;
- tooling;
- o descartarse.

---

# 13. Documentación estructurada del conocimiento de ADS

El conocimiento acumulado sobre ADS no debe quedar distribuido únicamente entre commits y changelogs.

El sistema debe distinguir al menos conceptualmente entre:

- qué cambió;
- por qué cambió;
- qué se aprendió;
- qué evidencia existe;
- qué se intentó y falló;
- qué está vigente;
- qué fue superado;
- qué proyectos originaron una mejora;
- qué reglas dependen de determinada evidencia.

Debe existir una documentación consultable que permita a futuros agentes responder preguntas del tipo:

- ¿qué hemos aprendido sobre diseño visual con agentes?;
- ¿qué mecanismos de revisión han reducido retrabajo?;
- ¿qué skills se probaron y fueron retiradas?;
- ¿por qué ADS usa actualmente este circuito?;
- ¿qué proyectos demostraron que esta regla era necesaria?;

sin tener que reconstruir la respuesta leyendo todo el historial Git.

---

# 14. ADS → proyectos: actualización y migración

El aprendizaje no puede ser únicamente upstream.

Cuando ADS mejore, los proyectos ya instalados deben poder recibir esas mejoras de forma controlada.

Debe existir un mecanismo equivalente conceptualmente a:

```text
proyecto usa ADS X
        ↓
existe ADS Y
        ↓
comparación
        ↓
compatibilidad + impacto
        ↓
plan de migración
        ↓
aplicación
        ↓
validación
        ↓
proyecto usa ADS Y
```

## 14.1 Una actualización no es copiar archivos encima

Debe considerar:

- versión instalada;
- cambios de contratos;
- cambios de esquemas;
- cambios de packs;
- cambios de skills;
- adaptadores;
- tooling;
- runtime;
- overrides del proyecto;
- personalizaciones locales;
- incompatibilidades;
- migraciones de estado;
- artefactos obsoletos;
- rollback de la actualización.

## 14.2 Debe existir una vista comprensible del cambio

Antes de aplicar una actualización relevante debería poder conocerse, por ejemplo:

```text
Versión instalada: ...
Versión candidata:  ...

Añade:       ...
Cambia:      ...
Retira:      ...
Migra:       ...
Conflictos:  ...
Overrides afectados: ...
Riesgo:      ...
Plan:        ...
```

La estructura definitiva queda por diseñar.

---

# 15. ADS instalable como sistema

ADS debe poder instalarse de forma reproducible y comprensible.

La experiencia final debería acercarse conceptualmente a una operación sencilla —CLI, instalador, skill principal u otra interfaz que se determine— que sea capaz de preparar el sistema completo.

No se impone el comando exacto, pero la experiencia ideal sería equivalente a:

```text
ads install
ads adopt
ads update
ads status
```

u otra interfaz igual de clara.

## 15.1 Instalación por entorno agentic

La instalación debe poder preparar lo necesario para los entornos soportados.

Por ejemplo:

- instrucciones para Claude Code;
- skills/subagentes disponibles para Claude;
- configuración equivalente para Codex;
- reglas/agentes para Cursor;
- configuración equivalente para Gemini;
- configuración genérica cuando el proveedor no tenga capacidades específicas.

## 15.2 La instalación debe ser verificable

No basta con que existan archivos.

Debe comprobarse que:

- el kernel está íntegro;
- las dependencias necesarias existen;
- los adaptadores son válidos;
- la estructura de estado es legible/escribible;
- Git está en una situación válida;
- los validadores funcionan;
- las fuentes únicas son resolubles;
- el agente principal puede iniciar el sistema;
- el sistema puede persistir y recuperar un checkpoint mínimo.

---

# 16. Runtime real

La siguiente evolución debe avanzar desde contratos ejecutados manualmente por agentes hacia un runtime que materialice realmente la organización cuando sea razonable.

El runtime debe estudiarse como producto del propio ADS, no como un script auxiliar aislado.

Como mínimo debe resolver o coordinar:

- persistencia del estado;
- items;
- rutas;
- paquetes;
- colas;
- equipos materializados;
- asignación de roles;
- selección de agentes/modelos;
- checkpoints;
- handoffs;
- devoluciones;
- bloqueos;
- dependencias;
- autoridad;
- gates;
- ejecución concurrente;
- aislamiento;
- reanudación;
- eventos;
- recuperación tras fallo;
- comandos del Owner;
- vistas ejecutivas;
- auditoría;
- integración con Git;
- integración con adaptadores agentic.

## 16.1 El runtime no debe convertirse en otra fuente de verdad desconectada

Los contratos declarativos y el runtime deben estar vinculados.

Siempre que sea viable, el runtime debe ejecutar o validar contratos existentes en lugar de duplicar su semántica en código independiente.

---

# 17. Creación y evolución de PROFILE, skills y especialización mediante ADS

El propio proceso por el que un proyecto obtiene su PROFILE y su organización específica debe formar parte de ADS.

No debería depender de que un humano recuerde un prompt especial.

Debe existir un proceso/circuito formal para:

1. recopilar evidencia del proyecto;
2. conversar con el Owner sólo sobre lo no inferible o reservado;
3. distinguir hechos, decisiones y suposiciones;
4. identificar riesgos;
5. determinar qué hereda del sistema común;
6. detectar qué falta;
7. proponer especialización;
8. crear skills/roles/métodos/herramientas locales necesarios;
9. verificar que no duplican innecesariamente ADS;
10. establecer su procedencia y autoridad;
11. validar que el proyecto queda gobernable;
12. mantener esas piezas a lo largo del tiempo.

El mismo sistema debe poder revisar posteriormente esa especialización y retirar piezas innecesarias.

---

# 18. ADS debe poder utilizar ADS para evolucionarse

Éste es un objetivo central.

Los cambios importantes del sistema no deberían hacerse mediante una conversación aislada seguida de modificaciones manuales sin estructura.

La evolución de ADS debe pasar por ADS.

Conceptualmente:

```text
Owner expresa una necesidad sobre ADS
            ↓
ENC
            ↓
item SIS / proceso correspondiente
            ↓
ruta y equipos
            ↓
investigación / arquitectura / construcción / verificación
            ↓
evidencia
            ↓
actualización del sistema
            ↓
nueva versión
```

SIS debe seguir siendo la propietaria de la fábrica, pero debe activar otras capacidades cuando el trabajo lo requiera.

Ejemplos:

- INV para investigar otras soluciones;
- ARQ para cambios estructurales;
- PLT para runtime/tooling;
- CON para implementación;
- SEG para límites de seguridad;
- VER para evidencia independiente;
- ENT cuando cambie un runtime operativo;
- APR para consolidar aprendizajes.

La evolución del propio sistema debe dejar:

- decisión;
- procedencia;
- impacto;
- implementación;
- pruebas;
- resultado;
- aprendizaje.

---

# 19. No depender de un chat

Toda la arquitectura debe diseñarse suponiendo que cualquier conversación puede desaparecer.

Un chat puede ser una interfaz temporal, nunca la base de datos del proyecto.

Debe poder cambiarse de:

- conversación;
- ventana;
- herramienta;
- modelo;
- proveedor;

sin perder el estado esencial.

Cualquier conversación que produzca una decisión, interpretación, bloqueo, nueva tarea o aprendizaje relevante debe terminar materializándolo en el sistema antes de depender de ello.

---

# 20. Estado ejecutivo para el Owner

ADS debe poder ofrecer al Owner una vista comprensible del proyecto sin obligarle a leer la estructura interna.

Preguntas naturales como:

- ¿cómo va el proyecto?;
- ¿qué está bloqueado?;
- ¿qué necesitas de mí?;
- ¿qué se está construyendo?;
- ¿qué cambió desde ayer?;
- ¿qué cosas están esperando validación?;
- ¿qué riesgos han aparecido?;
- ¿qué decisiones mías están pendientes?;
- ¿qué agentes están trabajando y en qué?;
- ¿qué fue rechazado y por qué?;
- ¿qué aprendimos recientemente?;

 deben poder responderse a partir del estado persistente, no de la memoria informal de un agente.

---

# 21. Criterios de realidad

Una característica ADS no se considera realmente construida sólo porque exista su documento.

Para cada parte debe distinguirse, cuando corresponda:

```text
CONTRATO DEFINIDO
        ↓
IMPLEMENTACIÓN EXISTENTE
        ↓
PRUEBA EJECUTABLE
        ↓
PRUEBA SUPERADA
        ↓
USO EN PROYECTO REAL
        ↓
EVIDENCIA DE FUNCIONAMIENTO
```

El repositorio debe seguir evitando confundir especificación con funcionamiento real.

La siguiente gran etapa debe buscar deliberadamente llevar partes fundamentales hasta proyectos reales.

---

# 22. Compatibilidad, migración y evolución

No debe asumirse que la siguiente versión puede romper la actual libremente.

Antes de sustituir contratos o conceptos debe conocerse:

- qué reemplaza;
- por qué;
- qué artefactos dependen de ello;
- cómo se migran;
- qué queda legado;
- durante cuánto tiempo convive;
- cómo se comprueba la migración.

Cuando una pieza actual resulte equivocada, debe poder retirarse. La compatibilidad no debe convertirse en una obligación de conservar indefinidamente malas decisiones.

---

# 23. Trabajo inicial requerido antes de cerrar la nueva arquitectura

Esta directiva **no autoriza a saltar directamente a implementar una colección de features**.

Antes de cerrar el diseño de la siguiente versión, ADS debe realizar al menos los siguientes trabajos como parte de su propio proceso:

## 23.1 Baseline del ADS actual

Reconstruir fielmente:

- qué existe;
- qué funciona;
- qué es sólo contrato;
- qué es manual;
- qué está pendiente;
- qué conceptos son transitorios;
- qué contradicciones o deudas conocidas existen.

## 23.2 Mapa de esta directiva contra ADS actual

Para cada requisito:

- ya cubierto;
- parcialmente cubierto;
- ausente;
- contradicho;
- necesita evidencia;
- requiere decisión normativa del Owner.

## 23.3 Minería de proyectos reales seleccionados

Estudiar los repositorios que el Owner ponga a disposición siguiendo el circuito de extracción definido en esta directiva.

El resultado debe ser un inventario trazable de candidatos, no una modificación caótica del kernel.

## 23.4 Síntesis

Comparar:

```text
ADS actual
+
visión del Owner
+
experiencia extraída de proyectos reales
+
evidencia disponible
```

antes de proponer la arquitectura objetivo.

## 23.5 Diseño integrado

La propuesta debe explicar cómo encajan entre sí:

- organización;
- kernel;
- packs;
- posible capa de base/blueprint;
- profile;
- skills;
- agentes;
- adapters;
- runtime;
- Git;
- instalación;
- adopción;
- actualización;
- aprendizaje;
- documentación;
- persistencia;
- pruebas.

No se aceptará una colección de subsistemas independientes unidos sólo por documentación.

---

# 24. Reglas para interpretar esta directiva

1. **No convertir cada párrafo en una feature independiente.** Buscar primero el modelo coherente que las explique conjuntamente.
2. **No preservar una estructura actual únicamente porque ya existe.** Preservarla cuando siga siendo correcta.
3. **No cerrar prematuramente tecnologías o formatos.** Justificarlos mediante requisitos y evidencia.
4. **No copiar indiscriminadamente soluciones de proyectos fuente.** Extraer, comparar, criticar y clasificar.
5. **No confundir minería con adopción.** Son circuitos distintos.
6. **No confundir Git del proyecto con versionado de `ads-kernel`.** Esta directiva exige gobierno Git sobre ambos ámbitos cuando corresponda, pero son materias distintas.
7. **No crear agentes permanentes si una skill, método o herramienta resuelve mejor el problema.**
8. **No volver específico el KERNEL para resolver una preferencia nuestra.** Estudiar dónde debe vivir cada conocimiento.
9. **No hacer que una mejora dependa exclusivamente de Claude Code, Codex o cualquier proveedor.** Lo específico debe vivir en adaptadores o extensiones apropiadas.
10. **No depender del chat actual.** Todo resultado importante debe materializarse y enlazarse.
11. **No declarar funcionamiento sin ejecución.** Mantener estados de evidencia reales.
12. **No modificar secciones normativas aprobadas silenciosamente.** Si la evolución las contradice, seguir el proceso de autoridad correspondiente.

---

# 25. Cómo debería sentirse ADS cuando esta evolución esté madura

El objetivo práctico puede resumirse con varios escenarios.

## Proyecto nuevo

El Owner crea o selecciona un repositorio, indica qué quiere construir y ADS:

- se instala;
- identifica el tipo de proyecto;
- conversa sólo sobre lo necesario;
- construye su PROFILE;
- selecciona conocimiento y packs apropiados;
- crea especialización cuando es necesaria;
- prepara agentes/skills/herramientas;
- configura el gobierno Git;
- deja CI y memoria mínimas;
- genera trabajo inicial;
- y empieza a operar de manera recuperable.

## Proyecto existente

ADS analiza el proyecto, reconstruye su realidad, conserva las buenas decisiones, identifica trabajo y contradicciones, crea su representación ADS y asume progresivamente su gobierno sin fingir que el proyecto empieza desde cero.

## Trabajo cotidiano

El Owner puede decir:

> «Quiero cambiar cómo funciona X.»

ADS decide qué proceso representa, qué capacidades intervienen, qué agentes necesita, cómo aislar su trabajo, cómo verificarlo y cómo integrarlo.

El Owner interviene cuando corresponde a su autoridad.

## Cambio de proveedor

El proyecto puede pasar de Claude Code a Codex, Cursor u otro sistema sin perder la organización, el estado ni la memoria. Se sustituye o añade el adaptador y se conservan las responsabilidades ADS.

## Mejora aprendida

Un proyecto descubre una forma mejor de trabajar. ADS conserva la evidencia, la evalúa, la promueve si procede y una nueva versión puede llevar ese aprendizaje a futuros proyectos y, mediante migración, a proyectos ya existentes.

## Evolución del propio ADS

El Owner dice:

> «Quiero que ADS haga mejor X.»

ADS convierte esa intención en trabajo SIS, investiga, diseña, implementa, verifica, documenta y publica una nueva versión utilizando el mismo sistema que gobierna los proyectos.

---

# 26. Resultado último buscado

ADS debe convertirse en una **organización de desarrollo portable y acumulativa**.

Portable porque puede operar con distintos proyectos, stacks, proveedores y agentes.

Acumulativa porque cada proyecto puede aportar experiencia que mejore la base común.

Persistente porque el trabajo sobrevive a chats y agentes.

Gobernable porque el Owner conserva las decisiones que realmente le pertenecen sin tener que gestionar la maquinaria interna.

Verificable porque distingue lo documentado de lo probado.

Instalable porque puede desplegar su organización sobre un proyecto real de forma reproducible.

Evolutiva porque puede actualizar proyectos existentes y puede modificarse a sí misma mediante sus propios procesos.

La meta no es crear más documentación alrededor de agentes.

La meta es que exista una **fábrica de software gobernada por el Owner, operada por agentes y capaz de aprender de todo lo que construye**.

