---
pack:    pack-web-app
kernel:  ^1.0.0
version: 1.1.0
scope:   Aplicaciones web con interfaz de usuario, con o sin backend propio
---

# PACK — Web App

Saber hacer común a **cualquier** aplicación web. No contiene decisiones de producto ni framework concreto: contiene lo que se olvida en todos los proyectos web y cuesta caro añadir después.

Se lee junto al KERNEL. Un PROFILE que declare `packs: [pack-web-app]` hereda estas reglas y **PUEDE** sobrescribirlas como override declarado.

---

## W1 — Qué es el "entorno real" para los spikes (G22)

Un proyecto web tiene la trampa de que *todo funciona en local con datos de juguete*. Los spikes obligatorios de esta clase de proyecto se ejecutan contra:

```text
Navegadores y dispositivos reales del público objetivo, no sólo el del Owner
Red degradada (3G simulada, latencia alta, pérdida de paquetes)
Volumen de datos realista, no 20 filas de seed
El proveedor real (auth, pagos, correo, storage) con credenciales reales
El entorno desplegado, no el servidor de desarrollo
```

Spikes recomendados por defecto en toda web app:

| ID | Pregunta | Qué se mide |
|---|---|---|
| W-SPIKE-a | ¿Aguanta la vista principal el volumen real de datos? | tiempo de respuesta con dataset realista, no con seed |
| W-SPIKE-b | ¿Qué hace la app con red mala o caída? | comportamiento observado, no diseñado |
| W-SPIKE-c | ¿Los límites del proveedor externo permiten el caso de uso? | rate limits, cuotas, coste por unidad |
| W-SPIKE-d | ¿Cuánto cuesta al mes con uso previsto? | coste real medido, no estimado |

## W2 — Presupuestos de rendimiento *(obligatorio antes de construir UI)*

El rendimiento web se degrada silenciosamente y se arregla caro. El PROFILE **DEBE** fijar presupuestos numéricos **antes** de la primera pantalla, y CI **DEBERÍA** verificarlos.

```text
DECISIÓN: presupuestos de rendimiento
ESTADO:   PROVISIONAL (ajustar en el PROFILE según público y dispositivo objetivo)
  · LCP                    < 2,5 s en dispositivo y red medianos del público objetivo
  · INP                    < 200 ms
  · CLS                    < 0,1
  · Peso de JS inicial     presupuesto explícito en KB, no "el que salga"
  · Consultas por vista    presupuesto explícito; prohibido el N+1 sin justificación
REVISIÓN: tras medir con datos y dispositivos reales (W-SPIKE-a)
```

Regla: una regresión de presupuesto es un **fallo de CI**, no una observación.

## W3 — Datos, migraciones y reversibilidad

En web, el esquema es la parte **menos reversible** del sistema. Reglas:

1. Toda migración **DEBE** ser reversible o tener plan de reversión escrito antes de aplicarse.
2. Los cambios destructivos de esquema (drop de columna/tabla, cambio de tipo con pérdida) se despliegan en **fases separadas**: añadir → escribir en ambos → migrar → dejar de leer → eliminar. Nunca en un solo despliegue.
3. **NUNCA** borrado físico en entidades con histórico o referencias: borrado lógico (`deletedAt`).
4. Toda entidad lleva `id`, `createdAt`, `updatedAt`. Identificadores ordenables (ULID/UUIDv7) salvo justificación.
5. **DEBE** existir backup verificado antes de la primera migración destructiva. Un backup que nunca se ha restaurado no es un backup.
6. Los datos de producción **NUNCA** se copian a desarrollo sin anonimizar (refuerza G27).

## W4 — Entornos y despliegue

```text
local → preview (por rama/PR) → staging (opcional) → producción
```

- Todo PR **DEBERÍA** generar un entorno de preview desplegado y enlazado en el propio PR. Es lo que hace posible la validación humana por lotes (G36) sin instalar nada.
- El despliegue a producción es materia de **autoridad**, no de técnica: por defecto `Owner Acceptance Required` hasta que el sistema demuestre fiabilidad medida (G25, G29).
- **DEBE** existir rollback de un solo paso a la versión anterior, y probarse al menos una vez antes de tener usuarios.
- Merge ≠ deploy ≠ release visible al usuario. Si el proyecto usa despliegue continuo, la separación se consigue con feature flags (G31), no eliminando la distinción.

## W5 — Autenticación, sesiones y autorización

- La autenticación **NO DEBE** implementarse a mano si existe una solución establecida adecuada, salvo decisión justificada por ADR.
- La autorización se comprueba **en el servidor**, siempre. Ocultar un botón no es autorización.
- Toda ruta o endpoint nace **denegado por defecto**; se abre explícitamente.
- Multi-tenant: toda consulta lleva el filtro de tenant a nivel de capa de datos, no a criterio de quien escribe la query. Un fallo aquí es una fuga de datos entre clientes, no un bug.
- Sesiones, tokens y cookies: `httpOnly`, `secure`, `sameSite` por defecto; expiración explícita; revocación posible.

## W6 — Seguridad web *(complementa G27)*

Reglas mínimas no delegables:

1. Toda entrada de usuario se valida **en servidor**, con esquema explícito. La validación de cliente es UX, no seguridad.
2. Nunca concatenar SQL con entrada de usuario. Consultas parametrizadas o query builder.
3. Escapado por defecto en render; el "HTML crudo" requiere justificación y saneado explícito.
4. CSRF cubierto en toda mutación con sesión de cookie.
5. Cabeceras de seguridad configuradas explícitamente (CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`).
6. Rate limiting en autenticación, recuperación de contraseña y endpoints costosos.
7. Subida de ficheros: tipo, tamaño y contenido verificados; almacenamiento fuera de la raíz servida; nombres generados, nunca los del usuario.
8. Dependencias: auditoría automática en CI (refuerza G28).
9. Ningún secreto en el bundle de cliente. Todo lo que llega al navegador es público, incluidas las variables "de entorno" del framework de cliente.

## W7 — Observabilidad y errores

Una web app sin observabilidad no se puede operar autónomamente: la organización no sabe si un cambio ha roto algo hasta que el Owner lo ve.

**DEBE** existir, desde el Circuito 2:

- logs estructurados con identificador de petición;
- captura de errores de servidor **y** de cliente, agrupada;
- alguna señal de disponibilidad del flujo crítico;
- métricas básicas de latencia por ruta.

Regla: un error en producción sin traza reproducible es un fallo de observabilidad, no sólo un bug.

## W8 — Accesibilidad e internacionalización

- Contraste, foco visible, navegación por teclado y etiquetas de formulario son **requisitos**, no mejoras. Se comprueban en CI con un linter de accesibilidad.
- Todo texto visible nace preparado para extraerse. Retrofitear i18n en una app hecha con literales incrustados es una de las refactorizaciones más caras y menos gratificantes que existen. Si el PROFILE decide **no** internacionalizar, **DEBE** decirlo explícitamente como decisión, no dejarlo al azar.
- Formatos de fecha, número y moneda: nunca concatenados a mano.

## W9 — Cookies, analítica y consentimiento

- Ninguna cookie o script no esencial antes del consentimiento, cuando aplique el marco legal declarado en el PROFILE.
- La analítica es una **decisión de producto con implicaciones de privacidad**, no un añadido técnico: pasa por el PROFILE.
- Los datos personales **NUNCA** en parámetros de URL ni en query strings (quedan en logs, en referrers y en la analítica de terceros).

## W10 — SEO y compartición *(sólo si hay contenido público)*

Si el PROFILE declara contenido público: renderizado indexable, metadatos por página, URLs canónicas, sitemap y previsualizaciones sociales. Si el producto es una herramienta tras login, esta sección **NO** aplica y el PROFILE **DEBE** decirlo para que nadie invierta ahí.

## W11 — Documentación específica esperable

```text
docs/API.md              contratos de endpoints o acciones de servidor
docs/DATA_MODEL.md       esquema, migraciones y su historia
docs/ENVIRONMENTS.md     entornos, variables, secretos (referencias, no valores)
docs/RUNBOOK.md          qué hacer cuando algo falla en producción
docs/PERFORMANCE.md      presupuestos vigentes y mediciones
```

## W12 — Validación humana en web *(instancia de G36)*

La ventaja de esta clase de proyecto es que el entorno de preview por PR permite validar **sin coste de set-up**. Por tanto:

- El Plan de Validación **DEBE** incluir el enlace de preview y datos de prueba ya cargados.
- El sistema **DEBE** dejar el estado preparado: si validar requiere que el Owner cree tres registros antes, el sistema los crea.
- Regla práctica: si el Owner necesita más de un minuto de preparación para empezar a validar, el plan está mal hecho.

## W13 — Sistema de diseño y resistencia al cambio *(exigido por G51)*

El cambio de criterio visual es **el más frecuente de todos** los cambios de dirección: el Owner ve la aplicación funcionando y quiere que se parezca a otra cosa. Que eso sea barato o carísimo se decide en el Circuito 2, no cuando llega la petición.

Reglas obligatorias antes de construir la primera pantalla:

1. **Capa de tokens.** Color, tipografía, espaciado, radios, sombras, duraciones y breakpoints se definen **una vez**, en una capa propia. Ningún componente contiene un valor literal de estas familias. Cambiar la identidad visual completa debe ser cambiar los tokens, no recorrer la aplicación.
2. **Primitivas propias envolviendo la librería.** El producto **NO DEBE** consumir directamente los componentes de una librería de terceros. Se envuelven en primitivas propias (`Button`, `Input`, `Dialog`, `Card`…) que exponen la API que necesita el producto.
   Sustituir la librería pasa entonces de "reescribir la aplicación" a "reimplementar N primitivas con la misma firma". Es la diferencia entre una semana y un trimestre.
3. **Inventario de primitivas** documentado en `docs/DESIGN_SYSTEM.md`: qué existe, qué variantes tiene y cuál es su API. Sin inventario, cada agente inventa su propio botón.
4. **Prohibido el estilo ad hoc en pantallas.** Un valor visual que no venga de un token o de una primitiva es una excepción que requiere justificación, y **DEBERÍA** detectarla el linter.
5. **Modo oscuro y densidad**, si van a existir alguna vez, se contemplan desde el diseño de tokens. Retrofitearlos es caro y siempre queda mal.

Cuando llega un cambio de dirección visual (G51), el sistema **DEBE** responder con el radio de impacto real medido sobre esta estructura: *"son N tokens y M primitivas"* o *"son 340 archivos con estilos incrustados, y eso es un problema nuestro, no tuyo"*. La segunda respuesta es un fallo de este pack.
