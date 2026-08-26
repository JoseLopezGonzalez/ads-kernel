# DIS — matrices de composición

Once roles **no significan once agentes permanentes**. El algoritmo de
[`C4`](../../contratos/C4-MATERIALIZACION.md) recorre estos bloques **en el orden en que
están escritos** y se queda con el primero cuya condición es verdadera. El orden es parte
del contrato.

```text
ORDEN DE EVALUACIÓN
 1 bug-visual            2 extension-de-patron      3 gap-de-diseno
 4 caso-nuevo            5 nueva-interaccion        6 animacion
 7 revision-implementacion  8 feature-visual        9 reconstruccion
10 proyecto-nuevo
```

Las tres adaptaciones —web, móvil y Wear OS— no son composiciones distintas: **son roles
especializados que aporta el pack instalado** y que se añaden a la composición elegida.
Están al final de este documento.

```yaml ads:composicion
id: composicion:dis-bug-visual
capacidad: DIS
clase_de_trabajo: "defecto visual: la superficie incumple un patrón vigente"
condicion: >
  El item es de tipo DEF, existe un patrón vigente cuyo alcance cubre la superficie, y la
  desviación se puede localizar comparando lo construido con ese patrón.
roles:
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: false
    agentes: "1"
    condicion: "la desviación revela que el patrón no cubría el caso que decía cubrir"
combinables:
  - roles: [DIS/revision-de-fidelidad, DIS/sistema-de-diseno]
    motivo: "comprobar la desviación y localizar el patrón que la permitió es el mismo acto de lectura"
    condicion: "la desviación afecta a un solo valor del sistema"
independientes:
  - rol: DIS/revision-de-fidelidad
    de: ["todo rol que produjo la superficie, en el equipo que la construyó"]
    motivo: "quien produjo la superficie reconoce en ella lo que quiso hacer, no lo que hay"
ampliacion: >
  Si la comparación revela que no había patrón que cubriera el caso, el item deja de ser
  DEF y cambia de proceso según b.1: la composición pasa a dis-caso-nuevo.
reduccion: "no admite reducción: un solo rol es el mínimo."
retirada: "al emitir el veredicto de fidelidad y quedar corregida la desviación."
```

```yaml ads:composicion
id: composicion:dis-extension-de-patron
capacidad: DIS
clase_de_trabajo: "aplicar un patrón vigente a una superficie nueva"
condicion: >
  La escala de novedad devuelve N0: existe patrón vigente cuyo alcance cubre el caso, se
  cumplen sus criterios comprobables y no se introduce nada fuera de su alcance.
roles:
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "1"
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1, distinto del anterior"
combinables: []
independientes:
  - rol: DIS/revision-de-fidelidad
    de: [DIS/diseno-visual]
    motivo: "quien especifica la superficie no comprueba si lo construido corresponde a su propia especificación"
ampliacion: >
  Si al aplicar el patrón aparece un caso que su alcance no cubre, se sube a N1 y la
  composición pasa a dis-caso-nuevo. Bajar de nivel para ahorrar exploración está prohibido.
reduccion: "no admite reducción."
retirada: "al quedar la superficie resuelta y comprobada su fidelidad."
```

```yaml ads:composicion
id: composicion:dis-gap-de-diseno
capacidad: DIS
clase_de_trabajo: "una superficie existente no alcanza la dirección aprobada"
condicion: >
  El item es de tipo GAP, existe dirección visual aprobada, y la superficie se construyó
  sin aplicarla o aplicándola parcialmente.
roles:
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de los anteriores"
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
combinables:
  - roles: [DIS/diseno-visual, DIS/sistema-de-diseno]
    motivo: "cerrar el hueco y ajustar el sistema son la misma decisión cuando afecta a una superficie"
    condicion: "el gap afecta a una sola superficie"
independientes:
  - rol: DIS/critica-visual
    de: [DIS/diseno-visual, DIS/sistema-de-diseno]
    motivo: "el dictamen de excelencia deja de detener nada si lo firma quien produjo el artefacto"
  - rol: DIS/revision-de-fidelidad
    de: [DIS/diseno-visual]
    motivo: "quien especifica no comprueba su propia fidelidad"
ampliacion: >
  Si el gap afecta a más de tres superficies, se añade DIS/direccion-artistica: dejó de ser
  un hueco de aplicación y es un problema de dirección.
reduccion: >
  DIS/sistema-de-diseno se retira si el gap se cierra sin tocar el sistema, lo que se
  comprueba extrayendo los valores usados.
retirada: "al cerrar el gate de excelencia visual con dictamen conforme."
```

```yaml ads:composicion
id: composicion:dis-caso-nuevo
capacidad: DIS
clase_de_trabajo: "caso que el sistema no cubre, dentro de una dirección vigente"
condicion: >
  La escala de novedad devuelve N1: existen patrones vigentes pero ninguno cubre este caso
  con su alcance declarado.
roles:
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "1"
  - rol: DIS/diseno-interaccion
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de todos los anteriores"
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-ux
    obligatorio: false
    agentes: "1"
    condicion: "no existen datos reales de la superficie afectada"
combinables:
  - roles: [DIS/diseno-visual, DIS/diseno-interaccion]
    motivo: "en un caso acotado, forma y comportamiento se deciden en el mismo acto"
  - roles: [DIS/sistema-de-diseno, DIS/direccion-artistica]
    motivo: "en nivel N1 la dirección ya está fijada y formalizar no compite con decidir"
independientes:
  - rol: DIS/critica-visual
    de: [DIS/diseno-visual, DIS/diseno-interaccion, DIS/sistema-de-diseno, DIS/investigacion-ux]
    motivo: "el dictamen de excelencia deja de detener nada si lo firma quien produjo el artefacto"
  - rol: DIS/revision-de-fidelidad
    de: [DIS/diseno-visual]
    motivo: "quien especifica no comprueba su propia fidelidad"
ampliacion: >
  Si la crítica devuelve porque las dos alternativas no difieren, se añade
  DIS/investigacion-visual: el material de partida no bastaba.
reduccion: >
  DIS/investigacion-ux se retira cuando ya existen datos reales registrados de la
  superficie.
retirada: "al cerrar el gate con dictamen conforme y el sistema actualizado."
```

```yaml ads:composicion
id: composicion:dis-nueva-interaccion
capacidad: DIS
clase_de_trabajo: "una forma de interactuar que el producto no tenía"
condicion: >
  El item introduce un gesto, un control o un flujo que no existe en docs/diseno/07-COMPONENTES.md
  ni en la memoria de adaptación.
roles:
  - rol: DIS/diseno-interaccion
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-ux
    obligatorio: true
    agentes: "1"
  - rol: DIS/movimiento
    obligatorio: true
    agentes: "1"
  - rol: DIS/prototipado
    obligatorio: true
    agentes: "1"
  - rol: DIS/validacion-de-uso
    obligatorio: true
    agentes: "1, distinto de diseno-interaccion y de prototipado"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de todos los anteriores"
combinables:
  - roles: [DIS/movimiento, DIS/prototipado]
    motivo: "el prototipo es el medio natural de especificar y medir el movimiento"
independientes:
  - rol: DIS/validacion-de-uso
    de: [DIS/diseno-interaccion, DIS/prototipado]
    motivo: "quien diseñó el flujo lo recorre sin dudar: validaría su memoria, no la interfaz"
  - rol: DIS/critica-visual
    de: [DIS/diseno-interaccion, DIS/movimiento, DIS/prototipado, DIS/investigacion-ux]
    motivo: "el dictamen de excelencia deja de detener nada si lo firma quien produjo el artefacto"
ampliacion: >
  Si el pack instalado declara roles especializados para el medio —gestos, corona, teclado—
  se añaden aquí, sin sustituir a ninguno de los anteriores.
reduccion: >
  DIS/investigacion-ux se retira si la interacción nueva sustituye a una existente cuyo
  perfil de uso ya está registrado.
retirada: "al validar la interacción con uso real y cerrar ambos gates."
```

```yaml ads:composicion
id: composicion:dis-animacion
capacidad: DIS
clase_de_trabajo: "movimiento nuevo sobre una superficie existente"
condicion: >
  El item introduce o modifica una transición o una microinteracción, y no cambia la
  composición estática de la superficie.
roles:
  - rol: DIS/movimiento
    obligatorio: true
    agentes: "1"
  - rol: DIS/prototipado
    obligatorio: true
    agentes: "el mismo agente que movimiento"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto"
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
combinables:
  - roles: [DIS/movimiento, DIS/prototipado]
    motivo: "el prototipo es el medio natural de especificar y medir el movimiento"
independientes:
  - rol: DIS/critica-visual
    de: [DIS/movimiento, DIS/prototipado]
    motivo: "juzgar el movimiento exige verlo sin haber decidido antes cómo debía verse"
  - rol: DIS/revision-de-fidelidad
    de: [DIS/movimiento]
    motivo: "quien especificó la duración tiende a reconocerla en la grabación aunque no coincida"
ampliacion: >
  Si la medición en dispositivo real incumple el presupuesto del pack, se añade una
  consulta a PLT sobre el coste de rendimiento, y el paquete puede devolverse a
  DIS/diseno-interaccion si hay que replantear el estado que la transición conecta.
reduccion: "no admite reducción: el estado reducido y la grabación son obligatorios."
retirada: "al quedar grabada la especificación y comprobada la fidelidad en dispositivo."
```

```yaml ads:composicion
id: composicion:dis-revision-implementacion
capacidad: DIS
clase_de_trabajo: "comprobar lo que Construcción ha entregado"
condicion: >
  CON entrega una capa que implementa una especificación de DIS, y el paquete de DIS es de
  revisión, no de producción.
roles:
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: false
    agentes: "1"
    condicion: "el veredicto de fidelidad es infiel o hay deuda propuesta sobre superficie premium"
combinables: []
independientes:
  - rol: DIS/revision-de-fidelidad
    de: ["todo rol que produjo la especificación que se compara"]
    motivo: "quien produjo la especificación reconoce en lo construido lo que imaginó, no lo que hay"
  - rol: DIS/critica-visual
    de: [DIS/revision-de-fidelidad]
    motivo: "el eje fidelidad se apoya en la comparación: quien la produjo no la juzga"
ampliacion: >
  Si la comparación revela que la especificación no era construible, se añade
  DIS/direccion-artistica para explorar alternativas que conserven la intención.
reduccion: "no admite reducción."
retirada: "al emitir el veredicto."
```

```yaml ads:composicion
id: composicion:dis-feature-visual
capacidad: DIS
clase_de_trabajo: "superficie importante nueva dentro de una dirección vigente"
condicion: >
  La escala de novedad devuelve N2: la superficie no está cubierta por ningún patrón
  vigente, y es premium o introduce interacción o movimiento que no existía.
roles:
  - rol: DIS/direccion-artistica
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-ux
    obligatorio: true
    agentes: "1"
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "1 o 2 en competencia declarada"
  - rol: DIS/diseno-interaccion
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: true
    agentes: "1"
  - rol: DIS/movimiento
    obligatorio: false
    agentes: "1"
    condicion: "la superficie introduce transición o microinteracción nueva"
  - rol: DIS/prototipado
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de todos los productores"
  - rol: DIS/validacion-de-uso
    obligatorio: true
    agentes: "1, distinto de diseno-interaccion y prototipado"
  - rol: DIS/revision-de-fidelidad
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-visual
    obligatorio: false
    agentes: "1"
    condicion: "el material registrado en 02-REFERENCIAS no cubre la materia de esta superficie"
combinables:
  - roles: [DIS/diseno-visual, DIS/diseno-interaccion]
    motivo: "con un solo flujo, forma y comportamiento se deciden en el mismo acto"
    condicion: "la superficie tiene un solo flujo principal"
  - roles: [DIS/movimiento, DIS/prototipado]
    motivo: "el prototipo es el medio natural de especificar y medir el movimiento"
  - roles: [DIS/direccion-artistica, DIS/sistema-de-diseno]
    motivo: "la dirección del producto ya está aprobada; aquí sólo se aplica y se formaliza"
independientes:
  - rol: DIS/critica-visual
    de: [DIS/direccion-artistica, DIS/diseno-visual, DIS/diseno-interaccion, DIS/sistema-de-diseno, DIS/movimiento, DIS/prototipado, DIS/investigacion-visual, DIS/investigacion-ux]
    motivo: "el dictamen de excelencia deja de detener nada si lo firma quien produjo el artefacto"
  - rol: DIS/validacion-de-uso
    de: [DIS/diseno-interaccion, DIS/prototipado]
    motivo: "quien diseñó el flujo lo recorre sin dudar: validaría su memoria, no la interfaz"
  - rol: DIS/revision-de-fidelidad
    de: [DIS/diseno-visual, DIS/movimiento]
    motivo: "quien especificó reconoce en lo construido lo que imaginó, no lo que hay"
ampliacion: >
  Dos agentes en DIS/diseno-visual trabajando en competencia declarada cuando la superficie
  concentra la diferencia del producto. El criterio de comparación se escribe ANTES de
  empezar, y DIS/direccion-artistica es el integrador declarado.
reduccion: >
  DIS/investigacion-visual y DIS/movimiento se retiran cuando sus condiciones son falsas,
  comprobadas contra la memoria. Ningún otro rol se retira por prisa.
retirada: "cuando ambos gates cierran y la memoria recoge decisiones y descartes."
```

```yaml ads:composicion
id: composicion:dis-reconstruccion
capacidad: DIS
clase_de_trabajo: "reconstruir la dirección de un producto existente"
condicion: >
  La escala de novedad devuelve N3: hay producto construido y no hay dirección visual
  escrita que lo explique.
roles:
  - rol: DIS/direccion-artistica
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: true
    agentes: "1, distinto del anterior"
  - rol: DIS/investigacion-ux
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-visual
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de todos los anteriores"
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "1"
combinables:
  - roles: [DIS/investigacion-ux, DIS/investigacion-visual]
    motivo: "en un producto pequeño, el inventario de uso y el de forma se recorren a la vez"
    condicion: "el producto tiene menos de diez superficies"
independientes:
  - rol: DIS/sistema-de-diseno
    de: [DIS/direccion-artistica]
    motivo: "formalizar y decidir a la vez produce un sistema que describe lo que se hizo en vez de gobernar lo que se hará"
  - rol: DIS/critica-visual
    de: [DIS/direccion-artistica, DIS/sistema-de-diseno, DIS/diseno-visual, DIS/investigacion-ux, DIS/investigacion-visual]
    motivo: "el dictamen sobre una reconstrucción no puede firmarlo quien la reconstruyó"
ampliacion: >
  Con más de treinta superficies, se reparte el inventario entre varios agentes de
  DIS/sistema-de-diseno por zona del producto, con DIS/direccion-artistica como integrador
  declarado.
reduccion: >
  DIS/investigacion-visual se retira cuando el encargo es sólo reconstruir y no proponer
  evolución.
retirada: "cuando el corpus inicial está escrito y el Owner ha confirmado qué se conserva."
```

```yaml ads:composicion
id: composicion:dis-proyecto-nuevo
capacidad: DIS
clase_de_trabajo: "fundar la dirección visual de un producto nuevo"
condicion: >
  La escala de novedad devuelve N4: no existe memoria:vision-artistica, o un item DIR
  aprobado sustituye la dirección del producto.
roles:
  - rol: DIS/direccion-artistica
    obligatorio: true
    agentes: "1"
  - rol: DIS/investigacion-visual
    obligatorio: true
    agentes: "1 o 2 repartidos por territorio"
  - rol: DIS/investigacion-ux
    obligatorio: true
    agentes: "1"
  - rol: DIS/diseno-visual
    obligatorio: true
    agentes: "2 o 3, uno por dirección explorada"
  - rol: DIS/diseno-interaccion
    obligatorio: true
    agentes: "1"
  - rol: DIS/sistema-de-diseno
    obligatorio: true
    agentes: "1"
  - rol: DIS/movimiento
    obligatorio: true
    agentes: "1"
  - rol: DIS/prototipado
    obligatorio: true
    agentes: "1"
  - rol: DIS/critica-visual
    obligatorio: true
    agentes: "1, distinto de todos los productores"
  - rol: DIS/validacion-de-uso
    obligatorio: true
    agentes: "1"
  - rol: DIS/revision-de-fidelidad
    obligatorio: false
    agentes: "1"
    condicion: "la fundación llega a construirse dentro del mismo item"
combinables:
  - roles: [DIS/movimiento, DIS/prototipado]
    motivo: "el prototipo es el medio natural de especificar y medir el movimiento"
  - roles: [DIS/diseno-interaccion, DIS/investigacion-ux]
    motivo: "en la fundación, establecer las tareas y decidir su flujo son el mismo trabajo"
independientes:
  - rol: DIS/critica-visual
    de: [DIS/direccion-artistica, DIS/diseno-visual, DIS/diseno-interaccion, DIS/sistema-de-diseno, DIS/movimiento, DIS/prototipado, DIS/investigacion-visual, DIS/investigacion-ux]
    motivo: "es el único juicio del sistema sobre si la dirección fundada es genérica"
  - rol: DIS/sistema-de-diseno
    de: [DIS/direccion-artistica]
    motivo: "formalizar y decidir a la vez produce un sistema que describe en vez de gobernar"
  - rol: DIS/validacion-de-uso
    de: [DIS/diseno-interaccion, DIS/prototipado]
    motivo: "quien diseñó el flujo lo recorre sin dudar: validaría su memoria, no la interfaz"
ampliacion: >
  Un agente de DIS/diseno-visual por cada dirección explorada, con DIS/direccion-artistica
  como integrador declarado. Es el caso de varios agentes con el mismo rol previsto por C4.
reduccion: >
  Ninguna. Es la única composición del kernel donde NINGÚN rol obligatorio se retira: es la
  decisión que gobierna todas las siguientes, y abaratarla se paga en cada superficie
  posterior del producto.
retirada: >
  Cada rol se retira al entregar su artefacto. El equipo se desmaterializa cuando la
  dirección está aprobada y el sistema inicial validado en dos superficies.
```

## Los tres roles de adaptación, y por qué no son composiciones

```text
web-app · mobile-app · wear-os NO tienen composición propia en el kernel.

Cada pack aporta uno o varios ROLES ESPECIALIZADOS con prefijo —por ejemplo
`wear:DIS/lectura-de-un-vistazo`— que se AÑADEN a la composición que el algoritmo eligió.

REGLA:  un rol de pack NO sustituye a un rol del kernel, y NO puede quedarse con la
        autoridad de uno. Añade materia; no redistribuye poder.

Cuando el proyecto instala varios packs, los roles especializados de cada uno se añaden
todos, y la precedencia entre ellos la fija packs/COMPOSICION.md.
```
