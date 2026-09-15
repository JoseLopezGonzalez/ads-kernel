# CONTRATO · LA OFICINA — trabajadores, entregas, niveles y supervisor

**Qué es.** El contrato derivado de la primera adopción real. Fija cómo un paquete se
ejecuta FUERA del proceso del runtime —por un trabajador que toma, late y entrega, o por
un agente sin chat que un supervisor lanza—, cómo una entrega se hace verificable, cómo un
item alcanza cada NIVEL DE TERMINACIÓN, y qué condiciones legítimas de parada tiene el
bucle que sustituye al chat. Su norma es la que ya existía —`§7` de `11-ARQ`, `C4`, `C5`,
`b.10`, `b.12`, `b.15`— y lo que aquí se añade es el CABLEADO que la adopción demostró
ausente: sin él, el kernel traía una oficina y la instancia la tenía apagada.

**Qué NO es.** No es un segundo sistema de estado: cada acto es una `Transicion` sobre el
`Almacen`, y la máquina de paquetes, leases, acuses y reintentos es la de
[`CONTRATO-RUNTIME-Y-DISPATCHER.md`](CONTRATO-RUNTIME-Y-DISPATCHER.md), sin una segunda.
No es norma sobre qué niveles exige cada trabajo: eso lo declara el PROYECTO en su
`PROFILE.md` (`ads:circuito-base`), y aquí sólo se hace cumplir.

---

## 1 · Lo que la oficina escribe, y dónde

```text
canonico/entregas/<paquete>-<intento>.json   la ENTREGA de un trabajador, validada
canonico/checkpoints/<paquete>.json          el checkpoint del trabajador, bajo lease
canonico/dictamenes/<id>.json                los dictámenes (ya existía; ahora por ROL)
canonico/handoffs/<id>.json                  las entregas entre paquetes (ya existía;
                                             ahora con `destino` y `entrega`)
canonico/planes/<id>.json                    planes por ROL, con corrección (`sustituye_a`)
```

**Vocabulario CERRADO añadido**, y ninguna otra palabra vale:

```text
VEREDICTO DE ENTREGA   entregado · devuelto · bloqueado · escalado
NIVEL DE TERMINACIÓN   implementado · revisado · integrado · verificado ·
                       validado-funcional · validado-visual · aceptado · cerrado
ESTADO DE UN NIVEL     alcanzado · pendiente · inaplicable · no-exigido · rechazado
PARADA DEL SUPERVISOR  sin-trabajo · todo-en-manos-ajenas · bloqueado · marcado ·
                       pasadas-agotadas · hay-trabajo
```

Y UNA transición nueva en la tabla del paquete: `ejecutando → bloqueado`, para el
trabajador que descubre a mitad que no puede seguir sin algo ajeno. No consume intento.

## 2 · El protocolo de trabajadores — tres actos durables

```text
TOMAR        `Runtime.tomar`: adquirir el lease (nunca roba) · abrir el intento · marcar
             `ejecutando`. Devuelve efecto y checkpoint. Un `ejecutando` sin lease —lo dejó
             un trabajador muerto cuyo lease fue reclamado y soltado— se toma igual y
             conserva su efecto
CHECKPOINT   `Runtime.checkpoint`: `checkpoints/<paquete>.json` y LATIDO en la MISMA
             transición. Sin titularidad no hay checkpoint
ENTREGAR     `Runtime.entregar`: el resultado del §4.4 —el efecto lo pone el runtime—
             publicado por `_publicar_resultado` y cerrado por la política: resultado,
             acuse y latido en UNA transición
```

**El trabajador ES la instancia del runtime.** Dos sesiones que tomen el mismo paquete
compiten por el MISMO lease con la misma comparación e intercambio, y exactamente una lo
consigue. Un trabajador que muere deja un lease sin latido; el barrido de otra instancia lo
OBSERVA `PACIENCIA` veces y lo reclama por la única puerta que hay, y —porque el paquete es
EXTERNO— lo SUELTA en el acto para que el siguiente trabajador lo tome y reanude desde el
checkpoint. Se publica como `reofrecido`; nunca como atendido, porque nadie lo ejecutó.

**Un paquete EXTERNO se distingue por su orden**: `orden.adaptador == "worker"`. El
barrido no lo despacha ni lo cuenta como postergado. `tomables()` publica lo que un
trabajador puede tomar AHORA —sin dependencia pendiente y sin lease ajeno— y, aparte, lo
que espera y a qué.

**El latido es obligación del trabajador.** `PACIENCIA` barridos de un supervisor sin latido
es lo que hace reclamable un lease, y el brief lo dice: escribir checkpoint al terminar
cada paso es lo que separa a un trabajador vivo de uno muerto.

## 3 · La entrega — verificable, o no se escribe

Una entrega cumple [`esquemas/entrega.yaml`](../esquemas/entrega.yaml) y ADEMÁS:

```text
AUTOEVALUACIÓN     recorre EXACTAMENTE las comprobaciones del gate del rol: ni una menos
                   —una sin anotar es una no hecha— ni una de más —un gate no crece por
                   conveniencia—
CHECKLIST          contesta ENTERO el del contrato operativo del rol, cuando lo tiene
ARTEFACTOS         los obligatorios del contrato operativo están, por tipo
DEVUELTO           trae los CUATRO campos de C5; sin ellos no es una devolución
BLOQUEADO/ESCALADO trae qué lo impide, qué lo desbloquearía y la autoridad; escalar exige
                   además las posturas enfrentadas (a.7)
DICTÁMENES         un rol que juzga trae su dictamen, y el dictamen lo aplica
                   `gates.aplicar` con revisor ≠ autor POR ROL; la autoevaluación del
                   productor NUNCA es el dictamen
```

Una entrega que no cumple es `ENTREGA_INVALIDA` y **no toca el estado**: ni el paquete, ni
el lease, ni nada. Se escribe una por INTENTO, y el reintento conserva la anterior.

## 4 · Qué pasa después de entregar, por veredicto

```text
entregado   se publica `completado` · se registra la entrega · se emiten HANDOFFS a cada
            sucesor del plan —la instancia declarada del par si existe, o una genérica de
            C5 derivada de las fichas— con `destino` y `entrega` en su trazabilidad
devuelto    ANTES de cerrar el paquete: paquete de CORRECCIÓN para el rol emisor, NUEVO
            paquete receptor que espera a la corrección, y los sucesores del receptor se
            REAPUNTAN al nuevo. Después se cierra el que devuelve. El handoff acusado pasa
            a `devuelto` y CUENTA para el freno de a.7; a la tercera devolución del item se
            ESCALA con las dos posturas y NO se recompone (`FRENO_DISPARADO`)
bloqueado   se registra la entrega · checkpoint con el bloqueo · `ejecutando → bloqueado`
            SIN consumir intento · lease soltado · `cierres/` del item en `bloqueado` con
            el trabajo de reemplazo nombrado
escalado    igual, con la autoridad y las posturas, y el cierre del item en `escalado`
```

**Por qué la corrección va ANTES de cerrar el paquete que devuelve.** Un sucesor del
receptor —VER espera a la revisión de construcción— se volvería elegible en el instante en
que la revisión cerrara. Reapuntarlo mientras la revisión sigue `ejecutando` es lo que
impide que nadie tome un sucesor sobre una capa devuelta. Es una propiedad medida
(`T466`), no una intención.

**Rechazo al recibir** (antes de acusar) no cuenta para el freno: la custodia nunca cambió.
Produce la misma corrección y el mismo receptor nuevo; el receptor vigente se CANCELA con la
autoridad de la capacidad receptora, porque su entrada fue rechazada.

## 5 · Paquetes POR ROL, y el orden que los encadena

`Planificador.planificar(roles_por_capacidad=…)` crea UN paquete por (participante, rol).
Dentro de una capacidad, un rol cuyo contrato exige independencia de otro de la misma
composición ESPERA a ese otro: `CNS/revision-de-construccion` espera a
`CNS/implementacion` porque su contrato lo dice, y ninguna composición lo puede evitar. La
vía 1 de la propietaria global sin obligación propia produce UN paquete de INTEGRACIÓN
SEMÁNTICA que espera a todos los demás (`b.10`: la integración la declara el propietario
global, y sólo él).

El orden entre capacidades es el de las OBLIGACIONES del proceso (`b.16`, en el orden
escrito) y, para las condicionales, el de las estaciones que los circuitos dibujan
(`planificacion.ORDEN_DE_ESTACIONES`, declarado como dato con su fuente). Sin esto,
`rutas.componer` ordenaba por (vía, capacidad) —alfabético— y la construcción quedaba
antes que la definición de producto.

**El orden entre estaciones lo manda la estación, y entre obligatorias el proceso.** Un
participante condicional —`DIS` por `C-DIS`— va donde su estación dice, no detrás de todas
las obligatorias; y un rol que exige independencia de otro —del circuito base o del corpus,
dentro de su capacidad— va DESPUÉS de ese otro. **Replanificar es una generación nueva**:
los paquetes anteriores se conservan, y un paquete que ya existe con otras dependencias
nunca se reutiliza en silencio (`T463`).

**G13 en la puerta.** Quien produjo la entrega que un paquete va a juzgar no puede tomar ese
paquete: se rechaza ANTES del lease, y no queda lease detrás (`T465`).

## 6 · Los niveles de terminación y el circuito base

La escalera vive en [`../recorrido/02-NIVELES-DE-TERMINACION.md`](../recorrido/02-NIVELES-DE-TERMINACION.md).
Cada nivel es un DICTAMEN de su gate, y `terminacion.evaluar` exige dos independencias:
por ROL (`gates.aplicar`) y por TRABAJADOR (el titular que firma el dictamen no es el que
entregó lo juzgado; un dictamen así queda `rechazado` con su nombre).

El circuito base del proyecto —[`esquemas/circuito-base.yaml`](../esquemas/circuito-base.yaml),
bloques `ads:circuito-base` en `PROFILE.md`— fija por clase de trabajo los niveles
obligatorios, las composiciones, las condiciones de ruta, los roles mínimos y la ÚNICA
forma de saltarse un nivel: una condición de inaplicabilidad sobre HECHOS del item, en una
gramática cerrada (`<hecho> <op> [<valor>]`, unidas por ` y ` / ` o `). Un hecho ausente
hace falso el término, y se dice. `cerrar_item` evalúa la escalera y FALLA CERRADO si un
nivel exigido no está alcanzado ni es inaplicable, antes de aplicar `gate:cierre-de-item`.

## 7 · El agente sin chat, y el supervisor

`adaptadores/agente.py` lanza el ejecutor que el PROYECTO declara (`ads:ejecutor`, con
marcadores `{brief}` `{entrega}` `{espacio}` `{modelo}` `{paquete}` `{repo}`) sobre el
adaptador de proceso local —timeout que mata, recibo abierto y cerrado, `ambiguo`—, y sólo
devuelve `completado` si el agente dejó una entrega JSON legible; sin ella, `fallido`
reintentable. La entrega viaja ENTERA en `salida`, para que registrarla en `entregas/` sea
derivable e idempotente aunque el supervisor muera después del acuse.

`runtime/supervisor.py` da PASADAS: escribe los briefs de los paquetes de agente
elegibles, ejecuta `Runtime.ciclo()`, y cierra la oficina de lo completado
(`registrar_entrega_de_agente`). Termina sólo por una parada legítima, y `bucle()` exige un
tope de pasadas: un bucle sin tope no se construye. Paralelismo real = N supervisores con N
instancias; el árbitro es el estado durable y no hay otro.

**Ventana declarada.** Entre el `completado` del dispatcher y `registrar_entrega_de_agente`
un sucesor ya es elegible; con varios supervisores otro podría despacharlo antes de que una
devolución lo reapunte. Cerrarla exige registrar la entrega en la MISMA transición que el
acuse, y es de otro corte. Con un supervisor por control repo no tiene testigo.

## 8 · El tablero

`tablero.derivar` responde, del estado y de nada más: items y su ruta con el estado de cada
paso, paquetes por estado, tomables, en ejecución con titular y latido, esperando y POR
QUÉ, equipos con cola y trabajadores, handoffs pendientes de acuse, devoluciones, rechazos,
escalados, bloqueos, reconciliaciones abiertas, y **qué hará el sistema si nadie dice
nada**. No se persiste.

## 9 · Qué demuestra, y dónde

```text
T460–T475   pruebas/test_oficina.py         tomar/checkpoint/entregar y reintento entre dos
                                            trabajadores · muerte con lease y reoferta ·
                                            carrera de dos procesos · paquetes por rol ·
                                            entregas inválidas · autocertificación ·
                                            devolución, corrección y freno · bloqueo sin
                                            intento · niveles y cierre · tablero · agente sin
                                            chat con ejecutor · dependencia circular ·
                                            handoff incompleto · Owner ausente · reinicio ·
                                            documentos inconsistentes
```

El bloque entero sobre encargos REALES —dos items en paralelo, uno bloqueado, devolución,
corrección, gates, aceptación, cierre, muerte y reinicio— no lo mide el kernel: lo mide cada
instancia con su dogfood, sobre su producto, y publica su evidencia. Un escenario de
laboratorio que lo imitara diría lo mismo que `T460`–`T475` con otras palabras.

Órdenes: `ads_ciclo.py tomar · soltar · checkpoint · entregar · acusar · brief · tablero ·
terminacion · aceptar · cerrar-item · supervisar`.

## 10 · Lo que este contrato NO cubre

```text
NO CUBRE   el contenido de ninguna entrega: qué es un buen dosier o un buen diff lo dicen
           el rol, su contrato operativo y su método. Aquí sólo se exige la FORMA y la
           independencia
NO CUBRE   la ventana del §7 con varios supervisores
NO CUBRE   qué ejecutable lanza un agente ni con qué modelo: es del PROFILE
NO CUBRE   qué clases de trabajo existen ni qué niveles exige cada una: es del PROFILE
```

**Y nada de esto está CERTIFICADO.** Implementado y probado no es certificado.
