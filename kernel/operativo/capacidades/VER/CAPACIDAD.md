# VER · VERIFICACIÓN — dosier de evidencia

**No emite un sí o un no.** Produce un artefacto que viaja hacia adelante y que un humano
puede juzgar. La revisión independiente de quien construyó deja de ser proporcional al
riesgo: es la estructura por defecto de esta capacidad (a.3).

```yaml ads:capacidad
id: VER
nombre: Verificación
clase: estacion
mision: >
  Producir la evidencia que permite a otros —y al Owner— saber si lo construido cumple lo
  que se le pidió, incluidos los estados extremos y las regresiones.
capa_de_valor: >
  Añade evidencia juzgable: tests, regresión incluida la visual, seguridad cuando aplica,
  presupuestos medidos, y capturas y grabaciones de los estados extremos.
entrada:
  - "una capa de CON depositada, con su commit y sus diferencias declaradas"
  - "los criterios de éxito de PRD y los dictámenes de DIS cuando existen"
  - "una decisión de un item DIR, para VER:decision"
salida:
  - "el dosier de evidencia, con lo comprobado y lo NO comprobado"
  - "el veredicto por criterio de éxito, con su evidencia enlazada"
  - "la regresión ejecutada, incluida la visual"
gate: gate:evidencia-suficiente
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/verificacion/COBERTURA.md — qué está cubierto por tests y qué no, con fecha"
  - "docs/verificacion/REGRESIONES.md — qué se rompió alguna vez y qué lo vigila ahora"
  - "CONVENTIONS.md — patrones técnicos, con ARQ y CON"
tablero: "estado/tableros/VER.md — paquetes en verificación y dosieres emitidos"
metodos: [VER/Dosier, VER/Decision]
checkpoint: "en el paquete, con qué criterios están comprobados y con qué evidencia"
autoridad:
  decide_sola:
    - "qué evidencia recoge y con qué método"
    - "si un criterio de éxito está satisfecho por la evidencia disponible"
    - "declarar que un criterio NO se pudo comprobar, y decirlo en el dosier"
  escala:
    - "la evidencia contradice el criterio de éxito y CON sostiene que cumple: freno de a.7"
  veta:
    - "el tránsito de un paquete mientras haya evidencia en rojo"
owner:
  nivel: opcional-acumulada
  criterio: >
    VER no pide decisiones al Owner. Su dosier alimenta la cola de validación humana por
    lotes (G36) cuando un criterio exige juicio suyo; el item no se detiene esperándolo,
    salvo que ese criterio sea condición de cierre.
roles: [VER/dosier, VER/decision]
deriva_de:
  - "a.3 · VER: no emite sí/no, produce dosier; G13 como estructura; veto con evidencia en rojo"
  - "b.16 · VER:decision como paquete obligatorio de todo DIR"
materializacion: >
  Se materializa en todo item con construcción, y en todo DIR mediante VER:decision. Nunca
  con el mismo agente que construyó.
retirada: >
  Los roles se retiran al emitir el dosier. La memoria de cobertura y regresiones persiste:
  es lo que impide volver a romper lo mismo.
```

```yaml ads:veto
id: veto:evidencia-en-rojo
capacidad: VER
materia:
  - "el tránsito de un paquete cuya evidencia muestra que un criterio de éxito no se cumple"
  - "el tránsito de un paquete con regresión detectada y no explicada"
  - "el tránsito cuando la evidencia exigida por el gate no existe"
no_materia:
  - "el criterio de éxito en sí: lo define PRD, y VER no lo redefine"
  - "la forma aprobada: la juzga DIS"
  - "el alcance: pertenece a PRD"
  - "la preferencia técnica sobre cómo se implementó, si cumple y pasa los tests"
evidencia_minima:
  - "el criterio concreto que no se cumple, citado de la capa de PRD"
  - "la salida, captura o medición que lo demuestra"
  - "la comparación con el estado anterior cuando se alega regresión"
efecto: >
  El paquete no pasa a ENT ni se integra. Vuelve a la capacidad propietaria de la capa que
  falla, con la evidencia. El veto se levanta cuando la evidencia deja de estar en rojo.
levantamiento: >
  Lo levanta VER al reejecutar y obtener evidencia en verde. Nadie más puede levantarlo, y
  no existe la excepción por urgencia: si el Owner decide entregar con evidencia en rojo,
  eso queda registrado como decisión suya con su alcance, y VER lo hace constar en el dosier.
apelacion: >
  CON apela demostrando que la evidencia se recogió mal o que el criterio se interpretó
  distinto de como lo escribió PRD. En el segundo caso decide PRD, no VER ni CON.
colision: >
  Frente al veto de SEG o de DOM, ambos detienen y se resuelven por separado: no se arbitran
  entre sí. Frente al veto de DIS por degradación de forma, ambos detienen igual.
```

```yaml ads:gate
id: gate:evidencia-suficiente
aplica_a: "el dosier de VER antes de que el paquete pase a entrega o a integración"
comprobaciones:
  - id: criterio-por-criterio
    comprueba: "cada criterio de éxito de PRD tiene veredicto y evidencia enlazada"
    como: "recorrido de la lista de criterios, uno por uno"
    automatizable: si
  - id: independencia
    comprueba: "el agente que verifica no construyó este paquete"
    como: "comparación de identificadores de agente en el registro de materialización"
    automatizable: si
  - id: regresion
    comprueba: "la regresión se ha ejecutado, incluida la visual cuando hay superficie"
    como: "salida de la suite de regresión y comparación de capturas"
    automatizable: si
  - id: estados-extremos
    comprueba: "existe evidencia de vacío, error, carga, mínimo y máximo cuando hay superficie"
    como: "recuento de capturas por superficie afectada"
    automatizable: si
  - id: presupuestos
    comprueba: "los presupuestos declarados por el pack están medidos"
    como: "medición registrada frente al presupuesto"
    automatizable: si
  - id: no-comprobado-declarado
    comprueba: "lo que no se pudo comprobar está DICHO en el dosier, no omitido"
    como: "sección de no comprobado presente, aunque sea vacía y declarada como tal"
    automatizable: si
evidencia:
  - "el dosier completo"
  - "salidas de test y de regresión"
  - "capturas y grabaciones de los estados"
  - "mediciones frente a presupuestos"
fallo: >
  El paquete no pasa. Vuelve a la capacidad propietaria de la capa que falla. Si lo que
  falta es evidencia y no comportamiento, vuelve a VER: un dosier incompleto no es un
  defecto de construcción.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
