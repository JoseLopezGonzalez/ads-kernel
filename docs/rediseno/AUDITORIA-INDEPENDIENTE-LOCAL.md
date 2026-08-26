# AUDITORÍA INDEPENDIENTE LOCAL — pasos 1 a 6 del kernel operativo


> Auditoría adversarial ejecutada por un agente sin contexto previo del trabajo, con el
> encargo explícito de **intentar refutar** la afirmación de que los pasos 1 a 6 están
> implementados. Este documento es el informe de la **primera pasada ciega**.

---

## 1 · Objeto auditado

```text
repositorio      JoseLopezGonzalez/ads-kernel
rama             claude/kernel-operativo-equipos-roles-s4dzfq
commit auditado  953b8aae3ac0aea87bd1d41b025ccfac29155ce1
                 «chore: sacar __pycache__ del repositorio y añadir .gitignore»
árbol            limpio en el momento de auditar
fecha            2026-08-26
```

Documentos normativos tomados como referencia, leídos íntegros y no modificados:

```text
docs/rediseno/a-CAPACIDADES-APROBADA.md    1119 líneas
docs/rediseno/b-RECORRIDO-APROBADA.md      1288 líneas
```

## 2 · Método de auditoría

1. **Posicionamiento no destructivo.** Sin `reset`, sin `checkout` destructivo, sin merge.
2. **Lectura ciega.** Durante toda la primera pasada NO se abrieron
   `REVISION-ADVERSARIAL.md`, `DECISIONES-Y-CONTRADICCIONES.md` ni `CHECKPOINT-OPERATIVO.md`,
   ni se leyeron mensajes de commit del agente anterior más allá de la lista de asuntos.
3. **Verificación por ejecución, no por lectura.** Toda cifra, estado o afirmación de
   cobertura se ha recontado o reejecutado. No se ha aceptado ninguna por estar escrita.
4. **Experimentos controlados sobre copia aislada** del repositorio (en directorio temporal,
   nunca sobre el árbol de trabajo) para probar si un validador detecta lo que afirma
   detectar.
5. **Sin subagentes.** La revisión es de un solo auditor para que la responsabilidad del
   muestreo sea única y trazable.

## 3 · Áreas y archivos revisados

```text
LEÍDOS ÍNTEGROS
  docs/rediseno/a-CAPACIDADES-APROBADA.md · docs/rediseno/b-RECORRIDO-APROBADA.md
  README.md · START_HERE.md · kernel/operativo/00-INDICE.md
  kernel/operativo/esquemas/*.yaml (16) · validadores/reglas.yaml
  kernel/operativo/validadores/ads_lint.py · comprobar_contratos.py · comprobar_packs.py
  kernel/operativo/contratos/C1 · C3 · C4 · C5
  kernel/operativo/entrada/00-INDICE · 02-CIRCUITO · 04-INCERTIDUMBRE · 05-ESCENARIOS (parcial)
  kernel/operativo/diseno/00 · 02 · 03 · 04 · 05
  kernel/operativo/circuitos/00-CIRCUITOS.md
  kernel/operativo/capacidades/{ENC,DSP,DIS,CON,APR}/CAPACIDAD.md
  kernel/operativo/capacidades/DIS/metodos/Fundacion.md · DSP/metodos/{Continua,Enrutamiento}.md
  kernel/operativo/capacidades/DIS/roles/critica-visual.md · DSP/roles/estado.md
  kernel/operativo/capacidades/DIS/prompts/critica-visual.md
  kernel/operativo/pruebas/REGISTRO.md · REGISTRO-generado.md · T122-T133-packs.md · evidencia/*
  packs/00-QUE-ES-UN-PACK.md · packs/COMPOSICION.md · packs/wear-os/PACK.md
  packs/wear-os/gates/gates.md · packs/web-app/gates/gates.md
  tooling/new-project.sh · tooling/kernel-status.sh
  kernel/KERNEL_CHANGELOG.md · kernel/VERSION

RECORRIDOS MECÁNICAMENTE (script propio o grep sobre el corpus completo)
  los 300 bloques canónicos · los 41 roles · los 34 métodos · los 28 gates ·
  las 38 composiciones · los 61 escenarios · los 17 handoffs ·
  todos los enlaces markdown del repositorio (241 ficheros)
```

## 4 · Comandos ejecutados

```bash
git status --short --branch ; git remote -v ; git fetch origin --prune
git checkout -b claude/kernel-operativo-equipos-roles-s4dzfq --track origin/claude/...
git branch --show-current ; git log -1 --oneline ; git rev-parse HEAD

python3 kernel/operativo/validadores/ads_lint.py
python3 kernel/operativo/validadores/comprobar_contratos.py
python3 kernel/operativo/validadores/comprobar_packs.py
python3 kernel/operativo/validadores/registro_pruebas.py
git status --short          # comprobar si la regeneración altera ficheros versionados

./tooling/kernel-status.sh
./tooling/new-project.sh mi-web-app pack-web-app,pack-design-led   # sobre copia aislada

python3 -c "import yaml; ..."         # recuento de campos obligatorios por esquema
python3 <script propio>               # grafo capacidad↔rol↔método, enlaces, huérfanos
```

## 5 · Resultado reproducible de los validadores

Ejecutados desde cero sobre el commit auditado. **Los cuatro terminan con éxito y su salida
coincide byte a byte con la evidencia archivada.** La regeneración de
`REGISTRO-generado.md` no produce diff: es determinista.

```text
ads_lint.py             bloques canónicos: 300 · identificadores: 300 · errores: 0 · avisos: 0
                        EXIT 0

comprobar_contratos.py  T86 T87 T88 T89 T90 T91 T92 T134 T135  → 9 superadas · 0 fallidas
                        EXIT 0   (idéntica a pruebas/evidencia/T086-T092-salida.txt)

comprobar_packs.py      T131 T132                              → 2 superadas · 0 fallidas
                        EXIT 0   (idéntica a pruebas/evidencia/T131-T132-salida.txt)

registro_pruebas.py     61 escenarios → pruebas/REGISTRO-generado.md
                        EXIT 0 · git status limpio tras regenerar

./tooling/kernel-status.sh   kernel version 2.0.0-alpha.1 · hash 83a29abc47407330 · LIMPIO
./tooling/new-project.sh     «Pack no encontrado: pack-web-app» · EXIT 1   ← ver A-02
```

Recuento del registro generado, verificado contra los bloques `ads:escenario` del corpus:

```text
CONTRATO DEFINIDO       50
VALIDADOR IMPLEMENTADO   0
PRUEBA EJECUTADA         0
PRUEBA SUPERADA         11      (T86–T92, T131, T132, T134, T135)
PRUEBA FALLIDA           0
total                   61
```

**La cifra de 11 superadas es aritméticamente correcta y sus evidencias existen y se
reproducen.** Lo que no resiste el examen es *qué* comprueban dos de ellas: ver A-03 y A-05.

---

## 6 · Hallazgos

Clasificación de gravedad y tipo. El tipo distingue:

```text
DEFECTO                    algo escrito que no funciona, no se cumple o se contradice
CONTRADICCIÓN NORMATIVA    algo que contradice (a) o (b), que son normativas
DECISIÓN DEL OWNER         no es un defecto: falta una decisión que sólo él puede tomar
DEUDA                      limitación asumida y consciente, sin consecuencia inmediata
LIMITACIÓN DE LA AUDITORÍA lo que esta revisión no ha podido comprobar
```

---

### CRÍTICO

#### A-01 · CONTRADICCIÓN NORMATIVA + DECISIÓN DEL OWNER — `ENC` es una decimoquinta capacidad del kernel que (a) no autoriza

**Evidencia.**

| dónde | qué dice |
|---|---|
| `a-CAPACIDADES-APROBADA.md:15,78` | «14 base» · «## a.3 — El catálogo · **14 capacidades**» |
| `a-CAPACIDADES-APROBADA.md:208` | DSP tiene **cuatro funciones**, y la primera es **Encuadre** |
| `a-CAPACIDADES-APROBADA.md:272` | «El kernel reserva los **catorce** códigos de tres letras. Toda extensión declara su código con **prefijo obligatorio**: `pack:<COD>` · `local:<COD>`» |
| `a-CAPACIDADES-APROBADA.md:248` | «**DSP y SIS** se materializan siempre» |
| `b-RECORRIDO-APROBADA.md:331` | «Un disparador entra por **DSP/Encuadre**. **DSP** escribe la ficha con el dosier de anclaje» |
| `kernel/operativo/00-INDICE.md:65,71` | «las **quince** capacidades» |
| `capacidades/ENC/CAPACIDAD.md:1-10` | declara la contradicción y la materializa igualmente |
| `capacidades/ENC/CAPACIDAD.md:50` | el **índice de lo existente**, que a.3 declara «memoria propia de DSP», pasa a ser memoria de ENC |
| `contratos/C4-MATERIALIZACION.md:92,100` | ENC se añade como **tercer equipo permanente** |
| `packs/00-QUE-ES-UN-PACK.md` | sigue diciendo «los **catorce** códigos están reservados» |
| `validadores/comprobar_packs.py:24` | `CODIGOS_KERNEL` lista **quince** códigos — y además nunca se usa (A-17) |

**Consecuencia práctica.** El catálogo instalado no es el catálogo aprobado. Contra la letra
de a.4, `ENC` es una extensión sin prefijo de espacio de nombres que además **altera la
autoridad de una capacidad del kernel** (retira a DSP una de sus cuatro funciones y su
memoria propia) — es decir, un *override* en el sentido de a.4, que exige K0.7 declarado.
Un instalador que aplicara T18 y T23 literalmente debería rechazarla. Además el corpus
queda con **tres recuentos incompatibles del catálogo** (14 en (a) y en `packs/`, 15 en el
índice y en el validador), lo que garantiza que cualquier prueba de conformidad futura
discrepe de alguna fuente.

**Corrección recomendada (no implementada).** No es un defecto que un agente pueda corregir:
es una decisión del Owner entre tres salidas, y sólo la tercera es gratis.

```text
OPCIÓN 1  ENC vuelve a ser DSP/Encuadre. Se conserva el contenido (los métodos, los roles
          y los prompts pasan a DSP) y desaparece la contradicción sin perder trabajo.
OPCIÓN 2  ENC se aprueba como decimoquinta capacidad del catálogo base. Exige modificar
          (a) — a.0, a.3, a.4 y el párrafo de materialización permanente — y actualizar
          packs/00-QUE-ES-UN-PACK.md. (a) deja de estar «intacta».
OPCIÓN 3  ENC se declara `local:ENC` o extensión de pack, con override K0.7 escrito.
```

Sea cual sea, **los tres recuentos deben quedar en uno solo**.

---

#### A-02 · DEFECTO — el único camino de arranque documentado falla

**Evidencia.** `README.md` («Versión corta») y `START_HERE.md` (Ruta A, paso 1) documentan:

```bash
./tooling/new-project.sh mi-web-app pack-web-app,pack-design-led
```

`tooling/new-project.sh:24` exige que cada pack sea un **directorio** de `packs/`. Los packs
vigentes son `web-app`, `mobile-app`, `wear-os`; `pack-web-app` y `pack-mobile-native` están
en `packs/legacy-1.3.0/` (que el script no mira) y `pack-design-led` fue **derogado** por
esta misma iteración (`KERNEL_CHANGELOG.md`: «Deroga: `pack-design-led` como pack»).

Reproducido sobre copia aislada:

```text
$ ./tooling/new-project.sh mi-web-app pack-web-app,pack-design-led
Pack no encontrado: pack-web-app (los packs son directorios)
EXIT=1
```

**Consecuencia práctica.** `README.md` declara que `START_HERE.md` es el documento que hay
que leer «si sólo lees un documento de todo el repositorio», y ese documento manda ejecutar
un comando que aborta, ofreciendo además un pack que este mismo trabajo derogó. Ningún
proyecto nuevo puede arrancarse siguiendo la documentación. Es el fallo más visible para el
primer usuario real y no lo cubre ninguna prueba: los 61 escenarios auditan el corpus, no el
tooling.

**Corrección recomendada.** Actualizar `START_HERE.md` y el bloque «Contenido» y «Versión
corta» de `README.md` a los tres packs vigentes; añadir un escenario de conformidad que
ejecute `new-project.sh` con cada pack instalado y falle si el `EXIT` no es 0.

---

#### A-03 · DEFECTO — `T131` se declara `prueba-superada` con evidencia que no ejecuta lo que el escenario afirma

**Evidencia.** `pruebas/T122-T133-packs.md`, bloque `ads:escenario` de T131:

```yaml
nombre: Lo más restrictivo gana entre dos packs
dado:    ["dos packs instalados que fijan valores distintos para la misma propiedad medible"]
cuando:  ["SIS ejecuta la detección de conflictos"]
entonces:["se aplica el valor más restrictivo y queda registrado cuál ganó y por qué"]
falla_si:["se aplica el menos restrictivo", "el conflicto no queda registrado"]
estado:  prueba-superada
validador: "kernel/operativo/validadores/comprobar_packs.py"
evidencia: "evidencia/T131-T132-salida.txt"
```

Lo que `comprobar_packs.py::t131_precedencia_declarada` hace realmente es **sólo dos cosas**:
que cada valor de `compatible_con` resuelva a un pack existente, y que el campo `precedencia`
no esté vacío. No instala dos packs, no compara propiedades, no ejecuta detección de
conflictos y no puede distinguir «lo más restrictivo» de «lo menos restrictivo». El propio
validador lo delata: imprime un nombre distinto del escenario —«*Todo pack declara su
compatibilidad y su regla de precedencia*»— y esa discrepancia queda archivada tal cual en
`evidencia/T131-T132-salida.txt`.

**Consecuencia práctica.** `REGISTRO.md` establece la regla dura: «`prueba-superada` AUTORIZA
A DECIR: *esto funciona*, y sólo en lo que la prueba cubre». Aquí se autoriza a decir que la
composición de packs resuelve conflictos por restricción, cuando lo único demostrado es que
dos campos de YAML no están vacíos. **Es una prueba estructural presentada como prueba de
comportamiento** — exactamente el modo de fallo que `REGISTRO.md` existe para impedir, y
ocurre dentro del fichero que lo prohíbe. Contamina además el recuento: de las 11 superadas,
al menos una no sostiene su enunciado.

**Corrección recomendada.** Devolver T131 a `contrato-definido` y crear un escenario nuevo
—`validador-estructural`— cuyo enunciado sea el que el validador sí comprueba. La conducta
«lo más restrictivo gana» no es comprobable sin dos packs con propiedades en conflicto y sin
la dirección de monotonía de cada propiedad declarada (ver A-25).

---

### GRAVE

#### A-04 · DEFECTO — `kernel-status.sh` no puede detectar un fork silencioso de los validadores

**Evidencia.** `tooling/kernel-status.sh:6`:

```bash
SUM=$(find kernel -name "*.md" -o -name "*.yaml" | sort | xargs sha256sum | sha256sum | cut -c1-16)
```

Los cuatro ficheros `kernel/operativo/validadores/*.py` quedan fuera del hash.

Reproducido sobre copia aislada:

```text
$ echo "# fork silencioso" >> kernel/operativo/validadores/ads_lint.py
$ ./tooling/kernel-status.sh
estado         : LIMPIO (coincide con el release)      ← no lo ve

$ echo "x" >> kernel/operativo/00-INDICE.md
$ ./tooling/kernel-status.sh
estado         : DIVERGENTE — el kernel ha sido editado localmente.
```

**Consecuencia práctica.** `README.md` («Las tres reglas que sostienen la reutilización»,
regla 1) afirma: «*`kernel-status.sh` detecta la divergencia. Un kernel editado localmente es
un fork silencioso y la reutilización desaparece*». La afirmación es falsa precisamente para
los ficheros que **ejecutan** la conformidad: un proyecto puede relajar `ads_lint.py`,
neutralizar `comprobar_contratos.py` o quitar una comprobación de `comprobar_packs.py` y
seguir reportando LIMPIO indefinidamente. Es la vía más barata para rebajar todos los gates
del sistema a la vez, y es invisible.

**Corrección recomendada.** Incluir `-o -name "*.py"` en el `find`, regenerar
`kernel/.upstream-hash`, y añadir un escenario que compruebe que una edición de un validador
produce `DIVERGENTE`.

---

#### A-05 · DEFECTO — `T134` pasa por coincidencia de nombre de fichero: 119 de 188 documentos están de hecho exentos

**Evidencia.** `comprobar_contratos.py::t134_sin_documentos_para_nadie` decide que un
documento tiene enlace entrante así:

```python
base = os.path.basename(ruta)
entrante = any(base in txt for txt in otros.values())
```

Es una búsqueda de **subcadena del nombre base** en el texto de cualquier otro fichero, no
una resolución de ruta. En el corpus hay 43 nombres base repetidos, que cubren **119 de los
188 ficheros** del ámbito: `composicion.md` ×18, `CAPACIDAD.md` ×15, `PACK.md` ×3,
`00-INDICE.md` ×3, `gates.md` ×3, `especializacion.md` ×3, más 37 nombres duplicados. Una
sola mención de `composicion.md` en cualquier parte satisface a los dieciocho a la vez.

Experimento controlado sobre copia aislada — dos ficheros genuinamente huérfanos, en un
directorio que nadie referencia, sin bloques canónicos:

```text
kernel/operativo/capacidades/DIS/huerfano/composicion.md         → NO detectado
kernel/operativo/capacidades/DIS/huerfano/zzz-nadie-me-enlaza.md → detectado

T134  FALLIDA   · .../zzz-nadie-me-enlaza.md: nadie lo enlaza y nadie cita sus bloques
```

**Consecuencia práctica.** El escenario se llama «Ningún documento del corpus existe para
nadie» y su cabecera lo presenta como la comprobación permanente del modo de fallo (b) de
a.7. Lo que garantiza en realidad es que ningún documento con **nombre único** esté
huérfano. Como la convención de este kernel es precisamente dar el mismo nombre a los
ficheros homólogos de cada capacidad, la comprobación está desactivada justo donde el corpus
crece: cualquier `composicion.md`, `CAPACIDAD.md` o `gates.md` futuro puede quedar muerto
sin que nada lo señale. Verificación independiente por ruta: 78 ficheros del repositorio no
tienen ningún enlace markdown entrante resuelto por ruta (la mayoría son alcanzables por
enlace a directorio o por campo `prompt:`, pero T134 no distingue un caso del otro).

**Corrección recomendada.** Resolver el enlace por **ruta normalizada** —como ya hace
`ads_lint.validar_enlaces`— y contar además como entrante el enlace a un directorio
contenedor y la referencia desde un campo `prompt:`/`metodo:`. Reejecutar y publicar el
resultado, sea cual sea.

---

#### A-06 · CONTRADICCIÓN NORMATIVA — `DIS` y `DOM` arbitran entre sí una colisión de vetos que a.5 reserva al Owner

**Evidencia.** `a-CAPACIDADES-APROBADA.md:435`:

> «**Regla de colisión de vetos:** dos vetos incompatibles **NO se arbitran entre las
> capacidades**. Escalan al Owner con ambas materias y ambas evidencias escritas.
> **Excepción única:** si uno de los dos es **no levantable por regla dura del kernel**
> (G27), ese prevalece».

Los dos contratos de veto implementados declaran lo contrario:

```text
capacidades/DIS/CAPACIDAD.md · veto:degradacion-de-forma · colision:
  «Frente al veto de DOM sobre recuperabilidad, prevalece DOM.»

capacidades/DOM/CAPACIDAD.md · veto:integridad-de-datos · colision:
  «Frente al veto de DIS por degradación de forma, prevalece DOM: la forma se explora de
   otra manera, los datos no se recuperan de otra manera.»
```

El veto de DOM **no** es no levantable: su propio campo `levantamiento` dice «Lo levanta DOM
cuando el plan incorpora la transición o la copia recuperable que faltaba». No cae por tanto
en la excepción única de a.5. Los pares SEG↔DOM, SEG↔DIS, VER↔SEG y VER↔DIS sí están
correctamente resueltos («ambos detienen», o prevalece SEG por G27).

**Consecuencia práctica.** Se ha creado una jerarquía de vetos que (a) prohíbe expresamente,
y se ha hecho en el punto exacto donde el Owner debía decidir. Un choque real entre
integridad de datos y dirección de forma se resolverá en silencio a favor de DOM sin que el
Owner llegue a verlo. T19 no lo detecta: comprueba que los seis campos existan, no que su
contenido respete la regla de colisión.

**Corrección recomendada.** Sustituir ambos campos `colision` por la fórmula de a.5 —«ambos
detienen y escalan al Owner con las dos materias y las dos evidencias»— y añadir a
`comprobar_contratos.py` una prueba que falle si un `ads:veto` declara prevalencia sobre otro
veto que no esté marcado como no levantable por G27.

---

#### A-07 · DEFECTO — la rama `N3` de la escala de novedad es inalcanzable: `DIS/Reconstruccion` nunca se elige

**Evidencia.** `diseno/03-ESCALA-DE-NOVEDAD.md`: «Se responden las seis preguntas **en
orden**. El nivel es el de la **primera** que se responde «sí»».

```text
N4  ¿No existe memoria:vision-artistica, o está vacía?
N3  ¿Existe producto construido y NO existe dirección visual escrita que lo explique?
```

El caso que N3 describe —producto construido sin dirección escrita— **responde «sí» a la
pregunta de N4**, porque si no hay dirección escrita no existe `memoria:vision-artistica`.
Como N4 se evalúa antes y gana la primera afirmativa, el resultado es siempre N4.
`DIS/Reconstruccion` declara en su `disparador` «la escala de novedad devuelve N3», que no
puede ocurrir.

**Consecuencia práctica.** Queda inalcanzable, a través del único procedimiento de decisión
declarado, todo lo siguiente: el método `DIS/Reconstruccion` (171 líneas), la composición
`composicion:dis-reconstruccion`, la prueba T94, y la fila N3 de la tabla «Qué exige cada
nivel». Y el efecto operativo es el opuesto al buscado: un proyecto existente al que hay que
reconstruirle la dirección recibirá `DIS/Fundacion` —«el método más largo del sistema», «sin
techo de sesiones»— en lugar del método cuya regla rectora es **conservar lo valioso**. Es
justo el escenario que `DIS/Reconstruccion` dice representar: «el caso real de la mayoría de
los proyectos que llegan a esta organización, **incluido el que motivó este kernel**». La
única entrada superviviente es la ruta `AUD`, que activa `DIS/Reconstruccion` por `C-DIS` sin
pasar por la escala — pero `00-SISTEMA-DE-EXCELENCIA.md` afirma que «cuál se ejecuta lo
decide la escala de novedad, no el criterio del agente».

**Corrección recomendada.** Hacer disjuntas las dos preguntas. Por ejemplo, condicionar N4 a
la ausencia **de producto construido** («no existe `memoria:vision-artistica` **y** no hay
superficie construida que explicar»), dejando N3 para el brownfield. Añadir un escenario que
recorra la escala con los cinco casos de entrada y falle si algún nivel resulta inalcanzable.

---

#### A-08 · DEFECTO — `N0` y `N1` se saltan gates que el sistema declara obligatorios, y tres documentos dicen tres cosas distintas

**Evidencia.** Tres fuentes sobre la misma verdad:

| fuente | qué dice de N0 |
|---|---|
| `diseno/04-CICLO-DE-CALIDAD.md:93` | `N0  1 · 10 · 11` — se ejecutan tres estaciones. La **8 (`gate:usabilidad`)** y la **9 (`gate:excelencia-visual`)** quedan fuera |
| `diseno/03-ESCALA-DE-NOVEDAD.md`, tabla | N0 · crítica visual: **«no obligatoria»** |
| `diseno/03-ESCALA-DE-NOVEDAD.md`, cierre | «El gate de excelencia visual **se aplica igual**, y el eje `acabado` no se relaja» |
| `capacidades/DIS/CAPACIDAD.md:41` | el gate de la capacidad DIS es `gate:excelencia-visual`, sin excepción por nivel |
| `diseno/02-RUBRICAS.md`, `gate:excelencia-visual` | comprobación `dictamen-existe`: exige dictamen de `DIS/critica-visual`, sin excepción por nivel |
| `capacidades/DIS/roles/critica-visual.md`, `activacion` | «**todo** paquete de DIS antes de cerrar el gate de excelencia visual» |
| `capacidades/DIS/prompts/critica-visual.md` | instruye al crítico sobre qué comprobar «N0 → ninguna», es decir, asume que sí actúa en N0 |

Para `N1`, `04-CICLO` lista `1 · 4 · 5 · 6 · 7 · 9 · 10 · 11 · 13`: **omite la estación 8**,
que es donde se aplica `gate:usabilidad`.

**Consecuencia práctica.** `00-SISTEMA-DE-EXCELENCIA.md` afirma que los dos gates «son
independientes y **ambos son obligatorios**». La tabla de estaciones por nivel los rebaja en
silencio: en N1 desaparece el gate de usabilidad, y en N0 desaparecen los dos. Y como el
mismo documento advierte, «**bajar el nivel es la forma más silenciosa de abaratar el
diseño**»: aquí bajar el nivel no reduce sólo la exploración —que es lo que N0 dice
eliminar— sino también la verificación. Un agente que lea `04-CICLO` cerrará sin dictamen; uno
que lea `03-ESCALA` o el contrato del rol exigirá dictamen; el gate no puede cerrarse sin él.
Las tres lecturas producen resultados distintos sobre el mismo paquete.

**Corrección recomendada.** Decidir cuál es la fuente única —la propuesta natural es que lo
sea `gate:excelencia-visual`, que es lo que un paquete tiene que pasar— y hacer que
`04-CICLO` y la tabla de `03-ESCALA` deriven de ella en lugar de afirmar por su cuenta. Si la
intención real es que N0 no lleve crítica, hay que declarar la excepción **dentro del gate**,
no en una tabla externa.

---

#### A-09 · DEFECTO — el aparato central de (b) —obligaciones, huérfanas y cierre— no tiene ningún portador operativo

**Evidencia.** Recuento sobre `kernel/operativo/` completo:

```text
"obligación_satisfecha" / "obligación_retirada" / "obligación_huérfana"   0 apariciones
"huérfana"                                                                0 apariciones
"avance_material"                                                         0 apariciones
"MAX_RECOMPOSICIONES"                                                     0 apariciones
"esperando-externo"  (uno de los 11 estados de b.2)                       0 apariciones
"b.10"                            sólo en capacidades/APR/{CAPACIDAD,composicion}.md
"b.4"                             sólo en capacidades/DSP/roles/estado.md, como conocimiento
```

No existe `gate:cierre-de-item` ni comprobación equivalente. `gate:despacho-coherente` tiene
seis comprobaciones y ninguna es la de b.10. No hay esquema, plantilla ni artefacto para una
obligación, ni para el informe de cierre que b.10 exige («obligaciones SATISFECHAS: N ·
obligaciones RETIRADAS: M»).

**Consecuencia práctica.** b.3, b.4 P10 y b.10 son el corazón de la sección (b): la distinción
entre *terminar la ejecución* y *producir el resultado*. De ahí salen 14 de las 49 pruebas de
(b) (T52, T53, T63–T69, T33, T46, T66, T64, T65). Ninguna tiene hoy dónde apoyarse en el
kernel operativo: no hay campo donde escribir una obligación, no hay predicado que evaluar,
y no hay gate que impida cerrar un item con una obligación huérfana. La consecuencia exacta
que b.10 nombra —«cancelarlos todos cerraría un item cuyo resultado nunca existió»— no está
impedida por nada de lo construido. `REGISTRO.md` clasifica T26–T74 como `contrato-definido`
«porque requieren runtime», y eso es cierto para la *ejecución*; pero el **vocabulario
canónico** que el runtime necesitará consumir tampoco existe, y eso no requería runtime.

**Corrección recomendada.** Añadir un esquema `obligacion.yaml`, el campo correspondiente en
la ficha de ruta, un `gate:cierre-de-item` con las cinco condiciones de b.10 como
comprobaciones, y la plantilla del informe de cierre con las dos cifras separadas. Es trabajo
de contenido, no de runtime.

---

#### A-10 · DEFECTO — los frenos de a.7 y b.9 no tienen rol, método, gate ni artefacto; la función `Supervisión` de DSP no está materializada

**Evidencia.** a.3 asigna a DSP **cuatro** funciones: Encuadre, Enrutamiento, Estado y
**Supervisión** («detecta estancados, aplica los frenos de a.7, escala»). La materialización:

```text
capacidades/DSP/CAPACIDAD.md   metodos: [DSP/Enrutamiento, DSP/Continua]
                               roles:   [DSP/enrutamiento, DSP/estado]
capacidades/DSP/composicion.md una sola composición, con esos dos roles
```

Encuadre se fue a ENC (A-01) y **Supervisión no está en ninguna parte**. Los frenos aparecen
sólo por referencia y sin condición comprobable:

```text
DSP/metodos/Enrutamiento.md paso 5   «...atender frenos...»
   termina_cuando: "el primero está elegido y el desempate es determinista"   ← no exige
                                                                                haberlos evaluado
DSP/metodos/Enrutamiento.md aprendizaje: «una ruta recompuesta tres veces sin avance material
   dispara el freno y se registra»    ← ningún paso lo cuenta, ningún gate lo comprueba
"ciclo multiparte" (FRENO 2, T07)     0 apariciones en kernel/operativo/
"racha SIS"        (FRENO 3, T08)     sólo en SIS/CAPACIDAD.md y SIS/roles/evolucion.md, en prosa
```

`gate:despacho-coherente` no incluye ninguna comprobación de freno, ni de inanición, ni de
racha.

**Consecuencia práctica.** Los frenos son el mecanismo con el que (a) responde a **los dos
modos de fallo** que justifican todo el rediseño. Tal como está el corpus, un agente que
ejecute `DSP/Enrutamiento` paso a paso cerrará su gate sin haber contado una sola devolución,
un solo ciclo ni una sola racha, y el gate no se lo impedirá. T06, T07, T08 y T41 no tienen
dónde engancharse. Es especialmente serio para el FRENO 3 (racha SIS), porque este mismo
proyecto —construir el kernel— es un caso donde la excepción declarada («no aplica mientras
el objetivo explícito sea construir el propio kernel») deja de aplicar en cuanto empiece
gym-wear.

**Corrección recomendada.** Un rol `DSP/supervision` con su método, contadores persistidos
por par de capacidades y por ruta, y comprobaciones de freno añadidas a
`gate:despacho-coherente`. Alternativamente, si se decide que los frenos son responsabilidad
exclusiva del runtime, declararlo por escrito y mover T06/T07/T08/T41 a una lista explícita
de «pendientes de (g)», que hoy no existe.

---

#### A-11 · DEFECTO — el `encuadre` tiene un vocabulario de estados propio, no reconciliado con b.2, que no puede expresar el estado que dos documentos le exigen

**Evidencia.** `esquemas/encuadre.yaml:58`:

```yaml
estado: {tipo: enum, valores: [en-conversacion, listo-para-dsp, entregado, descartado, aparcado-por-owner]}
```

Y sin embargo:

```text
entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md:127
   «el encuadre queda `esperando-owner`, NO `bloqueado`»
capacidades/ENC/metodos/Escucha.md:157  (campo `bloqueo`)
   «...el encuadre queda esperando-owner, no bloqueado»
```

`esperando-owner` **no está en el enum** y por tanto ningún encuadre puede declararlo.
Además `ENC/CAPACIDAD.md` establece que «un encuadre = un paquete de ENC, con custodia, gate
y checkpoint **normales**», de modo que ese paquete debería moverse por los once estados de
b.2 — donde `aparcado` está explícitamente excluido como estado de paquete: «*`aparcado` no
es un estado de paquete. Es global del item*» (b.2). El enum introduce `aparcado-por-owner`
como estado del artefacto.

**Consecuencia práctica.** Dos máquinas de estados sobre el mismo objeto, y la canónica —la
que el validador comprueba— no puede representar la situación más común de la puerta de
entrada: el Owner que no contesta. Un encuadre en esa situación sólo puede declararse
`en-conversacion`, que es falso, o quedar sin estado válido. Es una regla escrita que el
esquema hace imposible cumplir.

**Corrección recomendada.** Decidir si el estado del encuadre es un estado de paquete de b.2
—y entonces el enum sobra— o un sub-estado del artefacto, y en ese caso declarar la
correspondencia con b.2 explícitamente y añadir el valor que falta.

---

#### A-12 · DEFECTO — `START_HERE.md`, `README.md` y `KERNEL.md` no están reconciliados con el trabajo: tres versiones distintas del mismo artefacto

**Evidencia.**

```text
kernel/VERSION                  2.0.0-alpha.1
kernel/KERNEL.md línea 4        «Versión del kernel: 1.3.0»
README.md línea 43              «KERNEL.md   constitución reusable  (1.0.0)»
```

El bloque «Contenido» de `README.md` sigue describiendo el árbol de la versión 1.3.0: lista
`packs/pack-mobile-native.md`, `packs/pack-web-app.md` y `packs/pack-design-led.md` en la raíz
de `packs/` (están en `legacy-1.3.0/`, y el tercero derogado), y `PROJECT.md`, `PROFILE.md`,
`AGENTS.md` y `docs/UPSTREAM.md`, que no existen en este repositorio. `START_HERE.md` no
menciona `kernel/operativo/`, ni `ENC`, ni los tres packs nuevos, y su lista de «**cuatro**
preguntas» contiene **cinco** preguntas numeradas.

**Consecuencia práctica.** Los tres documentos de entrada del repositorio describen un
sistema que ya no es el que contiene. Un agente o un Owner que empiece por donde el propio
`README` le dice que empiece llega a la versión anterior del kernel. Y como `ads_lint` sólo
recorre `kernel/operativo/` y `packs/`, ninguna de estas incoherencias es detectable por los
validadores instalados.

**Corrección recomendada.** Reconciliar los tres, fijar una sola versión, y ampliar el ámbito
por defecto de `ads_lint` a la raíz del repositorio para enlaces y vocabulario.

---

#### A-13 · DEFECTO — `gate:usabilidad` declara aplicarse a las capas de `CON`, y ninguna ficha, rol o método de `CON` lo vincula

**Evidencia.** `diseno/02-RUBRICAS.md`:

```yaml
id: gate:usabilidad
aplica_a: "toda capa de DIS o de CON que produce o modifica una superficie usable"
```

Todas las vinculaciones existentes son de DIS: `DIS/roles/{investigacion-ux, diseno-interaccion,
prototipado, validacion-de-uso}`, `DIS/metodos/ValidacionDeUso` y `packs/mobile-app/roles/
interaccion-tactil.md` (que es `mob:DIS/...`, capacidad DIS). El gate de `CON` es
`gate:implementacion-completa`, cuyas siete comprobaciones no incluyen ningún eje de
usabilidad, y ningún rol de CON —ni del kernel (`CON/implementacion`, `CON/experimental`) ni
de pack (`web:CON/estados-de-red`, `mob:CON/ciclo-de-vida`, `wear:CON/energia-y-estados`)—
declara `gate: gate:usabilidad`.

**Consecuencia práctica.** La mitad del `aplica_a` de un gate obligatorio no tiene ningún
mecanismo que lo haga ocurrir. Una capa de construcción que modifica una superficie usable
—el caso normal— cierra por `gate:implementacion-completa` sin que los seis ejes de
usabilidad se evalúen sobre lo construido. Es una regla que nadie puede incumplir porque
nadie puede cumplirla.

**Corrección recomendada.** O bien acotar `aplica_a` a DIS y declarar explícitamente que
sobre lo construido la usabilidad se comprueba en `VER`, o bien añadir la comprobación
correspondiente a `gate:implementacion-completa`. Lo que no puede quedarse es el `aplica_a`
actual sin portador.

---

#### A-14 · DEFECTO — la crítica de encuadre obligatoria puede evaporarse, porque el gate se condiciona al grado **final** de incertidumbre

**Evidencia.** La crítica se activa por el grado inicial:

```text
entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md
   ALTA → «Crítica independiente OBLIGATORIA antes de entregar»
capacidades/ENC/composicion.md · composicion:enc-alta-incertidumbre · reduccion:
   «Si tras conversar la incertidumbre baja a media en todos los ejes ... la crítica sigue
    siendo obligatoria: ya se emitió el trabajo y su dictamen forma parte del gate.»
```

Pero el gate se evalúa sobre el valor declarado en el artefacto final:

```text
capacidades/ENC/CAPACIDAD.md:134 · gate:encuadre-listo · critica-cuando-corresponde
   comprueba: "si incertidumbre.grado es alta o nivel_owner es obligatorio, existe dictamen
               de ENC/critica-de-encuadre"
```

El escenario de referencia recorre exactamente ese camino: `05-ESCENARIOS.md`, Escenario A,
paso 5 → `GRADO GLOBAL = ALTA → PROHIBIDO FORMULAR. Se conversa.` Tras conversar, el grado
baja. Si además `nivel_owner` no es obligatorio, la condición del gate es **falsa** y el
encuadre pasa sin dictamen, pese a que la composición lo declaraba obligatorio e
irretirable.

**Consecuencia práctica.** La única salvaguarda contra la interpretación no contrastada —«el
crítico que impide que el interlocutor entregue su propia lectura como hecho»— se apaga sola
justo cuando el método ha funcionado. El principio que C4 declara («*Un rol independiente
nunca se retira para ahorrar una lectura*») queda sin efecto porque el gate no pregunta por
el rol materializado, sino por un valor que el propio trabajo ha cambiado.

**Corrección recomendada.** Condicionar la comprobación a que **la composición haya
materializado** `ENC/critica-de-encuadre` —dato que C4 paso 7 obliga a escribir— y no al
grado final. Alternativamente, persistir `incertidumbre.grado_inicial` además del vigente.

---

### MEDIO

#### A-15 · DEFECTO — `ENC/Critica` existe, se usa y se prueba, pero su capacidad no lo declara

`capacidades/ENC/CAPACIDAD.md:54` declara `metodos: [ENC/Escucha, ENC/Anclaje, ENC/Maduracion,
ENC/Orden, ENC/Formulacion]` — **cinco**. En disco hay **seis**, y el sexto, `ENC/Critica`, es
el método que ejecuta `ENC/critica-de-encuadre` (`roles/critica-de-encuadre.md:45`), lo invoca
`ENC/Escucha` paso 97 y lo prueba T85. `entrada/00-INDICE.md` afirma «tres roles, **seis**
métodos». Recorrido mecánico de los 34 métodos del corpus: es el **único** caso.
`00-INDICE.md` designa `capacidades/<COD>/CAPACIDAD.md` como fuente única de la ficha de una
capacidad, de modo que un agente que la lea no encontrará nunca el método de la crítica.
`comprobar_contratos.py::t90` no lo detecta porque valida la coherencia capacidad↔rol, no
capacidad↔método. **Corrección:** añadir `ENC/Critica` a `metodos` y extender t90 a los
métodos.

#### A-16 · DEFECTO — el ejemplo canónico de C4 invoca una composición que no existe

`contratos/C4-MATERIALIZACION.md:126` cita `composicion:dis-fundacion` como la composición
elegida por el algoritmo. Ese identificador no existe en ninguna otra parte del repositorio:
la composición real se llama `composicion:dis-proyecto-nuevo`. El orden de recorrido del
ejemplo (extension-de-patron → caso-nuevo → fundacion) tampoco corresponde al orden real de
`DIS/composicion.md`, que empieza por `dis-bug-visual`. `ads_lint` no lo detecta porque el
ejemplo vive en un bloque ```text, no en un bloque canónico. **Consecuencia:** el único
ejemplo trabajado del algoritmo de materialización —el paso 2 del cual declara que «el orden
es parte del contrato, no casual»— no se puede seguir contra el corpus real. **Corrección:**
corregir el identificador y el orden, o generar el ejemplo desde el corpus.

#### A-17 · DEFECTO — `comprobar_packs.py` declara comprobaciones que no ejecuta, y contiene una rama inalcanzable

Tres cosas, en el mismo fichero:

```text
1  CODIGOS_KERNEL (línea 24) se declara y NUNCA se usa. Es la lista con la que se
   comprobaría la colisión de identificador de T18. Código muerto.
2  La comprobación 4 —«Ningún gate de pack repite el identificador de uno del kernel»— es
   INALCANZABLE: `gates` es un dict indexado por id, de modo que `otro_id == gid` siempre
   devuelve la MISMA entrada, y la condición «esa entrada está bajo packs/» es falsa por
   construcción dentro de la rama que ya excluyó los de packs. Nunca puede disparar.
3  El docstring afirma comprobar «que los gates de pack SUMEN en vez de sustituir». No hay
   ninguna comprobación de eso. T132 lo declara en su `entonces` («ningún gate de pack
   sustituye a uno del kernel: se suma») y en su `falla_si` («un gate de pack que rebaja una
   comprobación del kernel»), y está en estado `prueba-superada`.
```

Además `REGISTRO.md:43` afirma que «`ads_lint` comprueba **prefijo**» para T18; el patrón de
`esquemas/capacidad.yaml` es `^([a-z0-9-]+:)?[A-Z]{3}$`, con el prefijo **opcional**: quien lo
comprueba es `comprobar_packs.py::t132`, y sólo para artefactos bajo `packs/`.
**Consecuencia:** T132 declara superadas tres afirmaciones y el validador sostiene dos.
**Corrección:** eliminar el código muerto, sustituir la comprobación 4 por una que compare
el conjunto de ids de kernel contra el de packs, e implementar o retirar la afirmación sobre
gates que suman.

#### A-18 · DEFECTO — `T86` sólo verifica el veto, no la decisión

`comprobar_contratos.py::t86_autoridad_subconjunto` compara únicamente `autoridad.veta` del
rol contra la de su capacidad. C1 declara tres reglas: «Un rol NO PUEDE **decidir** lo que su
capacidad escala. Un rol NO PUEDE **vetar** lo que su capacidad no veta. La autoridad de un
rol es SIEMPRE un **subconjunto** de la de su capacidad». Sólo la segunda está implementada,
y el escenario se llama «La autoridad de un rol no excede la de su capacidad», sin matices.
Ejemplo concreto de lo que hoy pasaría sin ser visto: `DIS/critica-visual` declara
`decide: ["el veredicto del dictamen: conforme o devuelto", "el nivel de cada eje", "si dos
direcciones son variaciones de la misma"]`, y ninguno de los tres figura en el `decide_sola`
de `DIS`. Puede ser correcto —la suma de los roles puede ser menor que la capacidad, no
mayor— pero **nadie lo comprueba**. **Corrección:** o implementar la contención de `decide`,
o renombrar T86 a lo que realmente verifica.

#### A-19 · DEFECTO — la incertidumbre `ALTA` tiene dos consecuencias incompatibles en el mismo bloque

`entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md`, sección 1:

```text
ALTA    PROHIBIDO formular. Se conversa hasta bajar a media, o la expresión va al vivero.
        Crítica independiente OBLIGATORIA antes de entregar.
```

Si formular está prohibido y la salida es *media* o *vivero*, no existe la entrega de un
encuadre con grado `alta`; y sin embargo se exige crítica «antes de entregar» un encuadre
alta. La rama «`incertidumbre.grado` es alta» de `gate:encuadre-listo` es, en consecuencia,
inalcanzable o contradictoria. La tabla de confirmación del mismo documento añade una tercera
lectura: «incertidumbre global **alta** tras haber conversado → **sí** [se pide
confirmación]», que es un desenlace distinto de los dos anteriores. **Corrección:** declarar
un único desenlace para `alta` persistente y hacer que el gate y la tabla deriven de él.

#### A-20 · DEFECTO — `gate:excelencia-visual` exige el eje `fidelidad` en un momento en que no puede existir

El eje `fidelidad` de `rubrica:excelencia-visual` tiene como evidencia «comparación
intención/resultado del procedimiento de fidelidad», que sólo existe después de construir. El
gate exige que «los **nueve** ejes tengan nivel y evidencia». Pero `04-CICLO-DE-CALIDAD.md`
sitúa la validación visual en la **estación 9**, antes de la entrega a construcción
(estación 10) y de la revisión de fidelidad (estación 11); y `DIS/Fundacion` —cuyo resultado
es una dirección visual, no código— declara `gate: gate:excelencia-visual`. Un paquete de
fundación no puede cerrar su gate. El prompt del crítico confirma que el gate también se
evalúa después («fidelidad → vuelve a CONSTRUCCIÓN»), es decir, dos evaluaciones distintas
del mismo gate sin que ninguna esté declarada. **Corrección:** declarar explícitamente las
dos pasadas del gate y qué ejes aplican en cada una, o extraer `fidelidad` a un gate propio.

#### A-21 · DEFECTO — dos de los nueve ejes pueden rechazar sin destino de retorno declarado

`04-CICLO-DE-CALIDAD.md` (tabla de retornos) y `prompts/critica-visual.md` declaran el
retorno de siete ejes: `personalidad · actualidad · alma` → exploración; `acabado · sistema ·
respuesta` → prototipo; `fidelidad` → construcción. Los ejes **`intencion`** y **`jerarquia`**
no aparecen en ninguna de las dos listas. Un veredicto `devuelto` por cualquiera de ellos deja
al paquete sin destino escrito, que es justo lo que C5 clasifica como devolución inválida
(«QUÉ LA CERRARÍA»). **Corrección:** completar las dos listas con los nueve ejes.

#### A-22 · DEFECTO — un handoff mal tipado y el handoff más transitado sin declarar

`circuitos/handoffs-generales.md:174`:

```yaml
id: handoff:cierre-a-apr
de: USO
cuando: "un item cierra con learning_candidate != none, o ha habido un incidente"
```

El disparador es el **cierre del item** (b.10), no la capa de USO; y `USO` es condicional
(`C-USO`), de modo que en `DEF`, `DEU`, `SIS` o `INV` sin fuente de uso real el handoff
declarado no tiene emisor. Además **no existe `handoff:con-a-ver`**, pese a que `CON → VER`
aparece en las diez rutas de b.16 y `00-CIRCUITOS.md` le dedica una fila explícita («CON → VER
· diferencias declaradas antes de la revisión · infiel: vuelve a CON con la comparación»). C5
permite que un par no tenga handoff declarado, pero `00-CIRCUITOS.md` dice que los declarados
son «aquellos donde hace falta precisión extra», y este es el tránsito más frecuente del
sistema. **Corrección:** retipar el emisor de `cierre-a-apr` y declarar `handoff:con-a-ver`.

#### A-23 · CONTRADICCIÓN NORMATIVA — `DSP/estado` **decide** una cancelación

`capacidades/DSP/roles/estado.md`, `autoridad.decide`: «convertir una espera no viable en
bloqueo, recomposición o **cancelación justificada**». Según C1, `decide` significa «lo
ejecuta y queda hecho. No pide permiso ni avisa antes». b.7 es explícito: «**DSP NUNCA posee
por sí mismo la AUTORIDAD SEMÁNTICA** para decidirla» (`b-RECORRIDO-APROBADA.md:369`). El
texto procede de b.8, que encarga a DSP «convertir la situación» en una de tres, pero
convertir no es poseer la autoridad. **Consecuencia:** un agente que ejecute el rol al pie de
la letra cancelará trabajo sin autoridad semántica y sin registrar ordenante distinto de sí
mismo, que es lo que T54 prohíbe. **Corrección:** mover ese ítem de `decide` a `propone` para
la variante de cancelación, dejando bloqueo y recomposición en `decide`.

#### A-24 · DEFECTO — recuentos incorrectos en documentos normativos y en la nota de versión

Todos verificados contra el corpus:

| dónde | dice | es |
|---|---|---|
| `KERNEL_CHANGELOG.md` 2.0.0-alpha.1 | «diecisiete esquemas» | **16** ficheros en `esquemas/` |
| `kernel/operativo/00-INDICE.md:61` | «los diecisiete tipos» | **16** |
| `KERNEL_CHANGELOG.md` | «35 métodos ejecutables» | **34** bloques `ads:metodo` |
| `KERNEL_CHANGELOG.md` · `C1:38,40` | «los 28 campos» / «veintiocho campos» | **29** obligatorios en `rol.yaml`, y la propia tabla de C1 tiene **29** filas |
| `C3-METODO-EJECUTABLE.md:8,10` | «los diecisiete campos del esquema `metodo.yaml`» | **19** obligatorios (la tabla de 17 incluye `modo`, que es subcampo de `pasos`, y omite `id`, `nombre` y `capacidad`) |
| `esquemas/capacidad.yaml` descripción | «los doce campos» | **19** obligatorios |
| `entrada/02-CIRCUITO.md:5` | «Trece estaciones» | **14** cajas en su propio diagrama, y `entrada/00-INDICE.md` dice «catorce» |
| `DIS/CAPACIDAD.md:139` | «doce matrices de composición» | **10** bloques en `DIS/composicion.md` |
| `entrada/05-ESCENARIOS.md:6` | «son las pruebas T75 a **T84**» | contiene **T75–T80**; T81–T85 están en otro fichero |
| `C4-MATERIALIZACION.md:92` | «Los **dos** equipos que no se retiran nunca» | enumera **tres** (DSP, SIS, ENC) |
| `diseno/00-SISTEMA-DE-EXCELENCIA.md` | «Cada uno [de los **diez** motivos] tiene su eje en la rúbrica» | la rúbrica tiene **9** ejes; `PLANA` y `SIN JERARQUÍA` mapean al mismo (`jerarquia`), y `acabado` no corresponde a ningún motivo |
| `pruebas/REGISTRO.md:43` | «la colisión de autoridad se comprueba en `pruebas/T78-*`» | **no existe** ese fichero; T78 es un escenario de `entrada/05-ESCENARIOS.md` sobre órdenes con base caducada, sin relación con colisión de autoridad |

**Consecuencia práctica.** Ninguno rompe la ejecución, pero en conjunto invalidan la lectura
del corpus como fuente fiable: son exactamente las «cifras duplicadas o desactualizadas» que
la regla de fuente única de `00-INDICE.md` existe para impedir, y aparecen en la nota de
versión que resume el trabajo, en cuatro de los cinco contratos y en el registro de pruebas.
**Corrección:** derivar todo recuento del corpus (un validador que compare cada cifra
declarada contra el recuento real es factible para la mayoría), o eliminarlos del texto.

#### A-25 · DEFECTO — la precedencia P1 de packs no es computable como está escrita

`packs/COMPOSICION.md`: «**P1 LO MÁS RESTRICTIVO GANA**, cuando ambos hablan de la misma
propiedad medible. Un tamaño mínimo de objetivo táctil de 48 y otro de 44 → gana 48. Un
contraste mínimo de 4.5 y otro de 7 → gana 7». Los dos ejemplos son propiedades donde
*restrictivo = mayor*. La regla no declara en ningún sitio **la dirección de monotonía de
cada propiedad**, de modo que para un presupuesto de tamaño de descarga o un tiempo máximo de
respuesta —donde restrictivo = *menor*— no hay forma mecánica de aplicarla. Tampoco existe un
registro de «propiedades medibles» compartido entre packs contra el que decidir si dos valores
son «la misma propiedad» (P1) o «no comparables» (P2). **Consecuencia:** `SIS/Conformidad`
tiene un paso declarado —«2 MISMA PROPIEDAD → se aplica P1»— que no puede ejecutar sin
criterio, y T131 declara superado su resultado (A-03). **Corrección:** exigir que toda
propiedad medible de un pack declare `direccion: minimo | maximo` y publicarlas en un
registro común.

#### A-26 · DEFECTO — `04-CICLO` afirma una cobertura de gates que no existe para la estación 12

«Cada una de esas seis omisiones tiene su comprobación en un gate. Ninguna depende de que
alguien se acuerde». La estación 12 es «PRUEBA EN DISPOSITIVO REAL». En el kernel no hay
ningún gate que la exija: las únicas comprobaciones de hardware real son
`gate:mob-dispositivo-real` y los tres gates de `wear-os`, ambos de pack. Un proyecto sin pack
—o con `web-app`— puede saltarse la estación 12 sin que nada la reclame, y el documento afirma
lo contrario. **Corrección:** matizar la afirmación, o añadir al kernel una comprobación
condicionada a que el pack instalado declare matriz de dispositivos.

---

### MENOR

**A-27 · DEUDA — la exención de vocabulario es por fichero completo.** `ads_lint` salta el
fichero entero cuando encuentra `<!-- ads-lint: permitir-vocabulario-prohibido -->`. Hay 19
ficheros exentos de 188, y son precisamente los normativos: los **seis** documentos de
`diseno/`, **cuatro de los cinco** contratos (C1, C3, C4, C5), `esquemas/00-LENGUAJE.md`,
`entrada/02-CIRCUITO.md`, `entrada/04-…`, `entrada/05-…`, `circuitos/00-CIRCUITOS.md`,
`packs/COMPOSICION.md`, `packs/00-QUE-ES-UN-PACK.md` y `pruebas/REGISTRO.md`. **Comprobado:
hoy ninguno abusa de la exención** — el único que contiene vocabulario prohibido es
`00-LENGUAJE.md`, y lo contiene porque es donde se enumera la lista. La deuda es que nada
impide que mañana lo hagan, en los documentos donde más importa (b.16: «cada una con su
CONDICIÓN DE ACTIVACIÓN escrita y COMPROBABLE. Prohibido “si aplica”»). **Corrección:**
exención por línea (`<!-- ads-lint-ignore-next-line -->`) en vez de por fichero.

**A-28 · DEUDA — el ámbito de `ads_lint` deja fuera media documentación.** Por defecto recorre
`kernel/operativo` y `packs`. `README.md`, `START_HERE.md`, `kernel/KERNEL.md`,
`kernel/BOOTSTRAP_PROMPT.md`, las plantillas y todo `docs/` quedan sin comprobación de enlaces
ni de vocabulario. Es la razón por la que A-12 pasó desapercibido. Comprobación independiente
de enlaces sobre los 241 ficheros del repositorio: **10 enlaces rotos, los 10 en documentos
históricos** (`a-EQUIPOS-v2-RECHAZADA.md`, `a-EQUIPOS-v3-SUPERADA.md`,
`a-CAPACIDADES-APROBADA.md`) y todos hacia rutas de ejemplo (`../items/FEA-021/...`) que
nunca pretendieron existir. **No hay ningún enlace roto en el corpus construido.**

**A-29 · MENOR — el pack `wear-os` se identifica por una plataforma concreta.**
`packs/00-QUE-ES-UN-PACK.md` establece que «NO VA una tecnología concreta: eso pertenece al
PROFILE». El contenido del pack es correctamente neutral (`nombre: Reloj`, sin marcas — T92 lo
confirma sobre todo el corpus), pero su identificador nombra el sistema operativo de un
fabricante. Un proyecto de reloj sobre otra plataforma tendría que instalar un pack llamado
`wear-os`. **Corrección:** renombrar a `reloj` o `wearable`, o declarar por qué la excepción
es deliberada.

**A-30 · DEUDA — profundidad muy asimétrica entre capacidades.** `DIS` tiene 11 roles y 6
métodos; las catorce restantes tienen entre 1 y 3 roles y entre 1 y 2 métodos (APR, INV, PLT,
USO: **un** rol y **un** método cada una). `DIS/CAPACIDAD.md` lo asume («sirve de patrón de
calidad para las demás: no de plantilla mecánica»), y la afirmación auditada —«equipos y
métodos de las demás capacidades»— es literalmente cierta. Se registra para que no se lea
como paridad: el paso 5 entrega la **forma** completa de las catorce, no su profundidad.

**A-31 · MENOR — el umbral de anclaje cambia de capa.** b.13 dice «*Umbral y margen son
parámetros del **runtime***»; `entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` dice «Ambos son
parámetros del **PROFILE**, no reglas del kernel». Además los pesos de puntuación
(+0.40/+0.25/+0.15/+0.10/+0.10/−0.30) sí quedan fijados en el kernel, sin declararse como tales.

---

## 7 · Afirmaciones que NO he podido verificar

```text
· Que las 50 pruebas en estado `contrato-definido` sean correctas COMO CONTRATOS. He
  comprobado que existen, que su bloque es conforme y que su estado declarado es honesto.
  No he podido comprobar que, ejecutadas, detectarían lo que dicen detectar: 39 exigen un
  proyecto real, hardware físico o juicio humano, y 4 exigen el runtime.

· Todo lo que depende del runtime: T01–T24 y T26–T74. El propio README lo declara
  («runtime y dispatcher: no existen»), y esta auditoría lo confirma: no hay ejecutable de
  despacho en el repositorio. Su clasificación como `contrato-definido` es honesta.

· La CALIDAD PROFESIONAL del contenido de diseño —si las rúbricas discriminan de verdad
  entre un producto con carácter y uno sin él— exige aplicarlas a una interfaz real. Sólo he
  podido auditar su estructura, su completitud y su coherencia interna.

· Si los 35 prompts operativos producen el comportamiento que describen al cargarse en un
  agente. He verificado que existen (T88), que los 41 roles apuntan a uno que existe, y que
  los 35 enlazan su contrato en cabecera. He auditado a fondo UNO (DIS/critica-visual)
  contra su contrato, y de ahí salieron A-08 y A-21. Los otros 34 no han recibido ese nivel
  de contraste: es el muestreo más débil de esta auditoría.

· Si `composicion:*` recorridas en orden por el algoritmo de C4 cubren todos los casos de
  trabajo posibles de cada capacidad. He comprobado que las 38 son estructuralmente válidas
  y que ninguna combina roles que un contrato declara independientes (T87/T135, reejecutadas).
  No he construido el árbol de decisión completo de las quince capacidades.

· El contenido de `kernel/KERNEL.md` 1.3.0 (1557 líneas). Sólo he auditado su cabecera y su
  relación de convivencia con el corpus nuevo (A-12). Las reglas G0x/K0x que (a) declara
  derogadas, sustituidas o ajustadas no se han recorrido una por una.
```

## 8 · Límites de la auditoría

```text
LIMITACIÓN 1  PASADA CIEGA. Este informe se escribe ANTES de leer REVISION-ADVERSARIAL.md,
              DECISIONES-Y-CONTRADICCIONES.md y CHECKPOINT-OPERATIVO.md. Es posible que
              alguno de los hallazgos de arriba ya esté registrado allí como decisión
              consciente y no como defecto. La sección 2 de este documento, que se añade
              después, resuelve cuáles.

LIMITACIÓN 2  UN SOLO AUDITOR, UN SOLO MUESTREO. Sin subagentes: la responsabilidad del
              muestreo es única y trazable, pero la cobertura profunda se concentró donde
              la afirmación auditada es más fuerte (Diseño, entrada, packs, validadores,
              contratos). ARQ, PRD, VER, ENT, INV, SEG, PLT, DOM y SIS se auditaron a
              nivel de ficha, autoridad, gate y grafo, no leyendo sus métodos y prompts
              íntegros.

LIMITACIÓN 3  SIN EJECUCIÓN REAL. Nada de este corpus se ha aplicado a un proyecto. Los
              defectos que sólo aparecen al usarlo —un método que se atasca, un gate que
              en la práctica nadie puede cerrar, un prompt que produce otra cosa— son
              indetectables desde aquí por construcción.

LIMITACIÓN 4  NO SE HA AUDITADO (g). Toda la disposición física del estado, la atomicidad
              multiarchivo, el event log y la recuperación pertenecen a una sección que no
              existe. T25 sigue legítimamente abierta.

LIMITACIÓN 5  LOS EXPERIMENTOS DE VALIDADOR se ejecutaron sobre COPIAS AISLADAS del
              repositorio en directorio temporal. El árbol de trabajo auditado no se ha
              modificado en ningún momento: `git status` está limpio salvo por este mismo
              informe.
```

## 9 · Balance

Lo que la afirmación auditada sostiene **y resiste el examen**:

```text
· 300 bloques canónicos conformes a 16 esquemas, con 0 errores y 0 avisos, reproducible
· 15 fichas de capacidad completas, 41 roles con los 29 campos, 34 métodos con condición
  de salida por paso y prueba de reanudación, 38 composiciones, 28 gates, 17 handoffs
· el sistema de excelencia de Diseño es real y no es decorativo: dos gates independientes,
  dos rúbricas con niveles descritos en palabras, crítico independiente con contrato de
  independencia verificado sobre todo el corpus, y un procedimiento de fidelidad cuya
  cláusula central —la deuda se acuerda ANTES, no al ser descubierta— sostiene el resto
· el circuito de entrada conserva la expresión literal del Owner, separa interpretación de
  hecho, y declara que la mayoría de las expresiones NO producen item
· los tres packs amplían sin rebajar: no reclaman autoridad del kernel, usan prefijo, y
  wear-os está construido explícitamente contra el antipatrón «un reloj es un móvil pequeño»
· el REGISTRO de pruebas es honesto en su forma: declara 50 contratos y 11 superadas, no
  las presenta como sistema probado, y el generado es determinista
· ningún enlace roto en el corpus construido
```

Lo que **no** resiste el examen, en una frase: el corpus está construido con seriedad, pero
**el catálogo instalado no es el catálogo aprobado (A-01)**, **el único camino de arranque
documentado no funciona (A-02)**, **dos de las once pruebas superadas no comprueban lo que
su enunciado afirma (A-03, A-05)**, **el aparato central de (b) —obligaciones y cierre— y los
frenos de a.7 no tienen portador operativo (A-09, A-10)**, y **el mecanismo que debía impedir
un fork silencioso no ve los ficheros que ejecutan la conformidad (A-04)**.

Ninguno de esos seis es un problema de redacción. Cinco son corregibles sin decidir nada; el
primero es del Owner.

---
---

# SECCIÓN 2 — Contraste con la revisión anterior

> Añadida **después** de publicar la sección 1 y sólo entonces leer
> [`REVISION-ADVERSARIAL.md`](REVISION-ADVERSARIAL.md),
> [`DECISIONES-Y-CONTRADICCIONES.md`](DECISIONES-Y-CONTRADICCIONES.md) y
> [`CHECKPOINT-OPERATIVO.md`](CHECKPOINT-OPERATIVO.md). Nada de la sección 1 se ha
> modificado a la luz de estas lecturas: los hallazgos quedan como se formularon a ciegas,
> y lo que cambia se registra aquí.

## 2.0 · Lo primero que hay que decir

`REVISION-ADVERSARIAL.md` **declara por escrito que la revisión independiente no llegó a
ejecutarse**: el agente revisor terminó por un límite de gasto y la revisión la hizo quien
escribió el corpus. Lo llama «la limitación más importante de esta entrega» y lo repite en
el checkpoint. Eso es honesto y es correcto, y significa que esta auditoría ocupa
exactamente el hueco que aquella dejó abierto. **La comparación que sigue no es entre dos
revisiones equivalentes**: es entre una autorrevisión declarada como tal y la primera
lectura externa.

## 2.1 · Hallazgos coincidentes

| mío | suyo | comentario |
|---|---|---|
| **A-01** ENC como capacidad no autorizada | **C1** y **O1** de `DECISIONES` | Coincidimos en el núcleo y en el diagnóstico —trabajo conversacional es trabajo de contenido, y (a) dice que DSP no lo tiene—, y también en que el contenido no depende de la decisión: mover `capacidades/ENC/` bajo `DSP/` no reescribe un rol. **Mi hallazgo es más ancho**: ver 2.3-S5 |
| **A-30** profundidad asimétrica | defecto 5 «equipos genéricos», resuelto en verde | Coincidimos en que ninguna capacidad comparte método y en que cada una tiene conocimientos y antipatrones propios. Yo lo registro además como deuda de **profundidad**, no de forma |
| **A-27** exención de vocabulario | defecto 1, «0 apariciones fuera de las exenciones» | Coincide el hecho —hoy nadie abusa de la exención— y lo he verificado por mi cuenta. Discrepo en la cifra: ver 2.3-S1 |
| tono general del `REGISTRO` | «Lo que esta revisión NO puede afirmar» | Coincidencia completa: el corpus es coherente consigo mismo y no está probado. Ambos lo decimos con las mismas palabras |
| **A-28** enlaces | H2 «siete documentos que existían para nadie» | Confirmo que el problema que H2 describe fue real y que la corrección funcionó **para esos siete**. Lo que no funciona es la prueba que instalaron para que no vuelva: A-05 |

También coincide, aunque por caminos distintos, la conclusión de **C2** de `DECISIONES`: el
juicio de excelencia no está escondido dentro del gate, sino materializado en
`DIS/critica-visual`. Ése es el diseño correcto y lo confirmo. Lo que la revisión anterior
no siguió es si ese diseño se sostiene a lo largo de los tres documentos que lo describen
—no se sostiene: A-08, A-20 y A-21.

## 2.2 · Hallazgos que la revisión anterior no detectó

De los 31 de la sección 1, **la revisión anterior registró uno** (A-01, como C1, y con
alcance menor). Los otros treinta son nuevos. Los que más importan, por qué se le
escaparon:

```text
A-02  el comando de arranque documentado falla
      → NADIE EJECUTÓ EL TOOLING. Los doce defectos buscados son propiedades del corpus;
        ninguno pregunta «¿funciona lo que la portada manda escribir?». Basta un
        `new-project.sh` sobre una copia para verlo.

A-03  T131 declarada superada sin comprobar lo que afirma
A-17  comprobar_packs declara comprobaciones que no ejecuta y tiene una rama muerta
      → SE LEYÓ LA SALIDA DEL VALIDADOR, NO SU CÓDIGO. La salida dice SUPERADA y el
        escenario dice prueba-superada; la discrepancia sólo aparece leyendo la función.
        Es el punto ciego característico de autorrevisarse: se confía en el instrumento
        que uno mismo escribió.

A-05  T134 se derrota con una colisión de nombre de fichero
      → MISMO PUNTO CIEGO, y más grave: T134 es la prueba que ESTA MISMA revisión instaló
        como remedio permanente de su hallazgo H2, y la declara «permanente: ningún
        documento del corpus puede quedarse sin entrada». Con 43 nombres base repetidos
        que cubren 119 de 188 ficheros, la afirmación no se sostiene.

A-04  kernel-status.sh no ve los .py
      → EL TOOLING NO ENTRÓ EN EL ALCANCE, otra vez. Y es el fichero que sostiene la
        primera de «las tres reglas que sostienen la reutilización» del README.

A-07  la rama N3 de la escala de novedad es inalcanzable
A-08  N0 y N1 se saltan gates obligatorios, con tres documentos discrepando
A-19  la incertidumbre ALTA tiene dos consecuencias incompatibles
A-20  el gate visual exige un eje que en la estación 9 no puede existir
A-21  dos de los nueve ejes rechazan sin destino declarado
      → NINGUNO DE LOS DOCE DEFECTOS BUSCADOS ERA «RAMA INALCANZABLE» NI «CONDICIONES QUE
        SE SOLAPAN». La lista de doce está orientada a lo que un documento DICE, no a
        recorrer sus bifurcaciones. Estos cinco sólo aparecen simulando entradas.

A-09  obligaciones, huérfanas y cierre sin portador operativo
A-10  los frenos de a.7 y b.9 sin rol, método ni gate; Supervisión de DSP sin materializar
      → CRITERIO DE COMPLETITUD BASADO EN INVENTARIO. El checkpoint cuenta fichas, roles,
        métodos y handoffs, y todos están. Lo que no se hizo fue el recorrido inverso:
        tomar cada mecanismo de (a) y (b) y preguntar QUIÉN lo ejecuta en el corpus. Es
        donde aparece que el aparato central de (b) no tiene dónde escribirse.

A-06  DIS y DOM se arbitran un veto que a.5 reserva al Owner
      → T19 comprueba que los seis campos EXISTEN, no qué dicen. Y «contradicciones con
        (a)» estaba en el encargo, pero se buscó a nivel de arquitectura, no dentro del
        texto de un campo.

A-11  el encuadre no puede declarar `esperando-owner`
A-13  gate:usabilidad se declara aplicable a CON y nada lo vincula
A-15  ENC/Critica no está en la ficha de su capacidad
A-16  C4 invoca composicion:dis-fundacion, que no existe
A-22  handoff mal tipado, y falta el handoff CON→VER
      → CINCO DEFECTOS DE REFERENCIA CRUZADA que ningún validador cubre: ads_lint resuelve
        las refs declaradas y los enlaces markdown, pero no la coherencia entre lo que un
        esquema PERMITE y lo que la prosa EXIGE, ni los identificadores citados dentro de
        bloques ```text.

A-12  README, START_HERE y KERNEL.md con tres versiones distintas
A-24  once recuentos incorrectos, en cuatro contratos y en la nota de versión
      → LO ADMITEN COMO LÍMITE: «La coherencia PROSA↔BLOQUE dentro de un mismo fichero no
        es comprobable automáticamente — la cubre la revisión adversarial». La revisión
        adversarial no la cubrió, porque la ejecutó quien había escrito las cifras. Es el
        límite declarado materializándose exactamente donde se anunció.

A-14  la crítica de encuadre obligatoria puede evaporarse
A-23  DSP/estado DECIDE una cancelación
A-25  «lo más restrictivo gana» no es computable
A-26  la estación 12 no tiene gate en el kernel
```

### Dos hallazgos nuevos que sólo aparecen al leer estos tres documentos

**A-32 · DEFECTO — `CHECKPOINT-OPERATIVO.md` está desactualizado respecto al commit que
declara terminado, incumpliendo su propia regla.**

Su cabecera dice: «**Se actualiza antes de cada commit**, no al final». El commit `17e618e`
(«revisión adversarial, correcciones y cierre») añadió T134 y T135 y no lo actualizó. Cifras
del checkpoint frente al corpus reejecutado hoy:

| checkpoint dice | es |
|---|---|
| «ads_lint … sobre **298** bloques canónicos» | **300** |
| «**TOTAL 59** escenarios: 50 contrato-definido, **9** PRUEBA SUPERADA» | **61** · 50 · **11** |
| «comprobar_contratos EJECUTADO, **7/7** superadas» | **9/9** |
| «T86-T92 PRUEBA SUPERADA (**7**)» | 7, más T134 y T135, que el checkpoint no menciona |
| «los **diecisiete** esquemas» | **16** |

**Consecuencia práctica.** Es el fichero cuya única función es que un agente nuevo pueda
decir «Continúa» sin conversación previa, y a.10 regla 3 es explícita: «*Un checkpoint
desactualizado —siguió trabajando y no lo escribió— es **un defecto del sistema**, no una
omisión menor*». El kernel incumple aquí su propia regla más citada.

**Un dato a favor, y es relevante:** el checkpoint tiene **bien** dos de las cifras que la
documentación operativa tiene mal — «**Diez** matrices de composición» (frente a las «doce»
de `DIS/CAPACIDAD.md`) y «Circuito de **catorce** estaciones» (frente a las «Trece» de
`02-CIRCUITO.md`). Es decir: en A-24, la fuente correcta es el checkpoint y la incorrecta es
el documento normativo. Eso acota la corrección y confirma que son erratas de redacción, no
desacuerdos de fondo.

**A-33 · DEFECTO — `DECISIONES-Y-CONTRADICCIONES.md` §2 O3 apunta a un fichero que no
existe.**

> «O3 · Umbral de anclaje y margen de ambigüedad de b.13 — por defecto implementado:
> `umbral 0.60` · `margen 0.15`, declarados en `entrada/03-CLASIFICACION.md`»

No existe `kernel/operativo/entrada/03-CLASIFICACION.md`. Los valores viven en
`entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` §3, y `entrada/03-FORMAS.md` ocupa ese número.
Es una cita en prosa, no un enlace markdown, así que `ads_lint` no la alcanza —y aunque lo
fuera, `docs/` está fuera de su ámbito (A-28). **Consecuencia:** el Owner que quiera ejercer
la decisión O3 no encuentra dónde está el parámetro que se le pide decidir.

## 2.3 · Supuestos de la revisión anterior que considero incorrectos

**S1 · «0 apariciones fuera de las *tres* exenciones declaradas».**
Las exenciones de vocabulario son **19** ficheros en `kernel/` y `packs/` (21 contando
`docs/`), no tres: los seis documentos de `diseno/`, cuatro de los cinco contratos,
`00-LENGUAJE.md`, tres de `entrada/`, `00-CIRCUITOS.md`, `REGISTRO.md` y los dos de `packs/`.
El resultado —hoy nadie abusa de ellas— lo he verificado y es correcto; el supuesto sobre el
tamaño de la superficie exenta no lo es, y es lo que hace que la deuda A-27 importe.

**S2 · «35 métodos, 0 fallos» y «los 28 campos» y «diecisiete esquemas».**
Son 34 métodos, 29 campos y 16 esquemas. El «0 fallos» de T91 es cierto y lo he
reejecutado; la cifra sobre la que se predica, no. Es el mismo patrón de A-24.

**S3 · «T134, permanente: ningún documento del corpus puede quedarse sin entrada».**
Demostrado falso con un experimento reproducible (A-05). El supuesto de fondo —que una
prueba escrita a la vez que el remedio garantiza que el defecto no vuelva— es el que hay que
revisar: T134 se escribió para cerrar H2 y se validó comprobando que H2 ya no aparecía, no
comprobando que **detectaría** un H2 nuevo. Una prueba que nunca se ha visto fallar sobre un
caso construido a propósito no está verificada.

**S4 · «`comprobar_packs.py`: T131 y T132 EJECUTADAS Y SUPERADAS» como cierre del bloque 6.**
T131 no comprueba su enunciado y T132 comprueba dos de sus tres afirmaciones (A-03, A-17).
El bloque 6 se cierra apoyado en una prueba que no sostiene lo que declara.

**S5 · «La única [decisión del Owner] con contenido normativo es C1» y «ninguna bloquea».**
Discrepo en dos puntos. Primero, **C1 registra menos de lo que la decisión implica**: no
menciona que `ENC` usa un código de tres letras sin el prefijo de espacio de nombres que a.4
declara obligatorio para toda extensión, ni que `C4` la convierte en un **tercer equipo
permanente** frente a los dos de a.4, ni que el corpus queda con **tres recuentos
incompatibles** del catálogo (14 en (a) y en `packs/00-QUE-ES-UN-PACK.md`, 15 en
`00-INDICE.md` y en `comprobar_packs.py`). Segundo, **hay una segunda contradicción normativa
sin registrar**: A-06, la prevalencia DOM sobre DIS, que contradice la regla de colisión de
vetos de a.5 y decide en silencio algo que a.5 escala al Owner.

**S6 · «LOS SEIS PASOS ESTÁN IMPLEMENTADOS. La iniciativa está TERMINADA».**
Sostengo que el paso 5 está **incompleto en un punto sustantivo, no cosmético**: el
vocabulario canónico de las obligaciones de proceso (b.3), la función de estado global (b.4)
y las cinco condiciones de cierre (b.10) no tienen esquema, campo, gate ni plantilla
(A-09), y los tres frenos de a.7 más el de b.9 no tienen portador (A-10), incluida la cuarta
función de DSP. Nada de eso requiere runtime: es contenido, que es justo lo que esta
iniciativa se encargó de producir. El inventario está completo; el recorrido inverso —cada
mecanismo normativo tiene quien lo ejecute— no.

**S7 · «los packs no mencionan gym-wear» como prueba de que no hay diseño orientado a un
único proyecto.**
La afirmación es cierta y la confirmo (T92 reejecutado, y grep propio sobre los tres packs).
Pero prueba menos de lo que parece: que un pack no nombre el proyecto no significa que su
frontera esté bien puesta. `packs/00-QUE-ES-UN-PACK.md` prohíbe la tecnología concreta y el
pack se llama `wear-os` (A-29), y la regla de precedencia P1 no es computable (A-25). Ninguna
de las dos se detecta buscando el nombre del proyecto.

## 2.4 · Posibles falsos positivos míos

Los declaro yo, porque un informe que no los declara pide que se le crea:

```text
A-07  N3 INALCANZABLE — lectura literal frente a lectura intencional
      Mi lectura es literal: N4 pregunta «¿no existe memoria:vision-artistica, o está
      vacía?», y para un producto construido sin dirección escrita la respuesta es sí.
      Cabe la lectura de que N4 se refiera implícitamente a proyecto nuevo, apoyada en el
      nombre del método (Fundacion) y en su segundo disparador (un DIR). Si esa es la
      intención, el defecto se reduce de «rama inalcanzable» a «condición mal escrita» —
      pero sigue habiendo que reescribirla, porque la escala se declara comprobable
      «leyendo la memoria de diseño, no interpretable».

A-20  EL EJE `fidelidad` EN LA ESTACIÓN 9
      Es posible que la intención sea evaluar gate:excelencia-visual DOS veces —antes y
      después de construir— y que sólo falte declararlo. Si es así, mi hallazgo es de
      documentación y no de imposibilidad. Lo mantengo porque hoy no está escrito en
      ninguna parte y porque DIS/Fundacion cierra contra ese gate sin construcción alguna.

A-23  DSP/estado DECIDE UNA CANCELACIÓN
      El texto del rol está copiado de b.8, que sí encarga a DSP «convertir la situación»
      en una de tres. La contradicción con b.7 puede estar ya en (b) y no haberla
      introducido el kernel operativo. Si es así, la corrección es una frase en (b), no en
      el rol, y es materia del Owner.

A-13  gate:usabilidad Y LAS CAPAS DE CON
      Cabe que la intención sea que sobre lo construido la usabilidad la compruebe VER a
      través de su dosier, y que el `aplica_a` esté simplemente mal redactado. No he
      encontrado nada que lo diga, pero es una lectura razonable.

A-26  LA ESTACIÓN 12 SIN GATE
      Es parcial: mobile-app y wear-os SÍ exigen dispositivo real por gate propio. El
      hueco existe sólo para web-app y para proyectos sin pack. La afirmación de
      04-CICLO sigue siendo demasiado amplia, pero el riesgo real es menor del que su
      redacción sugiere.

A-29  EL NOMBRE DEL PACK wear-os
      Es un juicio, no un defecto comprobable. El contenido del pack es neutral y T92 lo
      confirma. Si el Owner considera que el identificador de un pack puede nombrar una
      plataforma sin que eso sea tecnología «dentro» del pack, el hallazgo desaparece.

A-30  PROFUNDIDAD ASIMÉTRICA
      DIS/CAPACIDAD.md lo declara deliberado («sirve de patrón de calidad para las demás:
      no de plantilla mecánica»). No es un defecto; lo registro sólo para que «equipos y
      métodos de las demás capacidades» no se lea como paridad de profundidad.

A-24  LOS RECUENTOS
      Son ciertos uno por uno, pero su gravedad es de MEDIO discutible: ninguno rompe la
      ejecución. Los agrupo en un solo hallazgo precisamente para no inflar la lista.
```

Y una advertencia sobre el conjunto: **el muestreo profundo de prompts es de 1 sobre 35**
(sección 7). Ese único contraste produjo dos hallazgos (A-08 y A-21). No es prudente suponer
que los otros treinta y cuatro estén limpios; es prudente suponer lo contrario.

## 2.5 · Conclusión del contraste

La revisión anterior hizo bien lo que podía hacer: buscó los doce defectos del encargo,
encontró cinco reales, los corrigió, convirtió dos en prueba permanente y **declaró por
escrito que la independencia le faltaba**. Esa declaración era exacta.

Lo que la lectura externa añade se agrupa en tres clases, y las tres eran previsibles desde
esa declaración:

```text
1  LO QUE NO SE EJECUTÓ        el tooling, y el código de los validadores propios
                               → A-02, A-03, A-04, A-05, A-17

2  LO QUE NO SE RECORRIÓ       las bifurcaciones de las decisiones escritas, en vez de
   AL REVÉS                    su enunciado; y cada mecanismo de (a)/(b) preguntando
                               quién lo ejecuta
                               → A-06 a A-11, A-13, A-14, A-19 a A-23, A-25, A-26

3  LO QUE EL PROPIO AUTOR      la coherencia prosa↔bloque y los recuentos, que
   NO PUEDE VER                DECISIONES §4 ya anunciaba como no comprobable
                               automáticamente
                               → A-12, A-15, A-16, A-24, A-32, A-33
```

Ninguna de las tres clases contradice el trabajo hecho: lo completa donde el propio equipo
dijo que estaba incompleto. La deuda que `REVISION-ADVERSARIAL.md` declaró abierta queda,
con este informe, **saldada en su primera vuelta** — y con 33 hallazgos, de los cuales seis
son bloqueantes para declarar la iniciativa terminada y uno solo requiere una decisión del
Owner.
