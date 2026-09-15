# T460–T477 — la oficina: trabajadores, entregas, niveles, supervisor y contratos de rol

**Qué cierran.** El hallazgo de la auditoría forense de La Pesquerapp del 2026-09-14: el
kernel tenía escrito el runtime completo —paquetes, leases, dispatcher, ciclo, gates,
handoffs, freno de `a.7`— y **la instancia nunca lo invocaba**. Setenta y ocho items, cero
paquetes, cero leases, cero equipos. El trabajo ocurría en un chat, el estado se anotaba
después, y «cerrado» significaba «alguien lo escribió». Ningún mecanismo lo impedía porque
ningún mecanismo estaba conectado.

El contrato que estas pruebas instancian es
[`../runtime/CONTRATO-OFICINA.md`](../runtime/CONTRATO-OFICINA.md). Lo que añade al runtime
se mide aquí, y **todo se mide ejecutando**: control repos reales, trabajadores que son
procesos reales cuando la propiedad exige un proceso —una muerte con lease, una carrera por
el mismo paquete—, y un agente sin chat que es un ejecutable lanzado por el adaptador de
agente con su brief y su fichero de entrega.

**Lo que NO afirman.** Ninguna prueba certifica nada. Su estado es `validador-implementado`
hasta que la CI del kernel publique su evidencia en un release: en local corren en verde,
pero una evidencia registrada en una máquina con omisiones no es evidencia de release. Que la oficina se sostenga sobre encargos reales de un producto real lo
mide la instancia, con su propio dogfood, y no este fichero.

```text
T460  tomar · checkpoint · entregar · reintento entre dos trabajadores
T461  muerte con lease: reoferta tras PACIENCIA y reanudación desde el checkpoint
T462  dos procesos compiten por el mismo paquete y exactamente uno lo toma
T463  planificación por rol: un paquete por rol, orden por obligación, brief derivado
T464  una entrega incompleta se rechaza y no toca el estado
T465  la autocertificación se rechaza, por trabajador y por rol
T466  devolución → corrección → nuevo receptor; rechazo al recibir; freno a la tercera
T467  un bloqueo no consume intento y deja nombrado quién lo desbloquea
T468  el item no cierra como producto hasta alcanzar los niveles del circuito base
T469  el tablero es determinista y dice qué hará el sistema si nadie dice nada
T470  un agente sin chat ejecuta un paquete con su brief; sin entrega válida no completa
T471  una dependencia circular no se toma y el tablero la nombra
T472  un handoff incompleto no se emite; un acuse a medias no toma custodia
T473  con el Owner ausente el trabajo independiente continúa
T474  un reinicio completo reconstruye exactamente lo mismo
T475  los documentos inconsistentes se rechazan con su nombre
T476  todo rol materializable tiene contrato operativo efectivo y suficiente
T477  las bases de contrato son coherentes y ningún rol hereda de dos
```

---

```yaml ads:escenario
id: T460
nombre: Tomar, checkpoint, entregar y reintento entre dos trabajadores
cubre: ["CONTRATO-OFICINA §2", "worker protocol", "lease", "checkpoint"]
dado:
  - "un paquete externo (orden.adaptador = worker) listo y sin dependencias"
  - "dos instancias del runtime, w-A y w-B, sobre el mismo control repo"
cuando:
  - "w-A toma el paquete, deja un checkpoint y entrega un resultado fallido reintentable"
  - "w-B toma el mismo paquete después"
entonces:
  - "mientras w-A tiene el lease, w-B recibe AUTORIDAD_NO_DISPONIBLE"
  - "tras el fallo el paquete vuelve a listo y w-B lo toma como intento 2 con el checkpoint de w-A delante"
  - "un paquete que no es externo no se toma, y una entrega mal formada no mueve la revisión del estado"
falla_si:
  - "dos instancias sostienen el lease del mismo paquete a la vez"
  - "el checkpoint del intento anterior no llega al siguiente titular"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T461
nombre: Un trabajador que muere con el lease es reofrecido tras PACIENCIA
cubre: ["CONTRATO-OFICINA §2", "lease", "PACIENCIA", "checkpoint", "a.10"]
dado:
  - "un item planificado por la oficina y su primer paquete tomable"
  - "un PROCESO real que lo toma por la CLI, deja checkpoint y termina sin entregar ni soltar"
cuando:
  - "un supervisor da pasadas sobre el estado"
entonces:
  - "el paquete se reofrece exactamente en la pasada PACIENCIA, ni antes ni por vía rápida"
  - "el lease muerto desaparece y el paquete sigue en ejecutando"
  - "otro trabajador lo toma en el MISMO intento y recibe el checkpoint del muerto con su titular"
falla_si:
  - "el paquete se reofrece antes de PACIENCIA observaciones sin latido"
  - "la reoferta consume un intento o pierde el checkpoint"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T462
nombre: Dos procesos compiten por el mismo paquete y exactamente uno lo toma
cubre: ["CONTRATO-OFICINA §2", "lease", "CAS", "doble despacho"]
dado:
  - "un paquete tomable y dos procesos de la CLI lanzados a la vez con instancias distintas"
cuando:
  - "los dos ejecutan tomar sobre el mismo paquete"
entonces:
  - "uno sale con 0 y el otro con 1 y AUTORIDAD_NO_DISPONIBLE"
  - "el paquete tiene un solo intento y el lease nombra al ganador"
  - "un paquete que no está en ningún plan no se toma por la oficina y no deja lease detrás"
falla_si:
  - "ambos procesos salen con 0"
  - "una toma rechazada por la oficina deja el lease puesto"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T463
nombre: Planificación por rol, orden por obligación y brief derivado
cubre: ["CONTRATO-OFICINA §5", "C4", "b.16", "ORDEN_DE_ESTACIONES", "brief"]
dado:
  - "un control repo con catálogo de modelos y un circuito base de clase cambio-de-backend"
  - "una entrada del Owner de clase item con resultado perseguido y evidencia de cierre"
cuando:
  - "la oficina planifica el item"
entonces:
  - "hay un paquete por rol: PRD antes que CNS, la revisión depende de la implementación y VER de la revisión"
  - "la propietaria global cierra con una unidad de integración semántica que depende de todas las demás"
  - "todos los paquetes son externos: el barrido del dispatcher no los despacha ni los posterga"
  - "sin catálogo en el PROFILE no se planifica: RolSinAgente, no un agente por defecto"
  - "el brief del paquete se deriva del estado, lleva rol, contrato, método, gate, forma de entrega y prohibiciones, y su huella es estable"
falla_si:
  - "el orden de los paquetes sale del alfabeto y no de la obligación del proceso"
  - "un rol sin agente declarado se planifica igual"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T464
nombre: Una entrega incompleta se rechaza y no toca el estado
cubre: ["CONTRATO-OFICINA §3", "esquema entrega", "artefactos obligatorios", "checklist"]
dado:
  - "un paquete de CNS/implementacion tomado, con su contrato operativo"
cuando:
  - "se intenta entregar con el gate incompleto, sin un artefacto obligatorio, sin checklist, con una devolución sin los cuatro campos, con rol equivocado, con campo desconocido o con el gate de otro rol"
entonces:
  - "cada caso falla con EntregaInvalida y la revisión del estado no cambia"
  - "el paquete sigue en ejecutando con su lease"
falla_si:
  - "alguna de las siete mutaciones se registra como entrega"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T465
nombre: La autocertificación se rechaza, por trabajador y por rol
cubre: ["CONTRATO-OFICINA §3", "G13", "independencia", "dictamen"]
dado:
  - "w-A entregó la implementación y w-A toma la revisión"
cuando:
  - "w-A intenta emitir el dictamen sobre la implementación, o sobre su propio paquete"
entonces:
  - "AutocertificacionRechazada en los dos casos"
  - "w-B, otra instancia, emite los dos dictámenes y los niveles implementado y revisado quedan alcanzados"
  - "un dictamen cuyo revisor titular coincide con el autor titular se publica como rechazado en la escalera"
falla_si:
  - "el mismo titular firma la construcción y su revisión"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T466
nombre: Devolución con corrección y nuevo receptor; rechazo al recibir; freno a la tercera
cubre: ["CONTRATO-OFICINA §4", "C5", "a.7", "sustituye_a", "cuenta_para_el_freno"]
dado:
  - "implementación entregada y revisión tomada por otra instancia"
cuando:
  - "la revisión devuelve con los cuatro campos, dos veces, y una tercera"
  - "en otro caso, la revisión rechaza el handoff al recibir sin tomar custodia"
entonces:
  - "cada devolución abre un paquete de corrección y un nuevo receptor, y VER pasa a depender del nuevo receptor ANTES de que la revisión cierre"
  - "a la tercera devolución se escala al Owner con las dos posturas y FrenoDisparado"
  - "un rechazo al recibir no cuenta para el freno, cancela el receptor y abre la corrección"
falla_si:
  - "la capa devuelta sigue adelante hacia VER"
  - "las devoluciones se recomponen sin tope"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T467
nombre: Un bloqueo no consume intento y deja nombrado quién lo desbloquea
cubre: ["CONTRATO-OFICINA §4", "bloqueado", "ejecutando→bloqueado", "g.9"]
dado:
  - "un paquete de implementación tomado"
cuando:
  - "el trabajador entrega veredicto bloqueado con qué lo impide, qué lo desbloquearía y la autoridad"
entonces:
  - "el paquete pasa a bloqueado con un solo intento y sin lease, y no hay reconciliación pendiente"
  - "el cierre del item registra la salida bloqueado con el trabajo de reemplazo"
  - "el tablero lo publica en esperando con su motivo, y la autoridad lo reanuda y se retoma con el checkpoint del bloqueo"
falla_si:
  - "el bloqueo acaba en agotado o en una reconciliación de g.9"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T468
nombre: El item no cierra como producto hasta alcanzar los niveles del circuito base
cubre: ["CONTRATO-OFICINA §6", "02-NIVELES-DE-TERMINACION", "circuito-base", "gate:aceptacion-del-owner"]
dado:
  - "implementación y revisión entregadas por instancias distintas"
cuando:
  - "se intenta cerrar el item sin verificación ni aceptación, después sin aceptación, y por fin con el dictamen del Owner"
entonces:
  - "CircuitoBaseIncumplido nombra los niveles que faltan, y sólo con todos alcanzados el cierre es completado"
  - "el gate de aceptación lo firma OWNER y nadie más"
  - "sin el hecho afecta_superficie=false, validado-visual no es inaplicable y el cierre se niega"
falla_si:
  - "un item cierra como producto con un nivel obligatorio pendiente"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T469
nombre: El tablero es determinista y dice qué hará el sistema si nadie dice nada
cubre: ["CONTRATO-OFICINA §8", "tablero", "derivado del estado"]
dado:
  - "un item planificado"
cuando:
  - "se deriva el tablero dos veces en proceso y una por la CLI"
entonces:
  - "las tres derivaciones coinciden byte a byte en lo que publican"
  - "publica tomables, esperando con su motivo, equipos, handoffs pendientes y la frase de qué hará el sistema si nadie dice nada"
  - "no publica rutas absolutas"
falla_si:
  - "dos derivaciones del mismo estado difieren"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T470
nombre: Un agente sin chat ejecuta un paquete con su brief; sin entrega válida no completa
cubre: ["CONTRATO-OFICINA §7", "adaptador de agente", "ads:ejecutor", "supervisor"]
dado:
  - "un PROFILE con bloques ads:ejecutor cuyo argv es un ejecutable real que lee el brief y escribe la entrega"
  - "un plan cuyo paquete de implementación tiene orden de adaptador agente"
cuando:
  - "el supervisor da pasadas con el adaptador de agente"
entonces:
  - "el brief se escribe antes de despachar, el agente entrega, la entrega se registra en el estado y el handoff a la revisión queda emitido"
  - "repetir la pasada no vuelve a ejecutar ni a registrar"
  - "un ejecutor que sale con 0 y no deja entrega produce fallido reintentable; un modelo sin ejecutor, fallido no reintentable; un PROFILE sin ejecutores no construye el adaptador"
falla_si:
  - "un completado durable se apoya en una entrega que no existe"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T471
nombre: Una dependencia circular no se toma y el tablero la nombra
cubre: ["CONTRATO-OFICINA §8", "dependencias_circulares", "supervisor parada bloqueado"]
dado:
  - "dos paquetes externos que dependen uno del otro"
cuando:
  - "se piden los tomables, se deriva el tablero y el supervisor da pasadas"
entonces:
  - "no hay tomables, el tablero publica los dos en dependencias_circulares y lo dice en la frase de qué hará"
  - "el supervisor para con bloqueado, no con un bucle"
falla_si:
  - "la espera circular queda en silencio"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T472
nombre: Un handoff incompleto no se emite y un acuse a medias no toma custodia
cubre: ["C5", "handoff", "acuse", "handoff genérico"]
dado:
  - "la declaración handoff:con-a-ver del corpus"
cuando:
  - "se emite sin artefactos, o sin ruta en la trazabilidad; se acusa con una comprobación de menos, o desde la capacidad equivocada"
entonces:
  - "HandoffIncompleto en las dos emisiones, HandoffRechazado en los dos acuses"
  - "entre dos capacidades sin handoff declarado existe el genérico, con comprobaciones al recibir"
falla_si:
  - "un handoff sin artefactos se emite"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T473
nombre: Con el Owner ausente el trabajo independiente continúa
cubre: ["CONTRATO-OFICINA §7", "escalado", "trabajo independiente"]
dado:
  - "dos items planificados; la implementación del primero escala al Owner con dos posturas"
cuando:
  - "se piden los tomables y el tablero"
entonces:
  - "el primer item aparece en escalados y todos los tomables pertenecen al segundo"
  - "la frase de qué hará dice tomar y trabajar, no esperar al Owner"
falla_si:
  - "una decisión pendiente para la oficina entera"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T474
nombre: Un reinicio completo reconstruye exactamente lo mismo
cubre: ["CONTRATO-OFICINA §8", "reanudación", "b.14", "brief huella"]
dado:
  - "un paquete tomado con checkpoint, y el runtime cerrado"
cuando:
  - "OTRO proceso abre el control repo desde cero por la CLI con la misma instancia"
entonces:
  - "el tablero coincide clave a clave con el derivado antes de cerrar"
  - "el brief del paquete tiene la misma huella y trae el checkpoint"
  - "el trabajador que vuelve con su instancia sigue siendo el titular, en el mismo intento"
falla_si:
  - "algo del estado de la oficina sólo se reconstruye desde la conversación"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T475
nombre: Los documentos inconsistentes se rechazan con su nombre
cubre: ["esquema circuito-base", "esquema entrega", "fallo cerrado"]
dado:
  - "un circuito base sin los niveles mínimos, con una condición de inaplicabilidad vaga, o con un rol que no existe; un control repo sin PROFILE"
  - "una entrega que dice entregado con un dictamen no-superado, o un dictamen que dice superado con comprobaciones de menos"
cuando:
  - "se cargan los circuitos y se intenta la entrega"
entonces:
  - "CircuitoBaseIlegible en los cuatro primeros casos y EntregaInvalida en los dos últimos, con el paquete en ejecutando"
falla_si:
  - "un documento que dice dos cosas se acepta por la primera"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T476
nombre: Todo rol materializable tiene contrato operativo efectivo y suficiente
cubre: ["contrato-base", "contrato-de-rol", "contrato-operativo", "ciclo/contratos.py", "G13"]
dado:
  - "los roles del corpus, sus composiciones, los procesos que nombran capacidades y las bases de contrato por familia"
cuando:
  - "se clasifica cada rol —materializable, consultivo, conceptual, huérfano, sin-base— y se fusiona base + derivación + especialización"
entonces:
  - "cada rol materializable o consultivo tiene un contrato efectivo que cumple el esquema contrato-operativo"
  - "sus métodos están entre los del rol, su gate está en no_autocertifica y su independencia está en incompatibilidades"
  - "los conceptuales se publican por su nombre; un huérfano o un sin-base es un fallo"
falla_si:
  - "un rol que un proceso materializa queda sin base y el validador sale en verde"
  - "un contrato efectivo insuficiente se entrega en un brief como si bastara"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_contratos.py
estado: prueba-superada
evidencia: evidencia/contratos-salida.txt
```

```yaml ads:escenario
id: T477
nombre: Las bases de contrato son coherentes y ningún rol hereda de dos
cubre: ["contrato-base", "contrato-de-rol"]
dado:
  - "las bases de contrato, las especializaciones y los contratos completos del corpus"
cuando:
  - "se cruzan los roles que cada base nombra, la base que cada especialización hereda y los contratos completos"
entonces:
  - "toda base nombra roles que existen, ningún rol está en dos bases, cada especialización hereda de la base de su rol, y ningún rol tiene contrato completo y especialización a la vez"
falla_si:
  - "un rol hereda de dos familias y el contrato efectivo depende del orden de lectura"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_contratos.py
estado: prueba-superada
evidencia: evidencia/contratos-salida.txt
```
