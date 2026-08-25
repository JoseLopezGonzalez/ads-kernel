---
pack:    pack-mobile-native
kernel:  ^1.0.0
version: 1.1.0
scope:   Aplicaciones nativas móviles y/o wearable (Android, Wear OS, iOS, watchOS)
---

# PACK — Mobile / Wearable Nativo

Saber hacer común a cualquier app nativa móvil o de reloj. Es la generalización de lo aprendido en el proyecto de entrenamiento: **cierto en toda app con sensores, batería y ciclo de vida hostil, no sólo en ésa.**

---

## M1 — Qué es el "entorno real" para los spikes (G22)

```text
Dispositivo FÍSICO objetivo, no emulador
Con la app en background y la pantalla apagada
Con la batería como métrica, no como nota al pie
Con el fabricante concreto (las restricciones de background varían mucho entre OEM)
Con permisos denegados, además de concedidos
En movimiento y en condiciones reales de uso, no sentado en una mesa
```

El emulador sirve para flujo, UI y lógica. **NO** sirve para sensores, batería, latencia, ergonomía ni background.

Spikes recomendados por defecto:

| ID | Pregunta | Qué se mide |
|---|---|---|
| M-SPIKE-a | ¿Sobrevive el proceso a una sesión larga en background? | pérdida de estado o de datos en sesión completa |
| M-SPIKE-b | ¿Qué consume la captura continua durante uso real? | % de batería por unidad de tiempo |
| M-SPIKE-c | ¿Qué expone realmente la API de plataforma en este hardware? | inventario medido, no documentado |
| M-SPIKE-d | ¿Qué pasa con cada permiso denegado? | comportamiento observado en cada rama |

## M2 — Perfil de capacidades del dispositivo

**Nunca** asumir que una capacidad presente en la API está disponible, ni que está disponible con calidad usable. La app **DEBE** construir en runtime un perfil de capacidades y adaptarse.

```text
DeviceCapabilities
  sensor/característica → disponible | ausente | desconocido
  + calidad o frecuencia real alcanzada, no la nominal
  + comportamiento con pantalla apagada
```

La UI y los algoritmos consumen ese perfil. Una función cuya capacidad falta **NO DEBE** aparecer en gris: no debe aparecer.

## M3 — Degradación explícita *(regla central de esta clase de proyecto)*

> **Toda función que dependa de un sensor, permiso, conectividad o servicio potencialmente ausente DEBE tener definido su comportamiento degradado ANTES de implementarse. Una función sin plan de degradación no está diseñada.**

Además:

1. Toda señal de sensor **DEBE** llevar un **indicador de confianza**.
2. Con confianza baja, la UI **DEBE ocultar** la métrica derivada, no mostrar un valor dudoso con un asterisco.
3. El estado de runtime **DEBE** exponer qué funciones están degradadas (`degradedModes[]`), para que la UI decida sin adivinar.
4. La funcionalidad núcleo **DEBE** seguir siendo útil con los sensores opcionales completamente desactivados. Si no lo es, el diseño depende de una apuesta y hay que declararlo como riesgo (contrato K0, §5).

## M4 — Medido / derivado / estimado / recomendado

```text
MEDIDO       lo que el sensor entrega
DERIVADO     lo que se calcula de forma determinista a partir de lo medido
ESTIMADO     lo que se infiere con incertidumbre
RECOMENDADO  lo que la app sugiere hacer
```

Una estimación **NUNCA** se presenta como medición. Esta diferencia **DEBE** ser visible en la UI, no sólo estar en la documentación.

## M5 — Batería como requisito, no como optimización

- El presupuesto de consumo se fija **antes** de decidir frecuencias de muestreo, no después de que el usuario se queje.
- Regla: **más datos no significa mejor producto.** Se captura lo que aporta utilidad demostrable.
- Telemetría de alta frecuencia: a **fichero**, nunca como filas en base de datos.
- Transferencias grandes: **diferidas y por lotes**, preferentemente con el dispositivo cargando.
- Toda subida de frecuencia de muestreo o de sensor adicional es un cambio con impacto medible → requiere medición, no intuición.

## M6 — Ejecución prolongada y ciclo de vida hostil

El sistema operativo puede suspender, matar o limitar la app en cualquier momento, y **cada fabricante lo hace distinto**.

1. El estado de una operación larga **NO DEBE** vivir sólo en memoria ni depender de que el proceso sobreviva.
2. **DEBERÍA** poder reconstruirse desde persistencia — un log append-only de eventos es el mecanismo más robusto conocido para esto, y de paso resuelve sincronización y reproceso (ver M7).
3. Las restricciones de background **DEBEN** medirse en el dispositivo objetivo (M-SPIKE-a), no leerse en la documentación de la plataforma.
4. La pérdida de datos por muerte de proceso es un **defecto crítico**, no un caso límite.

## M7 — Multi-dispositivo: nodos, no base de datos compartida

Cuando hay teléfono + reloj (o varios dispositivos), son **nodos independientes** con proceso, almacenamiento y ciclo de vida propios. Los mecanismos de comunicación de la plataforma **NO** son una base de datos compartida.

Reglas:

1. Toda entidad sincronizable lleva desde el día uno: `id` global ordenable, `createdAt`, `updatedAt`, `deletedAt` (borrado **lógico**), `originDevice`, `schemaVersion`. Sin esto, la sincronización no es implementable sin migración.
2. **Preferir asignar un escritor propietario por tipo de entidad** antes que implementar resolución genérica de conflictos. La mayoría de los conflictos desaparecen por construcción.
3. Los flujos de trabajo capturados en un dispositivo **DEBERÍAN** modelarse como log append-only replicable: fusionar eventos no genera conflictos reales, fusionar filas editadas sí.
4. La app **DEBE** funcionar con el otro dispositivo ausente o desemparejado.

## M8 — Permisos

- Cada permiso **DEBE** tener definido el comportamiento con permiso **denegado** y con permiso **revocado a mitad de uso**.
- Los permisos sensibles (sensores corporales, ubicación, salud) tienen reglas distintas en primer plano y en **background**, y esas reglas **condicionan la arquitectura**, no la configuración. Hay que resolverlas en Circuito 1, no en Circuito 3.
- El permiso se pide **en contexto**, cuando el usuario entiende para qué, no en el arranque.

## M9 — UI en pantallas pequeñas y en movimiento

- Diseñar para el peor caso de atención: poca luz, movimiento, una sola mano, sudor, prisa.
- Acciones principales grandes; nada de formularios complejos; minimizar escritura; permitir corrección rápida.
- Los mecanismos físicos (corona, botones) reducen mucho la fricción **pero NO DEBEN** ser dependencia: siempre alternativa táctil.
- Retroalimentación háptica como canal de primera clase, con patrones distinguibles y sin resultar intrusiva.
- Las interfaces **DEBEN** probarse en hardware real y en movimiento. Una captura en emulador no valida nada de esto.

## M10 — Versionado de algoritmos y reproducibilidad

Todo resultado producido por un algoritmo sobre señales **DEBE** llevar la versión que lo produjo:

```text
algoVersions = { <detector>: 3, <estimador>: 2 }
```

Combinado con el log de eventos (M6/M7), esto permite **reprocesar el histórico** con una versión nueva y comparar. Es la única forma honesta de saber si un cambio de algoritmo mejora algo.

## M11 — El reproductor de trazas *(herramienta de mayor palanca)*

Todo proyecto de esta clase **DEBERÍA** construir, como entregable explícito del Circuito 2, una herramienta que reproduzca trazas grabadas de sensores/eventos contra el pipeline completo, **fuera del dispositivo**.

Por qué es la de mayor palanca:

1. Permite validar la lógica sin hardware y sin condiciones reales — ataca directamente el cuello de botella de validación humana (G36).
2. Convierte cada sesión real capturada en un **test de regresión permanente**.
3. Permite comparar versiones de algoritmo sobre datos idénticos (M10).
4. Es el puente natural hacia cualquier dataset o modelo futuro.

Requisitos: reproducción determinista, ejecutable en CI, con métricas de salida comparables.

## M12 — Distribución y tienda

- El identificador de aplicación es **inmutable tras publicar** y contamina paquetes, firmas y configuración desde el primer commit. **DEBE** decidirse el día uno, aunque el nombre comercial siga abierto.
- Firmas, claves de publicación y cuentas de desarrollador son materia reservada al Owner (G05).
- Las políticas de tienda para categorías sensibles (salud, finanzas, menores) **condicionan permisos y arquitectura**: se leen en Circuito 1, no antes de publicar.
- La app **DEBE** poder actualizarse sin pérdida de datos del usuario: plan de migración de esquema local desde la primera versión instalable.

## M13 — Documentación específica esperable

```text
docs/DEVICE_CAPABILITIES.md   qué expone realmente cada dispositivo probado
docs/SENSORS.md               APIs, frecuencias, formatos, consumo, limitaciones, calibraciones
docs/SYNC.md                  propiedad de entidades, transportes, casos offline
docs/PERMISSIONS.md           cada permiso, por qué, y comportamiento si falta
docs/BATTERY.md               presupuestos y mediciones reales
```

## M14 — Sistema de diseño y resistencia al cambio *(exigido por G51)*

Aplica el mismo principio que en web: los cambios de criterio visual llegan **siempre**, y su coste se decide antes de la primera pantalla.

1. **Tema y tokens propios.** Colores, tipografías, espaciados, formas y duraciones se definen una sola vez en el tema de la aplicación. Ningún composable contiene literales de estas familias.
2. **Primitivas propias sobre la librería de componentes.** El producto envuelve los componentes de la librería de plataforma en primitivas propias con la API que necesita el producto. Si mañana cambia la versión mayor de la librería, o se decide otro criterio visual, se reimplementan las primitivas, no las pantallas.
3. **Dos superficies, un solo lenguaje.** Teléfono y wearable tienen componentes distintos por necesidad física, pero **DEBEN** compartir la capa de tokens y el vocabulario de diseño. Dos sistemas de diseño divergentes en el mismo producto es un fallo evitable.
4. **Prohibido el estilo ad hoc en pantallas**, con la misma regla de excepción justificada que en web.
5. Accesibilidad — tamaños de toque, contraste, escalado de fuente del sistema — es parte de las primitivas, no algo que cada pantalla resuelva a su manera.
