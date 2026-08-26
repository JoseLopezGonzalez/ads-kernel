# ENMIENDA E2 a las SECCIONES (a) y (b) — un producto no es un repositorio

```text
identificador   E2
enmienda a      docs/rediseno/a-CAPACIDADES-APROBADA.md
                docs/rediseno/b-RECORRIDO-APROBADA.md
fecha           2026-08-26
autoridad       Owner
motivo          decisión de arquitectura multi-repositorio, aprobada para implementación
origen          ADS-ARQUITECTURA-MULTIREPO-APROBADA.md §20 §21 §31 §33 §34 §35 §80 §97
estado          APROBADA
```

> **Qué es este documento.** Las secciones (a) y (b) permanecen **íntegras y sin
> reescribir**. Esta enmienda es el único texto que las modifica, y lo hace por sustitución
> explícita. Un lector de (a) o (b) que llegue a cualquiera de los puntos de abajo debe leer
> aquí.
>
> **Lo que esta enmienda NO hace:** no altera el catálogo de capacidades, ni la autoridad de
> ninguna de ellas, ni los frenos de a.7, ni el contrato de veto, ni la condición compuesta
> de paralelismo, ni los estados de b.2, ni la función de estado global de b.4, ni el cierre
> de b.10, ni las diez rutas de b.16.

---

## E2.0 — La decisión

```text
PRODUCTO       !=   REPOSITORIO GIT
ADS PROJECT    !=   REPOSITORIO DE CÓDIGO
```

Un ADS Project gobierna **un producto**. Ese producto puede estar repartido entre `0..N`
repositorios Git independientes. El ADS Project vive en un **repositorio de control**
propio, y la composición del producto se declara en un manifiesto versionado,
`SOURCES.toml`, que es su fuente única.

Los catorce principios normativos que la decisión introduce viven en
[`C6`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md). Esta enmienda
sólo declara **qué texto de (a) y (b) deja de regir tal como estaba escrito**.

---

## E2.1 — a.9: «los ficheros del repo» pasa a ser el repositorio de control

### Texto que sustituye

| en (a) | decía | pasa a decir |
|---|---|---|
| a.9, encabezado | «Requisito del Owner: **el estado operativo ES los ficheros del repo**, legibles directamente, sin informe intermedio.» | «Requisito del Owner: **el estado operativo ES los ficheros del repositorio ADS de control**, legibles directamente, sin informe intermedio.» |

**Qué NO cambia.** El requisito es el mismo y se refuerza: el estado sigue siendo ficheros
legibles sin herramienta, versionados, sin informe intermedio. Lo único que se precisa es
**cuál** de los repositorios de un producto los contiene.

**Los seis invariantes `I1`–`I6` quedan intactos**, y ganan alcance:

```text
I1  PROPIEDAD INEQUÍVOCA    se aplica también al reparto entre control repo y sources:
                            la verdad de organización es del control repo, la verdad de
                            una implementación es de su source. Ver la regla de autoridad
                            de C6.
I5  SIN DUPLICIDAD          prohíbe expresamente copiar PROFILE, PROJECT, estado, items,
    EDITABLE                memoria, ADR globales, contratos maestros, kernel o packs
                            dentro de una source. Antes no había dónde copiarlos.
```

**Un estado global PUEDE referenciar una revisión de otra source. NO puede copiar su
contenido.** Es la misma regla de fuente única, aplicada a través de la frontera del
repositorio.

---

## E2.2 — a.5: un paquete puede atravesar varias sources

### Texto que amplía

En a.5, *«El paquete y lo que declara»*, la **DECLARACIÓN DE ACOPLAMIENTO** añade dos
campos a los seis que ya tenía. El bloque de (a) declara literalmente que los nombres
definitivos se fijan más adelante; éstos son de esa naturaleza y no sustituyen a ninguno:

```text
  lee_fuentes:      qué sources necesita como CONTEXTO, sin autoridad para modificarlas
  escribe_fuentes:  qué sources puede MODIFICAR
```

**Reglas:**

```text
1  Lectura y escritura son permisos DISTINTOS. Un paquete que adapta el frontend a una
   API existente lee `backend` y escribe `frontend`. Inspeccionar no autoriza a tocar.

2  NO se impone «un paquete, una source». Un repositorio es una frontera física, no
   necesariamente la frontera correcta del trabajo.

3  DSP prefiere el ALCANCE MÍNIMO que mantenga el trabajo coherente. Si basta
   `escribe_fuentes: [frontend]`, no se autoriza escritura en todo el producto.

4  Y NO se fragmenta artificialmente un trabajo coherente sólo porque existan dos
   repositorios. La regla 2 y la regla 3 se leen juntas.

5  Un paquete cuyas `escribe_fuentes` o `lee_fuentes` no estén materializadas queda
   `esperando-dependencia` — b.2, sin estado nuevo — hasta que lo estén. La ausencia de
   una source bloquea SÓLO los paquetes que la requieren.
```

**Efecto sobre la condición compuesta de paralelismo.** No la sustituye: la instrumenta. El
`aislamiento físico` que a.5 exige se comprueba ahora también entre sources, y dos paquetes
cuyas `escribe_fuentes` son disjuntas satisfacen esa componente sin más análisis. **Las
demás componentes siguen exigiéndose igual**: dependencias, autoridad sobre decisiones,
contratos compartidos, versiones de entrada y estrategia de integración. Dos paquetes que
escriben en sources distintas y tocan el mismo contrato **no** son paralelizables.

---

## E2.3 — a.10: el checkpoint referencia revisiones, no las copia

### Texto que amplía

El formato de checkpoint de a.10 conserva sus campos. `based_on` **gana forma explícita**
para múltiples fuentes, que es el uso que ya tenía y que ahora es obligatorio poder
expresar:

```text
based_on:    backend@<sha>
             api-contract@v4
```

Y el checkpoint de un paquete con `escribe_fuentes` registra, por cada source tocada:

```text
sources:
  <source-id>:  rama <ref> · commit <sha> · push <sí|no> · PR <ref|ninguno> · CI <estado>
```

**No se copia el contenido de otra source al checkpoint.** Se referencia su revisión
exacta. Es la regla 1 de a.10 —enlaces, no copias— aplicada a través de la frontera del
repositorio.

**Motivo.** La reanudación de un trabajo multi-source no puede depender de «abre la rama»:
hay varias, en repositorios distintos, y ninguna de ellas sabe de las demás. Lo que sabe es
el checkpoint.

---

## E2.4 — a.11: `G29` pasa de «sobrevive» a «revisada»

### Texto que sustituye

| en (a) | decía | pasa a decir |
|---|---|---|
| a.11, fila **Ajustadas** | `G29` figuraba entre las reglas que **SOBREVIVEN** intactas, en el mapa del rediseño | **`G29` queda REVISADA.** Su modelo de rama principal protegida, unidad de trabajo aislada, commit y push autónomos, PR como punto de convergencia, CI como autoridad automática, cuatro niveles de autoridad de merge, `merge ≠ release`, tags y rollback **se conserva íntegro y se aplica POR SOURCE**. Lo que se deroga es la relación implícita `un item → una rama → un PR` como relación universal. El contrato completo vive en [`C7`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) |

**La relación correcta:**

```text
item/package
    ↓
0..N source changes
    ↓
por cada source:  rama/worktree · commits · push · PR · CI
    ↓
Integration Set — convergencia lógica ADS
```

`main` sigue representando el último estado integrado y aceptado **de cada source**. El
estado del producto **no vive en ninguna rama**: se calcula en el control repo.

---

## E2.5 — b.1: la identidad de un item no depende de un repositorio

### Texto que precisa

b.1 declara: *«ITEM — la COSA sobre la que se trabaja. Identidad persistente en el
proyecto.»* Se precisa, sin sustituir:

> La identidad de un item es del **producto**, no de un repositorio. Un item puede afectar a
> `frontend`, `backend` y `mobile` y seguir siendo **un solo item**. Ni el proceso, ni la
> ruta, ni el criterio de cierre se fragmentan porque el código esté repartido.

**Y la regla de proceso único no se toca.** Un item sigue teniendo exactamente un proceso en
cada momento. Que su trabajo atraviese tres repositorios no lo convierte en tres items, del
mismo modo que atravesar tres capacidades no lo convertía en tres.

---

## E2.6 — b.10: qué significa cerrar un item multi-source

### Texto que amplía

El cierre de b.10 exige que todas las obligaciones vigentes estén **resueltas** y que
ninguna se apoye en una capa `invalidada`. Se añade una condición, del mismo tipo que las
que ya tiene:

```text
Un item con paquetes que escribieron en varias sources NO cierra mientras su convergencia
no esté declarada y evidenciada en un INTEGRATION SET.

Que el PR de una source se haya fusionado NO significa que el producto esté integrado.
Si una parte se fusionó y otra no, el estado es INTEGRACIÓN PARCIAL, no `cerrado`.
```

**Motivo.** Git no ofrece un commit físico multi-repositorio, y ADS **no debe fingir uno**.
Lo que sí puede afirmar, con evidencia, es que una combinación exacta de revisiones fue
probada e integrada conjuntamente. Eso es el Integration Set, y es atomicidad **lógica de
producto**, no atomicidad Git.

---

## E2.7 — Lo que esta enmienda deja expresamente abierto

```text
formato final del runtime distribuido · locks multi-agente · scheduler · colas ·
servicio cloud · estrategia universal de release · despliegues parciales ·
almacenamiento externo de eventos · mirrors · adaptadores de proveedor completos
```

Ninguno de esos puntos es necesario para que la arquitectura base funcione, y ninguno
autoriza a retrasarla. La disposición física del estado sigue perteneciendo a la sección
(g), y **E2 no la cierra**: sólo fija en qué repositorio vive.

---

## E2.8 — Pruebas de conformidad de esta enmienda

Los escenarios están en
[`pruebas/T159-T170-multirepo.md`](../../kernel/operativo/pruebas/T159-T170-multirepo.md), y
su estado real —como el de todas— en
[`pruebas/REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md).
