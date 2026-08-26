# Incertidumbre, confirmación y anclaje: los tres criterios comprobables


Tres decisiones del circuito de entrada que sin criterio escrito quedarían al gusto del
agente de turno: **cuánta incertidumbre hay**, **cuándo se molesta al Owner** y **cuándo
una orden es ambigua**.

---

## 1 · Escala de incertidumbre — cinco ejes

Se puntúa cada eje. **El grado global es el más alto de los cinco**, no el promedio: una
sola incógnita grave basta para que el encuadre no esté listo.

| eje | baja | media | alta |
|---|---|---|---|
| **resultado perseguido** | puede escribirse en una frase que nombre algo comprobable | puede escribirse, pero admite dos lecturas con consecuencias distintas | no puede escribirse sin inventarlo |
| **problema observado** | hay un caso concreto con pantalla, momento o dato | hay un caso, pero relatado de memoria y sin poder reproducirlo | sólo hay adjetivos, sin ningún caso |
| **alcance** | está escrito qué queda dentro y qué fuera | está el dentro; el fuera es incompleto | ni dentro ni fuera están escritos |
| **restricciones** | se sabe qué no puede tocarse, y el anclaje lo confirma | se sabe, pero no está confirmado contra lo implementado | se desconoce si hay restricciones |
| **criterio de terminado** | la evidencia de cierre la comprueba un tercero | la evidencia existe pero exige juicio de quien la escribió | no puede escribirse evidencia |

**Qué desencadena cada grado:**

```text
BAJA    ENC formula y entrega. Sin crítica independiente obligatoria.
MEDIA   ENC conversa el eje concreto que está en media, y sólo ése. Formula después.
        Sin crítica independiente obligatoria, salvo que el nivel de Owner sea obligatorio.
ALTA    PROHIBIDO formular. Se conversa hasta bajar a media, o la expresión va al vivero.
        Crítica independiente OBLIGATORIA antes de entregar.
```

> **Declarar incertidumbre alta no es un fallo del interlocutor.** Ocultarla con una
> redacción firme sí lo es, y es la causa más común de un item que se construye entero y
> resulta no ser lo que el Owner quería.

---

## 2 · Tabla de confirmación — cuándo se molesta al Owner

Deriva de a.8. Este documento no la redefine: la **operativiza** para la puerta de entrada.

| situación | ¿se pide confirmación? | por qué |
|---|---|---|
| primera dirección de producto | **sí** | a.8 · nivel obligatorio |
| primera instancia de un patrón visual, artístico o de interacción | **sí** | a.8 · nivel obligatorio |
| primera decisión dentro de un área reservada | **sí** | a.8 · G05 |
| decisión estratégica o difícilmente reversible | **sí** | a.8 · nivel obligatorio |
| cambio de dirección sobre algo ya decidido | **sí** | a.8 · G51 |
| incertidumbre global **alta** tras haber conversado | **sí** | el encuadre no puede sostenerse sin su lectura |
| la expresión contradice una decisión suya vigente | **sí**, mostrando ambas | nadie decide en su lugar entre dos criterios suyos |
| el item extiende un `owner_approved_pattern` dentro de su alcance | **no**, va a la cola de lotes | a.8 · opcional acumulada. **No detiene el item** |
| el item extiende un `capability_approved_pattern` vigente | **no** | a.8 · ninguna |
| el item extiende un `provisional_pattern` vigente | **no** | a.8 · ninguna |
| orden unívoca y reversible | **no** | b.13 · se aplica directamente |
| error evidente con comportamiento esperado conocido | **no** | reparar lo roto no es una decisión suya |
| mantenimiento, deuda interna o trabajo rutinario delegado | **no** | a.8 · ninguna |
| dejar algo en el vivero | **no** | no compromete capacidad |
| anotar una nota u observación en memoria | **no** | no crea trabajo |

**Regla de cierre de la tabla:** si una situación no aparece, se resuelve **por materia**
según la tabla de a.8 — no por defecto a «sí». Marcar confirmación por prudencia tiene un
coste real: convierte la atención del Owner en un cuello de botella y le enseña a aprobar
sin leer.

### Lo que la confirmación NO es

```text
NO ES CONFIRMACIÓN     informar de que algo se ha creado
NO ES CONFIRMACIÓN     preguntar por una preferencia dentro de un patrón ya aprobado
NO ES CONFIRMACIÓN     pedirle que elija entre dos opciones técnicas equivalentes
                       (eso es delegación mal ejercida: decide la capacidad competente)
```

---

## 3 · Umbral de anclaje y margen de ambigüedad

b.13 declara el contrato de ambigüedad y deja umbral y margen como parámetros del runtime.
Aquí quedan fijados sus **valores por defecto** y **cómo se puntúa**, de modo que dos
agentes distintos obtengan el mismo resultado.

### Puntuación de un candidato

```text
+0.40   coincide el RESULTADO PERSEGUIDO con lo que la expresión describe
+0.25   coincide la superficie, módulo o materia
+0.15   el Owner usó un término que el léxico asocia a ese item
+0.10   es el item más recientemente tocado por el Owner en esa materia
+0.10   está en un estado que hace plausible la intención
        (aparcado para «retoma», activo para «prioriza», cerrado para «feedback»)
-0.30   el estado hace IMPLAUSIBLE la intención
        (cancelado para «retoma», cerrado para «prioriza»)
```

### Umbral y margen

```text
UMBRAL_ANCLAJE = 0.60     por debajo, el mejor candidato no basta: se desambigua
MARGEN         = 0.15     si el primero y el segundo se diferencian en menos, se desambigua

se aplica directamente  si  p(1) >= 0.60  Y  p(1) - p(2) >= 0.15  Y  la orden es reversible
se desambigua           en cualquier otro caso
```

Ambos son **parámetros del PROFILE**, no reglas del kernel: un proyecto con pocos items
puede subir el umbral sin tocar ningún contrato. Lo que el kernel fija es que existan, que
estén escritos y que la puntuación sea reproducible.

### Cómo se desambigua

Por **nombre humano, naturaleza y estado**. Nunca por identificador. Máximo tres
candidatos: con más de tres, se pregunta primero por la materia.

```text
Hay dos cosas que encajan con «el gap»:
  · Trazabilidad de lotes en salidas    aparcado desde el 19 de agosto, en Diseño
  · Cuadre de stock por almacén         esperando una decisión tuya
```

---

## 4 · Qué hacer cuando el Owner no contesta

```text
el encuadre queda `esperando-owner`, NO `bloqueado`
    esperando-owner   se resuelve solo cuando él responda. No genera trabajo.
    bloqueado         exigiría crear un desbloqueador, y aquí no hay nada que crear.

· el encuadre NO se entrega a medias
· la conversación NO se reinicia cuando vuelva: se retoma por checkpoint
· el sistema NO insiste ni recuerda por antigüedad
· si el Owner vuelve con otra cosa, se atiende esa otra cosa y el encuadre sigue esperando
```

Un encuadre puede quedarse esperando indefinidamente. Es un resultado normal del sistema.
