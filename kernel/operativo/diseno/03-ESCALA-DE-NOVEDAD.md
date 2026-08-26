# La escala de novedad: cuánta exploración exige cada trabajo

<!-- ads-lint: permitir-vocabulario-prohibido -->

`C-DIS` (b.16) decide **si** Diseño se activa. Esta escala decide **qué método ejecuta y
cuánto explora**. Son dos preguntas distintas y la segunda no puede quedar al criterio del
agente: si queda, una corrección de espaciado acaba convocando el mismo procedimiento que
una pantalla nueva, o —lo que es peor— una pantalla nueva se resuelve con el esfuerzo de
una corrección de espaciado.

## Cómo se calcula el nivel

Se responden las seis preguntas **en orden**. El nivel es el de la **primera** que se
responde «sí».

```text
N4  FUNDACIÓN
    ¿No existe memoria:vision-artistica, o está vacía?
    ¿O un item DIR aprobado sustituye la dirección visual del producto?
        → método DIS/Fundacion · exploración SIN TECHO de sesiones

N3  RECONSTRUCCIÓN
    ¿Existe producto construido y NO existe dirección visual escrita que lo explique?
        → método DIS/Reconstruccion · inventario completo antes de proponer nada

N2  DIRECCIÓN NUEVA EN UNA SUPERFICIE
    ¿La superficie no está cubierta por ningún patrón vigente,
     Y es premium, o introduce una interacción o un movimiento que no existía?
        → método DIS/Evolucion en su rama DIVERGENTE · mínimo TRES direcciones

N1  CASO NUEVO DENTRO DEL SISTEMA
    ¿Existen patrones vigentes, pero ninguno cubre este caso con su alcance declarado?
        → método DIS/Evolucion en su rama de EXTENSIÓN · mínimo DOS alternativas

N0  EXTENSIÓN DE PATRÓN VIGENTE
    ¿Un patrón vigente cubre el caso, se cumplen sus criterios comprobables y no se
     introduce nada fuera de su alcance?
        → método DIS/Evolucion en su rama de APLICACIÓN · CERO exploración
        → se aplica el patrón y se registra que se aplicó

    Si ninguna se cumple, el nivel es N1 por defecto: ante la duda entre aplicar y
    explorar, se explora. El coste de explorar de más es una sesión; el de explorar de
    menos es un producto genérico.
```

> Las condiciones son **comprobables leyendo la memoria de diseño**, no interpretables. La
> pregunta de N0 es literalmente el test de «extiende un patrón aprobado» de a.8.

## Qué exige cada nivel

| | exploración mínima | crítica visual | Owner | memoria que se actualiza |
|---|---|---|---|---|
| **N4** | sin techo; mínimo tres territorios creativos con moodboard | obligatoria en divergencia y en convergencia | obligatorio: aprueba la dirección | visión · principios · referencias · sistema · decisiones |
| **N3** | inventario completo antes de proponer; mínimo dos propuestas de evolución | obligatoria | obligatorio: aprueba la reconstrucción | referencias · sistema · componentes · decisiones · deuda · historial |
| **N2** | mínimo tres direcciones distintas entre sí | obligatoria | obligatorio: primera instancia de patrón visual (a.8) | sistema · componentes · decisiones · movimiento si lo hay |
| **N1** | mínimo dos alternativas comparadas contra los principios | obligatoria | opcional acumulada: va a la cola de lotes | componentes · decisiones |
| **N0** | ninguna | **no obligatoria**; el gate de fidelidad sigue aplicando | ninguna | registro de aplicación del patrón |

### «Distintas entre sí» es comprobable

Dos direcciones son distintas si difieren en **al menos dos** de estas cinco dimensiones:

```text
[ ] estructura de la composición          dónde vive cada cosa
[ ] jerarquía                             qué domina y cómo se consigue que domine
[ ] sistema tipográfico                   familia, escala o uso del peso
[ ] tratamiento del color                 rol del color en la jerarquía, no la paleta
[ ] densidad y ritmo                      cuánto cabe y cómo respira
```

Tres propuestas que sólo cambian la paleta **son una sola dirección con tres pinturas**, y
el gate las rechaza por no cumplir el mínimo de exploración. Esta comprobación es del rol
`DIS/critica-visual`, y la ejecuta en la fase divergente, **antes** de la convergencia.

## Por qué N0 existe

Sin N0, cada ajuste dentro de un patrón aprobado convocaría exploración: eso es ceremonia
inútil y es el modo de fallo (b) de a.7. Con N0, el sistema **aplica lo aprobado sin
volver a discutirlo**, que es justamente para lo que sirve tener un sistema de diseño.

```text
N0 NO SIGNIFICA trabajo barato ni acabado inferior.
   El gate de excelencia visual se aplica igual, y el eje `acabado` no se relaja.
   Lo que N0 elimina es la EXPLORACIÓN, no la CALIDAD.
```

## Registro obligatorio

Todo paquete de DIS declara en su checkpoint:

```text
nivel_de_novedad: N0 | N1 | N2 | N3 | N4
motivo:           la pregunta de la escala que se respondió «sí», citada
```

Un paquete de DIS sin nivel declarado no puede cerrar: es una comprobación de
`gate:excelencia-visual` a través de la evidencia del dictamen, y la revisión adversarial
la busca expresamente, porque **bajar el nivel es la forma más silenciosa de abaratar el
diseño**.
