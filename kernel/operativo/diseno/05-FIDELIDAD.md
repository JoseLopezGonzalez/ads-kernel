# Fidelidad de implementación


> **Construcción no puede simplificar en silencio.** Si algo no es viable, devuelve con
> evidencia. Diseño, a su vez, no puede ignorar una imposibilidad física o técnica
> demostrada. Ninguna de las dos partes puede imponerse por cansancio.

## Las ocho cosas que no se simplifican en silencio

```text
1  ANIMACIONES        duración, curva, disparador, qué se mueve y qué permanece
2  TRANSICIONES       entre estados y entre superficies, incluida la de vuelta
3  COMPOSICIÓN        estructura, proporciones, alineaciones, anchos máximos
4  ESTADOS            vacío, error, carga, mínimo, máximo, y los propios del componente
5  ESPACIADO          los valores del sistema, no aproximaciones cómodas
6  DETALLES           bordes, radios, sombras, tipografía en sus tres pesos, juntas
7  RESPONSIVE         qué cambia en cada punto de adaptación declarado
8  MICROINTERACCIONES qué acusa recibo de qué acción, y con qué respuesta
```

Cualquiera de las ocho construida por debajo de lo aprobado **sin devolución registrada**
es un fallo del eje `fidelidad` de la rúbrica visual, y detiene el tránsito.

## El artefacto de comparación

`DIS/revision-de-fidelidad` produce, por superficie afectada:

```text
COMPARACIÓN — <superficie> · <ITEM-ID>/<nn>
intención aprobada:  <enlace a la especificación y su versión>
construido:          <commit o artefacto exacto>

ESTÁTICO
  captura de la intención  │  captura de lo construido  │  diferencia señalada
  · por cada entorno de la matriz del pack instalado
  · a tamaño real, y con zoom en las juntas

ESTADOS
  los cinco obligatorios más los propios del componente, en ambas columnas

MOVIMIENTO
  grabación de la intención  │  grabación de lo construido
  · duración medida frente a duración especificada
  · la curva se compara sobre la grabación, no sobre el código
  · el ESTADO REDUCIDO grabado también

DISPOSITIVO REAL
  · qué dispositivo, qué versión de sistema, qué condiciones
  · NO vale emulador cuando el pack declara prueba en hardware real

VALORES
  extracción de los valores realmente usados frente al sistema declarado
  · tipografía · escala · color por rol · unidad de espaciado · radios · elevación

VEREDICTO   fiel | fiel con deuda aceptada | infiel
```

## Los tres veredictos

```text
FIEL                    lo construido corresponde a la intención aprobada.

FIEL CON DEUDA ACEPTADA existe una diferencia, está REGISTRADA en memoria:deuda-de-diseno
                        con: qué se sacrificó · la restricción concreta que lo obligó ·
                        qué la saldaría · qué empeora si no se salda.
                        La acepta el Owner cuando la superficie es premium o el patrón es
                        suyo; DIS/direccion-artistica en los demás casos.

INFIEL                  hay diferencia y no está registrada.
                        → DEVOLUCIÓN a CON con la comparación como evidencia.
                        → NO se acepta como deuda a posteriori para evitar la devolución:
                          la deuda se acuerda ANTES de construir distinto, no después.
```

> La última frase es la que sostiene todo el procedimiento. Si una simplificación pudiera
> convertirse en «deuda aceptada» al ser descubierta, el sistema entero de fidelidad
> sería decorativo.

## Cuando algo NO es viable

El camino es este, y no admite atajos por ninguna de las dos partes:

```text
1  CON DEMUESTRA LA IMPOSIBILIDAD
   no basta con afirmarla. La evidencia exigida es una de estas:
     · medición que muestra que el presupuesto declarado por el pack se incumple
     · limitación documentada de la plataforma, con enlace y versión
     · prototipo que lo intenta y falla, con la grabación
     · coste medido que excede lo que el item tiene autorizado

2  DEVUELVE A DIS   con la evidencia. No propone la alternativa: nombra el obstáculo.

3  DIS EXPLORA ALTERNATIVAS
   DIS NO PUEDE ignorar una imposibilidad demostrada.
   DIS SÍ PUEDE rechazar una imposibilidad AFIRMADA sin la evidencia de arriba.
   La exploración busca otra forma de conseguir la MISMA INTENCIÓN, no de renunciar a ella.

4  SI NO HAY ALTERNATIVA
   se registra deuda de diseño con los cuatro campos, y se decide quién la acepta según
   la regla de arriba. La intención original QUEDA ESCRITA, para que se pueda retomar
   cuando la restricción desaparezca.

5  FRENO
   dos devoluciones entre DIS y CON sobre el mismo paquete y no hay tercera (a.7).
   Se escala con las dos posturas escritas: qué sostiene cada uno y con qué evidencia.
```

## Quién puede decir qué

```text
CON PUEDE       demostrar que algo no es viable, con la evidencia exigida
CON NO PUEDE    decidir qué se sacrifica cuando algo no es viable
CON NO PUEDE    construir una versión reducida y presentarla como terminada

DIS PUEDE       rechazar una imposibilidad afirmada sin evidencia
DIS PUEDE       vetar una solución técnica que degrada la forma SIN haber explorado
                alternativas (a.5, contrato de veto de DIS)
DIS NO PUEDE    ignorar una imposibilidad física o técnica demostrada
DIS NO PUEDE    exigir una reconstrucción completa por una diferencia que no incumple
                ningún eje de la rúbrica

EL OWNER        acepta la deuda cuando la superficie es premium o el patrón es suyo
```

## Enlace con el gate

`gate:excelencia-visual` comprueba el eje `fidelidad` **a través de este artefacto**. Sin
comparación no hay eje evaluable, y sin eje evaluable el gate no cierra. Es la
comprobación que impide que las estaciones 1 a 9 del ciclo hayan sido decorativas.
