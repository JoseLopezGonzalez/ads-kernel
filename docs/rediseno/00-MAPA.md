# PASO 1 — Mapa del kernel 1.3.0 frente al principio gobernante

> **ESTADO tras aprobar (a) y (b) el 2026-08-25.**
> Resueltas por (a): G07 · G08 · G11 · G12 · G14 · G15 · G17 · G32 · K0.9.
> Resueltas por (b): recorrido, estados, transiciones y composición de procesos.
> **Siguen pendientes** de secciones posteriores, ahora como items SIS dentro de un
> proyecto real: G24 · G26 · G34 vía rápida · G53 · K0.2 · G03 (ejecución desatendida).

Principio gobernante: un work item SE FABRICA EN CADENA. Cada equipo AÑADE UNA CAPA
DE VALOR, no valida. Implementación es casi la última parada. El uso real reentra
por el principio. Calidad sólida/profesional/autónoma es la DISPOSICIÓN POR DEFECTO.

## Hallazgo raíz

K0.9 declara: "el fallo más probable de este proyecto es que la organización produzca
documentación sobre sí misma y no compile nunca una aplicación. Todas las reglas sobre
timeboxes, gates fijos y presupuestos existen para prevenir eso."

Ese es el ANCLA de todo el sesgo barato del kernel actual (G24.1, G22 timebox, G34
Quick Change, G53 "fuera de premium, suficientemente bueno y barato"). Es un modo de
fallo real pero NO es el modo de fallo observado del Owner.

Modo de fallo observado (PesquerApp): sistemas paralelos ya implementados y
descoordinados; agentes que no recuerdan ni coordinan con lo existente; el Owner
reescribiendo cada sesión cómo guiar la conversación; sin procedimiento estándar
para gaps; el propio Owner sin memoria de lo pendiente.

Mientras K0.9 siga siendo la premisa, cualquier regla nueva será reinterpretada hacia
lo barato. K0.9 hay que sustituirlo, no matizarlo.

## SOBREVIVEN (intactas o casi)

K-1 tres capas · K0 contrato · K0.5 DEBE/PROVISIONAL · K0.7 overrides · K0.8
portabilidad · K0.10 test de contaminación · K0.11 vendorizado · K0.12 upstream ·
K0.13 éxito del Owner · G01 · G02 · G05 autoridad del Owner · G10 lenguaje natural ·
G13 creación != validación (reencuadrada: pasa de regla proporcional a riesgo a
ESTRUCTURA por defecto de la cadena) · G17 escritura coordinada · G27 seguridad dura ·
G28 supply chain · G29 Git / el Owner no es operador Git · G30 contención y
recuperación · G33 investigación y freshness · G36 validación por lotes · G37-G39 ·
G40-G42 · G51 cambio de dirección · G52 ledgers.

## SUSTITUIR

K0.9  premisa de fallo -> se reescribe con el modo de fallo real
K0.2  "no leer el kernel, compilar <400 líneas" -> incompatible con "protocolo
      ejecutable y verificable". Nueva forma: procedimientos por estación cargados
      bajo demanda, no una constitución en prosa que nadie lee.
G07   Owner Gateway como embudo único -> pasa a protocolo de consolidación; cada
      equipo conserva sus puntos de interacción propios.
G08   estado ejecutivo redactado a mano -> vista renderizada sobre bloques de estado
G11   13 cajas de "capacidades" (etiquetas) -> equipos reales con memoria, cola,
      autoridad y criterios propios
G12   "la tecnología de orquestación no se decide aquí" -> dispatcher concreto
G15   agente como unidad de trabajo -> agente = modelo+instrucciones+herramientas+
      contexto+presupuesto+función; individual, paralelo, competencia o productor/crítico
G22   timebox de C0 (3 sesiones / 2 semanas) -> el gate de entregables se queda,
      el timebox pasa a punto de control, no guillotina
G24   "la combinación más sencilla que mantenga la calidad necesaria" -> INVERTIR.
      El presupuesto deja de ser sesgo de diseño y pasa a ser observabilidad + stop-loss.
G26   JOURNAL narrativo append-only -> bloques tipados y enlazados
G32   "DEBE existir un task system" (delegado al bootstrap) -> estructura de estado
      concreta y ya definida por el kernel
G34   tres velocidades graduadas SOLO por riesgo -> ver pregunta (e)
G53   riesgo x valor diferencial, con "fuera de premium, barato" -> el eje sobrevive
      pero su contrapartida barata no. Todo pasa por la cadena; lo diferencial recibe
      más profundidad de estación y más juicio del Owner, no "el resto sale barato".

## CONFLICTOS DIRECTOS (decidir CON el Owner)

1. Vía rápida. G34 Quick Change + G35 Copilot Session dejan pasar lo pequeño casi sin
   tocar equipos. Choca de frente con el principio gobernante. -> sección (e)
2. Presupuesto. G24 + G53 fijan techos; el material bruto pide presupuesto ilimitado
   en diseño. -> sección (f)
3. Tres sistemas de ciclo solapados: Circuitos 0-4 (fases de proyecto), la cadena
   (por item), y los circuitos de diseño del material bruto (fundación /
   reconstrucción / evolución). Tres sistemas = la fragmentación exacta que el Owner
   quiere eliminar. Lectura previa: los circuitos de diseño NO son un sistema
   paralelo — son (i) un estado de proyecto que ya cae en C0/C1 y (ii) el
   procedimiento interno de la estación de Diseño, que D1-D12 ya describe. -> (f)
4. G03 "autonomía temporal no es requisito inicial, no introducir esa complejidad".
   "Continúa" (reanudación al abrir chat) NO es autonomía temporal: es requisito ya.
   Ejecución desatendida sí queda bajo G03. -> sección (g)

## AUSENTE POR COMPLETO (el problema real del Owner)

- Reconocimiento de lo ya existente antes de tocar nada
- Identidad persistente del item entre sesiones
- Procedimiento estándar de resolución de gaps
- Representación de "lo que el Owner tiene pendiente" que el propio Owner pueda leer
- Formato de handoff entre equipos
- Prueba de conformidad de una organización instalada
