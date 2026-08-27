# KERNEL CHANGELOG

Formato: semver (K0.11). MAJOR cambia el contrato con el PROFILE o el sentido de una regla DEBE.

## 2.0.0-alpha.9 — el validador de vigencia reventaba ante su propio manifiesto

Cuatro correcciones de la puerta pre-F4. Tres son de redacción y una es de código; el
contenido normativo no se toca.

**`T158` reventaba con `KeyError` ante un manifiesto inválido.** Reproducido contra
`8b6727a`: basta quitar `patron` de una entrada `vigencia` para obtener una traza en vez de un
fallo. Una traza **no es una detección**: no dice qué corregir, tumba las comprobaciones que
venían detrás, y deja la evidencia sin comprobar sin que nadie declare que quedó sin
comprobar. El contrato se valida ahora **de forma tipada antes de usarse** —lista, mapas,
cuatro campos con su tipo, ids no duplicados, fichero de evidencia declarado, regex que
compila y captura, valor entero y recuento registrado—, condición a condición y con un mensaje
por condición. **Sin `except Exception`**: convertir un defecto en silencio es el mismo error
con otra forma.

Y el arnés de `comprobar_negativos` se endureció para poder demostrarlo. Cada mutación declara
ahora el **diagnóstico que espera**, y una salida con `Traceback` se registra como **NO
DETECTADA** aunque el proceso termine con código distinto de cero. Sin eso, un validador que
revienta se habría contado como un validador que detecta. Ocho infracciones nuevas,
`N158h`–`N158o`.

**Tres afirmaciones que el corpus no podía sostener:**

- `10-CRITICA-INDEPENDIENTE-F3.md` decía «este documento no lo escribe quien escribió la
  síntesis». Los hallazgos son de un revisor independiente; **el fichero lo escribió el autor
  de F3**. La independencia real está en el juicio, no en quién teclea, y ahora se dice así.
- El addendum daba a Claude Code y Codex por **certificados**, contra el checkpoint y contra
  el resto del corpus: hoy no hay ningún adaptador certificado. `O13` fija un **objetivo**, y
  fijar el objetivo no es alcanzarlo.
- Tres documentos hablaban de «enmendar `C4`». `C4` es contrato **derivado** y no recibe
  enmiendas: la regla vive en `a.4` —«DSP y SIS se materializan siempre»— con `E1`
  confirmándolo para `ENC`. Cambiar el equipo permanente presiona `a.4`; hacer permanente a
  `ENC` contradice `E1`. `C4` se rehace después.


## 2.0.0-alpha.8 — la evidencia podía caducar sin que nada lo viera

Puerta correctiva anterior a la arquitectura integrada. Del kernel cambian los validadores,
su manifiesto y sus exclusiones; el contenido normativo no se toca.

**`T158` daba por buena una evidencia intacta y CADUCADA.** Se reprodujo primero, contra el
código anterior, con la cifra envejecida derivada del propio fichero:

```text
corpus vigente          : 282 ficheros
evidencia publicada dice: 280 ficheros
cabecera de procedencia : presente     codigo: 0
firma de exito          : presente     debe_contener: completo
T158 -> prueba-superada  (exit 0)
```

`T158` nació de una evidencia **corrupta** —ocho de diez ficheros con «can't open file»
mientras el informe afirmaba EXIT 0— y sus ocho comprobaciones preguntan por **procedencia y
forma**. Ninguna de esas preguntas se responde distinto cuando la evidencia **envejece**. Es
el mismo defecto por otra vía.

Cómo apareció: bajo un intérprete sin `tomllib`, `comprobar_fuentes` falla y el runner
—correctamente— **no sobrescribe su evidencia**. Esa negativa protege la evidencia buena de
ser pisada por una mala, y **no se toca**. Lo que faltaba era ver el efecto secundario.

**La corrección** es un contrato de `vigencia` declarativo en `validadores.yaml`: un validador
declara qué cifra de su evidencia es derivable del corpus, y `T158` la **recalcula**.
`comprobar_fuentes` gana `corpus_recorrido()` y `ficheros_recorridos()` —definición única del
recorrido de `T161`—, y `T158` la **importa** en vez de copiarla. Falla cerrado ante un
recuento sin implementación, no se acepta a sí mismo, y va la última de sus comprobaciones
para no enmascarar el motivo de otras mutaciones. Regresiones `N158g` y `N158h`.

**`P-08`, declarado abierto.** La vigencia cubre la cobertura de `T161` y nada más. Los otros
doce validadores publican cifras que pueden envejecer igual —«documentos analizados» de
`T147`, «unidades de instrucción revisadas» de `T153`, «Ran N tests» de workspace— y nada lo
detecta. La solución general exige declarar las **entradas** de cada validador, y eso es
arquitectura. **No puede afirmarse que toda la evidencia tenga vigencia garantizada.**

**`docs/owner/` y el final de las exenciones una a una.** La resolución `O10` fija el destino
canónico del material normativo en voz del Owner. Los dos documentos multi-repo se mueven ahí
con `git mv`, con todas sus referencias actualizadas, y `exclusiones.yaml` pasa de dos
entradas por fichero a **una por ubicación**. Cinco documentos del Owner entraron y los mismos
dos validadores los rechazaron cinco veces con el mismo remedio manual: una excepción que se
repite cinco veces es una clase que faltaba. La directiva, su prompt y el documento de
pendientes siguen fuera, con su migración declarada pendiente.

Y `comprobar_arranque` cazó un defecto de este mismo trabajo: dos enlaces nuevos desde
`docs/rediseno/` hacia `docs/evolucion/` habrían quedado **rotos en toda organización
instalada**, porque el primero viaja al proyecto y el segundo no.


## 2.0.0-alpha.7 — un quinto documento del Owner entra sin sitio, y P-07 se mide

Entra `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`, el documento vivo de
trabajo con el Owner que recoge qué quedó aceptado, qué sigue propuesto y qué debe
sintetizarse tras F2. **No es normativa vigente y no autoriza a implementar su contenido.**

Del kernel sólo cambia `validadores/exclusiones.yaml`: una entrada más de
`vocabulario_exento`, con su motivo escrito, porque el documento está en voz del Owner y
reescribir su vocabulario cerraría por redacción lo que él dejó abierto. Sus enlaces se
comprueban como los de cualquier documento, y lo alcanza el índice de la iniciativa.

**Lo que este release deja medido es el problema, no la solución.** Al entrar, el documento
fue rechazado por los mismos dos validadores que rechazaron a los cuatro anteriores:
`ads_lint` por dos expresiones de vocabulario, y `T147` por «existe para nadie». El remedio
vuelve a ser manual, y vuelve a ser una exención por fichero. Con éste son cinco:

```text
docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md
ADS-ARQUITECTURA-MULTIREPO-APROBADA.md
ADS-IDEAS-PENDIENTES-MULTIREPO.md
docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md
```

`P-07` deja de ser una observación y pasa a tener recuento. Su tratamiento —dónde viven
estos documentos, qué autoridad tienen y cómo se les aplica la exención por ubicación en vez
de por fichero— es materia de la síntesis, no de este release.


## 2.0.0-alpha.6 — pasada correctiva: verde no era correcto

Una revisión externa reprodujo defectos que la batería de `2.0.0-alpha.5` no detectaba, con
los trece validadores en verde y veintinueve pruebas pasando. Las decisiones de arquitectura
—`E2`, `C6`, `C7`, el `integration-set`, `SOURCES.toml` y la separación producto / fuente /
componente / workspace— se conservan enteras. Lo que se corrige es la implementación, las
pruebas, la documentación y **las afirmaciones de evidencia**.

**Los ocho bloqueantes de `tooling/workspace.py`.** Cada uno se reprodujo primero, se cubrió
con una prueba que falla contra el código anterior, y después se corrigió:

- **escape por enlace simbólico** — `normpath` es textual y no ve un symlink; `init` clonaba
  fuera del workspace. Todo destino se resuelve de verdad, sin crearlo, contra el `realpath`
  de su raíz autorizada.
- **fuentes dentro del control repo** — se rechazaba `path = "ads"` y pasaban `ads/frontend`
  y `ads/../ads/z`. La ruta reservada no es una cadena: es el sitio donde vive el manifiesto.
- **colisiones jerárquicas** — `app` y `app/interno` anidaban un repositorio Git dentro de
  otro, contra `N12`. Y `path = "."` haría del workspace un repositorio, que C6 prohíbe.
- **manifiesto inválido con efectos laterales** — `init` clonaba las fuentes válidas de un
  manifiesto roto. Ahora es **todo o nada** frente a cualquier error estático.
- **secretos en la salida** — un secreto puesto por error salía por texto, JSON, error de
  identidad y stderr de Git. Todo remoto que se imprime pasa por `redactar`, incluido el
  que se lee del disco, que no ha pasado por ninguna validación.
- **SSH válido confundido con credencial** — `ssh://git@github.com/org/repo.git` es una URL
  admitida por §39 y se rechazaba por llevar `@`.
- **normalización demasiado agresiva** — igualaba puertos distintos, plegaba la
  capitalización de la ruta y minusculaba rutas locales. Ahora sólo se pliega el host, se
  conserva el puerto, y lo ambiguo se devuelve **opaco**: igual sólo a sí mismo.
- **robustez del TOML** — tipos incorrectos producían traceback, y `schema = true` colaba
  como `1` porque en Python `True == 1`.

**Arranque.** `new-project.sh` documentaba `git push -u origin main` y `git init` creaba
`master` con la configuración global vacía. La rama vive en una sola variable, y `T168` la
comprueba **con `GIT_CONFIG_GLOBAL` a `/dev/null`**, que es donde el defecto aparece.

**Barrido semántico.** `E2` tenía precedencia, pero el corpus activo seguía enseñando el
modelo anterior en `K0.6`, `K0.8`, `G04`, `G12`, `G26`, `G27`, `G38`, `G39`, los entregables
del Circuito 0, `G46` y `G48`, y en `ARQ`, `ENC`, `DSP`, `SEG`, `CON`, `C2`, `C5` y
`C6`. Se clasificó cada aparición: referencia legítima a un repositorio Git concreto, al
control repo, a una fuente, al conjunto de fuentes necesarias, o resto real. Sólo se tocaron
los restos. La línea histórica sube a **1.5.0**.

**Pruebas.**

- `T161` deja de buscar tres literales: diez formulaciones con patrón, cada una con un
  fixture que debe detectar y un contraejemplo que no, y con la **cobertura publicada** —279
  ficheros—. Por debajo del mínimo es fallo: un validador que pasa por no leer nada es el
  defecto que esto evita.
- `T171` nueva: cada criterio de descubrimiento del §100 tiene un sitio declarado donde
  leerse en el proyecto recién creado. Publica que su alcance es **estructural** y que el
  descubrimiento real exige piloto.
- 29 → 57 pruebas de workspace. Entre ellas, la **reconstrucción de un producto de cuatro
  fuentes**, que antes era un «test mental»: se materializan, se borran las cuatro y el
  workspace se reconstruye desde el control repo con las mismas revisiones.
- **Sin red comprobado**: `GIT_ALLOW_PROTOCOL=file`. `https`, `ssh` y `git` mueren con
  «transport not allowed», y una prueba lo comprueba; otra comprueba que el transporte local
  sigue funcionando, para que la primera no pase por bloquearlo todo.
- Nueve pruebas negativas nuevas: `N161`–`N161g`, `N171`, `N171b`.

**Afirmaciones.** El checkpoint decía «CA-1 a CA-17 verificados» y «los diez criterios del
§100». Ninguna de las dos tenía evidencia detrás. La matriz con el grado real de cada
criterio —**nueve ejecutados, cinco estructurales, dos contrato y uno estructural
parcial**— vive en `docs/evolucion/08-EVIDENCIA-MULTIREPO.md`, en el repositorio del
kernel: es historia de esta entrega y **no se enlaza desde aquí**, porque un proyecto
instalado no la recibe y el enlace quedaría roto en cada instalación. `T169` y `T170`
siguen en `contrato-definido` y no se cuentan como demostradas.

**Requisito de entorno, escrito donde se ve.** Leer `SOURCES.toml` exige Python 3.11 o
superior: `tomllib` es estándar desde ahí. En 3.10 el manifiesto no se lee y tres
validadores fallan diciéndolo.

## 2.0.0-alpha.5 — un producto ADS no es un repositorio

Decisión de arquitectura del Owner, aprobada para implementación. Retira la suposición
histórica `ADS PROJECT = repositorio de código`, que nunca estuvo escrita en ninguna parte y
gobernaba todo el arranque, la adopción y el gobierno Git.

**Normativo.** Enmienda **E2** a las secciones (a) y (b), por sustitución explícita:

- `a.9` — «los ficheros del repo» pasa a ser **el repositorio ADS de control**. Los seis
  invariantes quedan intactos y ganan alcance: `I5` prohíbe ahora copiar PROFILE, estado,
  items o memoria dentro de una fuente, algo que antes no tenía dónde ocurrir.
- `a.5` — un paquete declara `lee_fuentes` y `escribe_fuentes`. Leer no autoriza a escribir.
- `a.10` — el checkpoint referencia revisiones de otras fuentes; nunca copia su contenido.
- `a.11` — **`G29` pasa de «sobrevive» a REVISADA**: se conserva íntegra y se aplica POR
  FUENTE; se deroga `un item → una rama → un PR` como relación universal.
- `b.1` — la identidad de un item es del producto: atravesar tres repositorios no lo parte.
- `b.10` — un item **no cierra** con una de sus fuentes sin integrar. Eso es integración
  parcial, y llamarlo terminado hace que el sistema informe de un producto que no existe.

**Dos contratos transversales nuevos**, que pasan de cinco a siete:

- `C6` — producto, fuentes y workspace: qué es cada cosa y dónde vive cada verdad.
- `C7` — gobierno Git multi-fuente: quién pide, ejecuta, bloquea y verifica **cada**
  operación. Es la tabla que faltaba desde que la línea 2.0 dejó `G29` sin recoger.

**Tipo canónico nuevo:** `integration-set` — la combinación exacta de revisiones que se
probó junta. Atomicidad **lógica** de producto, porque Git no ofrece commit físico
multi-repositorio y ADS no finge uno.

**Maquinaria.**

- `SOURCES.toml` como fuente única de la composición. TOML porque `tomllib` es estándar:
  leer el manifiesto no añade ninguna dependencia.
- `tooling/workspace.py` — `check`, `init`, `status`, `--json`. Sólo biblioteca estándar y
  Git. **Nunca borra, resetea, sobrescribe, cambia un remoto ni sincroniza.**
- `new-project.sh` crea `<workspace>/ads`, y el workspace **no** es un repositorio Git.
- `comprobar_fuentes.py` valida el ADS Project **sin tocar el disco**, para que la CI del
  control repo no necesite credenciales de ningún repositorio privado.
- La huella cubre ahora `.toml`, y su prueba negativa se actualizó con ella.

**Lo que se corrigió y era falso o estaba obsoleto:**

- `compile-agents.sh` buscaba los packs en `packs/*.md`, la forma plana retirada en la
  línea 1.3: en todo proyecto real devolvía «ninguno».
- la adopción documentada copiaba ADS dentro del repositorio de código.
- `AGENTS_EXAMPLE` enseñaba «una tarea = una rama», que ya no es cierto con varias fuentes.
- dos pruebas negativas —`N148` y `N152b`— habían dejado de encajar con el texto que
  mutaban, y una prueba negativa que no se aplica no prueba nada. `N152b` ya no fija las
  versiones a mano: las lee del árbol.

**Pruebas.** `T159`–`T170`, ejecutadas por tres validadores distintos según lo que cada una
comprueba, más veintinueve pruebas de workspace con repositorios Git locales temporales:
sin red y sin GitHub.

La línea histórica `kernel/KERNEL.md` sube a **1.4.0** con esta entrega: `K-1` declara que
el sujeto de las tres capas es el **producto**, y `G29` queda revisada en su propio texto.

## 2.0.0-alpha.4 — dos documentos más del Owner, y el defecto que ya es patrón

Tercera vez que material normativo escrito en voz del Owner entra al repositorio y los
mismos dos validadores lo rechazan. El remedio vuelve a ser manual, fichero a fichero.

- `validadores/exclusiones.yaml` — `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` y
  `ADS-IDEAS-PENDIENTES-MULTIREPO.md`, exentos de **vocabulario** con su motivo escrito.

**No cambia ningún contrato, esquema, rol, método ni gate.** Que la exención siga siendo
manual queda registrado como problema **P-07** en
`docs/evolucion/07-DECISION-MULTIREPO.md`.

## 2.0.0-alpha.3 — un documento en voz del Owner tiene sitio

Cambio mínimo, y lo provocó un defecto real. La directiva **ADS NEXT** entró al repositorio
y dos validadores la rechazaron: `ads_lint` marcó ocho expresiones de su vocabulario, y
`T147` la declaró inalcanzable —«existe para nadie»—. Ninguno de los dos se equivocaba: el
kernel **no tenía forma declarada de alojar material normativo escrito en voz del Owner**,
que no es corpus operativo y no puede reescribirse para cumplir la regla de condición
comprobable sin reescribir la orden.

- `validadores/exclusiones.yaml` — la directiva y su prompt de arranque quedan exentos de
  **vocabulario**, con su motivo escrito, por el mecanismo que el kernel ya tenía. Sus
  enlaces se comprueban como los de cualquier documento.

**No cambia ningún contrato, esquema, rol, método ni gate.** El corpus operativo queda
intacto, y con él las cifras derivadas.

## 2.0.0-alpha.2 — correcciones de la auditoría independiente

Resuelve los 33 hallazgos de una auditoría independiente, ejecutada por un lector que no
escribió el material. El informe y la matriz de resolución viven en el repositorio del
kernel, en `docs/rediseno/AUDITORIA-INDEPENDIENTE-LOCAL.md` y
`docs/rediseno/CORRECCIONES-POST-AUDITORIA.md`. **No viajan con el kernel instalado**: son
historia del kernel, no especificación que su corpus enlace.

**Normativo.** Enmienda **E1** a la sección (a), aprobada por el Owner: `ENC` es la
decimoquinta capacidad base, con su frontera con `DSP` y con materialización **bajo
demanda** — los equipos permanentemente activos siguen siendo dos.

**Lo que faltaba y ahora existe:**

- `recorrido/` — obligaciones del proceso, `gate:cierre-de-item` con las cinco condiciones
  de b.10, y los diez procesos de b.16 en forma canónica
- `DSP/supervision` — la cuarta función de DSP, que ejecuta los cuatro frenos
- `esquemas/nivel-novedad.yaml` — la escala de novedad con condiciones **formales**, que
  vuelve alcanzable el nivel N3
- `propiedades_medibles` en los packs — lo que hace computable la precedencia P1
- `validadores/huella.py` — la integridad cubre ahora a los validadores y al tooling
- `validadores/comprobar_negativos.py` — **cada prueba nueva falla cuando debe fallar**

**Lo que se corrigió y era falso:**

- el comando de arranque documentado terminaba con código 3
- un proyecto recién creado tenía once enlaces rotos: no se le enviaba la especificación
  normativa que su propio corpus enlaza
- `T131` estaba en `prueba-superada` afirmando un comportamiento que su validador no
  ejecutaba; `T134` pasaba por coincidencia de nombre de fichero
- `DIS` y `DOM` se arbitraban un veto que a.5 reserva al Owner
- `DSP/estado` **decidía** cancelaciones, que b.7 le niega
- once recuentos en prosa que ya no coinciden con nada porque **se derivan**: los comprueba
  `comprobar_recuentos.py`

**El corpus, contado desde el corpus** (`pruebas/RECUENTOS-generado.md`):

```text
15 capacidades · 42 roles · 35 métodos · 36 prompts · 29 gates
38 composiciones · 16 handoffs · 10 procesos · 18 esquemas
12 validadores · 73 escenarios de conformidad
```

## 2.0.0-alpha.1 — contenido operativo sobre la especificación aprobada

> **Las cifras de esta entrada eran incorrectas** y se corrigen aquí sin reescribir su
> historia: eran dieciséis esquemas y no diecisiete, treinta y cuatro métodos y no treinta
> y cinco, veintinueve campos de rol y no veintiocho. Fue el hallazgo A-24, y desde
> `2.0.0-alpha.2` ninguna cifra del corpus se escribe a mano.

**No es un kernel funcionando: es el contenido que el runtime consumirá.** El runtime y el
dispatcher siguen sin existir, por decisión del Owner.

Añade `kernel/operativo/`, con:

- lenguaje canónico de doble lectura y diecisiete esquemas
- quince capacidades con ficha de doce campos, gate propio y contrato de veto donde procede
- 41 roles con los 28 campos del contrato común, y sus prompts operativos
- 35 métodos ejecutables, todos con condición de salida por paso y prueba de reanudación
- los cinco contratos transversales C1 a C5
- el sistema de excelencia de Diseño: dos gates independientes, dos rúbricas, memoria de
  doce secciones, escala de novedad y procedimiento de fidelidad
- el circuito completo de la puerta de entrada, con catorce formas de conversación
- tres validadores ejecutables y 61 escenarios de conformidad con su estado REAL

Deroga: `pack-design-led` como pack — la excelencia visual pasa al kernel.
Retira a `packs/legacy-1.3.0/` los tres packs de la versión anterior.

Las secciones (a) y (b) aprobadas NO se han modificado. Las contradicciones encontradas
están registradas en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`.

## 1.3.0 — 2026-08-24

MINOR: nueva regla compatible. **Adopción recomendada para cualquier proyecto con un diferenciador cualitativo.**

- **G53 — Ejes de prioridad: riesgo y valor diferencial.** El kernel graduaba el proceso
  sólo por riesgo (G34), con una consecuencia grave: los cambios visuales, de interacción
  y de redacción son casi siempre de bajo riesgo, así que un sistema gobernado sólo por
  riesgo los trata como Quick Change, les da validación mínima y los resuelve por el
  camino más barato que exige G24. Si el diferenciador del producto es el diseño, la
  organización optimiza con precisión hacia la mediocridad.
- Nuevo campo obligatorio del contrato K0: `premium_areas` (1-3 máximo; más requiere
  justificación explícita del Owner, porque si todo es premium nada lo es).
- **G24 se invierte dentro de las áreas premium**: modelo más capaz, techo de iteraciones
  alto, y "la calidad más alta alcanzable" en lugar de "la combinación más sencilla".
- **Prohibido Quick Change dentro de un área premium**, por bajo que sea su riesgo técnico.
- Iteración obligatoria (≥2 direcciones) y evidencia visible como criterio de validación.
- Prioridad alta en la cola de aceptación humana (G36): la organización puede verificar
  que algo funciona, no que algo es bueno cuando "bueno" es el diferenciador.
- Contrapartida obligatoria: fuera de las áreas premium se busca lo suficientemente
  bueno y barato.

Pack nuevo publicado en paralelo: **`pack-design-led` 1.0.0** — para productos cuya razón
de existir es cómo se sienten al usarlos. Referencias analizadas en vez de aspiración
vaga, criterios comprobables, sistema de movimiento, listón de rechazo, regresión visual,
enrutamiento de modelo y orden de construcción.

## 1.2.0 — 2026-08-24

MINOR: nueva capacidad y nuevo mecanismo, compatibles. Adopción recomendada.

- **G52 — Aprendizaje del sistema: los dos ledgers.** El kernel registraba decisiones,
  estado, investigación y métricas, pero no lo más volátil y valioso: **qué ha funcionado
  y qué no**. Ahora hay dos ledgers con sujetos separados:
  `docs/agentic/ORG_LEARNINGS.md` (cómo trabajamos, dueño Agentic Engineering) y
  `docs/PROJECT_LEARNINGS.md` (qué construimos, dueño Evidence & Learning).
- **Nueva capacidad `Evidence & Learning`** en G11. No es plantilla permanente: se activa
  en momentos definidos. Su criterio de éxito no es el número de entradas, sino que una
  decisión no repita un error ya registrado.
- **Recuperación obligatoria**: consultar el ledger, y dejar constancia, antes de un ADR,
  una decisión Significant, trabajo en un módulo con entradas vigentes, un Owner Decision,
  un cambio de dirección (G51) o un spike sobre algo ya investigado.
- **Escalera de promoción** que enlaza con K0.12: observación → patrón → regla local →
  PACK → KERNEL. Una regla vale más que cien aprendizajes.
- **Anti-hinchazón**: techo de entradas vigentes, archivo de promovidas y superadas,
  retirada de anécdotas que no reaparecen.
- **Revisión de plantilla y regla de retirada** (refuerza G14/G25): toda auditoría DEBE
  proponer al menos un elemento a retirar o fusionar. Sin ella la organización sólo crece.
- G22: los dos ledgers pasan a ser entregable del gate del Circuito 0.
- G25: la retro de tarea incorpora una línea de aprendizaje (0 o 1, cero es legítimo).
- Plantillas incorporadas en `kernel/templates/`.

## 1.1.0 — 2026-08-24

MINOR: nueva regla compatible. Adopción recomendada.

- **G51 — Cambio de dirección: reabrir una decisión ya tomada.** El kernel 1.0.0 cubría
  cómo se toman, registran y revalidan decisiones, pero no el caso más frecuente en la
  práctica: el Owner ve el producto funcionando y quiere otra cosa. Ahora es un flujo de
  primera clase, con identificación de la decisión, radio de impacto, opciones con coste,
  desacuerdo explícito permitido, y **regla anti-deriva** obligatoria.
- G10 reconoce explícitamente la intención de cambio de dirección.
- G41: un ADR puede ser superado en cualquier momento; el antiguo se marca `Superseded by`.
- `BOOTSTRAP_PROMPT.md` y `PROJECT_TEMPLATE.md` incorporados al kernel.

Packs actualizados en paralelo (no forman parte del versionado del kernel):
`pack-web-app` 1.1.0 (W13 — sistema de diseño y resistencia al cambio),
`pack-mobile-native` 1.1.0 (M14 — equivalente).

## 1.0.0 — 2026-08-24

Primera versión extraída del MASTER v10 del proyecto `gym-wear`.

- Separación física en tres capas: KERNEL / PACK / PROFILE (K-1).
- Contrato KERNEL↔PROFILE con 10 apartados obligatorios (K0).
- Regla de pertenencia por capa y test de contaminación (K0.10).
- Versionado semántico y vendorización; prohibición de editar el kernel local (K0.11).
- Bucle de upstream con `docs/UPSTREAM.md` y reglas de promoción (K0.12).
- Definición de éxito del Owner obligatoria en todo PROFILE (K0.13).
- Procedimiento de arranque de proyecto nuevo (K0.14).
- Política de spikes generalizada: "entorno real de ejecución" en lugar de "hardware" (G22).
- Packs iniciales publicados aparte: `pack-mobile-native` 1.0.0, `pack-web-app` 1.0.0.

### Candidatos pendientes de promoción

Ninguno todavía. El bucle K0.12 se activa al cerrar el primer circuito de `gym-wear`.
