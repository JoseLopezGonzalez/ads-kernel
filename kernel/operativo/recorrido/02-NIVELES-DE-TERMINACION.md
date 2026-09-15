# Los niveles de terminación, y los dos gates que los cierran

> **Catálogo.** Este documento declara DOS bloques `ads:gate` —`gate:revision-de-construccion`
> y `gate:aceptacion-del-owner`— porque es la sede de la escalera de terminación, y los dos
> gates que faltaban para que la escalera fuera completa viven donde se define la escalera.

**Terminar la ejecución no es producir el resultado** —[`00-OBLIGACIONES-Y-CIERRE.md`](00-OBLIGACIONES-Y-CIERRE.md)—,
y **publicar una rama no es haber terminado**. La primera adopción real lo midió: treinta y
seis items «cerrados» cuya evidencia típica era «PR #14 … SIN FUSIONAR», con un solo estado
que colapsaba ocho hechos distintos. La escalera los separa, y cada escalón es un DICTAMEN
de un gate emitido por un revisor que no es el autor:

```text
NIVEL                 GATE                               QUIÉN LO ALCANZA
implementado          gate:implementacion-completa       lo juzga quien revisa; el productor
                                                         sólo se AUTOEVALÚA en su entrega
revisado              gate:revision-de-construccion      CNS/revision-de-construccion, que no
                                                         comparte agente con quien construyó
integrado             gate:convergencia-de-fuentes       ENT/convergencia, con el Integration Set ENTERO en su entrega
                                                         exactas
verificado            gate:evidencia-suficiente          VER/dosier
validado-funcional    gate:uso-comprobado                USO/validacion
validado-visual       gate:excelencia-visual             DIS/revision-de-fidelidad, en la
                                                         pasada de FIDELIDAD
aceptado              gate:aceptacion-del-owner          el OWNER, y nadie en su nombre
cerrado               gate:cierre-de-item                DSP verifica; no declara
```

**Qué niveles son obligatorios lo dice el CIRCUITO BASE del proyecto**, declarado en su
`PROFILE.md` con bloques `ads:circuito-base` (esquema
[`esquemas/circuito-base.yaml`](../esquemas/circuito-base.yaml)). Un nivel obligatorio se
alcanza con su dictamen o se declara **inaplicable por una condición sobre hechos del
item** escrita en el circuito. No hay tercera vía: «no hace falta» no es una condición, y
un agente no puede reducir el circuito por prisa, por contexto ni por tokens.

**La independencia se exige dos veces.** `gates.aplicar` exige revisor ≠ autor por
CAPACIDAD; `terminacion.evaluar` exige además que el TRABAJADOR que firma el dictamen no sea
el que entregó lo juzgado. Un dictamen del mismo trabajador se publica como `rechazado`, con
su nombre, y el nivel no se alcanza.

Mecanismo: [`runtime/ciclo/terminacion.py`](../runtime/ciclo/terminacion.py) ·
[`runtime/ciclo/oficina.py`](../runtime/ciclo/oficina.py) · contrato
[`runtime/CONTRATO-OFICINA.md`](../runtime/CONTRATO-OFICINA.md).

## `gate:revision-de-construccion`

La revisión del equipo de construcción **antes** de verificar. No sustituye al dosier de
`VER`: mira el DIFF, no el comportamiento. Lo que `VER` no puede ver —una decisión de
diseño interno mal tomada, una convención rota, una prueba que no muerde— lo ve esto.

```yaml ads:gate
id: gate:revision-de-construccion
aplica_a: "la capa de CNS/implementacion antes de pasar a VER; la emite CNS/revision-de-construccion"
comprobaciones:
  - id: diff-entero-leido
    comprueba: "el revisor ha recorrido el diff completo del commit entregado, no sólo los ficheros que el encargo nombraba"
    como: "lista de ficheros tocados con veredicto por fichero"
    automatizable: parcial
  - id: alcance-respetado
    comprueba: "el diff no toca nada fuera del alcance del paquete, o lo que toca de más está declarado en diferencias_declaradas"
    como: "cruce de los ficheros tocados contra el alcance declarado y las diferencias"
    automatizable: parcial
  - id: pruebas-muerden
    comprueba: "cada prueba nueva falla si se revierte el cambio que dice proteger"
    como: "revertir el cambio en una copia y ejecutar la prueba: tiene que ponerse roja"
    automatizable: si
  - id: convenciones-de-la-fuente
    comprueba: "el código sigue las convenciones vigentes de la fuente tocada, o declara la excepción"
    como: "comprobación automática de la fuente más lectura del revisor"
    automatizable: parcial
  - id: sin-redecidir
    comprueba: "no se ha cambiado ninguna decisión de una capa anterior sin devolverla"
    como: "comparación de lo construido contra las capas de PRD, DIS y ARQ"
    automatizable: parcial
  - id: independencia
    comprueba: "el revisor no es el trabajador que construyó la capa"
    como: "comparación de titulares en las entregas del paquete construido y del revisor"
    automatizable: si
  - id: hallazgos-con-linea
    comprueba: "todo hallazgo cita fichero y línea, dice si bloquea y propone el arreglo exacto"
    como: "lectura de la lista de hallazgos"
    automatizable: parcial
evidencia:
  - "la lista de ficheros tocados con su veredicto"
  - "la salida de las pruebas ejecutadas por el revisor"
  - "los hallazgos con fichero, línea y si bloquean"
fallo: >
  La capa no pasa a VER: vuelve a CNS/implementacion con los hallazgos bloqueantes como
  devolución de C5, y la corrección entra como paquete nuevo que espera la revisión de
  nuevo. Un hallazgo no bloqueante se registra y no detiene.
```

## `gate:aceptacion-del-owner`

El único gate cuyo revisor es el Owner. Se aplica sobre lo que el circuito base del
proyecto declara que exige aceptación humana, y se aplica con el estado preparado (G36):
se le convoca por lotes, con una tarea concreta, no con una pregunta abierta.

```yaml ads:gate
id: gate:aceptacion-del-owner
aplica_a: "todo item cuyo circuito base declara `aceptado` como nivel obligatorio"
comprobaciones:
  - id: lo-que-pidio
    comprueba: "el Owner reconoce en lo entregado lo que pidió, contra su expresión literal conservada"
    como: "el Owner recorre la definición de terminado del item, punto por punto"
    automatizable: no
  - id: en-el-entorno-declarado
    comprueba: "lo ha visto funcionar en el entorno que el PROFILE declara como objetivo, no en una captura"
    como: "el Owner declara dónde lo vio y con qué datos"
    automatizable: no
  - id: preparado-por-lotes
    comprueba: "se le convocó con el estado preparado y en lote, no item por item"
    como: "enlace a la cola de validación y a la preparación"
    automatizable: si
  - id: deuda-conocida
    comprueba: "toda deuda aceptada en las entregas del item está delante del Owner al aceptar"
    como: "la lista de deuda_aceptada de las entregas figura en la entrada del dictamen"
    automatizable: si
evidencia:
  - "la declaración del Owner, con fecha, sobre qué vio y dónde"
  - "la deuda aceptada que tuvo delante"
fallo: >
  El item NO está aceptado y no cierra como producto. Lo que el Owner señale vuelve como
  devolución a la capacidad propietaria de la capa que falla; si señala que pidió otra cosa,
  es `b.1`: cambio de proceso o item nuevo, y lo decide él.
```
