# Prompt de arranque — Evolución ADS NEXT

Usa este prompt desde la raíz del repositorio `ads-kernel`, proporcionando acceso de lectura a los proyectos reales que el Owner indique cuando llegue la fase de minería.

---

Lee íntegramente `ADS-NEXT-OWNER-BRIEF.md` —o la ruta donde se haya incorporado dentro del repositorio— y trata su contenido como una **directiva del Owner**, no como una especificación técnica cerrada ni como una lista de features para implementar literalmente.

Tu misión es evolucionar ADS hacia esa visión utilizando, en la medida que el propio estado actual lo permita, **ADS para trabajar sobre ADS**. El propietario global de esta evolución es SIS; activa ENC, INV, ARQ, PLT, CON, VER, ENT, APR y cualquier otra capacidad cuando sus contratos lo requieran. No concentres artificialmente todo el trabajo en un único agente o rol si el sistema exige separación de autoridad o crítica independiente.

No empieces construyendo features aisladas. Primero crea una representación persistente y trazable de:

1. el estado real de ADS en `main`: qué existe, qué funciona, qué se ejecuta todavía de forma manual, qué es sólo contrato y qué está pendiente;
2. el mapa completo entre la directiva del Owner y ADS actual: cubierto, parcial, ausente, contradictorio o pendiente de evidencia/decisión;
3. las decisiones normativas o arquitectónicas que no pueden modificarse silenciosamente;
4. el plan de investigación necesario antes de cerrar una arquitectura objetivo.

Después ejecuta una **fase explícita de minería de proyectos reales existentes para mejorar ADS**. Esta fase NO es la adopción de ADS en esos proyectos. Los proyectos son fuentes de conocimiento para `ads-kernel`.

Para cada proyecto que el Owner ponga a disposición, analiza no sólo archivos llamados `skills` o `agents`, sino la forma real de trabajo: AGENTS/CLAUDE/Cursor/Codex instructions, skills, agentes, prompts, scripts, hooks, CI/CD, Git, ramas/worktrees, PR, testing, auditorías, arquitectura, documentación, ADR, recuperación de contexto, workflows, revisión visual, diseño, bases de datos, migraciones, despliegue, observabilidad, automatizaciones y patrones repetidos aunque nunca hayan sido formalizados.

Detecta también **sistemas implícitos**: patrones de trabajo recurrentes que puedan convertirse en métodos, circuitos, gates, skills, herramientas, roles, capacidades o nuevas categorías de ADS.

No copies nada directamente al kernel. Registra cada candidato con procedencia, problema que resuelve, mecanismo, evidencia de uso, aplicabilidad, solapamiento con ADS, contradicciones y destino candidato. Clasifica cada hallazgo como candidato a kernel universal, pack, posible capa reutilizable/blueprint, skill, tooling, adaptador de proveedor, conocimiento de proyecto o descarte. Si algo valioso no encaja correctamente en la arquitectura actual, considera que puede revelar una categoría que ADS todavía no tiene; no lo deformes para hacerlo caber.

Sólo después de tener:

- baseline del ADS actual;
- mapa de la directiva;
- minería de los proyectos fuente disponibles;
- inventario de candidatos y evidencia;

realiza la síntesis y diseña una **arquitectura integrada** para la siguiente evolución.

Esa arquitectura debe resolver conjuntamente, y no como subsistemas inconexos:

- organización y autoridad ADS;
- KERNEL, PACKS y PROFILE y si necesitan una nueva capa intermedia reutilizable;
- creación y mantenimiento de especialización específica por proyecto;
- skills, agentes, métodos, gates y herramientas;
- gobierno Git del PROYECTO REAL: ramas, worktrees/aislamiento, commits, PR, revisión, integración, conflictos, releases, hotfixes, rollback y trazabilidad item/paquete ↔ código;
- instalación de ADS como sistema reproducible;
- adopción profunda de proyectos existentes, distinta de la minería;
- construcción automática/asistida del PROFILE y organización específica a partir de la realidad del proyecto;
- runtime, dispatcher, estado, colas, checkpoints, handoffs, reanudación, concurrencia y recuperación;
- neutralidad real respecto a Claude Code, Codex, Cursor, Gemini y proveedores futuros mediante adaptadores apropiados;
- conocimiento tecnológico reutilizable y defaults de nuestros proyectos sin contaminar el kernel universal;
- aprendizaje proyecto → ADS;
- documentación estructurada de lo aprendido;
- actualización ADS → proyectos instalados con compatibilidad, migración y rollback;
- capacidad de ADS para evolucionarse utilizando ADS;
- independencia respecto a cualquier chat o sesión.

No asumas que la estructura actual es necesariamente la correcta. Tampoco la sustituyas sin evidencia. Reutiliza todo lo que siga siendo válido y diseña migraciones explícitas para lo que deba cambiar.

Toda decisión importante, hallazgo, candidato extraído, mapa de impacto, plan, checkpoint y evidencia debe persistirse dentro del repositorio o en los artefactos ADS correspondientes. **La conversación actual no puede ser una fuente de verdad.**

Mantén siempre la distinción entre:

- contrato definido;
- implementación existente;
- prueba ejecutable;
- prueba realmente ejecutada;
- prueba superada;
- funcionamiento demostrado en proyecto real.

No declares como construido lo que sólo haya sido documentado.

Usa crítica independiente cuando corresponda y evita que quien propone la nueva arquitectura sea el único que certifique su suficiencia.

A partir del diseño aprobado por los mecanismos de autoridad existentes, descompón la transformación en items/procesos ADS trazables y ejecuta la evolución de forma incremental, manteniendo el repositorio en estados coherentes y verificables.

No pidas al Owner decisiones técnicas rutinarias. Escala únicamente las materias que realmente pertenezcan a su autoridad o las contradicciones normativas que el sistema no pueda resolver por sí solo.

El resultado no debe ser «más documentación sobre ADS», sino una progresión demostrable desde el sistema actual hacia una plataforma ADS instalable, portable, acumulativa, multiagente, recuperable y utilizable en proyectos reales.
