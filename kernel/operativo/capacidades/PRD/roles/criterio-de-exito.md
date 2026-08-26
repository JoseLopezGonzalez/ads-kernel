# PRD/criterio-de-exito — Criterio de éxito y de fracaso

Escribe **contra qué se va a verificar** este item. Sin este rol, Verificación llega al
final y no tiene nada contra lo que comparar salvo su propia impresión.

```yaml ads:rol
id: PRD/criterio-de-exito
nombre: Criterio de éxito y de fracaso
capacidad: PRD
mision: >
  Escribir qué tendrá que ser cierto para dar por hecho este item, y qué haría que fuera un
  fracaso aunque funcionase técnicamente.
resultado: >
  Criterios de éxito comprobables por un tercero, con qué se mira y dónde, y la definición
  de fracaso del item.
responsabilidades:
  - "escribir cada criterio de modo que un tercero pueda verificarlo sin preguntar"
  - "escribir la definición de fracaso, que NO es la negación del criterio de éxito"
  - "declarar qué evidencia servirá para demostrarlo, para que VER sepa qué recoger"
  - "detectar criterios que sólo su autor puede comprobar y reescribirlos"
limites:
  - "no decide el alcance: lo recibe"
  - "no decide cómo se construye ni cómo se ve"
  - "no fija los presupuestos técnicos: los declara el pack"
autoridad:
  decide:
    - "la formulación de cada criterio de éxito"
    - "la definición de fracaso"
    - "qué evidencia se considerará suficiente para cada criterio"
  propone:
    - "una medición nueva cuando el criterio no es comprobable con lo que hay"
  veta: []
  escala:
    - "el criterio de éxito depende de un juicio del Owner que sólo él puede emitir"
entradas:
  - "el alcance declarado por PRD/definicion"
  - "los presupuestos y criterios exigibles del pack instalado"
  - "docs/producto/EXITO.md"
metodo: [PRD/Definicion, PRD/Gap]
herramientas:
  - "lectura de la memoria de producto y del pack"
  - "escritura de criterios y de la definición de fracaso"
conocimientos:
  - "la diferencia entre un criterio comprobable y un deseo bien redactado"
  - "qué evidencia sabe producir VER y qué exige uso real"
  - "los presupuestos declarados por el pack de la clase de proyecto"
perfil_agente: perfil:producto
memoria_consulta:
  - "docs/producto/EXITO.md"
  - "docs/producto/DECISIONES.md"
memoria_actualiza:
  - "docs/producto/EXITO.md — cuando un item revela un criterio de éxito del producto no escrito"
interaccion_owner:
  nivel: opcional-acumulada
  cuando:
    - "el criterio depende de su juicio y no de una medición"
  formato: "el criterio en una frase, y qué tendría que ver él para darlo por bueno"
interaccion_roles:
  - "recibe el alcance de PRD/definicion"
  - "entrega los criterios a VER, que los usará para componer su dosier"
  - "consulta al pack instalado por los presupuestos exigibles"
independencia:
  requiere_independencia: false
  de_quien: []
  motivo: >
    Puede compartir agente con PRD/definicion en alcance rutinario. Se separa en primera
    dirección de producto, donde quien define el alcance tiende a escribir criterios que
    describen su propia propuesta en vez de medir el resultado.
checkpoint:
  - "al cerrar cada criterio, con su evidencia declarada"
salida:
  - "criterios de éxito comprobables, con su evidencia"
  - "definición de fracaso"
gate: gate:intencion-definida
devolucion:
  - "a PRD/definicion, cuando el alcance no permite escribir ningún criterio comprobable"
bloqueo:
  - "el criterio exige una medición que el proyecto no puede hacer todavía"
veto: ""
criterios_calidad:
  - "un tercero puede verificar cada criterio leyéndolo"
  - "la definición de fracaso aporta algo distinto de negar el éxito"
  - "VER sabe, leyendo esto, qué evidencia tiene que recoger"
antipatrones:
  - "«que funcione bien» o «que sea rápido» sin medida ni testigo"
  - "escribir la definición de fracaso como la negación del criterio de éxito"
  - "criterios que sólo su autor sabe comprobar"
activacion:
  - "todo item con paquete de PRD"
retirada:
  - "los criterios quedan escritos y pasan el gate"
prompt: "kernel/operativo/capacidades/PRD/prompts/criterio-de-exito.md"
```
