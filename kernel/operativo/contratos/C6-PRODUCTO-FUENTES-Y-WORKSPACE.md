# C6 — PRODUCTO, FUENTES Y WORKSPACE

Un ADS Project gobierna **un producto**. El producto puede estar repartido entre varios
repositorios Git independientes. Este contrato fija qué es cada cosa, dónde vive cada
verdad y qué comprueba el sistema antes de trabajar.

Deriva de la [enmienda E2](../../../docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md), que es la que
viaja con el kernel instalado. La decisión del Owner que la originó
—`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`— es historia del repositorio del kernel y **no se
enlaza desde aquí**: un proyecto instalado no la recibe, y enlazarla dejaría un enlace roto
en toda organización que lo instale. Es el mismo motivo por el que las auditorías tampoco
viajan.

## La relación que sustituye a la anterior

```text
ANTES (implícito, nunca escrito)      AHORA (normativo)

ADS PROJECT = repositorio de código   PRODUCTO
                                        └── ADS PROJECT
                                            ├── repositorio ADS de CONTROL   (uno)
                                            ├── COMPONENTES lógicos          (0..N)
                                            └── FUENTES / repos técnicos     (0..N)
```

## Los catorce principios

```text
N1   un ADS Project representa un PRODUCTO o sistema, no un repositorio
N2   un ADS Project tiene UN ÚNICO repositorio de control
N3   el repositorio de control es la autoridad organizativa global
N4   el producto puede tener 0..N fuentes
N5   una FUENTE es una ubicación física versionada
N6   un COMPONENTE lógico referencia una fuente y una ruta dentro de ella
N7   componente y fuente NO tienen cardinalidad 1:1 obligatoria
N8   el workspace local estándar son repositorios HERMANOS
N9   la identidad de una fuente NO depende de su ruta local
N10  el estado global NO se copia en las fuentes
N11  un item o paquete PUEDE atravesar varias fuentes
N12  Git permanece INDEPENDIENTE por fuente
N13  la integración multi-fuente es LÓGICA y evidenciada, no un commit Git ficticio
N14  el kernel es neutral respecto al proveedor agentic
```

## Los tres conceptos, y por qué son tres

```text
FUENTE       unidad física de versionado y materialización. Normalmente un repositorio
             Git. Tiene identidad remota canónica y una ruta donde se materializa.

COMPONENTE   unidad lógica del producto: `web`, `api`, `mobile`, `infra`. Referencia una
             fuente y una ruta dentro de ella.

WORKSPACE    el contenedor físico donde el repositorio de control y las fuentes aparecen
             como hermanos. NO es un repositorio Git.
```

**Componente y fuente no son lo mismo, y confundirlos encierra a ADS en `1 repo = 1
componente`.** El mismo modelo cubre los tres casos sin excepciones:

```text
MULTI-REPO   web → repo frontend, ruta .        api → repo backend, ruta .
MONOREPO     web → repo app, ruta apps/web      api → repo app, ruta apps/api
HÍBRIDO      web → repo producto, ruta apps/web       mobile → repo mobile, ruta .
```

## Topología

```text
<workspace>/                 NO es un repositorio Git. Es el contenedor del producto.
├── ads/                     el repositorio de CONTROL. Ruta convencional.
│   └── .git/
├── frontend/  .git/         fuentes, con la ruta que declara el manifiesto
├── backend/   .git/
└── mobile/    .git/
```

**Prohibido como topología ADS:** clonar las fuentes **dentro** del repositorio de control.
Un repositorio de control que contiene `.git` de otros deja de ser gobierno y pasa a ser un
contenedor, y su historia deja de ser legible.

**Las rutas predecibles son deliberadas.** Reducen configuración, errores, contexto para el
agente, código especial, diferencia entre local y nube, dificultad de recuperación y
dependencia de un proveedor. La flexibilidad arbitraria de rutas no es un objetivo.

## Fuente única de la composición

`SOURCES.toml`, en la raíz del repositorio de control, **es** la composición del producto.

```text
NADIE MÁS LA DECLARA   ni PROJECT.md, ni PROFILE.md, ni AGENTS.md, ni un pack, ni un
                       prompt. Pueden ENLAZARLA y explicarla. Copiar su contenido
                       semántico es un defecto de conformidad (I5).

POR QUÉ TOML           legible, admite comentarios, estable para configuración, y la
                       biblioteca estándar de Python lo lee con `tomllib`. Leer el
                       manifiesto NO introduce ninguna dependencia externa.
```

La forma del manifiesto, campo a campo, vive en su plantilla:
[`plantillas/SOURCES.toml`](../plantillas/SOURCES.toml). Su validación estática la ejecuta
[`comprobar_fuentes.py`](../validadores/comprobar_fuentes.py) y la operacional
[`workspace.py`](../../../tooling/workspace.py).

## Identidad frente a materialización

```text
IDENTIDAD         el remoto Git canónico, más un id estable dentro de ADS.
                  NO cambia porque el repositorio se clone en otro sitio.

MATERIALIZACIÓN   la ruta relativa al workspace donde debe aparecer.
                  Es dónde está, no qué es.
```

De ahí las prohibiciones del manifiesto, que no son estilo sino consecuencia: rutas
absolutas, rutas que escapan del workspace con `..`, rutas duplicadas, `ads` como ruta de
una fuente técnica, e ids duplicados. **Y ninguna credencial**: el manifiesto declara
identidad, nunca secretos. La autenticación la aporta el entorno.

## Regla de autoridad

```text
REPOSITORIO DE CONTROL   la verdad de la ORGANIZACIÓN y del PRODUCTO
FUENTES                  la verdad de SUS IMPLEMENTACIONES
INTEGRATION SET          la evidencia versionada de una composición verificada
RUNTIME                  estado operacional efímero, cuando exista
```

**Un runtime no sustituye en silencio la verdad durable del repositorio de control.**

### Qué NO puede vivir en una fuente

```text
PROFILE · PROJECT · estado global · items · rutas · paquetes · memoria · ADR globales ·
contratos maestros · kernel · packs · AGENTS global · documentación organizativa
```

Copiarlos crearía una organización ADS por repositorio que después habría que sincronizar,
que es el modo de fallo (a) de `a.7` reproducido a escala de producto.

### Qué SÍ puede vivir en una fuente

Documentación **pegada al código**, cuya utilidad depende directamente de él: README de
construcción, instrucciones de desarrollo del componente, documentación de migraciones,
documentación generada desde el código, configuración de CI, despliegue específico del
componente, y notas que deban versionarse exactamente con esa implementación.

La frontera es una pregunta: **¿esto deja de ser cierto si cambia el código de al lado?**
Si sí, vive con el código. Si no, vive en el control repo.

## Entrada por ADS

```text
abrir el repositorio de control
    ↓  el Owner expresa su intención
ADS determina item · ruta · paquete
    ↓
ADS determina componentes y fuentes afectadas
    ↓
verifica o materializa esas fuentes
    ↓
habilita al agente el contexto mínimo: lee_fuentes y escribe_fuentes
    ↓
trabaja sobre una o varias fuentes
    ↓
integra el resultado en el estado global
```

**Trabajar directamente sobre una fuente sin cargar el ADS Project es trabajo fuera de
ADS.** No se impide técnicamente —Git pertenece a sus dueños— y **ADS no finge** que ese
trabajo pasó por sus gates, rutas, decisiones, contratos, estado ni trazabilidad. Duplicar
todo ADS dentro de cada fuente para evitarlo sería el remedio peor que la enfermedad.

## Alcance mínimo

Tener cuatro repositorios disponibles **no** significa cargar cuatro repositorios en
contexto.

```text
necesidad → componentes afectados → fuentes necesarias → lee/escribe → contexto mínimo
```

Una fuente ausente bloquea **sólo** los paquetes que la requieren. Un trabajo de frontend
puro continúa aunque el backend no esté materializado.

## Neutralidad de proveedor

El soporte multi-fuente se apoya **sólo** en: sistema de ficheros, directorios, Git,
shell y credenciales aportadas por el entorno.

```text
CONTRATO DEL KERNEL   el agente recibe el repositorio de control como contexto principal,
                      y las rutas de las fuentes necesarias como directorios adicionales
                      de lectura o de escritura.

ADAPTADOR             cómo se le entregan esos directorios en cada entorno agentic.
                      Es adaptación, NO semántica del kernel.
```

Una integración de proveedor puede mejorar la experiencia. **La arquitectura base funciona
sin ninguna.** Ningún flag de ninguna herramienta aparece en este contrato, y `T92` lo
comprueba.

## Materialización

```text
LOCAL     si la fuente ya existe en el workspace y su identidad remota coincide,
          ADS la REUTILIZA. No vuelve a clonar. No crea copias temporales.

NUBE      el modelo lógico no cambia. Dos modos, ambos válidos:
            A  el proveedor ya materializó varias fuentes → ADS valida el workspace
            B  sólo está el repositorio de control → ADS lee el manifiesto y clona
          El kernel NO asume que siempre ocurra A ni siempre B.
```

### Lo que la materialización nunca hace

```text
[ ] borrar un directorio
[ ] resetear cambios locales
[ ] hacer checkout destructivo
[ ] hacer pull forzado
[ ] cambiar el remoto de un repositorio existente
[ ] clonar encima de un directorio ocupado
[ ] sincronizar implícitamente: preparar un workspace y sincronizar un trabajo son
    operaciones distintas, y confundirlas altera repos con trabajo local sin avisar
```

**Una fuente con cambios sin confirmar no es automáticamente un error**: se informa, y la
política de aislamiento del paquete decide. Lo que nunca ocurre es destruirlos.

```yaml ads:gate
id: gate:workspace-conforme
aplica_a: "todo paquete que declara lee_fuentes o escribe_fuentes"
comprobaciones:
  - id: manifiesto-valido
    comprueba: "existe SOURCES.toml, su schema está soportado y su layout está soportado"
    como: "python3 tooling/workspace.py check"
    automatizable: si
  - id: identidad-sin-colision
    comprueba: "los ids y las rutas de las fuentes son únicos, y ninguna ruta es 'ads'"
    como: "workspace check: comprobación de unicidad y de ruta reservada"
    automatizable: si
  - id: sin-escape-de-workspace
    comprueba: "ninguna ruta de fuente ni de componente sale del workspace"
    como: "resolución de ruta normalizada contra WORKSPACE_ROOT"
    automatizable: si
  - id: sin-credenciales
    comprueba: "ningún remoto del manifiesto embebe usuario, token o contraseña"
    como: "inspección de la URL declarada"
    automatizable: si
  - id: fuentes-del-alcance-presentes
    comprueba: "las fuentes que el paquete lee o escribe están materializadas y son el repositorio esperado"
    como: "workspace check sobre las fuentes del alcance: es repo Git y su remoto corresponde"
    automatizable: si
  - id: alcance-minimo-declarado
    comprueba: "el paquete no declara escritura sobre una fuente que no necesita modificar"
    como: "lectura: el objetivo del paquete justifica cada fuente de escribe_fuentes"
    automatizable: parcial
evidencia:
  - "salida de workspace check, con su código de salida"
  - "las fuentes del alcance, con su rama y su revisión"
fallo: >
  El paquete no se despacha. Si falta una fuente del alcance, queda esperando-dependencia
  hasta materializarla. Si el directorio está ocupado por otro repositorio, o el remoto no
  corresponde, es ERROR y no se resuelve automáticamente: clonar encima o cambiar el remoto
  destruiría trabajo de alguien.
```

## Validación estática frente a disponibilidad del workspace

**Son dos cosas distintas y se comprueban por separado.** Confundirlas haría imposible
validar el repositorio de control en CI sin credenciales de todos los repos privados.

```text
comprobar_fuentes.py    el ADS Project es VÁLIDO: el manifiesto está bien formado, los
                        componentes referencian fuentes que existen en él, y el corpus no
                        se contradice. NO exige que ninguna fuente esté clonada.

workspace check         el WORKSPACE está DISPONIBLE: qué fuentes están materializadas,
                        si son el repositorio esperado y en qué estado. Exige el disco.
```

## Lo que este contrato no autoriza

```text
servidor central · base de datos · registry · daemon · broker · cola · API cloud ·
servicio Git · servicio de locks · gestor de submodules · tooling de monorepo ·
sincronización distribuida · commits atómicos multi-repo · mirrors · federación de
proyectos ADS
```

La arquitectura debe **permitirlos sin necesitarlos**. Ficheros, Git y una herramienta
ligera resuelven la semántica y la materialización reproducible.
