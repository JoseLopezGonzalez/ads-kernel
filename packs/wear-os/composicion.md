# wear-os — ejemplos de composición de equipo

## Caso 1 · superficie principal del reloj, proyecto nuevo

```text
La escala devuelve N4 → composicion:dis-proyecto-nuevo

CLAVE                     la dirección visual es COMÚN con el móvil si existe. Lo que el
                          reloj define es su propia escala, densidad y componentes.
ROLES DEL KERNEL          los once de dis-proyecto-nuevo
ROLES DEL PACK            wear:DIS/lectura-de-un-vistazo · wear:CON/energia-y-estados
EXPLORACIÓN               las tres direcciones se exploran AL TAMAÑO DEL RELOJ, nunca
                          escaladas desde una pantalla grande
GATES                     los dos del kernel + gate:wear-vistazo + gate:wear-ambiental +
                          gate:wear-consumo
EVIDENCIA                 fotografía al sol · grabación andando · consumo medido sin cargador
```

## Caso 2 · complicación o tile que muestra un dato

```text
Es una superficie propia, no un fragmento de otra. La escala devuelve N1 o N2.

ROLES DEL KERNEL          DIS/diseno-visual · DIS/sistema-de-diseno · DIS/critica-visual ·
                          DIS/revision-de-fidelidad
ROLES DEL PACK            wear:DIS/lectura-de-un-vistazo · wear:CON/energia-y-estados
DECISIÓN PREVIA           qué muestra, con qué frecuencia se actualiza y a dónde lleva
GATES                     gate:wear-vistazo + gate:wear-consumo
ESTADOS OBLIGATORIOS      sin datos · sin conexión · error, además de los cinco del kernel
```

## Caso 3 · el producto pasa de acompañante a independiente

```text
Es un DIR: sustituye una decisión de producto ya implementada.

PROPIETARIO GLOBAL        la capacidad propietaria de la decisión que se sustituye — aquí
                          PRD, porque la independencia es alcance de producto
OBLIGATORIO EN EL DIR     radio de impacto medido por ARQ · el Owner en el punto de
                          decisión · registro de qué decisión sustituye · items derivados ·
                          VER:decision
ROLES DEL PACK            participan en modo consulta: qué cambia en consumo y en estados
NO OCURRE AQUÍ            la implementación. Va en los items derivados, y son
                          paralelizables entre sí.
```
