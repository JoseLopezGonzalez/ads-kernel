# Especialización de Diseño para web app

Amplía el sistema de excelencia del kernel
([`kernel/operativo/diseno/`](../../../kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md)).
**No lo sustituye ni rebaja sus dos gates.**

## Qué añade la web a la rúbrica de excelencia visual

Los nueve ejes siguen siendo los mismos. Lo que este pack aporta es **qué cuenta como
evidencia** en un navegador:

| eje | evidencia adicional exigida en web |
|---|---|
| `personalidad` | comparación contra dos productos web de la misma categoría, en el mismo tamaño de ventana |
| `sistema` | extracción de los valores computados en el navegador, no de los declarados en el código |
| `acabado` | captura a tamaño real en cada motor de la matriz, con zoom en las juntas |
| `respuesta` | grabación con la preferencia de movimiento reducido activada, además de la normal |
| `jerarquia` | prueba de entrecerrado sobre la superficie con el volumen de datos REAL, no de ejemplo |
| `fidelidad` | comparación en los dos tamaños extremos de la matriz, no sólo en uno |

## Lo que la web hace fácil y hay que vigilar

```text
LA TENTACIÓN                   POR QUÉ FALLA
usar los valores por defecto   el eje `intencion` queda en rechazo: no hay decisión detrás
de la biblioteca de estilos

resolver la densidad quitando  el usuario que usa esto a diario pierde su herramienta
información

crear la jerarquía sólo con    al desactivar el color no queda orden de lectura, y hay
color                          usuarios que lo desactivan

animar todo lo que aparece     el eje `respuesta` mide si el movimiento EXPLICA algo;
                               decorar hace el producto más lento sin serlo

diseñar tres tamaños fijos     el tamaño de ventana es continuo, y entre los tres hay
                               composiciones rotas que nadie miró
```

## Superficies web que casi siempre se olvidan

Cada una es una superficie con sus cinco estados, no un detalle:

```text
· la vista de impresión o exportación
· la superficie de error del servidor
· la superficie sin permisos
· el resultado de búsqueda vacío
· el estado de sesión caducada
· la primera visita, sin datos todavía
```

Están en el inventario de `DIS/Reconstruccion` y en la lista de estados de `gate:usabilidad`.
Que sean feas es la norma; que **no estén diseñadas** es un incumplimiento.

## Densidad: el patrón que este pack aporta al sistema de diseño

```text
UNA LÍNEA DOMINA        un dato por fila lleva el peso; el resto se atenúa hasta que se
                        necesita. La jerarquía la crea el CONTRASTE DE PESO, no el color.

EL TEXTO LARGO REAL     se resuelve, no se evita. Truncar sin dar acceso al valor completo
                        es un fallo de usabilidad, no una decisión de diseño.

EL RITMO VERTICAL       constante hace legible la densidad alta. Es lo que separa una tabla
                        trabajada de una hoja de cálculo con bordes.
```

Este patrón se declara en la memoria de diseño del proyecto con su alcance y sus criterios
comprobables, como cualquier otro (a.8). El pack aporta el conocimiento; **el patrón es del
proyecto**.
