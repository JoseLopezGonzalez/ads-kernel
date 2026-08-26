# C2 — Agentes, modelos y perfiles

> **Un rol no es un modelo.** El rol es una responsabilidad permanente del sistema; el
> agente es la instancia que la ocupa hoy. Cambiar de proveedor no puede cambiar quién
> responde de qué.

## Los cuatro conceptos, separados

```text
ROL       responsabilidad declarada. Vive en el kernel o en un pack. Permanente.
PERFIL    qué capacidades de modelo exige ese rol, escritas SIN NOMBRAR MARCA.
AGENTE    instancia concreta: modelo + instrucciones + herramientas + contexto +
          presupuesto + rol o roles que ocupa. Temporal.
ADAPTADOR traducción entre un perfil y los modelos reales de un proveedor. Vive en el
          PROFILE del proyecto o en la instalación, NUNCA en el kernel.
```

**Regla de portabilidad (K0.8 aplicada aquí):** ningún fichero de `kernel/operativo/` ni
de `packs/` nombra un proveedor, un modelo comercial ni una herramienta de marca como
requisito. Los nombres de marca sólo aparecen en el adaptador del proyecto.

```text
PROHIBIDO en kernel y packs   "usar el modelo X de la empresa Y"
CORRECTO                      perfil_agente: perfil:critica-visual
                              → el adaptador del proyecto decide qué modelo lo cumple
```

## Cómo se asigna el mejor agente disponible

La asignación es **determinista y explicable**: mismo perfil y mismo catálogo instalado
producen la misma elección, y queda escrito por qué.

```text
1 LEER PERFIL     el rol declara su perfil_agente
2 FILTRAR         del catálogo del proyecto, los modelos que CUMPLEN O SUPERAN cada
                  exigencia del perfil. Un modelo sin visión no puede ocupar un rol que
                  declara vision: requerida, por barato que sea
3 FILTRAR         los que ofrecen las herramientas declaradas y el tamaño de contexto
4 ORDENAR         a) cumplimiento del eje dominante del perfil (el declarado en `exige`
                     con nivel `maximo`, y si hay varios, el primero por orden del esquema)
                  b) coste, dentro del techo declarado en `coste`
                  c) identificador del modelo — desempate determinista
5 ASIGNAR         el primero. Se registra: rol, perfil, modelo elegido, modelos
                  descartados y el motivo de cada descarte
6 DEGRADAR        si NINGÚN modelo cumple: se aplica `degradacion_permitida` del perfil.
                  Si el perfil no permite degradar, el paquete queda `bloqueado`
                  nombrando qué capacidad de modelo falta. NO se ocupa el rol a medias
```

> **`coste` es un techo, no un criterio de diseño.** Ordena entre candidatos que ya
> cumplen; nunca sustituye a un candidato que cumple por otro que no.

## Los siete ejes

```text
razonamiento       encadenar consecuencias, sostener una contradicción sin resolverla mal
creatividad        producir direcciones distintas entre sí, no variaciones de una
vision             leer imágenes: capturas, referencias, grabaciones, dispositivos
investigacion      buscar, contrastar fuentes, declarar frescura y fiabilidad
programacion       escribir y modificar código que compila, pasa tests y encaja
uso_herramientas   operar repositorio, navegador, dispositivo, CI sin supervisión
critica            encontrar el fallo en un trabajo terminado, incluido el propio
```

Niveles: `bajo` · `medio` · `alto` · `maximo`. `vision`: `no` · `util` · `requerida`.

## Un agente, varios roles — y cuándo está prohibido

```text
PERMITIDO   un agente ocupa VARIOS roles cuando la composición lo declara `combinables`
PERMITIDO   varios agentes ocupan EL MISMO rol en trabajos grandes, repartidos por
            artefacto o por superficie, con un integrador declarado
PERMITIDO   dos agentes con el mismo rol trabajando en COMPETENCIA sobre el mismo
            objetivo, cuando el método declara una fase divergente
PROHIBIDO   un agente ocupa a la vez un rol productor y el rol que critica su producto
PROHIBIDO   un agente ocupa a la vez dos roles con veto sobre la misma materia
PROHIBIDO   un agente ocupa dos roles que la composición declara `independientes`
```

La prohibición no es de cortesía: **es la instrumentación de G13**. Un crítico que también
construyó no encuentra el fallo que cometió; encuentra los que evitó.

## Relevo de agente

El relevo es **normal**, no una excepción. Un agente puede caer, agotarse o ser sustituido
por otro modelo a mitad de un paquete.

```text
1 el agente saliente deja checkpoint conforme a a.10 — es el gate de suspensión
2 el rol NO cambia: la identidad, la memoria y la autoridad son del rol
3 el agente entrante carga: contrato del rol, prompt operativo, método, checkpoint
4 comprueba `based_on`: si alguna fuente cambió de versión, marca
   `freshness: requiere revalidación` y revalida SÓLO la parte afectada
5 continúa desde el paso exacto. NO reinicia y NO pide resumen al Owner
```

> **Sustituir el modelo no pierde la identidad del rol ni su memoria**, porque ninguna de
> las dos vive en el agente: viven en el contrato y en los ficheros de memoria.

## Catálogo de perfiles del kernel

Los packs **PUEDEN** añadir perfiles con prefijo (`wear:perfil:…`). **NO PUEDEN** rebajar
las exigencias de un perfil del kernel: eso es un override y requiere K0.7.

```yaml ads:perfil-agente
id: perfil:interlocucion
exige:
  razonamiento: alto
  creatividad: medio
  vision: util
  investigacion: medio
  programacion: bajo
  uso_herramientas: medio
  critica: alto
contexto: amplio
herramientas: [lectura del estado persistido, búsqueda en el índice de lo existente, escritura de encuadres]
coste: alto
degradacion_permitida: >
  ninguna en el eje razonamiento ni en critica. Con vision no disponible, el rol sigue
  siendo ocupable pero NO puede recibir imágenes del Owner: en ese caso deriva la lectura
  de imágenes a un rol con vision requerida y lo deja escrito en el encuadre.
prohibido:
  - "ocupar simultáneamente un rol de construcción sobre el mismo item"
  - "decidir por el Owner en materia de su autoridad"
```

```yaml ads:perfil-agente
id: perfil:anclaje
exige:
  razonamiento: alto
  creatividad: bajo
  vision: no
  investigacion: alto
  programacion: medio
  uso_herramientas: maximo
  critica: alto
contexto: maximo
herramientas: [lectura del control repo y de las fuentes del alcance, búsqueda de código, lectura del estado persistido, lectura de ledgers]
coste: contenido
degradacion_permitida: >
  ninguna en uso_herramientas ni en contexto: un anclaje que no puede leer todo el
  repositorio produce el modo de fallo (a) que el sistema existe para evitar.
prohibido:
  - "afirmar que algo no existe sin haber ejecutado la búsqueda declarada en su método"
  - "interpretar la intención del Owner: eso pertenece a ENC/interlocutor"
```

```yaml ads:perfil-agente
id: perfil:critica-independiente
exige:
  razonamiento: maximo
  creatividad: medio
  vision: util
  investigacion: medio
  programacion: medio
  uso_herramientas: medio
  critica: maximo
contexto: amplio
herramientas: [lectura de artefactos, lectura de evidencia, escritura de dictámenes]
coste: alto
degradacion_permitida: >
  ninguna. Un crítico degradado produce dictámenes complacientes, que son peores que
  ningún dictamen porque cierran el gate con falsa autoridad.
prohibido:
  - "ocupar cualquier rol que haya producido el artefacto que critica"
  - "proponer la solución en lugar de nombrar el defecto y su evidencia"
```

```yaml ads:perfil-agente
id: perfil:direccion-artistica
exige:
  razonamiento: alto
  creatividad: maximo
  vision: requerida
  investigacion: alto
  programacion: bajo
  uso_herramientas: medio
  critica: maximo
contexto: amplio
herramientas: [lectura y escritura de la memoria de diseño, lectura de imágenes, generación de moodboards, búsqueda de referencias]
coste: sin-techo
degradacion_permitida: >
  ninguna en creatividad ni en vision. Sin vision el rol NO es ocupable: dirigir una forma
  que no se puede ver es imposible, y el paquete queda bloqueado nombrando esa carencia.
prohibido:
  - "decidir alcance de producto"
  - "aprobar su propia dirección: la crítica visual es un rol independiente"
```

```yaml ads:perfil-agente
id: perfil:investigacion-visual
exige:
  razonamiento: alto
  creatividad: alto
  vision: requerida
  investigacion: maximo
  programacion: bajo
  uso_herramientas: alto
  critica: alto
contexto: amplio
herramientas: [búsqueda en la web, lectura de imágenes, captura de referencias, escritura en la memoria de diseño]
coste: alto
degradacion_permitida: >
  ninguna en vision ni en investigacion. Sin acceso a fuentes externas el rol produce
  referencias recordadas en vez de comprobadas, y eso es material inventado.
prohibido:
  - "reproducir una obra concreta en lugar de extraer su principio"
  - "presentar una referencia sin enlace, autor y fecha comprobables"
```

```yaml ads:perfil-agente
id: perfil:diseno-visual
exige:
  razonamiento: alto
  creatividad: maximo
  vision: requerida
  investigacion: medio
  programacion: medio
  uso_herramientas: alto
  critica: alto
contexto: amplio
herramientas: [lectura de la memoria de diseño, producción de artefactos visuales, lectura de imágenes, captura de pantalla]
coste: sin-techo
degradacion_permitida: >
  ninguna en creatividad ni vision. Con programacion por debajo de medio el rol conserva
  su autoridad pero entrega la maqueta a DIS/prototipado en vez de construirla.
prohibido:
  - "entregar una única dirección cuando el método exige exploración divergente"
  - "reutilizar un patrón fuera del alcance declarado del patrón"
```

```yaml ads:perfil-agente
id: perfil:sistema-de-diseno
exige:
  razonamiento: maximo
  creatividad: medio
  vision: requerida
  investigacion: medio
  programacion: alto
  uso_herramientas: alto
  critica: maximo
contexto: maximo
herramientas: [lectura y escritura del sistema de diseño, lectura del código de componentes, comparación de artefactos]
coste: alto
degradacion_permitida: >
  ninguna en razonamiento ni critica: el rol existe para detectar inconsistencia, que es
  exactamente lo que un modelo poco crítico no ve.
prohibido:
  - "aprobar un componente nuevo sin declarar qué patrón extiende o por qué no extiende ninguno"
```

```yaml ads:perfil-agente
id: perfil:movimiento
exige:
  razonamiento: alto
  creatividad: maximo
  vision: requerida
  investigacion: medio
  programacion: alto
  uso_herramientas: alto
  critica: alto
contexto: medio
herramientas: [producción de prototipos animados, grabación de pantalla, lectura de grabaciones, medición de tiempos]
coste: sin-techo
degradacion_permitida: >
  ninguna en vision: el movimiento no se juzga leyendo su descripción. Sin capacidad de
  grabar y ver el resultado, el rol queda bloqueado.
prohibido:
  - "especificar una animación sin curva, duración y disparador"
  - "entregar movimiento sin su estado reducido para quien lo tenga desactivado"
```

```yaml ads:perfil-agente
id: perfil:prototipado
exige:
  razonamiento: alto
  creatividad: alto
  vision: requerida
  investigacion: bajo
  programacion: maximo
  uso_herramientas: maximo
  critica: medio
contexto: amplio
herramientas: [escritura de código, ejecución local, captura de pantalla, grabación de pantalla]
coste: alto
degradacion_permitida: >
  con vision no disponible el rol construye pero NO juzga el resultado: la validación
  visual pasa entera a DIS/critica-visual, y queda escrito en el checkpoint.
prohibido:
  - "integrar un prototipo en la rama productiva"
  - "presentar un prototipo sin declarar qué parte es real y qué parte está simulada"
```

```yaml ads:perfil-agente
id: perfil:construccion
exige:
  razonamiento: alto
  creatividad: medio
  vision: util
  investigacion: medio
  programacion: maximo
  uso_herramientas: maximo
  critica: alto
contexto: maximo
herramientas: [escritura de código, ejecución de tests, ejecución local, control de versiones]
coste: alto
degradacion_permitida: >
  ninguna en programacion. Con contexto por debajo de amplio, el trabajo se reparte en
  paquetes menores en vez de ocuparse a medias.
prohibido:
  - "redecidir una capa anterior en vez de devolverla"
  - "simplificar en silencio una intención de diseño aprobada"
```

```yaml ads:perfil-agente
id: perfil:verificacion
exige:
  razonamiento: maximo
  creatividad: medio
  vision: requerida
  investigacion: medio
  programacion: alto
  uso_herramientas: maximo
  critica: maximo
contexto: amplio
herramientas: [ejecución de tests, captura y comparación de imágenes, grabación, medición de presupuestos, lectura de código]
coste: alto
degradacion_permitida: >
  ninguna en critica. Sin vision, la regresión visual NO puede declararse comprobada y el
  dosier lo dice expresamente en vez de omitirlo.
prohibido:
  - "haber construido lo que verifica"
  - "emitir un sí o un no en lugar de un dosier de evidencia"
```

```yaml ads:perfil-agente
id: perfil:arquitectura
exige:
  razonamiento: maximo
  creatividad: alto
  vision: no
  investigacion: alto
  programacion: alto
  uso_herramientas: maximo
  critica: maximo
contexto: maximo
herramientas: [lectura del control repo y de las fuentes del alcance, búsqueda de código, medición de dependencias, escritura de ADR]
coste: alto
degradacion_permitida: >
  ninguna en contexto ni uso_herramientas: un radio de impacto estimado en vez de medido
  es precisamente lo que este rol existe para eliminar.
prohibido:
  - "estimar el radio de impacto en lugar de medirlo sobre el repositorio"
  - "devolver a Diseño sin traer al menos una alternativa de forma"
```

```yaml ads:perfil-agente
id: perfil:producto
exige:
  razonamiento: maximo
  creatividad: alto
  vision: util
  investigacion: alto
  programacion: bajo
  uso_herramientas: medio
  critica: alto
contexto: amplio
herramientas: [lectura del estado persistido, lectura de la memoria de producto, escritura de criterios de éxito]
coste: alto
degradacion_permitida: >
  ninguna en razonamiento: el criterio de fracaso de un item mal escrito contamina toda la
  cadena posterior.
prohibido:
  - "escribir criterios de éxito que no pueda comprobar alguien distinto de quien los escribió"
  - "decidir forma visual: esa materia pertenece a DIS"
```

```yaml ads:perfil-agente
id: perfil:dominio
exige:
  razonamiento: maximo
  creatividad: medio
  vision: no
  investigacion: alto
  programacion: alto
  uso_herramientas: alto
  critica: maximo
contexto: maximo
herramientas: [lectura de esquemas y migraciones, ejecución de consultas de sólo lectura, escritura del vocabulario de dominio]
coste: alto
degradacion_permitida: >
  ninguna. Este rol tiene veto sobre recuperabilidad de datos; un veto emitido por un
  modelo degradado es peor que la ausencia de veto.
prohibido:
  - "imponer una preferencia arquitectónica que no afecte a integridad ni recuperabilidad"
```

```yaml ads:perfil-agente
id: perfil:seguridad
exige:
  razonamiento: maximo
  creatividad: alto
  vision: no
  investigacion: maximo
  programacion: alto
  uso_herramientas: alto
  critica: maximo
contexto: amplio
herramientas: [lectura del control repo y de las fuentes del alcance, análisis de dependencias, consulta de avisos publicados, lectura de configuración]
coste: sin-techo
degradacion_permitida: >
  ninguna. Un veto duro no admite ocupación degradada: si no hay modelo que cumpla, el
  paquete queda bloqueado y se dice qué falta.
prohibido:
  - "decidir dirección de producto"
  - "levantar su propio veto sin la evidencia declarada en su contrato"
```

```yaml ads:perfil-agente
id: perfil:plataforma
exige:
  razonamiento: alto
  creatividad: medio
  vision: no
  investigacion: alto
  programacion: maximo
  uso_herramientas: maximo
  critica: alto
contexto: amplio
herramientas: [configuración de CI, gestión de entornos, observabilidad, aislamiento de agentes]
coste: contenido
degradacion_permitida: >
  ninguna en uso_herramientas. El resto admite degradación si el trabajo es de
  mantenimiento declarado como rutinario en su método.
prohibido:
  - "tomar custodia de un paquete de producto: PLT tiene backlog propio"
```

```yaml ads:perfil-agente
id: perfil:operacion
exige:
  razonamiento: maximo
  creatividad: medio
  vision: util
  investigacion: alto
  programacion: alto
  uso_herramientas: maximo
  critica: maximo
contexto: amplio
herramientas: [despliegue, lectura de logs y métricas, ejecución de smoke tests, reversión]
coste: alto
degradacion_permitida: >
  ninguna. Este rol puede revertir en producción; degradarlo es degradar la contención.
prohibido:
  - "publicar sin autorización del Owner: la publicación es materia reservada"
  - "revertir de forma destructiva o no probada en lugar de contener y escalar"
```

```yaml ads:perfil-agente
id: perfil:uso-real
exige:
  razonamiento: alto
  creatividad: medio
  vision: requerida
  investigacion: alto
  programacion: bajo
  uso_herramientas: alto
  critica: alto
contexto: medio
herramientas: [lectura de telemetría y logs, preparación de planes de validación humana, lectura de grabaciones, operación de dispositivo real]
coste: contenido
degradacion_permitida: >
  con vision no disponible el rol puede trabajar sobre telemetría y logs, y declara
  expresamente que la evidencia de observación directa no fue recogida.
prohibido:
  - "presentar la opinión del Owner como telemetría, ni la telemetría como juicio del Owner"
```

```yaml ads:perfil-agente
id: perfil:aprendizaje
exige:
  razonamiento: maximo
  creatividad: medio
  vision: no
  investigacion: alto
  programacion: bajo
  uso_herramientas: medio
  critica: maximo
contexto: maximo
herramientas: [lectura de ledgers, lectura del histórico de items, escritura de reglas candidatas]
coste: contenido
degradacion_permitida: >
  ninguna en critica: el fallo característico de este rol es promover a regla lo que fue
  una casualidad de un solo item.
prohibido:
  - "promover un aprendizaje que sólo se ha observado una vez, salvo incidente"
  - "escribir en el ledger para justificar la existencia del propio paquete"
```

```yaml ads:perfil-agente
id: perfil:despacho
exige:
  razonamiento: alto
  creatividad: bajo
  vision: no
  investigacion: medio
  programacion: alto
  uso_herramientas: maximo
  critica: alto
contexto: maximo
herramientas: [lectura y escritura del estado persistido, regeneración de vistas derivadas, registro de eventos]
coste: minimo
degradacion_permitida: >
  el despacho es mecánico y determinista por diseño: admite el modelo más barato que
  cumpla los mínimos. Lo que NO admite es degradar uso_herramientas ni contexto.
prohibido:
  - "decidir contenido de ninguna capa"
  - "marcar prioridad urgente, desaparcar o cerrar por contenido"
```

```yaml ads:perfil-agente
id: perfil:sistema
exige:
  razonamiento: maximo
  creatividad: alto
  vision: no
  investigacion: alto
  programacion: maximo
  uso_herramientas: maximo
  critica: maximo
contexto: maximo
herramientas: [lectura y escritura del kernel operativo, ejecución de validadores, ejecución de pruebas de conformidad]
coste: alto
degradacion_permitida: >
  ninguna. SIS modifica la fábrica; un error suyo se multiplica por todos los items.
prohibido:
  - "modificar una sección normativa aprobada sin registrar la contradicción y proponer el cambio"
  - "declarar superada una prueba que sólo está escrita"
```
