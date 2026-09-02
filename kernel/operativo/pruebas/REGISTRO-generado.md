# REGISTRO DE PRUEBAS — generado

<!-- GENERADO por validadores/registro_pruebas.py. No editar a mano. -->
<!-- source_revision: a50d3073acf515c0 -->

Fuente: los bloques `ads:escenario` de `kernel/operativo/` y `packs/`.
Los cuatro estados y qué autoriza a decir cada uno: [`REGISTRO.md`](REGISTRO.md).

## Recuento

| estado | pruebas |
|---|---|
| CONTRATO DEFINIDO | 56 |
| VALIDADOR IMPLEMENTADO | 0 |
| PRUEBA EJECUTADA | 0 |
| PRUEBA SUPERADA | 62 |
| PRUEBA FALLIDA | 0 |
| **total** | **118** |

## Detalle

| id | prueba | cubre | ejecución | estado | evidencia |
|---|---|---|---|---|---|
| [T75](../entrada/05-ESCENARIOS.md) | El comentario subjetivo no se traduce a tarea técnica | paso 1.6 · forma:comentario-subjetivo · gate:encuadre-listo · gate:anclaje-completo | requiere-juicio-humano | **CONTRATO DEFINIDO** | — |
| [T76](../entrada/05-ESCENARIOS.md) | Deíctico resuelto sin preguntar y sin desaparcar | forma:referencia-anterior · b.13 desambiguación · a.2 aparcado | guion-manual | **CONTRATO DEFINIDO** | — |
| [T77](../entrada/05-ESCENARIOS.md) | Relevo de agente a mitad de conversación sin pedir resumen al Owner | forma:interrupcion · a.10 checkpoint · ENC/Escucha · T01 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T78](../entrada/05-ESCENARIOS.md) | Orden emitida sobre base que dejó de ser vigente | ENC/Orden · gate:orden-emitida · a.9 protocolo de órdenes · T24 | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T79](../entrada/05-ESCENARIOS.md) | Un comentario sin objetivo no genera ningún artefacto de trabajo | 01-TAXONOMIA · a.7 modo de fallo (b) · b.15 regla dura | guion-manual | **CONTRATO DEFINIDO** | — |
| [T80](../entrada/05-ESCENARIOS.md) | Duplicado con item aparcado se convierte en propuesta de retomar | ENC/Anclaje · gate:anclaje-completo · a.2 aparcado · T10 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T81](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Anclaje sin repetir búsquedas | ENC/Anclaje · a.10 checkpoint · gate:anclaje-completo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T82](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Maduracion sin repetir alternativas rechazadas | ENC/Maduracion · forma:idea-inmadura · a.10 checkpoint | guion-manual | **CONTRATO DEFINIDO** | — |
| [T83](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Orden sin aplicar dos veces el mismo evento | ENC/Orden · gate:orden-emitida · a.9 idempotencia por id | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T84](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Formulacion desde campos parcialmente escritos | ENC/Formulacion · gate:encuadre-listo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T85](T081-T085-reanudacion-ENC.md) | La crítica no se reanuda si su lectura independiente no se escribió | ENC/Critica · gate:critica-de-encuadre · G13 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T86](T086-T092-contratos.md) | La autoridad de un rol no excede la de su capacidad | C1 · a.1 AUTORIDAD · autoridad silenciosa | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T87](T086-T092-contratos.md) | La independencia gana siempre a la combinación | C4 paso 5 · C2 combinaciones prohibidas · G13 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T88](T086-T092-contratos.md) | Todo rol es materializable porque su prompt existe | C1 campo prompt · regla R02 · C4 prohibiciones | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T89](T086-T092-contratos.md) | Ninguna reanudación se declara posible sin prueba que la respalde | C3 regla 7 · regla R03 · a.10 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T90](T086-T092-contratos.md) | Capacidades y roles se referencian mutuamente sin huérfanos | a.1 · C1 · C4 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T91](T086-T092-contratos.md) | Ningún paso de ningún método dura lo que el agente decida | C3 regla 1 · esquemas/metodo.yaml | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T92](T086-T092-contratos.md) | El kernel es portable porque ningún contrato exige una marca | K0.8 · C2 regla de portabilidad | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T93](T093-T098-diseno.md) | Reanudación de DIS/Fundacion sin reproponer lo descartado | DIS/Fundacion · a.10 checkpoint · memoria:decisiones-de-diseno | guion-manual | **CONTRATO DEFINIDO** | — |
| [T94](T093-T098-diseno.md) | Reanudación de DIS/Reconstruccion sin recapturar | DIS/Reconstruccion · a.10 checkpoint | guion-manual | **CONTRATO DEFINIDO** | — |
| [T95](T093-T098-diseno.md) | DIS/Evolucion no se reanuda sin rama declarada | DIS/Evolucion · 03-ESCALA-DE-NOVEDAD · a.10 checkpoint | guion-manual | **CONTRATO DEFINIDO** | — |
| [T96](T093-T098-diseno.md) | La crítica visual no dictamina sin comparación con la categoría | DIS/CriticaVisual · rubrica:excelencia-visual · gate:excelencia-visual | guion-manual | **CONTRATO DEFINIDO** | — |
| [T97](T093-T098-diseno.md) | Reanudación de la revisión de fidelidad sin recapturar entornos | DIS/RevisionDeFidelidad · 05-FIDELIDAD | guion-manual | **CONTRATO DEFINIDO** | — |
| [T98](T093-T098-diseno.md) | La validación de uso no reconvoca al Owner por lo ya observado | DIS/ValidacionDeUso · rubrica:usabilidad · G36 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T99](T093-T098-diseno.md) | Una interfaz usable puede ser rechazada por el gate visual | gate:usabilidad · gate:excelencia-visual · los dos gates independientes | requiere-juicio-humano | **CONTRATO DEFINIDO** | — |
| [T100](T100-T121-capacidades.md) | Reanudación de PRD/Definicion sin repreguntar al Owner | PRD/Definicion · a.10 checkpoint | guion-manual | **CONTRATO DEFINIDO** | — |
| [T101](T100-T121-capacidades.md) | Un GAP registra por qué apareció el hueco | PRD/Gap · b.16 GAP · aprendizaje del hueco | guion-manual | **CONTRATO DEFINIDO** | — |
| [T102](T100-T121-capacidades.md) | Reanudación de ARQ/Encaje sin repetir el radio | ARQ/Encaje · gate:plan-tecnico | guion-manual | **CONTRATO DEFINIDO** | — |
| [T103](T100-T121-capacidades.md) | Reanudación de un diagnóstico sin repetir hipótesis descartadas | ARQ/Diagnostico | guion-manual | **CONTRATO DEFINIDO** | — |
| [T104](T100-T121-capacidades.md) | Las condiciones de dominio llegan antes de construir | DOM/Condiciones · b.16 DOM dos veces | guion-manual | **CONTRATO DEFINIDO** | — |
| [T105](T100-T121-capacidades.md) | Una migración no se declara reversible sin haber revertido | DOM/Migracion · veto:integridad-de-datos | guion-manual | **CONTRATO DEFINIDO** | — |
| [T106](T100-T121-capacidades.md) | Construcción devuelve en vez de redecidir | CON/Implementacion · a.3 CON no redecide | guion-manual | **CONTRATO DEFINIDO** | — |
| [T107](T100-T121-capacidades.md) | Un experimento no se reanuda sin criterio de descarte previo | CON/Experimental · b.16 CON:experimental | guion-manual | **CONTRATO DEFINIDO** | — |
| [T108](T100-T121-capacidades.md) | Reanudación de un dosier sin repetir mediciones | VER/Dosier · gate:evidencia-suficiente | guion-manual | **CONTRATO DEFINIDO** | — |
| [T109](T100-T121-capacidades.md) | VER:decision detecta un impacto sin item derivado | VER/Decision · b.16 VER:decision · T71 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T110](T100-T121-capacidades.md) | Un despliegue no empieza sin reversión comprobada | ENT/Despliegue · gate:entrega-observada | guion-manual | **CONTRATO DEFINIDO** | — |
| [T111](T100-T121-capacidades.md) | Rollback autónomo sólo con los cinco requisitos | ENT/Contencion · a.3 rollback autónomo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T112](T100-T121-capacidades.md) | El Owner se convoca por lotes, no por item | USO/Validacion · G36 · b.11 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T113](T100-T121-capacidades.md) | Un INV cierra sin generar un segundo item | INV/Investigacion · T39 · b.16 INV | guion-manual | **CONTRATO DEFINIDO** | — |
| [T114](T100-T121-capacidades.md) | Un veto de seguridad sobrevive al cambio de agente | SEG/Condiciones · veto:seguridad | guion-manual | **CONTRATO DEFINIDO** | — |
| [T115](T100-T121-capacidades.md) | Una dependencia no se incorpora sin veredicto fechado | SEG/Dependencia · G28 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T116](T100-T121-capacidades.md) | La maquinaria sólo cuenta si se reproduce desde cero | PLT/Maquinaria · gate:maquinaria-disponible | guion-manual | **CONTRATO DEFINIDO** | — |
| [T117](T100-T121-capacidades.md) | Sin aprendizaje promovible es un resultado legítimo | APR/Promocion · gate:aprendizaje-fundado · T20 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T118](T100-T121-capacidades.md) | Toda ruta declara lo que no activó y por qué | DSP/Enrutamiento · a.6 traza · T05 | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T119](T100-T121-capacidades.md) | Continúa retoma sin pedir permiso ni resumen | DSP/Continua · b.14 · T36 | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T120](T100-T121-capacidades.md) | Ningún cambio del sistema entra sin validador ni estado real de prueba | SIS/Evolucion · gate:sistema-conforme | guion-manual | **CONTRATO DEFINIDO** | — |
| [T121](T100-T121-capacidades.md) | La auditoría de conformidad no escribe contenido ajeno | SIS/Conformidad · a.3 coherencia documental | guion-manual | **CONTRATO DEFINIDO** | — |
| [T122](T122-T133-T149-packs.md) | Toda la matriz de navegadores tiene evidencia | web-app · gate:web-accesibilidad · VER/Dosier | guion-manual | **CONTRATO DEFINIDO** | — |
| [T123](T122-T133-T149-packs.md) | El recorrido completo se hace con teclado solo | web-app · gate:web-accesibilidad | guion-manual | **CONTRATO DEFINIDO** | — |
| [T124](T122-T133-T149-packs.md) | Lo escrito sobrevive a un fallo de red | web-app · gate:web-estados-de-red · web:CON/estados-de-red | guion-manual | **CONTRATO DEFINIDO** | — |
| [T125](T122-T133-T149-packs.md) | El emulador no sustituye al dispositivo real | mobile-app · gate:mob-dispositivo-real | guion-manual | **CONTRATO DEFINIDO** | — |
| [T126](T122-T133-T149-packs.md) | La terminación forzada no pierde el trabajo del usuario | mobile-app · gate:mob-ciclo-y-permisos · mob:CON/ciclo-de-vida | guion-manual | **CONTRATO DEFINIDO** | — |
| [T127](T122-T133-T149-packs.md) | Los tres estados de cada permiso están resueltos | mobile-app · gate:mob-ciclo-y-permisos | guion-manual | **CONTRATO DEFINIDO** | — |
| [T128](T122-T133-T149-packs.md) | La superficie del reloj se entiende en el tiempo declarado | wear-os · gate:wear-vistazo · wear:DIS/lectura-de-un-vistazo | requiere-juicio-humano | **CONTRATO DEFINIDO** | — |
| [T129](T122-T133-T149-packs.md) | Volver del ambiental no reinicia el trabajo | wear-os · gate:wear-ambiental · wear:CON/energia-y-estados | guion-manual | **CONTRATO DEFINIDO** | — |
| [T130](T122-T133-T149-packs.md) | El consumo se mide sin cargador y en reloj real | wear-os · gate:wear-consumo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T131](T122-T133-T149-packs.md) | La compatibilidad entre packs es simétrica y la precedencia está escrita | packs/COMPOSICION · A-03 · T18 | validador-estructural | **PRUEBA SUPERADA** | evidencia/packs-salida.txt |
| [T132](T122-T133-T149-packs.md) | Un rol de pack no reclama autoridad de un rol del kernel | packs/00-QUE-ES-UN-PACK · T18 · C1 | validador-estructural | **PRUEBA SUPERADA** | evidencia/packs-salida.txt |
| [T133](T122-T133-T149-packs.md) | La entrega móvil-reloj admite versiones distintas conviviendo | wear-os · mobile-app · packs/COMPOSICION | guion-manual | **CONTRATO DEFINIDO** | — |
| [T135](T086-T092-contratos.md) | Ninguna composición rebaja la independencia que exige un contrato | C1 independencia · C4 paso 5 · G13 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T136](T136-T152-post-auditoria.md) | Ningún veto arbitra a otro veto levantable | A-06 · a.5 regla de colisión de vetos · veto:degradacion-de-forma · veto:integridad-de-datos | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T137](T136-T152-post-auditoria.md) | DSP no declara autoridad semántica sobre ninguna cancelación | A-23 · b.7 autoridad orden y ejecución · T54 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T138](T136-T152-post-auditoria.md) | La escala de novedad es total y sus cinco niveles son alcanzables | A-07 · 03-ESCALA-DE-NOVEDAD · DIS/Reconstruccion · DIS/Fundacion | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T139](T136-T152-post-auditoria.md) | Ningún nivel de novedad omite un gate obligatorio | A-08 · 03-ESCALA-DE-NOVEDAD · 04-CICLO-DE-CALIDAD · gate:usabilidad · gate:excelencia-visual | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T140](T136-T152-post-auditoria.md) | Las obligaciones del proceso existen y el cierre las comprueba | A-09 · b.3 · b.4 P10 · b.10 · b.16 · gate:cierre-de-item · T52 · T53 · T64 · T65 · T66 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T141](T136-T152-post-auditoria.md) | Los frenos tienen ejecutor operativo, no sólo prosa | A-10 · a.7 los tres frenos · b.9 avance material · b.12 inanición · T06 · T07 · T08 · T41 | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T142](T136-T152-post-auditoria.md) | El encuadre expresa todos los estados que sus métodos le exigen | A-11 · b.2 los once estados de paquete · gate:encuadre-listo · ENC/Escucha | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T144](T136-T152-post-auditoria.md) | El gate de usabilidad tiene portador computable en Construcción | A-13 · gate:usabilidad · gate:implementacion-completa · DIS/validacion-de-uso | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T145](T136-T152-post-auditoria.md) | La crítica de encuadre exigible no se evapora al bajar la incertidumbre | A-14 · gate:encuadre-listo · composicion:enc-alta-incertidumbre · C4 un rol independiente no se retira | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T146](T136-T152-post-auditoria.md) | Ningún rol decide lo que su capacidad escala ni lo que decide otra | A-18 · C1 autoridad del rol frente a la de la capacidad · sustituye parte de lo que T86 prometía | validador-estructural | **PRUEBA SUPERADA** | evidencia/contratos-salida.txt |
| [T147](T136-T152-post-auditoria.md) | Todo documento es alcanzable por ruta, y ninguna referencia es ambigua | A-05 · A-28 · sustituye a T134 · a.7 modo de fallo (b) · regla de fuente única | validador-estructural | **PRUEBA SUPERADA** | evidencia/referencias-salida.txt |
| [T148](T136-T152-post-auditoria.md) | El arranque documentado crea un proyecto conforme con cada pack | A-02 · tooling/new-project.sh · README · START_HERE · K0.14 | validador-estructural | **PRUEBA SUPERADA** | evidencia/arranque-salida.txt |
| [T149](T122-T133-T149-packs.md) | Lo más restrictivo gana entre dos packs, y queda registrado por qué | A-03 · A-25 · packs/COMPOSICION precedencia P1 · composicion_packs.py | validador-estructural | **PRUEBA SUPERADA** | evidencia/packs-salida.txt |
| [T150](T136-T152-post-auditoria.md) | La huella de integridad cubre a los validadores y detecta su edición | A-04 · K0.11 · tooling/kernel-status.sh · validadores/huella.py | validador-estructural | **PRUEBA SUPERADA** | evidencia/integridad-salida.txt |
| [T151](T136-T152-post-auditoria.md) | Ninguna cifra del corpus contradice el recuento derivado | A-24 · regla de fuente única · RECUENTOS-generado.md | validador-estructural | **PRUEBA SUPERADA** | evidencia/recuentos-salida.txt |
| [T152](T136-T152-post-auditoria.md) | Los puntos de entrada no se contradicen sobre la versión | A-12 · kernel/VERSIONES.md · K0.11 · O2 | validador-estructural | **PRUEBA SUPERADA** | evidencia/versiones-salida.txt |
| [T153](T136-T152-post-auditoria.md) | Cada unidad de instrucción declara y enlaza las señales estructurales que su contrato exige | revisión de las unidades de instrucción · C1 contrato común de rol · 00-INDICE la excepción de los prompts | validador-estructural | **PRUEBA SUPERADA** | evidencia/prompts-salida.txt |
| [T154](../entrada/05-ESCENARIOS.md) | Con dirección aprobada incumplida, la expresión subjetiva produce un GAP | forma:comentario-subjetivo · ENC/Anclaje · b.16 GAP · 9.4 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T155](../entrada/05-ESCENARIOS.md) | Sin dirección de diseño, la expresión produce dirección más GAP enlazado | forma:comentario-subjetivo · ENC/Anclaje · 03-ESCALA-DE-NOVEDAD N4 y N3 · 9.4 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T156](../entrada/05-ESCENARIOS.md) | Con dirección vigente que el Owner quiere sustituir, la salida es un DIR | forma:cambio-de-direccion · b.16 DIR · G51 · 9.4 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T157](../entrada/05-ESCENARIOS.md) | Con la intención todavía ambigua, la expresión NO produce ningún item | forma:comentario-subjetivo · 04-INCERTIDUMBRE · a.7 modo de fallo (b) · 9.4 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T158](T136-T152-post-auditoria.md) | La evidencia publicada demuestra lo que el informe afirma | evidencia reproducible · REGISTRO.md regla dura · registrar_evidencia.py · validadores.yaml | validador-estructural | **PRUEBA SUPERADA** | evidencia/evidencia-salida.txt |
| [T159](T159-T170-multirepo.md) | La plantilla de SOURCES.toml es válida y arranca sin fuentes | C6 fuente única de la composición · E2.0 | validador-estructural | **PRUEBA SUPERADA** | evidencia/fuentes-salida.txt |
| [T160](T159-T170-multirepo.md) | El manifiesto de un ADS Project, cuando existe, es válido sin tocar el disco | C6 validación estática frente a disponibilidad · §62 | validador-estructural | **PRUEBA SUPERADA** | evidencia/fuentes-salida.txt |
| [T161](T159-T170-multirepo.md) | El corpus no conserva la equivalencia proyecto igual a repositorio | E2.0 · E2.1 · E2.4 · 78 qué debe cambiar en el corpus | validador-estructural | **PRUEBA SUPERADA** | evidencia/fuentes-salida.txt |
| [T162](T159-T170-multirepo.md) | Una fuente ya clonada se reutiliza y no se vuelve a clonar | C6 materialización · §12.1 · CA-3 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T163](T159-T170-multirepo.md) | Un directorio ocupado por otro repositorio produce error y no se destruye | C6 lo que la materialización nunca hace · §63 · CA-5 · CA-6 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T164](T159-T170-multirepo.md) | Ninguna ruta del manifiesto escapa del workspace | C6 identidad frente a materialización · §11.2 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T165](T159-T170-multirepo.md) | La identidad de una fuente no depende de la forma de su URL | C6 identidad · 39 normalización de remotes · N9 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T166](T159-T170-multirepo.md) | Un componente puede vivir dentro de una fuente, y dos componentes compartirla | C6 los tres conceptos · §9 · §10 · CA-7 · CA-8 · N7 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T167](T159-T170-multirepo.md) | Una fuente ausente no bloquea el trabajo que no la necesita | C6 alcance mínimo · 63 source ausente · E2.2 regla 5 | validador-estructural | **PRUEBA SUPERADA** | evidencia/workspace-salida.txt |
| [T168](T159-T170-multirepo.md) | El arranque crea un workspace con el control repo dentro, en la rama que documenta, y el workspace no es un repositorio | C6 topología · §45 · §46 · CA-1 · CA-9 | validador-estructural | **PRUEBA SUPERADA** | evidencia/arranque-salida.txt |
| [T169](T159-T170-multirepo.md) | Un item que atraviesa dos fuentes no cierra con una sin integrar | E2.6 · C7 integración parcial · gate:convergencia-de-fuentes · §30 | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T170](T159-T170-multirepo.md) | Un agente nuevo reanuda un trabajo multi-fuente sin abrir ningún repositorio para adivinar | E2.3 · C7 recuperación · §34 · §35 · CA-12 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T171](T159-T170-multirepo.md) | El proyecto recién creado declara dónde se lee cada criterio de descubrimiento del 100 | §100 · CA-1 · CA-9 · CA-10 | validador-estructural | **PRUEBA SUPERADA** | evidencia/arranque-salida.txt |
| [T172](T172-T181-estado-durable.md) | Un intérprete insuficiente detiene la batería antes de correr, y no como defecto del producto | A14 · F6-I · corte V1 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T173](T172-T181-estado-durable.md) | El estado canónico se inicializa y se lee sin reproyectar el diario | g.1 · g.2 I-g1 · g.16 G-A1 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T174](T172-T181-estado-durable.md) | Una transición multiarchivo se ve entera o no se ve | g.3 · g.4 · g.12 · g.16 G-A2 · g.16 G-A3 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T175](T172-T181-estado-durable.md) | Una interrupción en cualquier frontera termina en COMPLETAR o en MARCAR, y en nada más | g.8 · g.3 · g.16 G-A2 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T176](T172-T181-estado-durable.md) | Dos escritores concurrentes se serializan y no hay doble éxito para la misma revisión | g.6 · g.12 I-g4 · g.16 G-A5 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T177](T172-T181-estado-durable.md) | La corrupción, el truncamiento y la evidencia manipulada fallan CERRADO | g.5 · g.13 · g.15 · g.16 G-A4 · g.16 G-A9 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T178](T172-T181-estado-durable.md) | La reconciliación pendiente se deduce del registro auxiliar y sólo se retira por transición explícita | g.9 · g.2 I-g7 · g.16 G-A5 · g.16 G-A6 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T179](T172-T181-estado-durable.md) | Una versión de esquema desconocida falla CERRADO, y subir de versión exige migración declarada | g.10 · g.11 · g.16 G-A7 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-durable-salida.txt |
| [T180](T172-T181-estado-durable.md) | Los quince pasos del escenario extremo a extremo, sobre un control repo real | g.3 · g.4 · g.5 · g.6 · g.8 · g.9 · g.13 · g.16 | validador-estructural | **PRUEBA SUPERADA** | evidencia/estado-e2e-salida.txt |
| [T181](T172-T181-estado-durable.md) | La especificación normativa vigente viaja al proyecto instalado, derivada y no escrita a mano | FD-3 · C6 · E2.0 | validador-estructural | **PRUEBA SUPERADA** | evidencia/arranque-salida.txt |
| [T182](T182-T194-runtime-y-admision.md) | El dispatcher deriva el trabajo del estado y lo despacha por un adaptador | F6-D · 11-ARQ 7.2 · g.12 I-g4 | validador-estructural | **PRUEBA SUPERADA** | evidencia/runtime-salida.txt |
| [T183](T182-T194-runtime-y-admision.md) | La autoridad sobre un paquete es exclusiva, y expira por observaciones y no por reloj | g.6 · g.2 I-g3 · F6-D | validador-estructural | **PRUEBA SUPERADA** | evidencia/runtime-salida.txt |
| [T184](T182-T194-runtime-y-admision.md) | Las cuatro clases de fallo se distinguen, y agotar los intentos abre reconciliación | 11-ARQ 7.3 · g.9 · g.16 G-A5 | validador-estructural | **PRUEBA SUPERADA** | evidencia/runtime-salida.txt |
| [T185](T182-T194-runtime-y-admision.md) | Pausa, reanudación y cancelación son transiciones reales del estado canónico | 11-ARQ 7.3 · F6-D | validador-estructural | **PRUEBA SUPERADA** | evidencia/runtime-salida.txt |
| [T186](T182-T194-runtime-y-admision.md) | Una caída entre el efecto y su acuse no repite el efecto al recuperarse | g.8 · g.3 · F6-D | validador-estructural | **PRUEBA SUPERADA** | evidencia/runtime-salida.txt |
| [T187](T182-T194-runtime-y-admision.md) | Forzar una referencia del control repo es imposible por política y detectable si se intenta | g.14 · g.16 G-A8 · O16 | validador-estructural | **PRUEBA SUPERADA** | evidencia/gobierno-git-salida.txt |
| [T188](T182-T194-runtime-y-admision.md) | Toda lectura de Git usa una representación inequívoca, y la admisión juzga la mutación | V6-01 · V6-02 · V6-03 · V6-04 · V6-05 · V6-06 · V6-07 · V6-08 · V6-09 | validador-estructural | **PRUEBA SUPERADA** | evidencia/admision-salida.txt |
| [T189](T182-T194-runtime-y-admision.md) | El censo de zonas cubre el CONTENIDO, incluida la raíz, y el instrumento se incluye a sí mismo | V6-10 · V6-11 · V6-12 · S1-02 | validador-estructural | **PRUEBA SUPERADA** | evidencia/admision-salida.txt |
| [T190](T182-T194-runtime-y-admision.md) | La matriz adversarial mide cero falsos verdes y cero falsos rojos, y cada fórmula tiene una sede | V6-13 · V6-14 · V6-17 · V6-18 · V6-19 | validador-estructural | **PRUEBA SUPERADA** | evidencia/admision-salida.txt |
| [T191](T182-T194-runtime-y-admision.md) | El adaptador local ejecuta un proceso real, lo mata de verdad y no repite un efecto aplicado | V7 · 11-ARQ 6 · 11-ARQ 3.4 | validador-estructural | **PRUEBA SUPERADA** | evidencia/adaptadores-salida.txt |
| [T192](T182-T194-runtime-y-admision.md) | La identidad de firma vive fuera del árbol, rota con solapamiento y no filtra secretos | O25 · g.15 · FD-1 | validador-estructural | **PRUEBA SUPERADA** | evidencia/identidad-salida.txt |
| [T193](T182-T194-runtime-y-admision.md) | Los veinticinco pasos del segundo escenario extremo a extremo, con dos runtimes y dos fuentes | F6-D · g.14 · V6-10 · V7 · g.9 · g.16 | validador-estructural | **PRUEBA SUPERADA** | evidencia/e2e-runtime-salida.txt |
| [T194](T182-T194-runtime-y-admision.md) | Un control repo que ya existe se actualiza sin perder lo que el proyecto tiene | C6 · FD-3 · macrocircuito de actualizacion | validador-estructural | **PRUEBA SUPERADA** | evidencia/arranque-salida.txt |
