# Especialización de Diseño para reloj

Amplía el sistema del kernel. **La dirección visual es común con el móvil cuando ambos
existen**: lo que el reloj define es cómo se expresa esa dirección en dos segundos.

## Evidencia adicional por eje

| eje | evidencia adicional exigida en reloj |
|---|---|
| `jerarquia` | prueba de entrecerrado sobre captura al tamaño real, y cronometraje del vistazo |
| `acabado` | fotografía de la pantalla real, no captura del sistema: el reflejo y el brillo forman parte |
| `respuesta` | grabación en reloj real: la fluidez depende del hardware más que en ningún otro medio |
| `sistema` | escala tipográfica PROPIA del reloj, derivada de la común pero no heredada |
| `fidelidad` | comparación en reloj físico, incluido el estado ambiental |
| `personalidad` | comparación contra dos aplicaciones de reloj de la misma categoría, no contra móviles |

## La regla que gobierna toda esta materia

```text
UN RELOJ NO ES UN MÓVIL PEQUEÑO.

No se diseña reduciendo: se diseña desde la pregunta de cuántos segundos dura el uso.
La dirección visual se hereda; la composición, la densidad y la escala, no.
```

## Lo que cambia respecto al móvil

```text
MÓVIL                                RELOJ
uso de minutos                       uso de segundos
se mira                              se ojea
una pantalla con varias acciones     una pantalla, una acción
texto legible                        número o icono legible sin enfocar
apagado                              ESTADO AMBIENTAL, que es una superficie
teclado disponible                   no hay entrada de texto
la batería importa                   la batería DECIDE
```

## Componentes propios del reloj

Se declaran en la memoria de diseño del proyecto, con su alcance y sus criterios, como
cualquier otro patrón (a.8). Los que este pack anticipa:

```text
· dato dominante        el número o estado que se lee sin enfocar
· lista recorrible      pensada para la corona, con posición siempre visible
· confirmación breve    para acciones destructivas, alcanzable sin precisión fina
· estado ambiental      variante atenuada de la superficie, con la información principal
· acuse táctil          patrón de vibración con significado declarado
```

## Validación: cómo se usa de verdad

```text
ANDANDO                    no sentado en una mesa
AL SOL                     no sólo en interior
CON EL RELOJ MÁS PEQUEÑO   de la matriz
CON EL DEDO PUESTO         mirando qué tapa al pulsar
CRONOMETRADO               el vistazo dura lo que se declaró, o no dura
```

Cualquier validación que no cumpla estas cinco condiciones **no es evidencia** para este
pack: es una comprobación de que la pantalla se dibuja.
