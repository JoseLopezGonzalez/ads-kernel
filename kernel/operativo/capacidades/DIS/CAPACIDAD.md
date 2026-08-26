# DIS · DISEÑO — forma, en sus dos niveles

`DIS` es la primera capacidad desarrollada hasta nivel operativo, y sirve de **patrón de
calidad** para las demás: no de plantilla mecánica. Lo que se copia de aquí es la
exigencia —roles con autoridad delimitada, métodos con condición de salida, crítica
independiente, memoria obligatoria—, no el contenido, que es propio de la materia.

Los dos niveles de a.3 son **simultáneos y ambos exigibles**:

```text
FUNCIONAL / EXPERIENCIA   flujo · estados · información · densidad · accesibilidad ·
                          fluidez percibida            → gate:usabilidad
ESTÉTICA / DIRECCIÓN      identidad · carácter · actualidad · intención · acabado ·
DE ARTE                   capacidad de sorprender      → gate:excelencia-visual
```

El sistema completo de excelencia está en [`../../diseno/`](../../diseno/00-SISTEMA-DE-EXCELENCIA.md).

```yaml ads:capacidad
id: DIS
nombre: Diseño
clase: estacion
mision: >
  Decidir la forma del producto en sus dos niveles —cómo se usa y cómo es— de modo que sea
  comprensible, operable y reconociblemente de este producto, y no genérico.
capa_de_valor: >
  Añade forma decidida: convierte una intención de producto en una dirección visual y de
  interacción concreta, con sus patrones, sus estados y su movimiento, y deja escrito lo
  que se descartó y por qué.
entrada:
  - "un encuadre o un paquete cuyo item cumple C-DIS de b.16"
  - "una devolución de CON con evidencia de imposibilidad demostrada"
  - "una consulta en modo consulta desde ENC, PRD, ARQ o USO"
  - "un item DIR que sustituye la dirección visual aprobada"
salida:
  - "dirección visual aprobada, o patrón aplicado, según el nivel de novedad"
  - "especificación construible: composición, estados, valores del sistema y movimiento"
  - "memoria de diseño actualizada con lo decidido Y lo descartado con su porqué"
  - "dictamen de excelencia visual del rol crítico"
  - "comparación de fidelidad cuando la capa vuelve construida"
gate: gate:excelencia-visual
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/diseno/00-VISION.md a 11-HISTORIAL.md — las doce secciones del corpus"
  - "el sistema de diseño ejecutable del proyecto, cuando existe como código"
tablero: "estado/tableros/DIS.md — paquetes de diseño, su nivel de novedad y su fase"
metodos: [DIS/Fundacion, DIS/Reconstruccion, DIS/Evolucion, DIS/CriticaVisual, DIS/RevisionDeFidelidad, DIS/ValidacionDeUso]
checkpoint: "en el paquete, con nivel de novedad, fase del método y direcciones ya descartadas"
autoridad:
  decide_sola:
    - "qué dirección visual se elige entre las exploradas, dentro de lo aprobado por el Owner"
    - "qué patrón cubre un caso y con qué alcance"
    - "los valores del sistema de diseño: escala, ritmo, roles de color, elevación"
    - "qué movimiento acompaña a cada estado y con qué curva y duración"
    - "si una imposibilidad afirmada por CON está demostrada o sólo afirmada"
    - "aceptar deuda de diseño en superficies no premium"
  escala:
    - "primera dirección visual del producto: la aprueba el Owner (a.8)"
    - "primera instancia de un patrón visual, artístico o de interacción"
    - "deuda de diseño en superficie premium o sobre un patrón aprobado por el Owner"
    - "conflicto con otra capacidad que no se resuelve en dos devoluciones (a.7)"
  veta:
    - "soluciones técnicas que degradan una dirección aprobada sin haber explorado alternativas"
owner:
  nivel: mixto
  criterio: >
    Obligatorio en la primera dirección visual del producto, en la primera instancia de
    cada patrón visual, artístico o de interacción, en el cambio de dirección y en la
    aceptación de deuda sobre superficie premium. Opcional acumulada cuando el trabajo
    extiende un owner_approved_pattern dentro de su alcance. Ninguna cuando aplica un
    patrón vigente de clase capability_approved o provisional.
roles:
  - DIS/direccion-artistica
  - DIS/investigacion-visual
  - DIS/investigacion-ux
  - DIS/diseno-interaccion
  - DIS/diseno-visual
  - DIS/sistema-de-diseno
  - DIS/movimiento
  - DIS/prototipado
  - DIS/critica-visual
  - DIS/revision-de-fidelidad
  - DIS/validacion-de-uso
deriva_de:
  - "a.3 · DIS: dos niveles simultáneos, condición de entrada y salida de memoria, veto"
  - "a.5 · contrato de veto de seis campos"
  - "b.16 · C-DIS y el papel de DIS en FEA, GAP, DEF y DIR"
materializacion: >
  Se materializa cuando DSP crea un paquete cuya capacidad responsable es DIS. La
  composición concreta la elige el algoritmo de C4 recorriendo composicion.md en orden.
retirada: >
  Cada rol se retira al entregar su artefacto. El equipo se desmaterializa cuando el
  tablero de DIS queda sin cola durante dos auditorías. La memoria de diseño NO se retira
  nunca: sobrevive al equipo y es lo que permite rematerializarlo sin empezar de cero.
```

## Contrato de veto

```yaml ads:veto
id: veto:degradacion-de-forma
capacidad: DIS
materia:
  - "sustituir una solución de forma aprobada por otra más simple, cuando no se han explorado alternativas que conserven la intención"
  - "eliminar un estado, una transición o una microinteracción especificados, sin evidencia de imposibilidad"
  - "usar valores fuera del sistema de diseño declarado, existiendo valores del sistema que sirven"
no_materia:
  - "la elección de tecnología, biblioteca o arquitectura, mientras el resultado conserve la forma aprobada"
  - "el alcance de producto: qué entra y qué no, que pertenece a PRD"
  - "una imposibilidad física o técnica DEMOSTRADA con la evidencia que exige 05-FIDELIDAD"
  - "el orden y la ruta, que pertenecen a DSP"
evidencia_minima:
  - "la especificación aprobada y su versión"
  - "la comparación intención/resultado que muestra la degradación"
  - "la lista de alternativas que DIS ha explorado o propone explorar, con al menos una concreta"
efecto: >
  El paquete no pasa el gate de excelencia visual y vuelve a CON con la comparación. El
  trabajo de CON no se borra: la capa queda vigente y se corrige la parte degradada.
levantamiento: >
  Lo levanta DIS/direccion-artistica cuando CON aporta la evidencia de imposibilidad que
  exige 05-FIDELIDAD, o el Owner cuando decide aceptar la deuda. NO es no levantable.
apelacion: >
  CON apela devolviendo con la evidencia de imposibilidad. Si DIS la rechaza y CON insiste,
  se agota el freno de dos devoluciones y DSP escala con las dos posturas escritas: qué
  intención sostiene DIS y qué obstáculo demuestra CON.
colision: >
  Frente al veto duro de SEG (G27), prevalece SEG y el paquete se recompone buscando otra
  forma de conservar la intención. Frente al veto de DOM sobre recuperabilidad, prevalece
  DOM. Frente al veto de VER por evidencia en rojo, ambos detienen y se resuelven por
  separado: no se arbitran entre sí.
```

## Índice del equipo

| | fichero |
|---|---|
| roles | [`roles/`](roles/) — once contratos |
| métodos | [`metodos/`](metodos/) — seis procedimientos |
| prompts | [`prompts/`](prompts/) — once instrucciones operativas |
| composición | [`composicion.md`](composicion.md) — doce matrices de composición |
| handoffs | [`../../circuitos/DIS-handoffs.md`](../../circuitos/DIS-handoffs.md) |
