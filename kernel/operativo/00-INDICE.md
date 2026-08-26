# KERNEL OPERATIVO — índice y regla de fuente única

`kernel/operativo/` es la **instanciación ejecutable** de la especificación aprobada en
[`docs/rediseno/a-CAPACIDADES-APROBADA.md`](../../docs/rediseno/a-CAPACIDADES-APROBADA.md)
y [`docs/rediseno/b-RECORRIDO-APROBADA.md`](../../docs/rediseno/b-RECORRIDO-APROBADA.md), con
sus enmiendas [E1](../../docs/rediseno/a-ENMIENDA-E1-ENC.md) y
[E2](../../docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md).

```text
(a) y (b) + E1 · E2   ESPECIFICACIÓN NORMATIVA — invariantes, autoridad, estados,
                      recorrido. Aprobadas. No se modifican desde aquí: se enmiendan.
kernel/operativo/     CONTENIDO OPERATIVO — roles, métodos, gates, prompts, plantillas,
                      circuitos, rúbricas, validadores y pruebas. Es lo que un equipo
                      ejecuta. Deriva de (a) y (b) y las cita; no las repite.
packs/<clase>/        ESPECIALIZACIÓN POR CLASE DE PROYECTO. Amplía. No sustituye.
PROFILE.md            UN producto concreto. Uno por producto, nunca uno por repositorio.
SOURCES.toml          QUÉ REPOSITORIOS Y COMPONENTES lo forman. Fuente única.
```

> **Un ADS Project gobierna un PRODUCTO, no un repositorio.** El código vive en las fuentes
> declaradas en `SOURCES.toml` y aparece como repositorios hermanos del de control. Un
> producto de un solo repositorio es el caso particular de tener una sola fuente.
> Contrato: [`C6`](contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md).

## Regla de fuente única

> **Una verdad vive en un fichero.** Los demás la **enlazan**. Repetirla es un defecto de
> conformidad, no una comodidad de lectura.

Cuando un documento necesita una verdad que ya existe:

```text
CORRECTO    «la condición compuesta de paralelismo (a.5)» + enlace
INCORRECTO  copiar las seis condiciones aquí «para que se lea de un tirón»
```

`ads_lint` no detecta toda duplicación semántica. La detecta la revisión adversarial, y
cuando aparece se resuelve **borrando la copia**, nunca sincronizando las dos.

> **Los prompts son la excepción declarada.** Un prompt se carga solo en un agente que no
> va a leer nada más, y por tanto **repite operativamente** lo que necesita para trabajar.
> Eso no es duplicación de fuente: la fuente sigue siendo el contrato o el catálogo, y el
> prompt enlaza a ella en su cabecera. Cuando la fuente cambia, el prompt se revisa —es una
> comprobación del gate de SIS— y si divergen, manda la fuente.

## Mapa de fuente única

| verdad | fuente única |
|---|---|
| catálogo de capacidades, autoridad, veto, frenos, paralelismo, checkpoint | (a) |
| estados, transiciones, cierre, obligaciones, rutas por tipo, `Continúa` | (b) |
| obligaciones de cada proceso y condiciones de cierre, en forma canónica | [`recorrido/`](recorrido/00-OBLIGACIONES-Y-CIERRE.md) |
| niveles de novedad, sus gates y su evidencia reutilizable | [`diseno/03-ESCALA-DE-NOVEDAD.md`](diseno/03-ESCALA-DE-NOVEDAD.md) |
| propiedades medibles de un pack y su precedencia | [`packs/COMPOSICION.md`](../../packs/COMPOSICION.md) |
| formato canónico de los artefactos operativos | [`esquemas/00-LENGUAJE.md`](esquemas/00-LENGUAJE.md) |
| forma de cada tipo canónico | `esquemas/<tipo>.yaml` |
| ficha operativa de una capacidad | `capacidades/<COD>/CAPACIDAD.md` |
| contrato de un rol | `capacidades/<COD>/roles/<rol>.md` |
| perfiles de modelo y política de asignación | [`contratos/C2-AGENTES-Y-MODELOS.md`](contratos/C2-AGENTES-Y-MODELOS.md) |
| qué es una fuente, un componente y un workspace, y dónde vive cada verdad | [`contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`](contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) |
| gobierno Git del producto y convergencia multi-fuente | [`contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md`](contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) |
| la composición del producto: qué repositorios y componentes lo forman | `SOURCES.toml` del ADS Project |
| procedimiento de un rol | `capacidades/<COD>/metodos/<Metodo>.md` |
| prompt operativo de un rol | `capacidades/<COD>/prompts/<rol>.md` |
| entrada del Owner y su circuito | [`entrada/00-INDICE.md`](entrada/00-INDICE.md) |
| excelencia de diseño | `diseno/` |
| entregas entre capacidades | [`circuitos/00-CIRCUITOS.md`](circuitos/00-CIRCUITOS.md) |
| pruebas de conformidad nuevas | `pruebas/` y los bloques `ads:escenario` de cada documento |
| estado real de cada prueba | [`pruebas/REGISTRO.md`](pruebas/REGISTRO.md) |

## Qué hay aquí

| directorio | contenido | entrada |
|---|---|---|
| `esquemas/` | el lenguaje canónico y los diecinueve tipos | [`00-LENGUAJE.md`](esquemas/00-LENGUAJE.md) |
| `contratos/` | los siete contratos transversales | [`00-INDICE.md`](contratos/00-INDICE.md) |
| `entrada/` | PASO 1 — de la frase del Owner al item | [`00-INDICE.md`](entrada/00-INDICE.md) |
| `diseno/` | PASO 3 — el sistema de excelencia | [`00-SISTEMA-DE-EXCELENCIA.md`](diseno/00-SISTEMA-DE-EXCELENCIA.md) |
| `capacidades/` | PASOS 4 y 5 — las quince capacidades | tabla de abajo |
| `recorrido/` | obligaciones del proceso, cierre del item y los diez procesos | [`00-OBLIGACIONES-Y-CIERRE.md`](recorrido/00-OBLIGACIONES-Y-CIERRE.md) |
| `circuitos/` | los circuitos y los handoffs | [`00-CIRCUITOS.md`](circuitos/00-CIRCUITOS.md) |
| `plantillas/` | artefactos rellenables | tabla de abajo |
| `validadores/` | los validadores ejecutables, incluidas las pruebas negativas; el manifiesto canónico dice cuáles y qué se espera de cada uno | [`validadores.yaml`](validadores/validadores.yaml) · [`huella.py`](validadores/huella.py) · [`exclusiones.yaml`](validadores/exclusiones.yaml) |
| `pruebas/` | escenarios y su registro honesto | [`REGISTRO.md`](pruebas/REGISTRO.md) |

### Las quince capacidades

| | | | |
|---|---|---|---|
| [`ENC`](capacidades/ENC/CAPACIDAD.md) Encuadre | [`PRD`](capacidades/PRD/CAPACIDAD.md) Producto | [`DIS`](capacidades/DIS/CAPACIDAD.md) Diseño | [`ARQ`](capacidades/ARQ/CAPACIDAD.md) Arquitectura |
| [`DOM`](capacidades/DOM/CAPACIDAD.md) Dominio | [`CON`](capacidades/CON/CAPACIDAD.md) Construcción | [`VER`](capacidades/VER/CAPACIDAD.md) Verificación | [`ENT`](capacidades/ENT/CAPACIDAD.md) Entrega |
| [`USO`](capacidades/USO/CAPACIDAD.md) Uso real | [`INV`](capacidades/INV/CAPACIDAD.md) Investigación | [`SEG`](capacidades/SEG/CAPACIDAD.md) Seguridad | [`PLT`](capacidades/PLT/CAPACIDAD.md) Plataforma |
| [`APR`](capacidades/APR/CAPACIDAD.md) Aprendizaje | [`DSP`](capacidades/DSP/CAPACIDAD.md) Despacho | [`SIS`](capacidades/SIS/CAPACIDAD.md) Sistema | |

Cada carpeta tiene la misma forma: `CAPACIDAD.md` · `roles/` · `metodos/` · `prompts/` ·
`composicion.md`.

### Plantillas rellenables

| | |
|---|---|
| [`ENCUADRE.md`](plantillas/ENCUADRE.md) | el dosier que ENC entrega a DSP |
| [`CHECKPOINT.md`](plantillas/CHECKPOINT.md) | el formato de a.10, copiable, con los cuatro errores que lo estropean |
| [`DEVOLUCION.md`](plantillas/DEVOLUCION.md) | los cuatro campos sin los cuales una devolución no es una devolución |
| [`DICTAMEN.md`](plantillas/DICTAMEN.md) | la forma común de todo juicio independiente |
| [`CIERRE.md`](plantillas/CIERRE.md) | el informe que separa obligaciones satisfechas de retiradas |
| [`SOURCES.toml`](plantillas/SOURCES.toml) | la composición del producto, que arranca vacía |
| [`INTEGRATION-SET.md`](plantillas/INTEGRATION-SET.md) | la combinación exacta de revisiones que se probó junta |

### Los tres packs del catálogo

`web-app` · `mobile-app` · `wear-os`. **En un proyecto instalado sólo existe el directorio
de los packs que ese proyecto instaló**, y por eso aquí se nombran en vez de enlazarse: un
enlace a un pack no instalado sería un enlace roto en toda organización que no los use los
tres. El catálogo completo y sus reglas viajan siempre con `packs/`:
[qué es un pack](../../packs/00-QUE-ES-UN-PACK.md) ·
[composición y precedencia](../../packs/COMPOSICION.md).

## Cómo se usa esto sin haber visto ninguna conversación

```text
1  lee esquemas/00-LENGUAJE.md            cómo se leen los bloques canónicos
2  lee contratos/C1-EQUIPO-ROL-AGENTE-METODO.md   qué es un rol y qué debe declarar
3  localiza tu capacidad en capacidades/<COD>/CAPACIDAD.md
4  localiza tu rol y su prompt operativo
5  ejecuta su método paso a paso, escribiendo checkpoint donde el método lo exige
6  cierra por su gate, no por tu criterio
```

Nada de lo anterior requiere leer el kernel entero, ni conocer la historia del proyecto.

## Relación con `kernel/KERNEL.md` 1.3.0

`KERNEL.md` es la constitución en prosa de la versión 1.3.0. La sección a.11 declara qué
reglas suyas quedan derogadas, sustituidas, ajustadas o pendientes. **Mientras el runtime
no exista, `KERNEL.md` sigue siendo el documento de arranque de un proyecto**, y este
directorio es el contenido que ese runtime consumirá. La convivencia y su fecha de
resolución están registradas en
[`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`](../../docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md).
