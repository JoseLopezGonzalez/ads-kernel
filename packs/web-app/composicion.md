# web-app — ejemplos de composición de equipo

Los roles del pack **se añaden** a la composición que el algoritmo de `C4` eligió. Estos son
tres casos completos.

## Caso 1 · listado operativo nuevo, con tabla densa

```text
La escala de novedad devuelve N2 → composicion:dis-feature-visual

ROLES DEL KERNEL          DIS/direccion-artistica · DIS/investigacion-ux ·
                          DIS/diseno-visual · DIS/diseno-interaccion ·
                          DIS/sistema-de-diseno · DIS/prototipado ·
                          DIS/critica-visual · DIS/validacion-de-uso ·
                          DIS/revision-de-fidelidad
ROL AÑADIDO POR EL PACK   web:DIS/densidad-y-tablas
COMBINACIONES             DIS/diseno-visual + DIS/diseno-interaccion en un agente
                          web:DIS/densidad-y-tablas NO se combina con DIS/critica-visual
GATES QUE DEBE PASAR      gate:usabilidad · gate:excelencia-visual ·
                          gate:web-accesibilidad · gate:web-rendimiento-percibido
EVIDENCIA DEL PACK        capturas en dos motores y dos tamaños extremos ·
                          recorrido con teclado solo · el nombre más largo real resuelto
```

## Caso 2 · formulario largo con envío contra la red

```text
La escala devuelve N1 → composicion:dis-caso-nuevo, más construcción

ROLES DEL KERNEL          DIS/diseno-interaccion · DIS/diseno-visual ·
                          DIS/sistema-de-diseno · DIS/critica-visual ·
                          CON/implementacion · VER/dosier
ROL AÑADIDO POR EL PACK   web:CON/estados-de-red
INDEPENDENCIA             VER/dosier de CON/implementacion Y de web:CON/estados-de-red
GATES QUE DEBE PASAR      los dos del kernel + gate:web-accesibilidad +
                          gate:web-estados-de-red
CONSULTA OBLIGATORIA      DOM: ¿el envío es idempotente? Sin esa respuesta no se reintenta
```

## Caso 3 · corrección de contraste en un patrón vigente

```text
La escala devuelve N0 → composicion:dis-extension-de-patron

ROLES                     DIS/diseno-visual · DIS/revision-de-fidelidad
ROL DEL PACK              ninguno: no hay tabla ni operación de red
GATES                     gate:excelencia-visual (eje acabado) + gate:web-accesibilidad
                          (contraste y texto ampliado)
EXPLORACIÓN               ninguna: N0 aplica el patrón. La calidad NO se relaja.
```

## La regla que estos tres ejemplos ilustran

```text
El pack NO cambia la composición: la AMPLÍA con roles de su materia, y AÑADE gates.
Ninguna composición del kernel se sustituye, y ninguna autoridad se redistribuye.
```
