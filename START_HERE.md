# START HERE — Arrancar un proyecto con ADS

Instrucciones completas para iniciar **cualquier** proyecto con esta organización. Sirven igual para una app móvil, una web app, una API o una herramienta de línea de comandos.

Si sólo lees un documento de todo el repositorio, que sea éste.

---

## Antes de empezar: qué necesitas tener

| Requisito | Por qué |
|---|---|
| Git instalado y una cuenta de repositorio remoto | El repositorio existe desde el primer día (G48) |
| Un entorno agentic (Cursor, Claude Code, Codex o equivalente) | Es la interfaz de trabajo |
| Saber responder a 4 preguntas (abajo) | Sin ellas el sistema optimiza a ciegas |
| **Nada más** | No necesitas estructura, ni stack elegido, ni diseño, ni documentación previa |

Las cuatro preguntas. No hace falta que las escribas bien; basta con que sepas responderlas cuando el sistema te las haga:

1. **¿Qué ganas tú con este proyecto?** Ordenado por prioridad, con criterio de fallo. *(Es lo que evita que el sistema optimice hacia "más completo".)*
2. **¿Dónde se prueba de verdad?** Cuál es el entorno real donde un experimento dice la verdad y no el entorno de desarrollo.
3. **¿Quién valida, cuándo y bajo qué condiciones?** Si eres tú y sólo puedes hacerlo dos veces por semana, eso cambia toda la planificación.
4. **¿Qué 2-4 supuestos, si son falsos, tiran el proyecto abajo?**
5. **¿Cuáles son las 1-3 áreas por las que este producto merece existir?** Son tus áreas premium (G53): ahí se invierte más y se acepta más coste. Fuera de ellas, lo suficientemente bueno y barato.

---

## Ruta A — Proyecto nuevo desde cero *(la normal)*

### Paso 1 — Crear el esqueleto

```bash
./tooling/new-project.sh mi-proyecto pack-web-app
```

Packs disponibles: `pack-web-app`, `pack-mobile-native`, `pack-design-led` (este último se combina con uno de plataforma, no lo sustituye). Puedes indicar varios separados por coma, o ninguno si tu proyecto no encaja en ninguna clase existente.

Esto te deja:

```text
../mi-proyecto/
├── PROJECT.md          plantilla del binder
├── PROFILE.md          plantilla a rellenar
├── BOOTSTRAP_PROMPT.md el texto exacto que le darás al agente
├── kernel/             copia congelada, NO se edita
├── packs/              copias congeladas, NO se editan
├── docs/               JOURNAL.md y UPSTREAM.md vacíos
└── tooling/
```

### Paso 2 — Repositorio remoto

```bash
cd ../mi-proyecto
git add . && git commit -m "chore: semilla ADS (kernel 1.1.0)"
git remote add origin <tu-repo>
git push -u origin main
```

Hazlo **ahora**, no cuando haya código. El sistema necesita poder hacer push desde la primera sesión (G29).

### Paso 3 — El PROFILE

Tienes dos opciones, ambas válidas:

**Opción A — lo rellenas tú.** Abre `PROFILE.md` y responde. Tardas entre 30 y 90 minutos.

**Opción B — lo rellena el sistema contigo (recomendada).** Abre el proyecto en tu entorno agentic y di:

> Lee `kernel/PROFILE_TEMPLATE.md` y `kernel/KERNEL.md` §K0. Vamos a rellenar el PROFILE de este proyecto por conversación. Pregúntame lo que necesites, de una en una, empezando por la definición de éxito. Cuando tengas suficiente, escribe `PROFILE.md` y me lo enseñas para que lo apruebe. No empieces el Circuito 0 todavía.

Lo que **no** es aceptable es saltarse este paso. Arrancar con el contrato K0 incompleto significa descubrir a mitad de Circuito 1 que nadie sabía qué se estaba optimizando.

### Paso 4 — Aprobar el PROFILE

Léelo entero una vez. Comprueba específicamente:

- [ ] La **definición de éxito** es la tuya, no una interpretación razonable de tu interlocutor.
- [ ] Los **riesgos centrales** son de verdad los que te preocupan.
- [ ] El **timebox del Circuito 0** encaja con tu ritmo real de trabajo, no con un ideal.
- [ ] Las **decisiones fuertes** son cosas que realmente no quieres discutir.
- [ ] Lo que está en **ABIERTO** es de verdad algo que la implementación no va a forzar.

### Paso 5 — Escribir PROJECT.md

Rellena la tabla de composición: qué versión de kernel, qué packs, qué overrides declarados (normalmente ninguno).

### Paso 6 — Lanzar el Circuito 0

Pega en tu agente principal el contenido de `BOOTSTRAP_PROMPT.md`. Literalmente eso, sin añadir instrucciones tuyas: si hicieran falta, el fallo estaría en la semilla.

### Paso 7 — Qué esperar

El Circuito 0 termina cuando existen los 10 entregables de G22, dentro del timebox. Durante ese tiempo el sistema **no** debe escribir código de producto ni elegir stack definitivo.

Al terminar, tendrás:

```text
AGENTS.md              compilado, <400 líneas — a partir de aquí es lo que se lee cada sesión
docs/README.md         mapa de documentación
docs/decisions/        primeros ADR
docs/JOURNAL.md        con entradas reales
docs/agentic/          agentes, skills, METRICS.md, ORG_LEARNINGS.md
docs/PROJECT_LEARNINGS.md   ledger de producto, con su techo declarado
CI en verde            aunque sólo ejecute un test trivial
lista de spikes        priorizada, con hipótesis y criterio de éxito
```

**Señal de alarma:** si el Circuito 0 lleva más tiempo del previsto y lo que ha producido es más documentación sobre sí mismo, párale. Es el fallo más probable de todo el sistema y G22 existe para prevenirlo.

### Paso 8 — Circuito 1: primero medir

Lo primero que se construye **no** es el producto: es el experimento mínimo que responde a varios spikes a la vez. Un documento de arquitectura bien argumentado sobre supuestos no medidos es deuda, no progreso.

---

## Ruta B — Proyecto ya empezado

Si ya tienes código y quieres adoptar esta organización:

```bash
cd tu-proyecto-existente
cp -r /ruta/a/ads/kernel .
cp /ruta/a/ads/packs/pack-<clase>.md packs/
cp kernel/PROFILE_TEMPLATE.md PROFILE.md
```

Y luego, en tu agente:

> Este proyecto ya existe. Lee el código, la documentación y el historial de commits, y rellena `PROFILE.md` con lo que **ya está decidido de hecho**, marcando cada punto como `DECISIÓN FUERTE`, `PROVISIONAL` o `NO REGISTRADA`. Las decisiones no registradas son las importantes: quiero verlas. No cambies nada de código todavía.

El Circuito 0 en un proyecto existente tiene un entregable extra: **una lista de decisiones que están implementadas pero nunca se registraron.** Suele ser la parte más reveladora del ejercicio.

---

## Ruta C — "Quiero probar esto sin comprometerme"

```bash
./tooling/new-project.sh prueba-ads
```

Rellena sólo la sección 1 del PROFILE (definición de éxito) y lanza el bootstrap. En una sesión verás si el modelo operativo te encaja. El coste de abandonarlo es borrar una carpeta.

---

## Durante el proyecto: lo que necesitas saber como Owner

**No tienes que aprender comandos.** Todo se dirige en lenguaje natural (G10). Si en algún momento sientes que necesitas memorizar sintaxis para dirigir tu propio proyecto, es un fallo del sistema, no tuyo.

Cosas que puedes decir en cualquier momento:

| Lo que dices | Lo que hace el sistema |
|---|---|
| "¿Cómo va el proyecto?" | Estado ejecutivo sintetizado (G08) |
| "No lo veo claro, discutámoslo" | Activa deliberación con especialistas (G09) |
| "Quiero una segunda opinión" | Activa un especialista que no participó en la propuesta |
| "Esto no me gusta, quiero que se parezca más a X" | Flujo de cambio de dirección (G51) |
| "¿Por qué se ha hecho así?" | Recupera el ADR y su contexto |
| "Investiga esto antes de decidir" | Convierte la decisión en investigación o spike |
| "Vamos a hacer retoques rápidos" | Sesión copiloto, sin ceremonia (G35) |
| "Esto se está complicando" | Reevalúa alcance y presupuesto (G24) |
| "¿Qué hemos aprendido sobre X?" | Consulta los ledgers de aprendizaje (G52) |
| "¿Sigue teniendo sentido el equipo actual?" | Revisión de plantilla, con retirada obligatoria (G52) |

**Lo que sí es tuyo y nadie decide por ti:** visión y alcance, dinero, publicación, asuntos legales, privacidad material, monetización, y cualquier cosa difícilmente reversible con impacto serio.

**Lo que no deberías estar haciendo nunca:** decidir cuándo hacer commit, qué rama usar, cómo abrir un PR, o mantener la estructura documental a mano. Si acabas haciendo eso, algo se ha roto.

---

## Cuando algo va mal

| Síntoma | Qué significa | Qué hacer |
|---|---|---|
| El Circuito 0 se alarga y sólo produce documentos | El fallo clásico (K0.9) | Invocar el gate G22 y parar |
| Te preguntan cosas técnicas de bajo nivel | El sistema no está usando su autoridad (G05) | "Eso decídelo tú, es ingeniería rutinaria" |
| Te llegan acceptance tests de uno en uno | No está aplicando G36 | "Agrúpalos en un plan de validación" |
| Corriges lo mismo por segunda vez | Falta una regla | "Convierte esto en una regla de AGENTS.md" |
| El estilo antiguo reaparece tras un cambio | Anti-deriva incompleta (G51) | "Actualiza también convenciones y AGENTS.md" |
| Las sesiones empiezan sin contexto | No se está usando el journal (G26) | "Lee las últimas entradas de JOURNAL.md antes de nada" |
| El sistema te da la razón siempre | Fallo grave (G09) | "Quiero que me digas si crees que me equivoco" |

---

## Lista de verificación de arranque

```text
[ ] Repositorio creado, con remoto, primer commit hecho
[ ] kernel/ y packs/ copiados y SIN editar
[ ] PROFILE.md completo — las 4 preguntas respondidas
[ ] PROFILE.md leído y aprobado por ti
[ ] PROJECT.md con la composición declarada
[ ] Timebox del Circuito 0 ajustado a tu ritmo real
[ ] BOOTSTRAP_PROMPT.md lanzado
[ ] Primera entrada de JOURNAL.md existe
```

Si los ocho están marcados, el proyecto está arrancado correctamente.
