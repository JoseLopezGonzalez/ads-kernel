# C7 — GOBIERNO GIT MULTI-SOURCE

Quién pide, quién ejecuta, quién bloquea, quién verifica y qué evidencia queda por cada
operación Git de un producto repartido entre varias fuentes.

Existe porque faltaba. `G29` y `G30` de la línea 1.3.0 gobiernan Git con detalle —rama
principal protegida, unidad de trabajo aislada, commit y push autónomos, PR como punto de
convergencia, CI como autoridad automática, cuatro niveles de autoridad de merge,
`merge ≠ release`, tags, rollback y contención— y **ninguna capacidad de la línea 2.0 las
había recogido**. Un barrido del corpus encontraba Git sólo de pasada.

Deriva de la [enmienda E2 §E2.4](../../../docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md) y de la
decisión aprobada.

## Qué se conserva de `G29`, y qué se deroga

```text
SE CONSERVA, y se aplica POR FUENTE:
  main protegida y representando el último estado integrado y aceptado DE ESA FUENTE
  unidad de trabajo aislada: rama, worktree o sandbox
  commits como checkpoints lógicos y trazables; ni por microacción ni volcado final
  push autónomo dentro del trabajo autorizado, en los momentos que G29 declara
  PR como punto formal donde convergen tarea, diff, CI, revisión, docs y riesgos
  CI como autoridad automática: no vale «parece correcto» si hay algo que lo verifique
  los cuatro niveles de autoridad de merge, graduados por riesgo
  commit != push != merge != release != publicación
  tags y capacidad de revertir
  el Owner NO es operador Git

SE DEROGA:
  la relación implícita, nunca escrita y hasta ahora universal:

      un item  →  una rama  →  un PR
```

## La relación correcta

```text
item / paquete
    ↓
0..N SOURCE CHANGES
    ↓
por cada fuente, y de forma independiente:
    rama o worktree  →  commits  →  push  →  PR  →  CI
    ↓
INTEGRATION SET — convergencia lógica, verificada y evidenciada
```

**El estado del producto no vive en ninguna rama. Se calcula en el repositorio de control.**

## El source change

Todo paquete que escriba sobre una fuente registra, por cada fuente tocada:

```text
source            el id declarado en SOURCES.toml
rama              la referencia de trabajo, cuando existe
commit            el SHA, cuando hay commit
push              sí | no
PR                la referencia, cuando existe
CI                el estado disponible, con enlace a su evidencia
sin_confirmar     sólo cuando sea necesario para recuperar el trabajo
```

Para varias fuentes, la colección es `0..N`. **Vive en el checkpoint del paquete**
(enmienda E2 §E2.3), no en un artefacto nuevo.

### Los nombres de rama no tienen que coincidir

Un cambio transversal puede usar `feat/item-123` en el frontend y otra convención en el
backend si su plataforma la exige. **La asociación vive en ADS**, no en la coincidencia
textual del nombre. Suponer lo contrario ata el sistema a que todos los repositorios tengan
la misma política de nombres, que no es una propiedad que ADS pueda garantizar.

## Propiedad de cada operación

Sin esta tabla, la responsabilidad se reparte de forma ambigua entre `PLT`, `ENT`, `DSP` y
`CON`, que es exactamente el defecto que este contrato existe para cerrar.

| operación | la solicita | la ejecuta | puede bloquearla | la verifica | evidencia |
|---|---|---|---|---|---|
| materializar una fuente | `DSP` al despachar | `PLT` | `SEG` si el remoto no es de confianza | `gate:workspace-conforme` | salida de `workspace check` |
| crear rama o worktree | la capacidad con custodia | ella misma | `PLT` si el aislamiento no es suficiente | el propio paquete | rama declarada en el checkpoint |
| commit | la capacidad con custodia | ella misma | — | `gate` de su capa | SHA en el checkpoint |
| push | la capacidad con custodia | ella misma | `SEG` ante secreto detectado | CI de esa fuente | estado de push en el checkpoint |
| abrir PR | la capacidad con custodia | ella misma | — | CI de esa fuente | referencia del PR |
| revisión independiente | `DSP` al componer la ruta | `VER` | `VER` con dictamen `devuelto` | dictamen | `plantillas/DICTAMEN.md` |
| merge de una fuente | `ENT` | `ENT` | `SEG` · `VER` · el Owner en materia reservada | los cuatro niveles de `G29` | SHA de integración |
| declarar convergencia | `ENT` | `ENT` | `gate:convergencia-de-fuentes` | el Integration Set | el propio Integration Set |
| release | el Owner | `ENT` | el Owner | `gate:entrega-observada` | tag y su Integration Set |
| rollback | `ENT`, o autónomo con los cinco requisitos de `a.3` | `ENT` | el Owner si es irreversible | `ENT/Contencion` | Integration Set restaurado |
| retirar rama abandonada | `PLT` | `PLT` | la capacidad con custodia si la reclama | `DSP/estado` | registro de la retirada |

**`main` de cada fuente sigue protegida.** Ninguna capacidad empuja directamente sobre ella.

## Integration Set

Una combinación exacta de revisiones de fuentes que ha sido candidata o probada
conjuntamente. Es la **atomicidad lógica de producto** que sustituye a la atomicidad Git
que Git no ofrece.

```yaml ads:integration-set
id: IS-000
item: ITEM-000
estado: candidato
fuentes:
  - source: frontend
    commit: "0000000000000000000000000000000000000000"
    rama: feat/item-000
    pr: "ninguno"
  - source: backend
    commit: "1111111111111111111111111111111111111111"
    rama: feat/item-000
    pr: "ninguno"
contratos:
  - "api-contract@v0 — plantilla; un Integration Set real cita el contrato vigente"
verificacion:
  - ambito: frontend
    resultado: pendiente
    evidencia: "enlace a la ejecución de CI de esa fuente"
  - ambito: integracion
    resultado: pendiente
    evidencia: "enlace a la ejecución conjunta"
migraciones:
  - "ninguna en la plantilla; un Integration Set real declara las que intervienen"
restaura_a: "ninguno — es el primero de su item"
```

Este bloque es la **plantilla vacía y canónica** del tipo. Un Integration Set real vive con
su item; su forma copiable está en
[`plantillas/INTEGRATION-SET.md`](../plantillas/INTEGRATION-SET.md).

### Qué debe poder responder con evidencia

```text
[ ] ¿qué frontend fue probado con qué backend?
[ ] ¿qué commits componían el candidato?
[ ] ¿qué contratos estaban vigentes?
[ ] ¿qué migraciones intervenían?
[ ] ¿qué CI pasó, y dónde está su salida?
[ ] ¿qué combinación se desplegó?
[ ] ¿qué combinación hay que restaurar si se revierte el producto?
```

### Integration Set no es release

```text
INTEGRATION SET   la combinación exacta EVALUADA
RELEASE           la DECISIÓN de publicar o desplegar una combinación
```

Un Integration Set puede validarse y no desplegarse nunca. Un despliegue puede además ser
independiente por componente. Confundirlos hace que «verificado» y «publicado» se
pronuncien igual, y son la diferencia entre una comprobación y un compromiso.

## Integración parcial

```text
Si un item necesita el merge de dos fuentes y sólo una se fusiona:

    estado global  =  INTEGRACIÓN PARCIAL          NO  =  terminado
```

`ENT` puede entonces continuar la convergencia, bloquear la publicación, ejecutar
compensación o revertir. Lo que **no** puede es declarar el item cerrado: la enmienda E2
§E2.6 lo añade a las condiciones de `b.10`.

```yaml ads:gate
id: gate:convergencia-de-fuentes
aplica_a: "todo item cuyos paquetes escribieron en una o más fuentes"
comprobaciones:
  - id: existe-integration-set
    comprueba: "existe un Integration Set que enumera todas las fuentes escritas por el item"
    como: "cruce entre las escribe_fuentes de sus paquetes y las fuentes del Integration Set"
    automatizable: si
  - id: revisiones-exactas
    comprueba: "cada fuente del Integration Set declara un commit concreto, no una rama móvil"
    como: "el campo commit está presente y es un SHA"
    automatizable: si
  - id: verificacion-con-evidencia
    comprueba: "cada ámbito de verificación declara resultado y enlace a su evidencia"
    como: "ningún resultado queda en pendiente al declarar la convergencia"
    automatizable: si
  - id: contratos-vigentes
    comprueba: "los contratos transversales que el item tocó están citados con su versión"
    como: "lectura contra el contrato vigente en el control repo"
    automatizable: parcial
  - id: sin-integracion-parcial
    comprueba: "ninguna fuente del conjunto quedó sin integrar"
    como: "estado de integración de cada fuente"
    automatizable: si
  - id: restauracion-conocida
    comprueba: "el Integration Set declara a qué combinación se vuelve si hay que revertir"
    como: "campo restaura_a resuelto, o declarado primero de su item"
    automatizable: si
evidencia:
  - "el Integration Set con sus revisiones exactas"
  - "las ejecuciones de CI de cada fuente y la conjunta"
fallo: >
  El item no cierra. Si una fuente quedó sin integrar, el estado es INTEGRACIÓN PARCIAL y
  ENT decide entre continuar la convergencia, compensar o revertir. Declarar cerrado un item
  con una fuente sin integrar hace que el sistema informe de un producto que no existe.
```

## Contract-first para cambios transversales

Cuando un cambio de dos fuentes depende de una interfaz nueva o modificada, la ruta
establece **primero** la decisión contractual:

```text
ITEM-123
    ↓
contrato de API v4, aprobado y versionado en el repositorio de control
    ↓
frontend implementa contra v4        backend implementa v4
    ↓
verificación conjunta
```

**Dos agentes no inventan el mismo JSON por separado para descubrir la discrepancia al
final.** El contrato es una decisión, no un subproducto de la implementación, y ADS
distingue el **contrato**, su **implementación** y la **evidencia de compatibilidad**.

Los contratos entre componentes —OpenAPI, JSON Schema, GraphQL, protobuf, contratos de
eventos, tipos compartidos— son conceptos globales del producto y su fuente única vive en el
repositorio de control, salvo que una herramienta concreta exija materializarlos junto al
código por una razón técnica escrita.

## Recuperación

Reanudar un trabajo multi-fuente **no puede depender de «abre la rama»**: hay varias, en
repositorios distintos, y ninguna sabe de las demás.

```text
El checkpoint sabe:   item · paquete · fuentes implicadas · refs y commits ·
                      contrato vigente · último evento significativo · siguiente acción
```

Es la prueba de reanudación de `C3` aplicada a través de la frontera del repositorio: un
agente nuevo lee el checkpoint y continúa **sin abrir ninguno de los repositorios para
adivinar en qué estado estaban**.

## Lo que este contrato no promete

```text
[ ] un commit físico atómico entre varios repositorios. Git no lo ofrece y ADS no lo finge.
[ ] que los merges de varias fuentes ocurran a la vez.
[ ] que un nombre de rama sea el vínculo entre dos fuentes.
[ ] que fusionar el PR de una fuente signifique que el producto está integrado.
```
