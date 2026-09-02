# 01 · MODELO DEL SISTEMA

Las piezas de ADS, sus fronteras y dónde vive cada verdad. **Este documento explica el
modelo; no reformula ninguna norma.** Cada norma se enlaza a su sede.

Entrada recomendada: [`00-EMPEZAR-AQUI.md`](00-EMPEZAR-AQUI.md).

---

## 1 · Producto, ADS Project y repositorio Git no son lo mismo

**La confusión que ADS retira es `proyecto = repositorio`.** Es una equivalencia derogada,
y el corpus tiene un verificador que la persigue por FORMULACIÓN y no por palabra
—`T161`, en [`comprobar_fuentes.py`](../../kernel/operativo/validadores/comprobar_fuentes.py)—.

```text
PRODUCTO        lo que se construye y se entrega. Puede vivir en 1..N repositorios Git.

ADS PROJECT     el gobierno de UN producto. Tiene UN repositorio de CONTROL, y sólo uno.

REPOSITORIO     una ubicación física versionada. En ADS se llama FUENTE.
DE CÓDIGO

COMPONENTE      unidad LÓGICA del producto —`web`, `api`, `mobile`, `infra`—. Referencia
                una fuente y una ruta dentro de ella. Componente y fuente NO tienen
                cardinalidad 1:1: por eso el mismo modelo cubre multi-repo, monorepo e
                híbrido sin excepciones.

WORKSPACE       el contenedor físico donde el control repo y las fuentes aparecen como
                HERMANOS. **No es un repositorio Git**, y clonar las fuentes DENTRO del
                control repo está prohibido como topología.
```

**Sede normativa, con sus principios, su topología y sus condiciones de error:**
[`C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md).
El manifiesto que declara la composición es `SOURCES.toml`, cuya plantilla es
[`plantillas/SOURCES.toml`](../../kernel/operativo/plantillas/SOURCES.toml) y cuyo
materializador es [`tooling/workspace.py`](../../tooling/workspace.py).

## 2 · Las piezas, y qué las separa

```text
                    OWNER
                      │  expresión literal, que se conserva siempre
                      ▼
                    ENC ── encuadre ──► DSP ── item · ruta · paquete ──► CAPACIDADES
                                                                            │
   ═══════════ WORKSPACE DEL PRODUCTO (no es un repositorio Git) ═══════════ │
     ads/  CONTROL REPO            frontend/.git   backend/.git   mobile/.git
       distribución  kernel · packs · esquemas · contratos · validadores
       especialización  PROFILE · PROJECT · SOURCES.toml · overrides
       estado durable  items · paquetes · iniciativas · eventos · memoria
       derivados  vistas · tableros · dosieres · índices
       proyecciones  AGENTS.md · CLAUDE.md · reglas por entorno (GENERADAS)
       .ads/run/  operacional: lock, caché, índice. NO versionado
```

**Los cinco planos** —distribución, especialización, estado durable, proyección y
operacional— separan **ciclo de vida**, no conocimiento. Qué contiene cada uno, quién lo
versiona y con qué ciclo cambia está en
[`11-ARQUITECTURA-INTEGRADA.md` §1.2](../evolucion/11-ARQUITECTURA-INTEGRADA.md#12--los-cinco-planos-y-por-qué-son-cinco);
la topología completa, en su §1.1.

> **No los confundas con `K-1`**, que clasifica CONOCIMIENTO —universal, de clase, o de
> este producto—. Confundirlos fabrica una cuarta capa de conocimiento por la puerta de
> atrás, que es una decisión que el Owner tiene deferida.

## 3 · Capacidades, equipos, roles, agentes y métodos

**Son cinco conceptos distintos, y confundir cualquiera de ellos rompe algo concreto.** La
sede que lo fija, con los siete conceptos y el contrato común de rol, es
[`C1-EQUIPO-ROL-AGENTE-METODO.md`](../../kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md);
la asignación de modelos, la combinación de roles y el relevo sin pérdida de memoria, en
[`C2-AGENTES-Y-MODELOS.md`](../../kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md).

```text
CAPACIDAD     qué SABE HACER el sistema. Permanente, del catálogo, no consume nada.
EQUIPO        organización TEMPORAL materializada para trabajo real.
ROL           responsabilidad concreta dentro del equipo, con autoridad delimitada.
AGENTE        instancia de IA que ocupa uno o varios roles.
MÉTODO        procedimiento que el rol sigue, con pasos, checkpoints y gate.
HERRAMIENTAS  recursos que el rol PUEDE usar. Declaradas, no supuestas.
AUTORIDAD     qué puede DECIDIR, PROPONER, VETAR o ESCALAR.
```

**El catálogo de capacidades vive en `kernel/operativo/capacidades/`**, una carpeta por
código, cada una con `CAPACIDAD.md`, `roles/`, `metodos/`, `prompts/` y `composicion.md`.
Los códigos son:

```text
ENC encuadre      PRD producto     DIS diseño        ARQ arquitectura
DOM dominio       CON construcción VER verificación  ENT entrega
USO uso real      INV investigación SEG seguridad    PLT plataforma
APR aprendizaje   DSP despacho     SIS sistema
```

**El recuento no se escribe: se deriva.**

```bash
ls -1d kernel/operativo/capacidades/*/ | wc -l
```

Índice completo, con enlace a cada ficha:
[`kernel/operativo/00-INDICE.md`](../../kernel/operativo/00-INDICE.md).

### Quién decide, quién propone y quién veta

La autoridad **no es una convención de este documento**: la fija la especificación aprobada
—[`a-CAPACIDADES-APROBADA.md`](../rediseno/a-CAPACIDADES-APROBADA.md) y su enmienda
[`E1`](../rediseno/a-ENMIENDA-E1-ENC.md)— y la instancia el contrato de rol de `C1`. Un rol
que no declara su autoridad **no es materializable, y el instalador debe rechazarlo**.

## 4 · Estado persistido, memoria y fuentes de verdad

**Una verdad vive en un fichero; los demás la enlazan.** Repetirla es un defecto de
conformidad, no una comodidad de lectura. La regla y su mapa —qué verdad vive dónde dentro
del kernel— están en
[`kernel/operativo/00-INDICE.md`](../../kernel/operativo/00-INDICE.md); la matriz de
fuentes de verdad del sistema completo, con su autoridad y su ejecutor de mutación, está en
[`11-ARQUITECTURA-INTEGRADA.md` §1.3](../evolucion/11-ARQUITECTURA-INTEGRADA.md#13--matriz-de-fuentes-de-verdad).

```text
ESTADO DURABLE   items, paquetes, iniciativas, eventos, cobertura, memoria e integration
                 sets. Vive en el CONTROL REPO y NO se copia en las fuentes.

MEMORIA          corpus persistente de un equipo, seccionado, con capa —kernel, pack o
                 profile—, autoridad, contenido, ciclo de actualización, caducidad y qué
                 significa que esté vacía. Forma canónica:
                 esquemas/memoria.yaml.

OPERACIONAL      lock, cachés e índices compilados. No se versiona y es reconstruible.
                 Su desaparición no pierde ninguna verdad.
```

> **La DISPOSICIÓN FÍSICA de ese estado durable está DISEÑADA y NO CONSTRUIDA.** Qué
> ficheros, cómo se fragmentan, qué transacción, qué event log y qué recuperación es
> materia de `11-ARQUITECTURA-INTEGRADA.md` §2, y **está bloqueada por una presión
> normativa que sólo el Owner puede levantar**. Qué significa eso exactamente, y qué
> depende de ello, está en
> [`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md).

## 5 · Kernel, runtime, proyectos, repositorios y herramientas

```text
kernel/operativo/   EL CONTENIDO OPERATIVO. Roles, métodos, gates, prompts, plantillas,
                    circuitos, rúbricas, esquemas, validadores y pruebas. Deriva de la
                    especificación aprobada y la CITA; no la repite.
                    ESTADO: construido, versionado y verificado.

packs/              ESPECIALIZACIÓN POR CLASE DE PROYECTO. Amplía el kernel; no lo
                    sustituye. Los packs instalables se derivan de packs/*/PACK.md.
                    ESTADO: construido.

tooling/            LO EJECUTABLE HOY: creación de proyecto, materialización del
                    workspace multi-fuente, comprobación de huella y preparación de la
                    recompilación de proyecciones.
                    ESTADO: construido.

kernel/KERNEL.md    la constitución EN PROSA de la línea anterior. Mientras el runtime no
                    exista, sigue siendo el documento de arranque de un proyecto.
                    ESTADO: vigente por convivencia declarada, no derogado.

RUNTIME             el proceso que consume kernel/operativo/, compone rutas, materializa
                    equipos, despacha trabajo y persiste estado.
                    ESTADO: DISEÑADO, NO CONSTRUIDO. Su ciclo, sus fallos, reintentos,
                    bloqueo, pausa y la orden `Continúa` están especificados en
                    11-ARQUITECTURA-INTEGRADA.md §7.
```

**El inventario de lo construido frente a lo diseñado tiene una sola sede**, y es
[`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md). Los rótulos `ESTADO:` de esta
sección son una ORIENTACIÓN sobre las cinco piezas que nombra y **no son ese inventario**;
donde difieran, manda `04`.

## 6 · Multirrepositorio: la frontera que hay que respetar al construir

```text
N1   un ADS Project representa un PRODUCTO, no un repositorio
N2   tiene UN ÚNICO repositorio de control
N10  el estado global NO se copia en las fuentes
N11  un item o paquete PUEDE atravesar varias fuentes
N12  Git permanece INDEPENDIENTE por fuente
N13  la integración multi-fuente es LÓGICA y evidenciada, no un commit Git ficticio
```

**Éstos son seis de los principios de `C6`, citados para fijar la frontera; los demás, su
redacción exacta y sus condiciones de error viven en el contrato**, que es su única sede:
[`C6`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md). Quién pide,
ejecuta, bloquea y verifica cada operación Git, y cómo converge un cambio repartido entre
varias fuentes, es materia de
[`C7`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) y se explica en
[`02-MODELO-OPERATIVO.md`](02-MODELO-OPERATIVO.md).

## 7 · Adaptadores y entornos agentic

**ADS es neutral respecto al proveedor agentic.** La definición del comportamiento es
canónica y neutral; lo que cada entorno lee —`AGENTS.md`, `CLAUDE.md`, reglas de otros
entornos— es una **proyección generada**, con huella y validador de deriva.

```text
HOY   ningún adaptador está CERTIFICADO, y ninguno lo estará hasta superar una prueba de
      humo real en sesión nueva. Los dos primeros OBJETIVOS de soporte los fijó el Owner.
```

Arquitectura de adaptadores, sus cuatro piezas y el descubrimiento por entorno:
[`11-ARQUITECTURA-INTEGRADA.md` §6](../evolucion/11-ARQUITECTURA-INTEGRADA.md#6--arquitectura-de-adaptadores).
El estado de esa decisión y su autoridad:
[`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md).
