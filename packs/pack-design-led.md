---
pack:    pack-design-led
kernel:  ^1.3.0
version: 1.0.0
scope:   Proyectos donde el diseño, la interfaz y la sensación de uso SON el diferenciador
requires: G53 (áreas premium declaradas en el PROFILE)
---

# PACK — Design-Led

Para productos cuya razón de existir no es lo que hacen sino **cómo se sienten al usarlos**. Se combina con el pack de plataforma (`pack-web-app`, `pack-mobile-native`), no lo sustituye.

Premisa: el nivel de acabado que asociamos a los productos de las compañías que cuidan el diseño **no** sale de tener buen gusto. Sale de tener sistema, criterio escrito, iteración obligatoria y un listón de rechazo. Este pack aporta las cuatro cosas.

> **Un producto se siente barato por acumulación de detalles ignorados, no por un fallo grande. Nadie señala el culpable: simplemente no vuelve.**

---

## D1 — Declaración obligatoria en el PROFILE

Adoptar este pack **obliga** a declarar en el PROFILE (G53):

```text
premium_areas:  diseño visual · interacción y movimiento · <tercera si aplica>
```

Y a escribir sus **criterios de calidad comprobables** (D3). Sin criterios escritos, "que se vea bien" no es un requisito: es una esperanza, y no sobrevive a un cambio de sesión.

## D2 — Referencia explícita, no aspiración vaga

*"Que parezca de una gran tecnológica"* no es dirigible. El PROFILE **DEBE** convertirlo en referencias concretas y analizadas:

```text
REFERENCIAS
Producto de referencia:   <nombre>
Qué tomamos:              <jerarquía tipográfica · densidad · sistema de movimiento · uso del color>
Qué NO tomamos:           <lo que no encaja con nuestro contexto de uso>
Por qué funciona:         <análisis, no admiración>
```

Reglas:

1. Las referencias se **analizan**, no se copian. Copiar produce imitación evidente; analizar produce criterio propio.
2. **NO DEBE** copiarse identidad visual protegida, iconografía ni marca de un producto real.
3. La referencia **DEBE** tener contexto de uso comparable. Un panel de escritorio no es referencia válida para una pantalla de 45 mm que se mira sudando entre series.
4. Cuando el Owner diga *"esto no me transmite"*, el sistema **DEBE** volver a esta sección antes de proponer, y expresar la diferencia en términos de los ejes declarados, no de gusto.

## D3 — Criterios de calidad comprobables

El PROFILE **DEBE** fijar valores concretos. Ejemplos del tipo de criterio esperado — los números los decide el proyecto:

```text
TIPOGRAFÍA     escala fijada · nº máximo de tamaños y pesos en pantalla · altura de línea por rol
ESPACIADO      unidad base y múltiplos permitidos · nada fuera de la escala
COLOR          paleta cerrada · roles semánticos, no colores sueltos · contraste mínimo verificado
JERARQUÍA      un único elemento dominante por pantalla, declarado
DENSIDAD       información máxima por pantalla según contexto de uso
MOVIMIENTO     duraciones y curvas por tipo de transición · presupuesto de fotogramas
ESTADOS        toda superficie interactiva define reposo/pulsado/foco/deshabilitado/carga/error/vacío
```

Regla dura: **un valor visual que no proceda de un token o de una primitiva es una excepción que requiere justificación**, y el linter **DEBERÍA** detectarla (ver W13 / M14 del pack de plataforma).

## D4 — Sistema de movimiento *(no "animaciones")*

Las animaciones sueltas producen sensación de juguete. Un **sistema** de movimiento produce sensación de producto.

1. El movimiento **DEBE** definirse como sistema antes de la primera animación: catálogo de transiciones con su duración, curva y propósito.
2. Toda animación **DEBE** tener función: orientar en la navegación, dar continuidad entre estados, confirmar una acción o comunicar progreso. **La animación decorativa se rechaza.**
3. Coherencia por tipo: dos transiciones del mismo tipo **NUNCA** tienen duraciones distintas.
4. El movimiento **DEBE** respetar la preferencia de reducción de movimiento del sistema operativo. No es opcional ni es un extra de accesibilidad: es parte del acabado.
5. **Presupuesto de fluidez declarado y verificado en dispositivo real.** Una animación que pierde fotogramas es peor que no tener animación: comunica fragilidad.
6. La percepción de velocidad importa más que la velocidad: estados de carga bien diseñados, respuesta inmediata al toque, transiciones que empiezan antes de que termine el trabajo.

## D5 — Iteración obligatoria *(G53.3)*

La primera versión de una pantalla **NUNCA** es la que se acepta.

```text
1. EXPLORAR    ≥2 direcciones distintas, no dos variantes de la misma
2. COMPARAR    lado a lado, contra los criterios de D3 y las referencias de D2
3. ARGUMENTAR  por qué una gana, en términos de criterio, no de preferencia
4. REFINAR     el detalle es donde se gana o se pierde la sensación de producto
5. PRESENTAR   al Owner: la elegida, la descartada y el porqué
```

Presentar una sola opción sin haber explorado alternativas es un incumplimiento de este pack, no un atajo aceptable.

## D6 — Evidencia visual obligatoria

En área premium, "compila y los tests pasan" **NO** es evidencia de nada.

Todo cambio visual o de interacción **DEBE** acompañarse de:

- capturas en el dispositivo o navegador real, no en emulador, cuando el pack de plataforma lo exija;
- **grabación** de la interacción cuando haya movimiento — una captura estática no puede juzgar una transición;
- comparativa antes/después cuando se modifique algo existente;
- estados extremos: contenido mínimo, contenido máximo, texto largo, carga, error, vacío.

El estado **vacío** es el más ignorado y el que más define la percepción de acabado. **DEBE** diseñarse, nunca improvisarse.

## D7 — Listón de rechazo

Antes de dar por terminada una pantalla, se comprueba. Cualquier "no" bloquea:

```text
[ ] ¿Todos los valores vienen de tokens o primitivas?
[ ] ¿Hay un único elemento dominante y la jerarquía se lee sin esfuerzo?
[ ] ¿Los espaciados pertenecen a la escala, sin excepciones sin justificar?
[ ] ¿Están diseñados los estados de carga, error y vacío?
[ ] ¿El movimiento tiene función y respeta el sistema?
[ ] ¿Se sostiene con el texto más largo previsible y con el más corto?
[ ] ¿Se sostiene con la fuente ampliada del sistema?
[ ] ¿Contraste y tamaños de toque verificados?
[ ] ¿Se ve bien en el dispositivo real, en la mano, en las condiciones de uso reales?
[ ] ¿Se siente rápida, o sólo es rápida?
```

## D8 — Regresión visual

Sin esto, el acabado se degrada silenciosamente conforme el proyecto crece.

- **DEBE** existir captura automatizada de las pantallas principales en sus estados clave desde el Circuito 2.
- Un cambio visual inesperado en una pantalla no relacionada **DEBE** fallar la CI.
- El Owner **NO DEBE** ser el mecanismo de detección de regresiones visuales: su tiempo es para juzgar calidad, no para vigilar deterioro.

## D9 — Enrutamiento de recursos *(concreta G53.2)*

- El trabajo de diseño e interfaz usa **el modelo más capaz disponible**, con techo de iteraciones más alto. Ahorrar aquí es ahorrar en el producto.
- El trabajo no premium usa el enrutamiento económico normal. La contrapartida es obligatoria: si todo consume el presupuesto premium, el presupuesto premium no significa nada.
- **DEBE** existir una capacidad de **crítica de diseño independiente**: un revisor que no produjo la propuesta y cuyo encargo explícito es encontrar lo que falla (aplica G13). Producir y juzgar diseño en la misma pasada es el modo más fiable de acabar con trabajo mediocre y satisfecho.

## D10 — Orden de construcción

```text
1. Tokens y escala          antes de la primera pantalla
2. Primitivas               antes de la segunda pantalla
3. Sistema de movimiento    antes de la primera animación
4. Una pantalla completa    llevada al nivel de acabado objetivo, como patrón de referencia
5. El resto                 replicando el patrón ya validado
```

El paso 4 es el importante y el que casi nadie hace: **una sola pantalla llevada al final, aceptada por el Owner, y convertida en el listón**. Construir diez pantallas a medias y pulirlas después no funciona: el criterio nunca llega a existir y cada pantalla acaba con el suyo.

## D11 — Documentación específica

```text
docs/DESIGN_SYSTEM.md    tokens, primitivas, inventario y API de cada una
docs/MOTION.md           catálogo de transiciones: duración, curva, propósito
docs/DESIGN_CRITERIA.md  criterios de D3 y referencias analizadas de D2
docs/design/             capturas y grabaciones de referencia aceptadas por el Owner
```

## D12 — Advertencia honesta sobre el coste

Este pack es caro. Multiplica iteraciones, consumo de modelo y tiempo de validación humana en las áreas declaradas. Es la decisión correcta **sólo** si el diseño es de verdad el diferenciador del producto.

Y hay un límite que el sistema **DEBE** comunicar sin adornos: un agente puede aplicar sistema, coherencia, criterio escrito y acabado con mucha fiabilidad — pero **la dirección de arte la sigue marcando el Owner**. La organización puede llegar muy lejos con criterio explícito y iteración; no puede inventar por sí sola una identidad que el Owner reconozca como suya sin verla y reaccionar a ella. Por eso D5 y D6 existen: para que reaccionar sea rápido y barato.
