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

**Un trabajador posee UN paquete a la vez, y ninguno por adelantado.** No existe reserva
ni prefetch: lo único que un trabajador tiene es el lease del paquete que está ejecutando,
adquirido al tomar y devuelto al entregar o soltar. «Lo haré después» no es un estado del
runtime. Un paquete que nadie está ejecutando es tomable por cualquiera, y eso es lo que
hace fungibles a los trabajadores y posible la batería (`T460`, `T462`; OWN-ADS-0241 a 0243).

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
                   además las posturas enfrentadas (a.7) y la MATERIA: una de las que la
                   capacidad del rol declara que ESCALA en su ficha (`autoridad.escala`).
                   Una materia de `decide_sola` se rechaza: lo que el equipo resuelve no
                   se escala al Owner (Directiva del Owner §20, §41, §76; `T485`)
ACUSE PREVIO       lo que el paquete RECIBIÓ está acusado o rechazado ANTES de entregar; un
                   handoff recibido en `emitido` invalida la entrega. No existe «seguimos»
                   como transferencia implícita (Directiva §78; `T483`)
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

**Lo que viaja en cada handoff (los catorce campos de §78, `T484`).** Además de la
declaración de `C5` (once campos) y de la trazabilidad, todo handoff emitido lleva
`contenido`, DERIVADO al emitir de la entrega registrada, del plan y del item —el receptor
no reconstruye nada leyendo una conversación—, con esta correspondencia:

```text
origen                          capacidad, rol y paquete emisor
destino                         capacidad, rol y paquete receptor
paquete                         el paquete emisor
objetivo                        `objetivo` del item (vacío si el item no lo declara)
entrada_recibida                los handoffs que el emisor ACUSÓ
trabajo_realizado               la entrega registrada: id, veredicto, siguiente
entregables                     `artefactos` de la entrega
decisiones                      `decisiones_asumidas`
riesgos                         `riesgos`
evidencia                       `evidencias`
criterios_de_aceptacion         `comprueba_al_recibir` de la declaración + el gate autoevaluado
deuda                           `deuda_aceptada`
cuestiones_abiertas             `no_hecho` + `diferencias_declaradas`
que_puede_devolver_el_receptor  `rechaza_si` + `devolucion` de la declaración
```

Un contenido con un campo de menos no se emite (`HandoffIncompleto`).

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

**Participaciones dobles.** `DOM` y `SEG` participan dos veces en FEA, GAP y DEU: como
`DOM:condiciones` antes de construir y como `DOM:revision` después (`01-PROCESOS.md`). Cada
participación acuña sus propios paquetes por rol —la semilla entra el método cuando la
participación se repite, y sólo entonces, para que ningún plan ya escrito cambie de
identidad— y una dependencia por independencia (`DOM/migracion` de `DOM/modelo`) se resuelve
dentro de la misma participación: la migración previa espera al modelo previo, no al de la
revisión posterior (`T487`).

**Lo que el encargo declara y la oficina sólo transporta.** `proceso:DIR` deriva su
propietario global del encargo y `b.16` prohíbe que DSP lo elija: la entrada de `planificar`
lleva `propietario_global` (la capacidad propietaria de la decisión que se sustituye) y
`productores_declarados` (`{obligación: capacidad}` para las obligaciones con productora
DERIVADA, como `sustituciones-registradas`). Sin ellos la fase NO abre, con
`PROPIETARIO_NO_DERIVABLE` o `COMPOSICION_INCOMPLETA` (`T488`).

## 5 ter · La estación de análisis de impacto (Directiva §5, §32, §62)

La clase con la que se abrió un encargo fijó qué condiciones de ruta eran verdaderas; el
trabajo puede revelar otras. Cualquier rol declara en su entrega lo que vio con el
vocabulario CERRADO de `ciclo/impacto.py`:

```text
un cambio en backend puede introducir     nuevo-estado-visible · nueva-restriccion · nueva-accion ·
                                          nuevo-error · nuevo-permiso · nuevo-flujo · nueva-forma-de-presentar
un cambio de interfaz puede requerir      nuevo-dato · agregacion · endpoint · cambio-de-modelo ·
                                          nueva-semantica-de-dominio
un fix visual puede revelar               patron-roto · inconsistencia-entre-pantallas ·
                                          problema-de-accesibilidad · deuda-del-sistema-de-diseno
```

Cada disparador nombra la condición de ruta que dispara (`C-DIS`, `C-SEG`, `C-USO`, `C-DOM`,
`C-ARQ`). Si el circuito ya la declaró, no pasa nada: la entrega vale y el item sigue. Si NO
la declaró, la entrega vale igual —lo que un rol vio, cuenta— pero el plan queda MARCADO con
el rol, los disparadores, las condiciones sin cubrir y qué hacer; `tomar` rechaza cualquier
otro paquete del item (`IMPACTO_NO_CUBIERTO`) y `evaluar_terminacion` publica la marca. La
salida es replanificar el encargo con un circuito que cubra esas condiciones (`b.1`):
`planificar` con `generacion > 0` escribe el plan nuevo con `sustituye_a` y el vigente pasa a
ser el nuevo, sin marca. Un disparador fuera del vocabulario es `ENTREGA_INVALIDA`.

Así un `NO APLICA` deja de ser silencio (§32): la ruta registra qué capacidades no se
activaron y por qué condición, y la única manera de contradecirlo es un disparador
declarado, que el sistema atiende solo (`T489`–`T491`).

## 5 bis · El contrato operativo efectivo de cada rol

Un rol materializable —uno que la oficina puede convertir en paquete— tiene SIEMPRE
contrato operativo, y no hace falta escribirlo treinta veces. El contrato efectivo se
compone de tres capas (`ciclo/contratos.py`):

```text
BASE            ads:contrato-base, una por FAMILIA (productor · revisor · consultor ·
                investigador · operador · aprendizaje · orquestador): comprobaciones
                previas, apertura y cierre de la secuencia, prohibiciones, checklist,
                escalados, incompatibilidad de familia, gates que nunca se autocertifican
DERIVACIÓN      lo que los veintinueve campos del ROL ya dicen de forma estructurada:
                misión, entradas, decisiones propias, escalados, artefactos, devoluciones,
                prohibiciones, criterios, fuentes, incompatibilidades, métodos, gate
ESPECIALIZACIÓN ads:contrato-de-rol, corta y opcional: las listas se suman; misión,
                secuencia, artefactos y ejemplos sustituyen
```

La fusión se valida contra `esquemas/contrato-operativo.yaml`; un contrato escrito entero
como `ads:contrato-operativo` es la forma larga de lo mismo. El contrato dice, de forma
comprobable: qué entradas necesita (`entradas_obligatorias`), qué puede hacer
(`decisiones_propias`, `secuencia`), qué no (`actuaciones_prohibidas`), qué artefactos
produce (`artefactos`), qué evidencia adjunta (`evidencias_requeridas`), cuándo termina
(`condiciones_de_aceptacion`), a quién entrega (`entrega_a`: `segun-el-plan` es el
mecanismo real), qué provoca devolución (`condiciones_de_devolucion`), qué escala
(`reglas_de_escalado`), de quién es independiente (`incompatibilidades`), qué métodos usa
(`metodos`) y qué gates no puede autocertificar (`no_autocertifica`, que la entrega
comprueba). `comprobar_contratos` clasifica cada rol —materializable, consultivo,
conceptual, huérfano, sin-base— y FALLA si un rol materializable queda sin contrato
suficiente (`T476`, `T477`).

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

**El nivel `integrado` tiene rol, gate y comprobación mecánica.** `ENT/convergencia`
(composición `ent-convergencia`, condición de ruta `C-ENT`) declara el Integration Set
ENTERO dentro de su entrega y emite `gate:convergencia-de-fuentes` sobre la capa de
construcción; la oficina no admite ese dictamen sin un conjunto que valide contra
`integration-set`, nombre TODAS las fuentes que el item escribe (`hechos.fuentes_escritas`),
entre por SHA, no tenga ámbitos pendientes ni en fallo y no esté parcial. Es la frontera
entre «hay commits en ramas» (implementado, revisado) y «existe una combinación exacta
probada junta desde la que se puede volver» (integrado); `verificado` juzga comportamiento
sobre revisiones, `aceptado` es el Owner. Una clase que no escribe fuentes lo declara
inaplicable con `fuentes_escritas_cuenta == 0`, y sólo así.

**Las fronteras previas a la construcción (Directiva §77, `T486`).** Antes de
`implementado` un item pasa por estados que el sistema distingue y publica en
`evaluar_terminacion` como `fronteras`: `admitida` (tiene plan), `encuadrada` (el plan
tiene encuadre), `investigada` (un paquete `INV/*` entregó), `disenada` (`DIS/direccion-
artistica`, `DIS/diseno-visual` o `DIS/diseno-interaccion` entregó), `especificada`
(`DIS/sistema-de-diseno` o `DIS/prototipado` entregó), `aprobada` (la dirección aprobada
por el Owner: **sin mecanismo** hasta la línea de Diseño; se publica así, no se finge).
Una frontera es un hecho del plan —`alcanzado · pendiente · no-exigido · sin-mecanismo`—,
no un nivel con gate: no entra en `puede_cerrar`. «Cerrado» no es sinónimo de
«implementado», y «en curso» no es sinónimo de «diseñado».

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
T460–T477   pruebas/test_oficina.py         tomar/checkpoint/entregar y reintento entre dos
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
cronica · terminacion · aceptar · cerrar-item · supervisar`.

**Lo que los workers como PROCESOS enseñaron** (dogfood de certificación de La Pesquerapp,
2026-09-15), corregido y medido en esta misma batería: el barrido del supervisor sobrevive
a un trabajador que entrega entre la lectura de su lease y la observación (`T461`); un
lector que cae detrás de un escritor —revisión avanzada, o `replace` hecho y testigo aún
no escrito— espera y vuelve a mirar antes de declarar corrupción, y la corrupción real
sigue siendo fallo cerrado (`T474`); el brief lleva la `plantilla` de la entrega y la
forma exacta de cada elemento (`elementos`), porque un modelo real escribió prosa donde el
esquema exige un valor cerrado; y `no` sin comillas es False para el analizador YAML, así
que los valores cerrados se comparan como texto. `cronica` deriva la secuencia del diario:
quién tomó qué, qué entregó, qué handoff, qué dictamen, qué reoferta —una fila por
transacción CONFIRMADA, porque el diario guarda tres fases por transacción—.

**Y lo que enseñó una oficina entera escribiendo a la vez** (un supervisor y seis workers
como procesos, dogfoods 4 a 6 de la certificación): el `flock` del escritor no hace cola, y
80 sondeos de 50 ms no bastan cuando dos procesos reencadenan diez transacciones por entrega
—`INTENTOS_DE_BLOQUEO` son ahora 600, con la misma espera fija—; un lease que el titular
retira entre la lectura de `REVISION.json` y la del objeto no es corrupción sino
`RutaInvalida`, y `_atender_fallido` tolera al titular que suelta (`T474`); la puerta de G13
mira TODA entrega de la instancia para el item, no sólo los handoffs, porque quien corrigió
la implementación pasaba la puerta de VER/dosier (`T465`); y `oficina.entregar` exige
titularidad ANTES de escribir su primer paso, porque un supervisor puede reclamar el lease de
un worker vivo pero lento y la entrega son varias transacciones (`T461`). La regla de
explotación que sale de ahí: la espera del supervisor es al menos tres veces el latido del
worker, y el latido dura hasta que la entrega está escrita.

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
