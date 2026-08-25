# SECCIÓN (a) — EQUIPOS  · borrador 1, pendiente de aprobación del Owner

## a.0 — Qué es un equipo (definición previa, sin ella "equipo" es una etiqueta)

Un equipo existe si y sólo si tiene las nueve cosas. Sin las nueve, es una etiqueta
y el kernel DEBE rechazarlo.

  MISIÓN          una frase. Qué falta en el mundo si este equipo no existe.
  CAPA DE VALOR   qué añade al item que no traía al entrar. Es su razón de ser.
  ENTRADA         qué acepta y en qué estado mínimo
  SALIDA          qué deja escrito, siempre, aunque su respuesta sea "nada que añadir"
  MEMORIA PROPIA  su fuente de verdad persistente en el repo
  MÉTODO          su procedimiento interno; puede tener sus propios subcircuitos
  AUTORIDAD       qué decide solo · qué escala · sobre qué tiene veto
  OWNER           si su capa requiere al Owner: obligatorio, opcional o nunca
  DEVOLUCIÓN      en qué condiciones devuelve el item aguas arriba

DEVOLUCIÓN es la pieza que sustituye al "gate". Un equipo no aprueba ni rechaza:
o añade su capa, o devuelve el item al equipo cuya capa resultó insuficiente,
diciendo qué falta. Devolver es un resultado profesional normal, no un fracaso.

Regla de escala: en un proyecto pequeño una misma persona/agente PUEDE llevar
varios sombreros. Lo que NO PUEDE es saltarse una estación: la capa se escribe
siempre, aunque diga "sin impacto en mi materia, por esta razón".
Regla de existencia: ningún equipo sin cola propia. Un equipo sin trabajo real
se retira (hereda la regla de retirada de G52).

## a.1 — Tres clases de equipo

  ESTACIONES  el item las atraviesa físicamente. Dejan capa. 8.
  SERVICIOS   no poseen etapa; poseen una capacidad y su memoria. Los invoca
              cualquier estación. Tienen sus propios subcircuitos. 4.
  SISTEMA     no trabajan sobre el producto: trabajan sobre la fábrica. 2.

## a.2 — LAS ESTACIONES

### E1 · ENCUADRE
Misión        Que ningún item empiece a fabricarse ignorando lo que ya existe.
Capa          IDENTIDAD Y ANCLAJE. El item pasa de frase suelta a bloque
              persistente con: id, enunciado de una línea de lo que de verdad se
              pide, naturaleza (capacidad nueva | gap | defecto | deuda | cambio de
              dirección | pregunta), y DOSIER DE ANCLAJE:
                - qué sistemas, circuitos, módulos o agentes YA implementados tocan esto
                - qué decisiones previas lo gobiernan (ADR, PROVISIONALES, convenciones)
                - qué aprendizajes vigentes aplican
                - si duplica o solapa un item ya abierto
                - qué NO existe todavía y se creía que sí
Entrada       cualquier disparador: frase del Owner, defecto, evento externo,
              aprendizaje que reentra desde E8, hallazgo de un servicio
Salida        el bloque del item, creado y anclado. Nunca "no aplica".
Memoria       el registro de items + el índice de sistemas existentes que mantiene
Autoridad     decide sola la naturaleza y el anclaje; NO decide prioridad ni alcance
Owner         opcional — sólo para desambiguar el enunciado cuando hay dos lecturas
              que llevan a trabajo distinto
Devolución    no devuelve (es la primera). Puede CERRAR un item por duplicado,
              dejando el enlace al item vigente.
Por qué existe: es la respuesta directa a "los agentes no recuerdan ni coordinan con
lo ya implementado". Es la estación que el kernel 1.3.0 no tiene en absoluto.

### E2 · PRODUCTO
Misión        Que el item tenga intención antes que solución.
Capa          INTENCIÓN Y CRITERIO DE ÉXITO. Para quién, qué cambia para esa persona,
              qué queda explícitamente fuera, qué haría que esto fuera un fracaso
              aunque funcione, cómo se relaciona con la definición de éxito del Owner
              (K0.13), y prioridad relativa frente a la cola.
              En un GAP: aquí el gap deja de ser "falta algo" y pasa a ser un
              resultado definido con criterio de terminado. Éste es el procedimiento
              estándar de gaps que hoy no existe.
Entrada       item anclado por E1
Salida        intención + criterio de éxito + fuera de alcance + prioridad
Memoria       principios de producto, definición de éxito, historial de alcance
Autoridad     decide sola alcance rutinario; escala alcance relevante y prioridad
              estratégica (materias reservadas, G05)
Owner         OBLIGATORIO cuando el item altera alcance o prioridad; opcional si no
Devolución    a E1 si el anclaje reveló que el item real es otro

### E3 · DISEÑO
Misión        Que la forma la decida el diseño y la ingeniería esté a su servicio,
              no al revés.
Capa          FORMA, en dos niveles simultáneos y ambos exigibles:
                funcional / experiencia — flujo, estados, información, densidad,
                  accesibilidad, fluidez percibida
                estética / dirección de arte — identidad, carácter, capacidad de
                  sorprender
              Ancla obligatoria: la MEMORIA DE DISEÑO (visión estética, dirección
              de arte, referencias analizadas, sistema visual y de movimiento,
              patrones vigentes, decisiones descartadas y por qué). Consultarla
              ANTES de proponer cualquier pantalla nueva no es recomendación: es
              condición de entrada de la estación.
              Salida obligatoria: la memoria de diseño actualizada con lo decidido
              Y con lo descartado y su porqué.
Entrada       item con intención (E2)
Salida        propuesta de forma con alternativas comparadas + memoria actualizada
Memoria       docs/design/ — la memoria de diseño viva
Método        subcircuitos propios (fundación de identidad / reconstrucción-auditoría
              en proyecto existente / evolución diaria) — su relación con los
              Circuitos 0-4 y con D1-D12 se resuelve en la sección (f), no aquí
Autoridad     decide sola la forma dentro de la identidad vigente; VETO sobre
              soluciones técnicas que degraden la forma sin haber agotado alternativas
Owner         OBLIGATORIO — es el único que puede juzgar identidad y carácter
Devolución    a E2 si la intención no permite decidir la forma

### E4 · ARQUITECTURA
Misión        Que el item encaje en el sistema real, no en el imaginado.
Capa          ENCAJE Y PLAN TÉCNICO. Cómo entra esto en lo que ya hay; RADIO DE
              IMPACTO MEDIDO, no estimado (qué ficheros, módulos, contratos, datos,
              tests, documentos); qué contratos cambian; alternativas con su coste;
              qué se decide y queda registrado (ADR); descomposición en paquetes de
              trabajo con su orden y sus dependencias con otros items.
Entrada       item con forma (E3)
Salida        plan + radio de impacto + ADR cuando proceda + paquetes de trabajo
Memoria       arquitectura vigente, decisiones, contratos, deuda conocida
Autoridad     decide sola dentro de la arquitectura vigente; escala cambio estructural
Owner         opcional — sólo cuando el encaje obliga a un cambio de dirección (G51)
Devolución    a E3 si la forma es irrealizable — y DEBE traer alternativas de forma,
              no sólo la negativa

### E5 · CONSTRUCCIÓN
Misión        Convertir las capas anteriores en la cosa real.
Capa          LA IMPLEMENTACIÓN Y SUS TESTS. Código, tests propios, y la
              documentación de lo que hizo distinto a lo planificado.
              NO redecide las capas 2-4. Si descubre que una es errónea, DEVUELVE.
              Implementar sobre una capa que sabe mal es el fallo característico de
              esta estación.
Entrada       paquete de trabajo con plan (E4)
Salida        cambio implementado, aislado, con sus tests y su traza
Memoria       convenciones, patrones de código, deuda introducida conscientemente
Autoridad     decide sola todo lo interno; sin autoridad sobre forma ni intención
Owner         nunca directamente
Devolución    a E4 (plan inviable) o a E3 (forma que sólo se revela imposible al
              construirla)

### E6 · VERIFICACIÓN
Misión        Que exista evidencia, no opinión, de que las capas se cumplieron.
Capa          DOSIER DE EVIDENCIA — y esto es lo que la distingue de un gate:
              no emite un sí/no, produce un artefacto que viaja hacia adelante y que
              el Owner podrá usar en E7. Contiene: revisión independiente de quien
              construyó (G13 deja de ser proporcional al riesgo y pasa a ser
              estructura por defecto), tests, regresión incluida la visual,
              seguridad cuando aplica, presupuestos de rendimiento, y evidencia
              JUZGABLE POR UN HUMANO (capturas, grabaciones, comparativas
              antes/después, estados extremos: vacío, error, carga, mínimo, máximo).
Entrada       cambio implementado (E5)
Salida        dosier de evidencia, con lo que falla explícito
Memoria       histórico de defectos escapados, cobertura, regresiones
Autoridad     VETO sobre integración mientras haya evidencia en rojo
Owner         nunca directamente (prepara para E7)
Devolución    a E5 (defecto), a E4 (el plan no era verificable), a E2 (el criterio
              de éxito no era comprobable — hallazgo caro y valioso)

### E7 · USO REAL
Misión        Que el juicio del Owner llegue barato, agrupado y convertido en dato.
Capa          JUICIO. Prepara el item para que el Owner pueda probarlo con el mínimo
              set-up (hereda G36 íntegro: cola priorizada, plan de validación único,
              orden por coste de set-up, estado preparado de antemano), recoge la
              reacción y la convierte en salida estructurada: aceptado · rechazado ·
              nueva dirección (G51) · item nuevo.
Entrada       item con dosier de evidencia (E6)
Salida        veredicto del Owner, estructurado, con lo aprendido separado de lo pedido
Memoria       cola de aceptación, histórico de veredictos, throughput real del Owner
Autoridad     ninguna propia; opera la autoridad del Owner
Owner         OBLIGATORIO por definición
Devolución    a cualquier estación, según lo que el Owner haya dicho

### E8 · APRENDIZAJE
Misión        Cerrar el ciclo: que la próxima vuelta empiece con más criterio.
Capa          CRITERIO. Convierte el recorrido en cambio de criterio: entradas en los
              ledgers (G52), promoción de aprendizaje a regla, actualización de la
              memoria de diseño y de las memorias de equipo, candidatos a UPSTREAM
              (K0.12), ajuste de la propia cadena si el recorrido reveló una estación
              mal definida, Y — la parte que la convierte en ciclo y no en tubería —
              LOS ITEMS NUEVOS que nacen del uso real, que entrega a E1.
Entrada       item cerrado (aceptado o rechazado) + su recorrido completo
Salida        criterio cambiado + items nuevos hacia E1
Memoria       los dos ledgers (G52), UPSTREAM.md
Autoridad     decide sola la curación; escala cambios de plantilla que toquen
              autoridad, permisos o coste
Owner         opcional
Devolución    no devuelve; reinyecta por E1

## a.3 — LOS SERVICIOS

No poseen etapa. Poseen capacidad, memoria y subcircuitos propios. Cualquier
estación los invoca; la petición es explícita y trazable (nunca "lo miro yo de paso").
Un servicio devuelve su respuesta COMO CAPA, con la misma disciplina que una estación.

S1 · INVESTIGACIÓN Y EVIDENCIA
   Preguntas falsables, spikes contra el entorno real, freshness de la evidencia
   (G22 + G33). Invocado por cualquier estación que choque con una incógnita.
   Autoridad: puede declarar que una decisión NO puede tomarse todavía.

S2 · DOMINIO Y DATOS
   El modelo de dominio, el vocabulario compartido, los contratos de datos, la
   reversibilidad de los esquemas. Veto sobre cambios que rompan el modelo o la
   recuperabilidad de datos.

S3 · SEGURIDAD Y PRIVACIDAD
   G27 + G28 + el marco de cumplimiento declarado. Veto duro, no negociable por
   ninguna estación.

S4 · PLATAFORMA
   La fábrica técnica: build, CI, entornos, tooling, observabilidad, aislamiento
   multiagente. Tiene cola propia y su propio backlog: la fábrica es un producto
   con sus items, no una tarea de fondo.

## a.4 — LOS EQUIPOS DE SISTEMA

X1 · INGENIERÍA DEL SISTEMA  (evolución de G14)
   Dueño del sistema operativo: memoria en bloques, dispatcher, plantillas
   uniformes, definición de la cadena, prueba de conformidad de una organización
   instalada, enrutamiento de modelos, rendimiento de los equipos, revisión de
   plantilla con regla de retirada (G52).
   Trabaja sobre la fábrica, nunca sobre el producto.

X2 · DESPACHO
   El equipo más delgado y el que hace que esto funcione. Dueño del ESTADO DE LA
   CADENA COMPLETA, no de ningún item concreto: reconstruye el estado al abrir,
   contrasta el estado declarado contra la realidad del repo, resuelve
   inconsistencias, decide qué item avanza y a qué estación, detecta items
   estancados, y deja siempre preparado el paso siguiente.
   Es quien responde a "Continúa".
   El dispatcher (software) es su herramienta; se diseña en la sección (g).
   Autoridad: ninguna sobre el contenido de ninguna capa. Total sobre el ORDEN.

## a.5 — Lo que deliberadamente NO es equipo

- DOCUMENTACIÓN. No hay equipo de documentación. La documentación ES la capa que
  cada estación escribe. Un equipo de documentación es el sitio donde la
  documentación va a olvidarse, y crea el fallo exacto que este rediseño ataca:
  que lo que un equipo añadió se pierda en el handoff.
  La coherencia del corpus la lleva E8 con X1.
- QA como departamento separado de la verificación. E6 lo absorbe.
- "Orquestación" como capacidad abstracta (G12). Es X2, con nombre y cola.

## a.6 — Derivada sobre el kernel actual

G11 (13 cajas de capacidades) queda DEROGADA y sustituida por a.0-a.4.
G12 queda sustituida por X2 + la sección (g).
G13 sobrevive pero cambia de naturaleza: deja de ser "proporcional al riesgo" y
pasa a ser la estructura por defecto (E5 nunca es su propio E6).
G14 se convierte en X1.
G07 se convierte en protocolo, no en embudo: los puntos de interacción con el
Owner pertenecen a las estaciones (E2, E3, E7 obligatorios) y el Gateway los
consolida y agenda en vez de sustituirlos. -> se cierra en la sección (d).

## a.7 — Decisiones abiertas de ESTA sección (para el Owner)

A1  ¿E1 y E2 separadas o fusionadas? Separadas porque la capa de E1 (anclaje en lo
    existente) es exactamente lo que falta hoy y fusionarla con definición de
    producto la diluye. Fusionables si te parecen demasiada ceremonia.
A2  ¿DOMINIO Y DATOS es servicio o estación? Propuesto como servicio. En un
    proyecto con un modelo de dominio grande y vivo podría merecer estación propia
    entre E2 y E4.
A3  ¿DESPACHO es equipo o mecanismo? Propuesto como equipo, para que tenga dueño y
    cola. Alternativa: sólo software, propiedad de X1.
A4  ¿Confirmas que no hay equipo de documentación?
A5  14 equipos. ¿Te parece la escala correcta, o quieres una versión con menos
    estaciones para proyectos pequeños? La regla de sombreros (a.0) ya lo permite,
    pero puedo hacerla explícita.
