# T460–T499 — la oficina: trabajadores, entregas, niveles, supervisor, contratos de rol, handoffs de §78, fronteras de §77, el catálogo de clases, la estación de impacto de §5, las paradas de §36, los artefactos de Diseño, la base de partida de §63, el Integration Set de §71, la exclusión por recurso de §68 y el sentido único de la independencia de §81

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
T483  entregar con un handoff recibido sin acusar se rechaza: no existe «seguimos» (§78)
T484  el handoff emitido lleva los catorce campos de §78, derivados de la entrega y del plan
T485  escalar exige una materia que la capacidad ESCALA; una que decide sola se rechaza (§20, §41, §76)
T486  las fronteras previas a la construcción se distinguen: investigada · diseñada · aprobada · especificada (§77)
T487  una capacidad que participa DOS veces (DOM:condiciones y DOM:revision) acuña paquetes distintos, y la dependencia se resuelve dentro de la misma participación
T488  un cambio de dirección (DIR) deriva su propietario global y las productoras derivadas del encargo; sin ellas la fase no abre
T489  un impacto declarado que el circuito cubre no marca nada y el item sigue (§5)
T490  un impacto que el circuito no cubre marca el plan, ningún otro paquete se toma, y replanificar con una generación nueva sustituye al plan marcado (§5, §62, b.1)
T491  un disparador fuera de los dieciséis de §5 es una entrega inválida
T492  una barrera externa y un riesgo extraordinario son paradas del supervisor con nombre (§36.3, §36.4); sin clase sigue siendo bloqueado; una clase inventada no entra
T493  los contratos de la línea de Diseño exigen los artefactos que la Directiva nombra por fase (§12–§26): informe de realidad, análisis de uso, síntesis, auditoría con sus cinco salidas, alternativas de diez campos, recomendación, prototipo mirable, crítica por trece criterios, síntesis de ocho secciones, sesión de uso y especificación construible
T494  al tomar nace la base (rama, commit, base por repo) en el checkpoint 0; un avance compatible de la base se registra y el trabajo sigue (§61, §63)
T495  un avance de la base que toca lo mismo es contradicción: se ve en el checkpoint, `entregado` es BASE_CONTRADICHA sin escribir nada, y tras reconciliar en la rama se entrega
T496  un control repo sin Git no se mide y nada cambia
T497  con varias fuentes el Integration Set define orden de merge, compatibilidad, despliegue y dependencias; sin ellos, o con una fuente de menos o ajena, la convergencia no es admisible (§71)
T498  un recurso exclusivo —derivado del acoplamiento de a.5— en manos de otra ejecución hace al paquete temporalmente incompatible: no elegible, no tomable, publicado con quién lo posee; el de ámbito independiente sigue en paralelo (§68)
T499  la independencia de un rol se declara en UN solo sentido —la exige quien REVISA de quien PRODUCE—: declararla también en el productor la convierte en un ciclo que no ordena y empuja a los dos al final del plan, detrás de la construcción (§81)
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

```yaml ads:escenario
id: T483
nombre: Entregar con un handoff recibido sin acusar se rechaza
cubre: ["CONTRATO-OFICINA §3", "acuse", "Directiva del Owner §78", "OWN-ADS-0280"]
dado:
  - "un paquete de CNS/implementacion tomado con dos handoffs de PRD en `emitido`"
cuando:
  - "el trabajador entrega sin haber acusado ni rechazado lo recibido"
entonces:
  - "ENTREGA_INVALIDA que nombra los handoffs sin acusar; el paquete sigue `ejecutando` y nada se escribe"
  - "acusados los dos, la misma entrega se admite"
falla_si:
  - "una entrega con un handoff recibido en `emitido` toca el estado"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T484
nombre: El handoff emitido lleva los catorce campos de §78
cubre: ["CONTRATO-OFICINA §4", "handoff", "Directiva del Owner §78", "OWN-ADS-0278"]
dado:
  - "una entrega de CNS/implementacion con riesgos, decisiones asumidas y algo no hecho"
cuando:
  - "se entrega y se emiten los handoffs a los sucesores"
entonces:
  - "cada handoff trae `contenido` con exactamente los catorce campos: origen, destino, paquete, objetivo, entrada recibida, trabajo realizado, entregables, decisiones, riesgos, evidencia, criterios de aceptación, deuda, cuestiones abiertas y qué puede devolver el receptor"
  - "entrada recibida son los handoffs que este paquete acusó; riesgos, decisiones y no hecho son los de la entrega"
  - "un contenido a medias no se emite (HandoffIncompleto)"
falla_si:
  - "un handoff se emite sin alguno de los catorce campos"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T485
nombre: Escalar exige una materia que la capacidad ESCALA, y una que decide sola se rechaza
cubre: ["CONTRATO-OFICINA §3", "escalado", "Directiva del Owner §20 §41 §76", "OWN-ADS-0074", "OWN-ADS-0161", "OWN-ADS-0271"]
dado:
  - "un paquete de PRD/criterio-de-exito tomado; la ficha de PRD declara decide_sola y escala"
cuando:
  - "se entrega `escalado` sin materia, con una materia de decide_sola, con una inventada y con una de escala"
  - "se intenta escalar cuando la ficha de autoridad es ilegible o está incompleta"
entonces:
  - "las tres primeras son ENTREGA_INVALIDA y no tocan el estado; la cuarta deja el cierre `escalado` con la autoridad"
  - "sin ficha de autoridad verificable, la entrega se rechaza antes de escribir estado"
falla_si:
  - "un escalado al Owner con una materia que el equipo decide solo se admite"
  - "un error al leer el corpus autoriza una materia inventada"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T486
nombre: Las fronteras previas a la construcción se distinguen
cubre: ["CONTRATO-OFICINA §6", "fronteras", "Directiva del Owner §77", "OWN-ADS-0275", "OWN-ADS-0276"]
dado:
  - "un item planificado con el circuito cambio-con-interfaz (DIS antes que CNS)"
cuando:
  - "se evalúa la terminación antes y después de entregar DIS/diseno-visual, y sobre un plan con dos paquetes de diseño con uno solo entregado"
entonces:
  - "antes: admitida y encuadrada alcanzadas, investigada no-exigida, diseñada pendiente, aprobada sin-mecanismo"
  - "después: diseñada alcanzada —era el único paquete de la frontera—, y los niveles (implementado…) siguen faltando: las fronteras no son niveles"
  - "con dos paquetes de diseño y uno entregado, diseñada sigue pendiente y nombra sólo el que falta; con los dos, alcanzada"
falla_si:
  - "diseñada se da por alcanzada mientras algún paquete de diseño del plan sigue pendiente"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T487
nombre: Una capacidad que participa dos veces acuña paquetes distintos
cubre: ["CONTRATO-OFICINA §5", "planificacion", "a.5", "01-PROCESOS (revisión posterior de DOM y SEG)", "OWN-ADS-0022", "OWN-ADS-0112"]
dado:
  - "un circuito base con C-DOM y la composición dom-migracion (DOM/modelo y DOM/migracion) sobre FEA, donde DOM participa como DOM:condiciones y como DOM:revision"
cuando:
  - "se planifica el item, y se vuelve a planificar"
entonces:
  - "el plan tiene cuatro paquetes de DOM con identificadores distintos: dos antes de CNS/implementacion y dos después de VER/dosier"
  - "la migración previa depende del modelo previo, no del de la revisión posterior"
  - "replanificar produce los mismos identificadores: la semilla sólo entra el método cuando la participación se repite"
falla_si:
  - "`a.5` compara un paquete consigo mismo, que es lo que pasaba con TODA clase con C-DOM o C-SEG (medido en el catálogo de La Pesquerapp)"
  - "la migración previa espera a la revisión posterior y el plan se bloquea a sí mismo"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T488
nombre: Un cambio de dirección deriva su propietario del encargo
cubre: ["CONTRATO-OFICINA §5", "rutas.propietario_global", "b.16", "proceso:DIR", "OWN-ADS-0022", "OWN-ADS-0117"]
dado:
  - "un circuito base de materia direccion-ya-decidida (proceso DIR) con prd-direccion-nueva, arq-plan-completo, ver-decision y dsp-supervisor"
cuando:
  - "se planifica sin `propietario_global`; con propietario y sin `productores_declarados`; con los dos; y con un propietario que no es una capacidad"
entonces:
  - "sin propietario: PROPIETARIO_NO_DERIVABLE; con propietario y sin productoras: COMPOSICION_INCOMPLETA (sustituciones-registradas); con los dos: plan con proceso:DIR y propietario PRD, con ARQ/encaje y VER/decision y sin CNS/implementacion"
  - "con `ZZZ`: PROPIETARIO_NO_DERIVABLE"
falla_si:
  - "la oficina planifica un DIR eligiendo ella el propietario (b.16: NUNCA lo elige DSP)"
  - "la entrada del item no transporta lo que el encargo declara y ningún DIR se puede planificar desde la oficina"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T489
nombre: Un impacto que el circuito cubre no marca nada
cubre: ["CONTRATO-OFICINA §5 ter", "impacto", "Directiva del Owner §5", "OWN-ADS-0030", "OWN-ADS-0031"]
dado:
  - "un item planificado con cambio-con-interfaz (declara C-DIS) y su PRD/definicion tomado"
cuando:
  - "la entrega declara impacto.disparadores nuevo-estado-visible y nueva-accion"
entonces:
  - "la entrega vale, las condiciones derivadas son C-DIS, no hay ninguna sin cubrir, el plan no lleva marca y el siguiente paquete se toma"
falla_si:
  - "toda declaración de impacto se trata como alarma, o la declaración se ignora"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T490
nombre: Un impacto que el circuito no cubre marca el plan y para el item
cubre: ["CONTRATO-OFICINA §5 ter", "impacto", "Directiva del Owner §5", "Directiva del Owner §62", "b.1", "OWN-ADS-0030", "OWN-ADS-0032", "OWN-ADS-0033"]
dado:
  - "un item planificado con cambio-de-backend (sin C-DIS) y su PRD/definicion tomado"
cuando:
  - "la entrega declara nuevo-estado-visible y nuevo-permiso; después otra instancia intenta tomar PRD/criterio-de-exito; después se replanifica con cambio-con-interfaz y generación 1"
entonces:
  - "la entrega vale y el plan queda marcado con C-DIS y C-SEG sin cubrir, el rol que lo vio y qué hacer"
  - "tomar cualquier otro paquete del item es IMPACTO_NO_CUBIERTO y no deja lease; evaluar_terminacion publica la marca"
  - "el plan nuevo sustituye al marcado, es el vigente, no lleva marca y el item vuelve a andar"
falla_si:
  - "se sigue construyendo sobre una clasificación que ya se sabe incompleta"
  - "la replanificación deja dos planes vigentes o conserva la marca"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T491
nombre: Un disparador fuera de los dieciséis es una entrega inválida
cubre: ["CONTRATO-OFICINA §5 ter", "impacto", "Directiva del Owner §5", "OWN-ADS-0032"]
dado:
  - "un paquete tomado"
cuando:
  - "la entrega declara impacto.disparadores con un nombre fuera del vocabulario"
entonces:
  - "ENTREGA_INVALIDA nombrando los dieciséis, sin tocar el estado; el vocabulario tiene exactamente dieciséis disparadores"
falla_si:
  - "«impacto» es prosa libre que nadie puede contrastar con el circuito"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T492
nombre: Una barrera externa y un riesgo extraordinario son paradas con nombre
cubre: ["CONTRATO-OFICINA §7", "supervisor.PARADAS", "Directiva del Owner §36", "OWN-ADS-0146", "OWN-ADS-0147"]
dado:
  - "un paquete tomado cuya entrega es `bloqueado` con bloqueo.clase barrera-externa; otro con riesgo-extraordinario; otro sin clase; otro con una clase inventada"
cuando:
  - "el supervisor da dos pasadas sobre cada laboratorio"
entonces:
  - "para con `barrera-externa` nombrando el paquete; con `riesgo-extraordinario` nombrando el suyo y no la barrera (el riesgo manda); sin clase, `bloqueado`; la clase inventada es ENTREGA_INVALIDA"
  - "el paquete lleva `clase_de_bloqueo` escrita por el runtime"
falla_si:
  - "una barrera externa o un riesgo extraordinario paran como `bloqueado` genérico y TRABAJA los trata como algo que un desbloqueador resuelve"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T493
nombre: Los contratos de Diseño exigen los artefactos que la Directiva nombra por fase
cubre: ["contrato-operativo", "DIS/contratos/*", "Directiva del Owner §12–§26", "Directiva del Owner §28", "OWN-ADS-0097", "OWN-ADS-0051", "OWN-ADS-0054", "OWN-ADS-0055", "OWN-ADS-0058", "OWN-ADS-0064", "OWN-ADS-0068", "OWN-ADS-0071", "OWN-ADS-0077", "OWN-ADS-0087"]
dado:
  - "los diez roles de la línea de Diseño con contrato completo: investigacion-ux, investigacion-visual, sistema-de-diseno, direccion-artistica, prototipado, critica-visual, validacion-de-uso, diseno-interaccion, movimiento y diseno-visual"
cuando:
  - "se lee el contrato de cada uno y sus artefactos obligatorios"
entonces:
  - "cada rol exige como obligatorio el entregable de su fase con la estructura que la Directiva enumera: los siete apartados del informe de realidad (§12), los seis de la síntesis (§13), las preguntas y los estados del análisis de uso (§14), la auditoría con equivalentes, deuda de unificación y las cinco salidas nombradas (§15), los diez campos de cada alternativa (§16), la recomendación con su por qué (§17), el prototipo con estados, extremos, responsive, errores, vacíos y loading (§18), la crítica por los trece criterios con dictamen (§19, §24), la síntesis con las ocho secciones (§20), la especificación construible con los puntos de §21 y la sesión de uso con los ocho criterios y la viabilidad motivada (§25)"
  - "investigación UX, prototipado, crítica y validación dejan un artefacto mirable (captura · grabación · medición), no sólo prosa"
  - "DIS/direccion-artistica, que sostiene la función de Product Interface Lead, pregunta en su checklist las seis preguntas permanentes de §28: encaja con el producto completo, ya existe otra manera, variante innecesaria, unificar otras pantallas, deuda cercana, más coherente después"
falla_si:
  - "un rol de Diseño puede entregar «diseñado» sin el artefacto de su fase y ningún validador lo devuelve"
  - "la auditoría de reutilización admite una salida fuera de las cinco de §15"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_contratos.py
estado: prueba-superada
evidencia: evidencia/contratos-salida.txt
```

```yaml ads:escenario
id: T494
nombre: Al tomar nace la base y un avance compatible se registra
cubre: ["CONTRATO-OFICINA §2 bis", "ciclo/base.py", "Directiva del Owner §61", "Directiva del Owner §63", "OWN-ADS-0220", "OWN-ADS-0227", "OWN-ADS-0230"]
dado:
  - "un control repo que es un repositorio Git con `main` y una rama `trabajo`; la implementación se toma por la oficina"
cuando:
  - "el trabajador cambia src/a.php en su rama y otro agente avanza `main` desde un worktree aparte tocando docs/otro.md; el trabajador escribe un checkpoint y entrega"
entonces:
  - "el checkpoint 0 conserva por repo la rama `trabajo`, `nacio_de` = main de partida y la base que había"
  - "el checkpoint clasifica `compatible`, registra la base nueva, cuenta 1 commit de la base que no tiene y NO reescribe el nacimiento"
  - "la entrega vale y deja el veredicto en el último checkpoint; la integridad del estado se sostiene"
falla_si:
  - "un trabajo no sabe de qué commit nació ni en qué rama está, y la base avanza sin que nadie lo registre"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T495
nombre: Un avance que toca lo mismo contradice y no se entrega hasta reconciliar
cubre: ["CONTRATO-OFICINA §2 bis", "ciclo/base.py", "Directiva del Owner §63", "OWN-ADS-0229", "OWN-ADS-0231"]
dado:
  - "el mismo laboratorio Git; el trabajador cambió la primera línea de src/a.php y `main` avanzó añadiendo una tercera línea al mismo fichero"
cuando:
  - "el trabajador escribe un checkpoint, intenta entregar `entregado`, fusiona `main` en su rama, vuelve a escribir checkpoint y entrega"
entonces:
  - "el checkpoint dice `contradiccion` con el conflicto (control-repo, 1 commit, src/a.php) y no registra base nueva"
  - "`entregado` es BASE_CONTRADICHA nombrando el fichero; la revisión del estado no cambia y el paquete sigue `ejecutando`"
  - "tras reconciliar, el checkpoint dice `sin-cambio` con la base registrada, y la entrega vale"
falla_si:
  - "se entrega «terminado» sobre una base que ya cambió lo mismo, y Git descubre el conflicto al final"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T496
nombre: Un control repo sin Git no se mide y nada cambia
cubre: ["CONTRATO-OFICINA §2 bis", "ciclo/base.py"]
dado:
  - "un laboratorio corriente, que no es un repositorio Git"
cuando:
  - "se toma la implementación, se escribe un checkpoint y se entrega"
entonces:
  - "tomar no escribe checkpoint 0 ni devuelve base; el checkpoint conserva exactamente el contenido del trabajador; la entrega vale"
falla_si:
  - "una medida que no existe frena un control repo sin Git, o los laboratorios de la batería cambian de comportamiento"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T497
nombre: Con varias fuentes el Integration Set define orden de merge, compatibilidad y despliegue
cubre: ["CONTRATO-OFICINA §3", "esquemas/integration-set.yaml", "Directiva del Owner §71", "OWN-ADS-0255"]
dado:
  - "un item que escribe backend y frontend, y un Integration Set completo con orden_de_merge, compatibilidad, despliegue y dependencias"
cuando:
  - "se exige el conjunto completo; el de una sola fuente sin esos campos; y nueve variantes: sin orden, sin despliegue, sin compatibilidad, orden con una fuente de menos, orden con una ajena, despliegue incompleto, dos fuentes con el mismo orden, compatibilidad entre una fuente ajena, despliegue mal formado"
entonces:
  - "el completo y el de una fuente valen; las nueve variantes son ENTREGA_INVALIDA nombrando el campo y el motivo"
falla_si:
  - "varias PRs llegan al Owner como trabajos inconexos, sin orden de merge ni despliegue"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T498
nombre: Un recurso exclusivo en manos ajenas hace al paquete temporalmente incompatible
cubre: ["CONTRATO-OFICINA §2", "runtime/politica.py", "runtime/dispatcher.py", "runtime/externo.py", "Directiva del Owner §68", "OWN-ADS-0244", "OWN-ADS-0245", "OWN-ADS-0246"]
dado:
  - "tres paquetes externos: pq-a y pq-b afectan al mismo contrato api/v2/pedidos y escriben ficheros distintos; pq-c escribe otro fichero y sólo lee backend"
cuando:
  - "w-A toma pq-a; w-B intenta tomar pq-b y toma pq-c; w-A entrega pq-a y toma pq-b"
entonces:
  - "con pq-a en ejecución, pq-b sale de `elegibles` y de `tomables`, aparece en `esperando` con incompatible_por (contrato:api/v2/pedidos, lo posee pq-a) y en `incompatibles_por_recurso`; pq-c sigue tomable"
  - "tomar pq-b es RECURSO_OCUPADO nombrando el contrato, sin retener el lease y sin mover el paquete"
  - "al entregar pq-a no queda ningún incompatible y pq-b se toma; la integridad se sostiene"
falla_si:
  - "dos workers escriben el mismo contrato a la vez y el Owner arbitra a mano"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_oficina.py
estado: prueba-superada
evidencia: evidencia/oficina-salida.txt
```

```yaml ads:escenario
id: T499
nombre: La independencia se declara en un solo sentido, y la declara quien revisa
cubre: ["rol", "ciclo/planificacion.py", "Directiva del Owner §81", "OWN-ADS-0097"]
dado:
  - "`requiere_independencia` no es una marca simétrica: ORDENA. `_ordenar_por_estacion_de_rol` coloca a quien la exige DESPUÉS de aquel de quien la exige, porque quien revisa espera a quien produce lo revisado"
  - "todos los roles del corpus con su bloque `independencia`"
cuando:
  - "se buscan los pares A/B en los que A exige independencia de B y B la exige de A"
entonces:
  - "no existe ninguno: la separación la declara UNA vez el rol que REVISA, y el que produce la explica en su `motivo` con `requiere_independencia: false`, como ya hacía DIS/prototipado"
  - "con el ciclo roto, el plan de `dis-feature-visual` ordena investigación → sistema → dirección artística → producción → crítica, validación y fidelidad: la dirección se aprueba ANTES de construir, que es lo que §81 exige"
falla_si:
  - "dos roles se exigen independencia mutuamente: la relajación no tiene punto fijo, sube a los dos medio escalón por vuelta hasta el tope y los deja a ambos al final del plan"
  - "DIS/direccion-artistica cae detrás de CNS/implementacion y el Owner aprueba la dirección cuando ya está construida"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_contratos.py
estado: prueba-superada
evidencia: evidencia/contratos-salida.txt
```
