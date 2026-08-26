# Qué es un pack, y qué tiene prohibido hacer

<!-- ads-lint: permitir-vocabulario-prohibido -->

Un pack es el **saber hacer de una CLASE de proyecto**. Existe porque hay conocimiento que
no es universal pero tampoco es de un solo proyecto: toda aplicación web necesita
presupuestos de rendimiento percibido; todo reloj necesita política de batería y lectura de
un vistazo. Sin la capa intermedia, eso se reescribe en cada proyecto o contamina el kernel.

```text
KERNEL    cómo trabaja la organización          idéntico en todos los proyectos
PACK      saber hacer de una CLASE              reusable entre proyectos del mismo tipo
PROFILE   qué se construye AQUÍ                 único por proyecto
```

## Un pack AMPLÍA. No sustituye.

```text
PUEDE     añadir restricciones de plataforma que el kernel no puede conocer
PUEDE     añadir ROLES ESPECIALIZADOS con prefijo de espacio de nombres
PUEDE     añadir EXTENSIONES a métodos del kernel: pasos adicionales con su condición
PUEDE     añadir GATES adicionales, que se suman a los del kernel
PUEDE     añadir artefactos, matrices de entorno, pruebas y antipatrones propios
PUEDE     especializar el sistema de excelencia de Diseño para su medio

NO PUEDE  redefinir un contrato universal del kernel
NO PUEDE  rebajar un gate del kernel, ni saltárselo
NO PUEDE  quitar autoridad a un rol del kernel ni dársela a uno suyo
NO PUEDE  sombrear una capacidad del kernel: los quince códigos están reservados
NO PUEDE  rebajar las exigencias de un perfil de agente del kernel
```

Lo que **sí** puede hacer un pack cuando necesita cambiar comportamiento del kernel es
declararlo como **override en el PROFILE** (K0.7), con justificación, alcance y condición de
revisión. Un override es una decisión del proyecto, no una propiedad del pack.

## Espacio de nombres obligatorio

```text
capacidad de pack   <pack>:<COD>          wear:AMB
rol de pack         <pack>:<CAP>/<slug>   wear:DIS/lectura-de-un-vistazo
gate de pack        gate:<pack>-<slug>    gate:wear-consumo
```

Con prefijo, la colisión de identificador es **imposible por construcción**, y una extensión
**no puede** sombrear una capacidad del kernel (a.4).

## Cómo se aplica un rol de pack

Un rol especializado **se añade** a la composición que el algoritmo de
[`C4`](../kernel/operativo/contratos/C4-MATERIALIZACION.md) eligió. No sustituye a ningún rol
del kernel y no se queda con su autoridad: **añade materia, no redistribuye poder**.

## Los tres packs de esta versión

| pack | clase de proyecto | dónde vive |
|---|---|---|
| `web-app` | aplicación web con navegador como entorno | `packs/web-app/PACK.md` |
| `mobile-app` | aplicación móvil, sin atarse a una tecnología | `packs/mobile-app/PACK.md` |
| `wear-os` | reloj: pocos segundos, pantalla mínima, batería | `packs/wear-os/PACK.md` |

> **Las rutas no se enlazan aquí a propósito.** En un proyecto instalado existe únicamente
> el directorio de los packs que ese proyecto instaló; enlazar los tres dejaría enlaces
> rotos en toda organización que no use los tres. `./tooling/new-project.sh` sin argumentos
> lista los instalables.

Composición entre ellos, precedencia y detección de conflictos:
[`COMPOSICION.md`](COMPOSICION.md).

**El pack de ERP queda expresamente fuera de alcance** de esta iteración.

## Lo que NO va en un pack

```text
NO VA   una tecnología concreta: eso pertenece al PROFILE del proyecto, o a una
        extensión específica de tecnología, nunca al pack universal de la clase
NO VA   una preferencia del Owner
NO VA   un valor numérico que dependa del producto: el pack fija QUÉ se mide y en qué
        entornos; el PROFILE fija el umbral cuando el pack no puede conocerlo
```

El test para decidir si algo va al pack o al profile es el de contaminación de K0.10:
**¿sería igual de cierto en otro proyecto de la misma clase?** Si sí, pack. Si sólo aquí,
profile.
