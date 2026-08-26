# El ciclo de calidad de Diseño

<!-- ads-lint: permitir-vocabulario-prohibido -->

Trece estaciones. **No es una tubería**: seis de ellas pueden devolver hacia atrás, y una
devolución no es un fracaso del ciclo, es el ciclo funcionando.

```text
 1  COMPRENSIÓN          qué problema de forma hay que resolver, y para quién
        │                DIS/investigacion-ux · lee memoria y encuadre
        ▼
 2  INVESTIGACIÓN        cómo se ha resuelto esto, aquí y fuera
        │                DIS/investigacion-visual · produce hallazgos, no propuestas
        ▼
 3  REFERENCIAS          material externo con SU PRINCIPIO EXTRAÍDO
        │                DIS/investigacion-visual · nunca obras para copiar
        ▼
 4  EXPLORACIÓN          ◄── DIVERGENTE ──► direcciones distintas entre sí
        │                DIS/diseno-visual + DIS/direccion-artistica
        │                PROHIBIDO descartar durante esta fase
        ▼
 5  CRÍTICA              DIS/critica-visual, INDEPENDIENTE
        │                juzga la exploración: ¿son de verdad distintas? ¿alguna es genérica?
        ▼
 6  CONVERGENCIA         ◄── CONVERGENTE ──► se elige y se descarta CON MOTIVO ESCRITO
        │                DIS/direccion-artistica decide · PROHIBIDO añadir alternativas
        ▼
 7  PROTOTIPO            lo elegido, ejecutable y mirable
        │                DIS/prototipado + DIS/movimiento
        ▼
 8  VALIDACIÓN DE USO    gate:usabilidad
        │                DIS/validacion-de-uso · con personas o plan de validación (G36)
        ▼
 9  VALIDACIÓN VISUAL    gate:excelencia-visual
        │                DIS/critica-visual + Owner donde a.8 lo exige
        ▼
10  ENTREGA A CONSTRUCCIÓN   handoff DIS → CON, con la especificación y la evidencia
        │
        ▼
11  REVISIÓN DE FIDELIDAD    lo construido frente a lo aprobado
        │                DIS/revision-de-fidelidad
        ▼
12  PRUEBA EN DISPOSITIVO REAL   no en emulador, no en captura
        │                DIS/validacion-de-uso + USO
        ▼
13  APRENDIZAJE          qué se aprendió, qué envejeció, qué se promueve
                         DIS/direccion-artistica → memoria → APR si hay señal
```

## Los retornos

| desde | vuelve a | cuándo | qué acompaña |
|---|---|---|---|
| 4 exploración | 2 investigación | las tres direcciones se parecen porque el material de partida era pobre | qué falta investigar |
| 5 crítica | 4 exploración | las direcciones no son distintas en dos dimensiones, o alguna es genérica | los ejes incumplidos con evidencia |
| 6 convergencia | 4 exploración | ninguna dirección resuelve el problema declarado en 1 | qué exige el problema que ninguna da |
| 8 validación de uso | 6 convergencia | la dirección elegida no es usable con datos reales | el eje de usabilidad en rechazo y su evidencia |
| 9 validación visual | 4 exploración | rechazo por **personalidad**, **actualidad** o **alma** | el eje, la razón discutible y la referencia comparada |
| 9 validación visual | 4 exploración | rechazo por **intencion**: las decisiones formales no responden a ninguna intención escrita | qué decisión no tiene principio detrás |
| 9 validación visual | 6 convergencia | rechazo por **jerarquia**: la dirección elegida no sostiene la jerarquía con datos reales | la prueba de entrecerrado y el caso de dato largo que la rompe |
| 9 validación visual | 7 prototipo | rechazo por **acabado**, **sistema** o **respuesta** | qué valor está fuera del sistema, con la extracción |
| 9 validación visual | 10 construcción | rechazo por **fidelidad** | la comparación intención/resultado |
| 11 fidelidad | 10 construcción | lo construido simplificó lo aprobado sin devolverlo | comparación intención/resultado |
| 11 fidelidad | 6 convergencia | lo aprobado no es construible y la limitación es física o técnica | la evidencia de imposibilidad de CON |
| 12 dispositivo real | 7 prototipo | el movimiento o la densidad no funcionan en el hardware real | la grabación en el dispositivo |

> **Un rechazo por «personalidad, actualidad o alma» no vuelve al prototipo.** Vuelve a la
> exploración, porque el problema es de dirección y no se arregla retocando el acabado.
> Ésta es la regla que impide que el gate visual se convierta en una lista de retoques.
>
> **Los NUEVE ejes tienen destino.** `intencion` y `jerarquia` no lo tenían, y un rechazo
> por cualquiera de los dos dejaba al paquete sin sitio al que volver — que es justo lo que
> C5 clasifica como devolución inválida por no declarar «qué la cerraría» (hallazgo A-21).

## Dónde muere el ciclo si nadie lo defiende

```text
ESTACIÓN 3 se salta      → las referencias salen de la memoria del modelo: material
                           no comprobable presentado como investigación
ESTACIÓN 5 se salta      → la exploración produce tres variantes de la misma idea y
                           nadie lo dice
ESTACIÓN 6 no escribe    → seis semanas después se vuelve a proponer lo ya descartado
   los descartes
ESTACIÓN 11 se salta     → todo lo anterior fue decorativo: se construyó otra cosa
ESTACIÓN 12 se sustituye → el movimiento se aprueba en un emulador y da tirones en el
   por capturas            dispositivo del Owner
ESTACIÓN 13 se salta     → el equipo repite el mismo error en el siguiente item
```

Cinco de esas seis omisiones tienen su comprobación en un gate del kernel, y ninguna
depende de que alguien se acuerde:

```text
ESTACIÓN 3   → gate:excelencia-visual · referencias-con-principio
ESTACIÓN 5   → gate:excelencia-visual · dictamen-existe + dictamen-independiente
ESTACIÓN 6   → gate:excelencia-visual · memoria-actualizada
ESTACIÓN 11  → gate:excelencia-visual · eje `fidelidad` con su comparación
ESTACIÓN 13  → condición de cierre `learning_candidate` de b.10, comprobada en
               gate:cierre-de-item
```

**La ESTACIÓN 12 es la excepción, y se declara.** El kernel no tiene ningún gate que exija
dispositivo real: las únicas comprobaciones de hardware son de pack —`gate:mob-dispositivo-real`
y los tres de `wear-os`—. En un proyecto **sin pack**, o con `web-app`, saltarse la estación
12 no lo detiene nada. No es un descuido: es el límite de lo que el kernel puede exigir sin
conocer el medio, y por eso lo exige el pack que sí lo conoce (hallazgo A-26).

## Qué estaciones se ejecutan en cada nivel de novedad

**Esta tabla no es una fuente: se deriva.** Cada nivel declara sus estaciones en su bloque
`ads:nivel-novedad` de [`03-ESCALA-DE-NOVEDAD.md`](03-ESCALA-DE-NOVEDAD.md), y T139
comprueba que lo de aquí coincide con lo de allí. Antes eran dos textos independientes que
decían cosas distintas, y por eso N0 se saltaba los dos gates en un documento y los pasaba
en el otro (hallazgo **A-08**).

```text
N4  las trece
N3  1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 13         (10-12 van en los items derivados)
N2  las trece
N1  1 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · 11 · 13       (2 y 3 sólo si la memoria no basta)
N0  1 · 8 · 9 · 10 · 11 · 13                       (aplicar, VERIFICAR, entregar, comprobar)
```

> **Las estaciones 8 y 9 están en los cinco niveles.** Son los dos gates, y ningún nivel
> los omite: lo que cambia entre niveles es cuánta de su evidencia se reutiliza del patrón
> vigente, y eso lo declara cada nivel en `ejes_reutilizables`. Un nivel pequeño explora
> menos; no verifica menos.

La reducción de estaciones **no es discrecional**: la fija la escala de novedad, y el
nivel se declara con la condición que resultó verdadera. Saltarse una estación fuera de lo
que el nivel permite es un defecto de conformidad.
