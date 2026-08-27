# Decisiones, contradicciones y límites del kernel operativo


Registro vivo de la iteración que construye el contenido operativo (pasos 1 a 6) sobre
las secciones aprobadas (a) y (b). Tres partes: **decisiones tomadas** (reversibles, y por
qué se tomaron sin consultar), **decisiones que pertenecen al Owner** (agrupadas, no
interrumpen el trabajo) y **contradicciones detectadas** contra el material normativo.

---

## 1 · Decisiones tomadas sin consultar

Criterio para no consultar: reversible, dentro del alcance ya autorizado, y sin cambiar
autoridad ni semántica de (a) o (b) — la regla de b.15.1 aplicada a este trabajo.

| # | decisión | motivo | cómo se revierte |
|---|---|---|---|
| D1 | El contenido operativo vive en `kernel/operativo/`, no dentro de `KERNEL.md` | `KERNEL.md` es prosa constitucional de 1.3.0; mezclar ambos crearía dos fuentes de la misma verdad | mover el árbol; nada depende de su ruta salvo el índice |
| D2 | Formato canónico = bloques ` ```yaml ads:<tipo> ` dentro de Markdown | cumple las dos exigencias a la vez: legible por el Owner, no ambiguo para la máquina | cambiar el extractor de `ads_lint`; los datos no cambian |
| D3 | Los tres packs de 1.3.0 pasan a `packs/legacy-1.3.0/` | evita dos packs de web app compitiendo por la misma verdad | `git mv` inverso |
| D4 | `pack-design-led` **se promueve al kernel** en vez de reescribirse como pack | la excelencia visual dejó de ser propiedad de una clase de proyecto: es requisito central del kernel (enunciado del paso 3) | volver a extraerlo a un pack |
| D5 | Los packs nuevos son **directorios**, no ficheros sueltos | un pack aporta roles, métodos, gates y pruebas: no cabe en un fichero sin volverse ilegible | — |
| D6 | La numeración de pruebas nuevas empieza en **T75** | continúa T01–T74 sin renumerar nada aprobado | — |
| D7 | El rol que atiende al Owner se llama **`ENC` · Encuadre** como capacidad y `ENC/interlocutor` como rol | (a) sitúa Encuadre como función de DSP; separarlo como capacidad propia se explica en la contradicción C1 | ver C1 |
| D8 | `kernel/VERSION` pasa a `2.0.0-alpha.1` | hay contenido de kernel 2.0 real en el repositorio; dejarlo en 1.3.0 haría que `kernel-status.sh` mintiera | — |
| D9 | La composición del producto vive en `SOURCES.toml`, y **ningún otro documento la repite** | el mandato la declara fuente única; copiarla en `PROJECT.md` obligaría a editar dos sitios cada vez que cambie una URL | borrar el manifiesto y declarar las fuentes en prosa; se perdería la validación mecánica |
| D10 | Los dos contratos nuevos son **`C6` y `C7`**, transversales, en vez de una capacidad nueva de Git | el 8.2 del mandato avisa de que repartir Git entre `PLT`, `ENT`, `DSP` y `CON` es el problema; una capacidad más lo repartiría otra vez. Un contrato transversal declara la propiedad **operación a operación** sin crear un equipo | fundir ambos en uno, o mover su contenido a las fichas de capacidad |
| D11 | `source` y `component` **no** son tipos canónicos con bloque `ads:` | duplicarían `SOURCES.toml`, que el mandato declara fuente única. Sí lo es `integration-set`, porque es evidencia nueva y no vive en el manifiesto | añadir los esquemas si aparece una necesidad que el manifiesto no cubra |
| D12 | El alcance de fuentes de un paquete se declara como **dos campos más de la declaración de acoplamiento** de `a.5`, no como artefacto nuevo | `a.5` ya declara que los nombres definitivos se fijan más adelante, y el mandato pide adaptar el formato existente en vez de introducir uno | renombrarlos al cerrar la sección (g) |
| D13 | Las pruebas de `workspace.py` viven en `tooling/tests/` y el manifiesto de validadores gana un campo `dir` | prueban tooling, no el corpus; meterlas en `validadores/` las habría mezclado con las pruebas de conformidad. Sin el campo `dir` habrían quedado fuera de la evidencia | mover el fichero y quitar el campo |
| D14 | La huella de integridad cubre ahora `.toml` | `SOURCES.toml` es contenido vendorizado del kernel: sin cubrirlo, editar la plantilla sería un fork invisible, que es el hallazgo A-04 otra vez | quitar la extensión de `huella.py` |
| D15 | `kernel/KERNEL.md` sube a **1.4.0** en vez de quedar congelada | `K-1` y `G29` cambian de alcance, y un lector que sólo abra la constitución leería el modelo retirado. La política de versiones ya preveía que la línea histórica suba «cuando cambia ella» | revertir el texto y dejar la revisión sólo en `E2` |

---

## 2 · Decisiones que pertenecen al Owner

**Ninguna bloquea el trabajo.** Todas tienen un valor por defecto ya implementado y
declarado; cambiarlas es una orden, no un rediseño.

| # | decisión | por defecto implementado | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| O1 | ~~¿`ENC` es capacidad propia o sigue siendo una función de `DSP`?~~ **RESUELTA** | El Owner la aprobó como decimoquinta capacidad base el 2026-08-26: [enmienda E1](a-ENMIENDA-E1-ENC.md). Materialización **bajo demanda**, no permanente. | nada: la decisión está tomada y enmendada en (a) |
| O2 | Convivencia de `KERNEL.md` 1.3.0 con el kernel operativo | conviven; 1.3.0 arranca proyectos, `operativo/` es lo que el runtime consumirá | reescribir `KERNEL.md` como índice delgado sobre `operativo/` es un item `SIS` que aún no existe |
| O3 | Umbral de anclaje y margen de ambigüedad de b.13 | `umbral 0.60` · `margen 0.15`, declarados en `entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` §3, **como provisionales y calibrables por uso real** | son parámetros; cambiarlos no toca contratos |
| O4 | Presupuesto de exploración de Diseño | `DIS/Fundacion` sin techo de sesiones; `DIS/Evolucion` con exploración proporcional a la novedad, medida por la tabla de novedad | subir o bajar el número mínimo de direcciones exploradas |
| O5 | Quién puede levantar el veto de excelencia visual | sólo el Owner, y sólo tras ver las alternativas exploradas | delegarlo en `DIS/direccion-artistica` |
| O6 | Idioma de los artefactos operativos | castellano, como (a) y (b) | traducir es mecánico y no afecta a los identificadores |

### `O7`–`O14` · resueltas por el Owner el 2026-08-27, tras la crítica independiente de F3

A diferencia de `O1`–`O6`, éstas **no tenían valor por defecto implementado**: son las
preguntas que la síntesis de la iniciativa ADS NEXT elevó al Owner, y que su crítica
independiente reformuló. Fijan dirección para F4; **ninguna está construida**, y ninguna
enmienda (a), (b), `E1`, `E2` ni `K-1`.

> **Aquí no se enlaza esa iniciativa, y no es un descuido.** `docs/evolucion/` es historia
> del repositorio del kernel y **no viaja a un proyecto instalado**; este fichero sí. Un
> enlace a `09-SINTESIS.md` o a `10-CRITICA-INDEPENDIENTE-F3.md` quedaría roto en toda
> organización que instale ADS, que es el mismo motivo por el que `C6` no enlaza la decisión
> del Owner que lo originó y por el que las auditorías tampoco viajan. Quien lea esto dentro
> del repositorio del kernel los encuentra en `docs/evolucion/`.

| # | decisión | lo resuelto | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| O7 | ¿puede el sistema abrir trabajo de auditoría sin petición del Owner? | **política revocable de auditoría recurrente.** Detectar e inventariar es automático y **no crea trabajo**. Abrir auditorías se autoriza por evento, riesgo, recurrencia y caducidad **dentro de la política aprobada**. Las correcciones mecánicas y locales se ejecutan sólo en campañas y umbrales preautorizados, con pruebas y `VER` independiente. Producto, UX, arquitectura, seguridad, datos y comportamiento crítico **conservan sus gates y su autoridad**. Una única decisión declara alcance, prioridad, presupuesto, umbrales y revocación | revocar la política devuelve el sistema a proponer y esperar. `G03` no queda levantado en bloque: sólo lo que la política declara |
| O8 | ¿dónde cae el mínimo documental de un producto? | **las doce áreas semánticas del §5.18**, obligatorias como MATERIA y no como ficheros. Compactables físicamente, con profundidad proporcional a tamaño, naturaleza y riesgo. Las condicionales se activan por aplicabilidad, y «no aplicable» exige motivo registrado. Reanudación, decisiones seguras y gates son **comprobaciones** del mínimo, no su única razón | subir o bajar el número de áreas obligatorias, o su profundidad exigida por perfil de producto |
| O9 | ¿trae la distribución catálogo o equipo materializado? | **catálogo completo y estructura preconfigurada.** `C4` gobierna la materialización: `DSP` y `SIS` permanentes, `ENC` y las demás bajo demanda. No es una decisión nueva: es la lectura de `C4` y `E1` que la síntesis no hizo | cambiar el equipo mínimo permanente exigiría enmienda a `C4` o a `E1`, y aquí no se propone ninguna |
| O10 | ¿dónde vive el material normativo en voz del Owner? | **`docs/owner/`** como destino canónico. La clasificación pasa a ser por **ubicación y metadata de autoridad**, en vez de una exención manual por fichero. El material temporal de evolución **no se retira todavía** | mover el directorio, o volver a la exención por fichero — que es lo que falló cinco veces |
| O11 | ¿cómo se llama la unidad amplia, y qué es? | **`iniciativa`.** Tipo o artefacto canónico de **coordinación**, con identidad, estado durable, alcance, gates y dosier vivo **derivado**. **No es un proceso nuevo**: compone rutas, items y paquetes existentes | elegir otro nombre es mecánico. Convertirla en proceso sí sería un rediseño, y contradiría `H1` |
| O12 | ¿qué certificación permite empezar a trabajar? | **Integrada + baseline aprobado + ningún desconocido crítico sin clasificar.** La certificación **Completa** es lo que permite declarar una instalación o adopción terminada y plenamente certificada | exigir Completa para empezar bloquearía todo producto sin runtime; exigir sólo Estructural dejaría entrar sin saber si el sistema arranca |
| O13 | ¿qué entornos agentic entran en la primera matriz? | **Claude Code y Codex** son el primer **objetivo** de soporte y certificación. **Hoy no hay ningún adaptador certificado**, y ninguno de los dos lo estará hasta superar una **prueba de humo real** en sesión nueva. **Cursor y Gemini** figuran desde el diseño en nivel compatible o genérico hasta superar la suya. **Fallback genérico obligatorio** para proveedores no certificados. **Ningún soporte se declara sin ejecución real: fijar el objetivo no es alcanzarlo** | añadir o quitar entornos de la matriz. Lo que no cambia es la regla: sin prueba de humo ejecutada, no hay nivel certificado |
| O14 | ¿qué producto se usa para el piloto? | **PesquerApp**, en clones y workspace aislados, **sin modificar ramas productivas**. Debe probar adopción multi-repo de un producto existente, `T169`, `T170`, `CA-10`, `CA-11`, el §100 y los límites de fan-out. **No se ejecuta todavía**: queda seleccionado, con sus condiciones escritas | elegir otro producto exigiría uno con historia real y varios repositorios. `gym-wear` sigue retirado como fuente contaminada, y esa retirada era para la minería, no para el piloto |

**Procedencia:** las ocho llegan de la revisión independiente de F3 y de la respuesta del
Owner a ella, el 2026-08-27. `O7` cierra `X6`, `O8` cierra `X7` y `O9` cierra `X8`; `O10`
cierra la ubicación de `P-07`, que era la parte que la síntesis había dejado al Owner.

---

## 3 · Contradicciones detectadas contra (a) y (b)

Se registran; **no se modifican (a) ni (b)**. Cada una lleva una propuesta de cambio
mínima que el Owner puede aceptar o rechazar.

### C1 · Encuadre: función de DSP en (a), y sin embargo necesita rol, método y memoria propios

**Qué dice (a).** a.3 sitúa *Encuadre* como una de las cuatro funciones de `DSP`, junto a
Enrutamiento, Estado y Supervisión, y describe `DSP` como *«implementación software/runtime
primero»*, sin autoridad sobre el contenido de ninguna capa.

**Qué exige el paso 1.** Un rol que escucha, conversa, hace brainstorming, consulta
especialistas, mide incertidumbre y ayuda al Owner a descubrir lo que quiere. Eso no es
runtime: es trabajo de contenido, con método, memoria y checkpoint.

**Contradicción real:** si el trabajo conversacional vive dentro de `DSP`, entonces `DSP`
tiene trabajo de contenido, y (a) afirma que no lo tiene.

**Propuesta de cambio mínima (una frase en a.3):**

```text
DSP · DESPACHO — Encuadre
  ANTES:  «Encuadre — id, enunciado de una línea […] Se apoya en el índice de lo existente»
  DESPUÉS: añadir «El TRABAJO CONVERSACIONAL del encuadre —escuchar, interpretar,
           conversar, medir incertidumbre— lo ejecuta la capacidad ENC, que entrega a DSP
           un encuadre listo. DSP conserva la ficha, el anclaje mecánico y el índice de
           lo existente.»
```

**Cómo se ha continuado sin la decisión:** `ENC` se ha construido como capacidad completa
con los doce campos; su ficha declara `deriva_de: a.3 DSP/Encuadre`. Si el Owner prefiere
la lectura estricta de (a), el contenido de `capacidades/ENC/` se mueve bajo `DSP/` sin
reescribir un solo rol ni método. **El trabajo no dependía de la decisión.**

### C2 · «El gate no es un juicio: es una lista» frente a la excelencia visual

**Qué dice (a).** a.1: *«GATE — lista COMPROBABLE […] No es un juicio: es una lista. Si
hiciera falta juicio, ese juicio es otra capacidad activada, no una aprobación oculta.»*

**Qué exige el paso 3.** *«La excelencia no puede reducirse a una puntuación automática.
Usa rúbricas y evidencia, pero conserva crítica profesional y juicio del Owner donde
corresponda.»*

**Contradicción aparente, resuelta sin cambiar (a).** El juicio no se mete dentro del
gate: se materializa como **rol independiente** —`DIS/critica-visual`— cuya salida es un
artefacto. El gate `gate:excelencia-visual` sigue siendo una lista comprobable, y lo que
comprueba es que **exista** ese artefacto, con veredicto explícito, ejes puntuados,
evidencia enlazada y desacuerdos registrados. Es exactamente lo que a.1 ordena: *«ese
juicio es otra capacidad activada»*.

**No se propone cambio a (a).** Se registra porque es el punto donde más fácil sería
introducir una aprobación oculta, y la revisión adversarial debe volver aquí.

### C3 · `C-DIS` de b.16 no distingue superficie nueva de superficie tocada

**Qué dice (b).** `C-DIS` se activa cuando el item *«toca una superficie que un humano
percibe […] O altera la experiencia de un flujo existente»*.

**Problema operativo.** Esa condición es binaria y `DIS` tiene tres procedimientos
distintos (`Fundacion`, `Reconstruccion`, `Evolucion`) más una escala de exploración.
Aplicada tal cual, una corrección de espaciado dentro de un patrón vigente convoca el
mismo procedimiento que una pantalla nueva.

**Resuelto sin tocar (b):** `C-DIS` sigue decidiendo **si** `DIS` se activa. Cuál de sus
métodos se ejecuta y cuánta exploración exige lo decide la **tabla de novedad** de
[`kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md`](../../kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md),
que es contenido de método, no condición de ruta. **No hay contradicción; hay un hueco que
el kernel operativo rellena.**

### C4 · `owner_attention_slots: 1` frente a una conversación de fundación de Diseño

**Qué dice (b).** b.11 fija `owner_attention_slots` por defecto en 1.

**Tensión.** `DIS/Fundacion` es explícitamente una conversación larga y repetida con el
Owner. Mientras dure, ningún otro paquete puede consumir su atención, y el paso 3 prohíbe
limitar artificialmente las sesiones necesarias.

**Resuelto sin tocar (b):** b.11 ya separa atención de ejecución, y su regla 4 lo dice con
todas las letras. `DIS/Fundacion` declara sus puntos de atención como **sesiones
delimitadas** —no como ocupación continua del slot— de modo que entre sesión y sesión el
slot queda libre. Está implementado en el método: cada punto de atención abre y cierra.

**Límite honesto:** si el Owner quiere conversar con dos equipos a la vez, `owner_attention_slots`
es un parámetro de proyecto, no una regla del kernel. Ese cambio es suyo (O6 no lo cubre;
se decide en el PROFILE).

---

## 4 · Límites declarados de esta iteración

> **Actualizado el 2026-08-26 por la implementación multi-repositorio.** Los límites de
> abajo son los de la iteración que construyó el kernel operativo. Lo que la implementación
> del mandato multi-repo añadió —`C6`, `C7`, `E2`, `SOURCES.toml`, `workspace.py` y sus
> pruebas— **no cambia ninguno de ellos**: sigue sin haber runtime, sigue sin haber piloto
> en un proyecto real, y las pruebas que exigen runtime siguen en `contrato-definido`.

```text
NO se ha implementado el dispatcher ni el runtime          — encargo explícito del Owner
NO se ha instalado el kernel en gym-wear                   — encargo explícito
NO se ha empezado el pack ERP                              — encargo explícito
NO se han diseñado las secciones (c) a (i) en abstracto    — (c) y (d) quedan cubiertas
                                                             PARCIALMENTE y de forma
                                                             operativa, no como sección
NINGUNA prueba que requiera runtime puede superarse hoy    — registro en pruebas/REGISTRO.md
La coherencia PROSA↔BLOQUE dentro de un mismo fichero no
  es comprobable automáticamente                           — la cubre la revisión adversarial
```
