# Especialización de Diseño para móvil

Amplía el sistema del kernel; no lo sustituye.

## Evidencia adicional por eje

| eje | evidencia adicional exigida en móvil |
|---|---|
| `acabado` | captura a tamaño real en el dispositivo de mayor y de menor densidad de la matriz |
| `respuesta` | grabación en el dispositivo MÁS LENTO: es donde el movimiento se rompe |
| `fidelidad` | comparación en dispositivo real, nunca en emulador |
| `jerarquia` | prueba de entrecerrado con el teclado abierto, además de sin él |
| `sistema` | comprobación de que la escala tipográfica sobrevive al texto ampliado del sistema |

## Lo que el móvil hace fácil y hay que vigilar

```text
LA TENTACIÓN                    POR QUÉ FALLA
diseñar en la pantalla grande   el pulgar no llega, y eso sólo se ve en el dispositivo grande
del ordenador

validar en emulador             el movimiento va fluido donde no va a ejecutarse

resolver el camino feliz del    la mayoría de los fallos reales están en denegado y revocado
permiso

usar el gesto como única vía    quien no lo conoce no encuentra la función y no sabe que existe

diseñar sin abrir el teclado    media pantalla desaparece y el botón de confirmar con ella
```

## El uso interrumpido como criterio de diseño

Un móvil se usa **entre otras cosas**. Eso cambia la forma:

```text
[ ] volver tras una interrupción deja al usuario donde estaba, no en el inicio
[ ] una tarea larga se puede abandonar y retomar, o dice expresamente que no
[ ] lo escrito sobrevive a todo: a la suspensión, a la terminación y a la llamada entrante
```

Es una exigencia de forma tanto como de construcción: si la interfaz no comunica que lo
escrito está a salvo, el usuario no lo sabe aunque lo esté.
