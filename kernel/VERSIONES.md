# Política de versiones

> **Cuatro cosas distintas se versionan aquí, y confundirlas fue el hallazgo A-12.** El
> repositorio llegó a declarar tres números para el mismo artefacto: `kernel/VERSION` decía
> `2.0.0-alpha.1`, la cabecera de `KERNEL.md` decía `1.3.0`, y el árbol de contenido del
> `README` decía `1.0.0`. No era un descuido de redacción: eran versiones **de cosas
> distintas** escritas como si fueran de la misma.

## Las cuatro versiones, y qué versiona cada una

```text
VERSIÓN DEL RELEASE      kernel/VERSION        qué copia del kernel lleva un proyecto
                         2.0.0-alpha.6         Es la que compara kernel-status.sh y la que
                                               se estampa en el commit de semilla.

LÍNEA HISTÓRICA          kernel/KERNEL.md      la constitución en prosa que sigue
                         1.5.0                 arrancando proyectos mientras el runtime no
                                               exista. NO se sube al ritmo del release:
                                               sube cuando cambia ella.

VERSIÓN NORMATIVA        docs/rediseno/        las secciones (a) y (b) aprobadas y sus
                         (a) · (b) · E1 · E2   enmiendas. No lleva semver: lleva fecha de
                                               aprobación y número de enmienda.

VERSIÓN DE ESQUEMA       esquemas/<tipo>.yaml  la forma de cada tipo canónico, con su
                         version: 1            propio contador. Un bloque escrito contra
                                               la versión 1 sigue siendo legible aunque el
                                               release cambie.
```

## Por qué conviven la línea 1.3 y la 2.0, y hasta cuándo

No es una contradicción: es una **migración declarada**.

```text
kernel/KERNEL.md 1.5.0     constitución en prosa. Es el documento de arranque de un
                           proyecto MIENTRAS EL RUNTIME NO EXISTA. La sección a.11 declara
                           qué reglas suyas quedan derogadas, sustituidas, ajustadas o
                           pendientes. Subió a 1.4.0 con la enmienda E2 —K-1 declara que el
                           sujeto de las tres capas es el PRODUCTO, y G29 queda revisada
                           para aplicarse por fuente—, y a 1.5.0 con el barrido semántico
                           que alcanza a K0.6, K0.8, G04, G12, G26, G27, G38, G39, los
                           entregables del Circuito 0, G46 y G48: E2 tenía precedencia, pero
                           esas reglas seguían enseñando el modelo anterior.

kernel/operativo/ 2.0      el contenido operativo que ese runtime consumirá: capacidades,
                           roles, métodos, prompts, gates, circuitos y validadores.

CONVIVEN                   porque lo segundo todavía no tiene quien lo ejecute. El día que
                           el runtime exista, KERNEL.md se reescribe como índice delgado
                           sobre kernel/operativo/ — y eso es un item SIS, no una nota.
```

La decisión y su condición de revisión están registradas como **O2** en
[`../docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`](../docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md).

## Reglas

```text
1  Cada punto de entrada —README, START_HERE, KERNEL.md, CHANGELOG— cita la versión de la
   COSA de la que habla, y dice de cuál de las cuatro se trata.

2  kernel/VERSION es la única fuente de la versión del release. Nadie la repite: se lee.

3  La entrada más reciente del CHANGELOG coincide con kernel/VERSION. Si no coinciden, o
   falta la entrada o falta el cambio de versión.

4  Subir el release NO sube la línea histórica, y al revés. Son contadores distintos.

5  Ningún documento declara una versión de un artefacto que no esté en esta tabla.
```

Lo comprueba [`validadores/comprobar_versiones.py`](operativo/validadores/comprobar_versiones.py)
en la prueba **T152**, y una infracción deliberada lo demuestra en `comprobar_negativos.py`.
