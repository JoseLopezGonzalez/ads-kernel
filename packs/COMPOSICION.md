# Composición de packs: qué ocurre cuando un proyecto usa varios

<!-- ads-lint: permitir-vocabulario-prohibido -->

Un proyecto puede instalar más de un pack. Es el caso normal en cuanto hay una web y una
aplicación móvil, o un móvil y un reloj.

## Las tres combinaciones previstas

```text
web-app + mobile-app                un producto con superficie web y superficie móvil
mobile-app + wear-os                un móvil con acompañante en el reloj
web-app + mobile-app + wear-os      los tres, con el móvil como pieza central
```

## Regla de superficie: cada pack gobierna la suya

```text
Un pack gobierna las SUPERFICIES DE SU MEDIO. No las de los demás.

Un paquete de trabajo pertenece a UNA superficie, y por tanto a UN pack, salvo que
toque explícitamente dos —y entonces la regla de conflicto de abajo decide.
```

Lo que es común —modelo de dominio, contratos, criterio de éxito, dirección visual del
producto— **no pertenece a ningún pack**: pertenece al kernel y a las capacidades. Un pack
que intentara gobernar el modelo de dominio estaría redefiniendo un contrato universal, y
eso está prohibido.

## Precedencia cuando dos packs dicen algo sobre lo mismo

Se evalúa en orden, y gana la primera que aplica:

```text
P1  LO MÁS RESTRICTIVO GANA, cuando ambos hablan de la misma propiedad medible.
    Un tamaño mínimo de objetivo táctil de 48 y otro de 44 → gana 48.
    Un contraste mínimo de 4.5 y otro de 7 → gana 7.
    Motivo: relajarlo perjudicaría al usuario del medio más exigente.

P2  EL PACK DE LA SUPERFICIE GANA, cuando la propiedad no es comparable.
    La navegación de un reloj no se decide con la regla de navegación de una web.

P3  EL KERNEL GANA, cuando lo que está en juego es un contrato universal.
    Ningún pack rebaja un gate del kernel ni redistribuye autoridad.

P4  SI NINGUNA APLICA, hay CONFLICTO: se registra y lo arbitra el PROFILE.
    Sin arbitraje declarado, la organización NO es conforme (T18).
```

## Detección de conflictos

`SIS/Conformidad` la ejecuta al instalar un pack nuevo y en cada auditoría:

```text
1  IDENTIFICADORES   dos packs no pueden declarar el mismo identificador.
                     Imposible por construcción: cada uno usa su prefijo.

2  MISMA PROPIEDAD   dos packs fijan un valor distinto para la misma propiedad medible
                     → se aplica P1 y se registra cuál ganó y por qué

3  MISMA MATERIA     dos roles de packs distintos reclaman la misma materia sobre la
                     MISMA superficie
                     → conflicto real: lo arbitra el PROFILE

4  AUTORIDAD         un rol de pack reclama autoridad que un rol del kernel ya tiene
                     → PROHIBIDO. El instalador lo rechaza (T18)

5  GATE REBAJADO     un pack declara una comprobación que sustituye a una del kernel en
                     lugar de sumarse
                     → PROHIBIDO. Los gates de pack SUMAN
```

## Roles especializados sin duplicar autoridad

```text
CORRECTO    wear:DIS/lectura-de-un-vistazo AÑADE la materia «se lee en dos segundos»
            a la composición de Diseño. DIS/direccion-artistica sigue decidiendo la
            dirección; el rol de pack aporta la restricción del medio.

INCORRECTO  un rol de pack que decidiera la dirección visual del reloj por su cuenta:
            habría dos direcciones artísticas y el producto dejaría de ser uno.
```

Cuando dos packs aportan roles a la misma composición, **ambos entran**. Su materia es
distinta porque su superficie es distinta. Si de verdad reclaman lo mismo sobre la misma
superficie, es el conflicto 3 y lo arbitra el PROFILE.

## Las tres combinaciones, en concreto

### web-app + mobile-app

```text
COMPARTEN     dominio, contratos, criterio de éxito, y la DIRECCIÓN VISUAL del producto
NO COMPARTEN  matriz de entornos, medios de entrada, presupuestos de rendimiento,
              patrones de navegación
DIRECCIÓN     UNA sola, con dos aplicaciones distintas. El sistema de diseño declara qué
              es común —tipografía, color, personalidad— y qué es propio de cada medio.
RIESGO REAL   que la web y el móvil evolucionen por separado hasta parecer dos productos.
              Lo vigila la revisión de consistencia de DIS/sistema-de-diseno, y es un
              hallazgo del eje `personalidad` cuando ocurre.
```

### mobile-app + wear-os

```text
COMPARTEN     dominio, contratos, y la relación de dependencia entre las dos aplicaciones
NO COMPARTEN  prácticamente nada de forma: un reloj no es un móvil pequeño
ENTREGA       COORDINADA: las dos versiones tienen que poder convivir. Un reloj con una
              versión y un móvil con otra es el estado NORMAL, no la excepción.
RIESGO REAL   diseñar el reloj como una reducción del móvil. Es el antipatrón central del
              pack wear-os, y su rol de lectura de un vistazo existe para impedirlo.
```

### los tres

```text
El móvil es la pieza central: comparte dominio con la web y es el acompañante del reloj.

REGLA         ninguna funcionalidad se diseña una vez y se «adapta» dos veces. Cada
              superficie se decide en su medio, sobre una dirección visual común.

ENTREGA       tres cadencias distintas. La coordinación obligatoria es móvil↔reloj; la web
              se entrega por su cuenta, salvo cambio de contrato compartido.
```

## Qué declara el PROFILE cuando hay varios packs

```text
[ ] qué packs están instalados y en qué versión
[ ] el arbitraje de todo conflicto de materia detectado (conflicto 3)
[ ] los valores que P1 resolvió, con cuál ganó
[ ] los overrides declarados (K0.7), con justificación y condición de revisión
```

Sin esto, la prueba T18 falla y la organización instalada **no es conforme**.
