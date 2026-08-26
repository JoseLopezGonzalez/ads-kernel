# El circuito completo: de la expresión del Owner al trabajo distribuido

<!-- ads-lint: permitir-vocabulario-prohibido -->

Trece estaciones. **No es una cadena rígida**: casi todas pueden devolver hacia atrás, y
varias terminan legítimamente sin item.

```text
                       ┌──────────────────────────────────────────────┐
                       │  1  EXPRESIÓN ORIGINAL                       │
                       │     el Owner dice algo, por cualquier canal   │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │  2  CAPTURA LITERAL          ENC/interlocutor │
                       │     texto exacto + fecha + canal. Antes de    │
                       │     interpretar nada. NUNCA se sobrescribe.   │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │  3  INTERPRETACIÓN INICIAL   ENC/interlocutor │
                       │     qué parece pedirse, con confianza medida  │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │  4  ANCLAJE CON EL PROYECTO       ENC/anclaje │
                       │     qué existe · qué lo gobierna · qué se     │
                       │     aprendió · duplica · QUÉ NO EXISTE        │
                       └───┬───────────────┬──────────────────────────┘
              duplicado ───┘               ▼
              → paso 11 como            ┌──────────────────────────────┐
                ORDEN                   │  5  MEDICIÓN DE INCERTIDUMBRE│
                                        │     cinco ejes, grado global │
                                        └───────────────┬──────────────┘
                                                        ▼
                       ┌──────────────────────────────────────────────┐
                       │  6  CONVERSACIÓN · PREGUNTAS · BRAINSTORMING │
                       │     la forma del catálogo que corresponda.    │
                       │     Consulta a especialistas en modo consulta │
                       └───┬───────────────┬──────────────────────────┘
        sigue inmadura ────┘               ▼
        → VIVERO (sin item)             ┌──────────────────────────────┐
                                        │  7  FORMULACIÓN PROFESIONAL  │
                                        │     el encuadre completo      │
                                        └───────────────┬──────────────┘
                                                        ▼
                       ┌──────────────────────────────────────────────┐
                       │  8  CLASIFICACIÓN                            │
                       │     naturaleza + tipo de proceso propuesto    │
                       │     + crítica independiente cuando toca       │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │  9  CONFIRMACIÓN — SÓLO CUANDO CORRESPONDE   │
                       │     según la tabla de 04-CONFIRMACION.md      │
                       └───────────────────┬──────────────────────────┘
                                           ▼
        ══════════════════════ frontera: aquí ENC entrega y DSP toma ══════════════
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │ 10  CREACIÓN DEL ITEM                    DSP │
                       │     ficha · identidad persistente · tipo      │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │ 11  COMPOSICIÓN DE RUTA                  DSP │
                       │     grafo r1 · activadas y NO activadas con   │
                       │     motivo · propietario global               │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │ 12  CREACIÓN DE PAQUETES                 DSP │
                       │     unidades de custodia con su declaración   │
                       │     de acoplamiento                           │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │ 13  ENTREGA A EQUIPOS                    DSP │
                       │     despacho determinista y explicable        │
                       └───────────────────┬──────────────────────────┘
                                           ▼
                       ┌──────────────────────────────────────────────┐
                       │ 14  RESPUESTA AL OWNER       ENC/interlocutor │
                       │     qué se entendió · qué va a pasar ·        │
                       │     QUÉ NO SE CREÓ Y POR QUÉ                  │
                       └──────────────────────────────────────────────┘
```

## Los caminos hacia atrás

El circuito **no es una tubería**. Estos retornos son normales, no excepciones:

| desde | vuelve a | cuándo |
|---|---|---|
| 4 anclaje | 3 interpretación | el dosier revela que la interpretación no encaja con lo que existe |
| 4 anclaje | 11 como orden | el anclaje encuentra un item abierto que persigue lo mismo |
| 5 incertidumbre | 6 conversación | el grado es alto en el eje del resultado perseguido |
| 6 conversación | 4 anclaje | la conversación destapa una zona del proyecto sin explorar |
| 6 conversación | VIVERO | la idea sigue sin pasar la prueba de frontera |
| 7 formulación | 6 conversación | un campo del encuadre no puede escribirse sin preguntar |
| 8 clasificación | 3, 4, 6 o 7 | la crítica independiente devuelve con huecos concretos |
| 9 confirmación | 6 conversación | el Owner corrige el entendimiento al ver el encuadre |
| 10-13 DSP | 7 formulación | DSP no puede componer ruta porque falta un campo del encuadre |
| cualquiera | fin sin item | el Owner retira la expresión, o el anclaje demuestra que ya está resuelta |

**Límite de rebotes.** Entre los pasos 7 y 8 se aplica el freno de a.7: dos devoluciones
del crítico, y la tercera no se ejecuta. Se escala con las dos posturas escritas.

## Dónde termina cada clase de entrada

```text
observación   → paso 4 y anotación en la memoria del equipo competente. FIN sin item.
nota          → paso 2 y anotación en memoria. FIN sin item.
idea inmadura → paso 6, y de ahí al VIVERO. FIN sin item, reabrible cuando el Owner vuelva.
orden         → pasos 2, 4 y 11 en su variante ENC/Orden. FIN con evento, sin item nuevo.
decisión      → pasos 2 y 4, registro en la memoria de la capacidad propietaria; si
                sustituye a una decisión implementada, continúa como proceso DIR.
candidato     → recorrido completo hasta el paso 14.
```

**La mayoría de las expresiones del Owner terminan sin item, y eso es correcto.** Un
sistema donde toda frase produce una tarea es el sistema que el Owner pidió no construir.

## Quién es dueño de qué en este circuito

```text
pasos 1-9    ENC   trabajo de contenido: escuchar, anclar, comprender, formular
paso 9       OWNER autoridad de confirmación, cuando la tabla la exige
pasos 10-13  DSP   orden y ruta. NINGUNA autoridad sobre el contenido del encuadre
paso 14      ENC   la respuesta al Owner es de quien habló con él
```

DSP **puede** devolver el encuadre a ENC por falta de un campo estructural —no puede
componer ruta sin tipo de proceso—, pero **no puede** cambiar la interpretación, el
resultado perseguido ni la evidencia de cierre. Eso es contenido, y no es suyo.

## Qué garantiza este circuito

```text
[ ] la expresión literal del Owner sobrevive a todo el recorrido, sin excepción
[ ] ninguna intención real se pierde: si no es item, es vivero, memoria o evento
[ ] ningún comentario se convierte en trabajo por sí solo
[ ] nada llega a un equipo sin haber pasado por el anclaje
[ ] el Owner recibe siempre una respuesta que incluye QUÉ NO SE CREÓ
[ ] cada paso deja checkpoint: un corte de sesión no borra lo comprendido
```
