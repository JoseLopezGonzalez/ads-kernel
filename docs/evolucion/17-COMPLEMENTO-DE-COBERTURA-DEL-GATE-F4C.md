# COMPLEMENTO DE COBERTURA DEL GATE DE F4C — NIVEL 0

> **Nota de transcripción — la escribe el agente principal, NO los revisores ni el adjudicador.**
>
> ```text
> QUÉ ES ESTE DOCUMENTO   el cierre del **NIVEL 0** que el gate final dejó escrito como su
>                         requisito `0.1`: cubrir las fuentes obligatorias que NINGÚN revisor
>                         del gate abrió. **No es una revisión nueva** y **no emite veredicto
>                         de suficiencia**: el veredicto vigente sigue siendo el del
>                         documento 16, INSUFICIENTE PARA F5.
>
> QUIÉN JUZGA             TRES agentes con CONTEXTO LIMPIO, ninguno autor de F4 ni de sus
>                         correcciones, ninguno participante en el gate:
>                           REVISOR D      leyó PRIMERO las fuentes y DESPUÉS los hallazgos,
>                                          en ese orden explícito, para reducir anclaje
>                           REVISOR E      en paralelo, con énfasis en C1–C3, C5, handoffs y
>                                          los documentos del Owner
>                           ADJUDICADOR F  recibió los dos dictámenes ya cerrados, verificó
>                                          contra los ficheros originales y consolidó
>
> CÓMO SE PROTEGIÓ LA     D y E trabajaron EN PARALELO y no vieron el dictamen del otro hasta
> INDEPENDENCIA           terminar. F recibió los dos DESPUÉS de que ambos cerraran, y **no
>                         resolvió por mayoría**: corrigió a los tres que le precedieron —a
>                         `C` sobre `SEG`, a `D` sobre la lista de criterios, a `E` sobre una
>                         cita imposible— y rechazó tres piezas.
>
> QUIÉN TRANSCRIBE        el agente principal, que SÍ escribió las correcciones de F4 y por
>                         tanto NO PUEDE CERTIFICAR SU PROPIO TRABAJO. Copia los tres textos
>                         LITERALMENTE. **No ha suavizado, reinterpretado ni corregido ningún
>                         hallazgo**, y NO ha tocado `11-ARQUITECTURA-INTEGRADA.md`, el
>                         documento 15, el documento 16 ni el registro de decisiones.
>
> SOBRE QUÉ ÁRBOL         HEAD `7c7856ccb88ea3851fb5e1fc1ec04af38d03ab96`, rama
>                         `redesign/kernel-2.0`, árbol limpio, DOCE commits sin publicar.
>
> QUÉ NO SE HA HECHO      NINGÚN hallazgo se ha corregido. `F4c` sigue ABIERTA.
> ```

---

## Inventario de las fuentes del nivel 0

**El requisito `0.1` del documento 16 dice «dieciocho» y su propia enumeración lista
DIECINUEVE ficheros.** La discrepancia se detectó antes de empezar y **se cubrieron las
diecinueve**: cubrir de más cierra la ambigüedad; cubrir dieciocho habría dejado un fichero
sin leer bajo el listado del propio documento. El adjudicador `F` lo registra como una de las
tres instancias del hallazgo `F-12`.

| # | ruta exacta | líneas | SHA-256 (16 primeros) |
|---|---|---|---|
| 1 | `kernel/operativo/circuitos/DIS-handoffs.md` | 247 | `87bb395766164dfd` |
| 2 | `kernel/operativo/circuitos/handoffs-generales.md` | 245 | `1902884c33728729` |
| 3 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026` |
| 4 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3` |
| 5 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac21` |
| 6 | `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | 264 | `8695161d660b9bc5` |
| 7 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c0` |
| 8 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603` |
| 9 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f` |
| 10 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d` |
| 11 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9` |
| 12 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8d` |
| 13 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3 343 | `64d170f5acc15144` |
| 14 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f` |
| 15 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c` |
| 16 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `e204167c8895bff9` |
| 17 | `kernel/operativo/entrada/03-FORMAS.md` | 557 | `cdb3b575f8a28a5a` |
| 18 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d` |
| 19 | `kernel/operativo/entrada/05-ESCENARIOS.md` | 637 | `31f2dcece59e2ecb` |
| | **TOTAL** | **8 310** | |

**Cobertura suplementaria que el nivel 0 cerró sin que el requisito la pidiera:**
`kernel/operativo/entrada/01-TAXONOMIA.md` (309 líneas), que el documento 16 daba por cubierto
sólo en dos bloques de nueve y del que depende `M-6` — leído íntegro por `E`. Y
`kernel/operativo/circuitos/00-CIRCUITOS.md` (240 líneas), **que no estaba entre las
diecinueve** — leído íntegro por `D`, que lo declaró por delante porque **refuta parcialmente
su propio hallazgo**, y por `F`, que resolvió con él la única discrepancia material.

**La evidencia de lectura fichero a fichero** —secciones relevantes, decisiones que aporta,
hallazgos que toca, y cita comprobable de la primera y de la última sección sustantiva— vive
en la sección 2 de cada dictamen, y no se repite aquí.

---

## DICTAMEN DEL REVISOR D

### 1 · Identidad, procedencia y modo

**Quién soy.** Revisor D del NIVEL 0 del gate final de `F4c`. Repositorio `/home/jose/ads-kernel`, rama `redesign/kernel-2.0`, HEAD verificado por `git rev-parse` → `7c7856ccb88ea3851fb5e1fc1ec04af38d03ab96`. Árbol limpio al iniciar.

**Qué NO soy.** No escribí `F4`, ni `F4b`, ni `F4c`, ni ninguna de sus correcciones. No participé en el gate: no soy el Revisor A, no soy el Revisor B, no soy el Adjudicador C. No consulté al Revisor E ni supongo nada de lo que diga; nada de este dictamen depende de él.

**Modo.** Sólo lectura. No he modificado ningún fichero del repositorio, no he ejecutado ninguna escritura de git, no he hecho commits. Los únicos comandos ejecutados fueron `git rev-parse`, `git status`, `wc`, `cat`, `sed -n`, `grep` y `ls`. No he usado Google Calendar ni Google Drive (ambos conectores exigen autorización en esta sesión; no la solicité y no la necesito).

**Orden de lectura, y por qué importa.** Leí **primero las diecinueve fuentes íntegras**, en el orden en que el encargo las lista, y **no abrí el documento 16 hasta haberlas terminado**. Entre medias contrasté contra `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` sólo en cinco tramos (§2.1, §3.3, §8.0–§8.4, §15.2/§15.4/§15.7, §18 por referencia indirecta) y contra `kernel/operativo/recorrido/01-PROCESOS.md`, para poder juzgar por mí mismo qué dicen las fuentes antes de que nadie me dijera qué buscar. La consecuencia de este orden es visible en las seis comprobaciones: mi lectura de `C5` frente a `B-2` se formó **antes** de leer `B-2`.

**Un fichero adyacente que abrí y declaro.** Para responder honestamente a la comprobación 3 abrí `kernel/operativo/circuitos/00-CIRCUITOS.md` (240 líneas, íntegro). **No es una de las diecinueve.** Lo digo por delante porque **refuta parcialmente** mi hallazgo nuevo más fuerte y **refuerza** dos de los hallazgos ajenos. Marco en cada punto qué conclusión descansa en él.

---

### 2 · Evidencia de lectura de las diecinueve fuentes

Las diecinueve, íntegras. Recuento verificado con `wc -l`: **8 310 líneas**, coincidente con el encargo. La tabla del documento 16 lista cinco ficheros de `entrada/` y su prosa dice «dieciocho»: cubro los **diecinueve**.

| # | ruta exacta | líneas | lectura | secciones relevantes | qué decisiones o contratos aporta | hallazgos que toca | cita de su primera sección sustantiva | cita de su última sección sustantiva |
|---|---|---|---|---|---|---|---|---|
| 1 | `kernel/operativo/circuitos/DIS-handoffs.md` | 247 | **íntegra** | grafo de cabecera · 8 bloques `ads:handoff` · «Reglas comunes» | Ocho instancias concretas: `prd-a-dis`, `dis-a-arq`, `dis-a-con`, `con-a-dis`, `dis-a-ver`, `uso-a-dis`, `inv-a-dis`, `dis-a-ent`. Cada una con sujeto, emisor, receptor, `cuando`, `entrega`, `comprueba_al_recibir`, `rechaza_si`, `devolucion`, `evidencia_de_devolucion`, `owner`, `checkpoint` | `B-2`, `G-4`, `M-9`, `ND-1`, `ND-2` | «Forma del handoff y de la devolución: `C5`. Aquí están las **instancias concretas**.» (L3-4) | «4 EL RECHAZO AL RECIBIR no cuenta como devolución a efectos del freno de a.7, porque la capa nunca se depositó. La devolución posterior sí cuenta.» (L245-246) |
| 2 | `kernel/operativo/circuitos/handoffs-generales.md` | 245 | **íntegra** | 9 bloques `ads:handoff` · «La regla que atraviesa todos estos handoffs» | Nueve instancias: `enc-a-dsp`, `prd-a-arq`, `arq-a-con`, `dom-a-con`, `seg-a-con`, `ver-a-ent`, `ent-a-uso`, `cierre-a-apr`, `con-a-ver`. Fija que **DSP crea el item** y que el emisor del handoff de cierre es DSP, no USO | `B-1`, `B-2`, `G-1`, `G-2`, `M-5`, `ND-1` | «owner: "ninguna: DSP crea el item y ENC informa después."» (`handoff:enc-a-dsp`, L28) | «EL RECEPTOR COMPRUEBA ANTES DE TOMAR CUSTODIA. Rechazar al recibir NO cuenta como devolución a efectos del freno de a.7: la capa nunca se depositó.» (L238-241) |
| 3 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | **íntegra** | dos gates · diez motivos de rechazo · «Cómo se conserva el juicio» · «Los tres procedimientos» | Promueve `pack-design-led` al kernel. Separa `gate:usabilidad` de `gate:excelencia-visual`. **Declara que `DIS/Fundacion`, `DIS/Reconstruccion` y `DIS/Evolucion` son MÉTODOS de la capacidad `DIS`, no capacidades**, y que cuál se ejecuta lo decide la escala, no el agente (L109-116) | `B-1`, `G-4`, `ND-2` | «**No buscamos interfaces usables. Buscamos productos con personalidad, actuales, expresivos y visualmente excelentes**» (L4-6) | «El equipo que lo ejecuta, con sus once roles y sus seis métodos: `capacidades/DIS/`.» (L140-141) |
| 4 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | **íntegra** | tres capas · ubicación física · **doce bloques `ads:memoria`** · regla de entrada y salida | Doce identificadores canónicos ya declarados (`memoria:vision-artistica`, `memoria:principios-visuales`, `memoria:referencias`, `memoria:sistema-visual`, `memoria:materia`, `memoria:movimiento`, `memoria:adaptacion`, `memoria:componentes`, `memoria:decisiones-de-diseno`, `memoria:areas-premium`, `memoria:deuda-de-diseno`, `memoria:historial-de-diseno`), cada uno con `autoridad`, `caducidad`, `se_actualiza_cuando`, `se_consulta_en`, `vacio_significa` y fichero físico | `G-4`, `M-9` | «KERNEL lo que es cierto en CUALQUIER producto con interfaz… No contiene un solo valor concreto: ni un color, ni una fuente, ni un número.» (L16-18) | «SALIDA ningún paquete de DIS cierra sin haber escrito en la memoria: [ ] lo decidido [ ] LO DESCARTADO Y SU PORQUÉ… Es una comprobación del gate, no un buen hábito.» (L346-351) |
| 5 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | **íntegra** | `rubrica:usabilidad` (6 ejes) · `gate:usabilidad` · `rubrica:excelencia-visual` (9 ejes) · `gate:excelencia-visual` · dos pasadas · portador de la evidencia de `CON` | Dos gates con comprobaciones enumeradas y automatizabilidad declarada. Accesibilidad y responsive tienen eje, umbral y evidencia. Resuelve `A-20` (dos pasadas) y `A-13` (quién produce la evidencia de usabilidad de una capa construida) | `G-4`, comprobación 4 | «LA RÚBRICA ORDENA EL JUICIO. NO LO SUSTITUYE. Quien la aplica sigue teniendo que mirar, y sigue respondiendo de lo que dictamina.» (L9-10) | ««genérica» no basta: «resuelve la tabla con los valores por defecto del framework y la jerarquía la crea sólo el color, que es lo que hace cualquier panel de su categoría» sí basta» (L340-342) |
| 6 | `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | 264 | **íntegra** | cinco variables · fórmulas booleanas `N4`–`N0` · qué exige cada nivel · cinco bloques `ads:nivel-novedad` · registro obligatorio | **El nivel de novedad se CALCULA, no se elige**, con cinco variables observadas sobre «el control repo y sus fuentes». `N3 = superficie_construida and not memoria_vigente`. Ningún nivel omite gate | `B-1`, `M-9`, `ND-2` | «El nivel **no se elige**: se calcula. Y para calcularlo hacen falta cinco cosas que se responden **mirando el producto —el control repo y sus fuentes— y la memoria de diseño**, no interpretando» (L12-15) | «**Bajar el nivel es la forma más silenciosa de abaratar el diseño**, y por eso el nivel se calcula con las cinco variables de arriba y se cita la condición que resultó verdadera, en vez de elegirse.» (L262-264) |
| 7 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | **íntegra** | trece estaciones · tabla de retornos · «Dónde muere el ciclo» · estaciones por nivel | Doce retornos declarados, con el destino de los nueve ejes. Declara expresamente el límite del kernel en la estación 12 (`A-26`) y que la tabla de estaciones por nivel **se deriva**, no es fuente (`A-08`) | `G-4`, comprobación 4 | «Trece estaciones. **No es una tubería**: seis de ellas pueden devolver hacia atrás, y una devolución no es un fracaso del ciclo, es el ciclo funcionando.» (L4-5) | «La reducción de estaciones **no es discrecional**: la fija la escala de novedad… Saltarse una estación fuera de lo que el nivel permite es un defecto de conformidad.» (L128-130) |
| 8 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | **íntegra** | ocho cosas que no se simplifican · artefacto de comparación · tres veredictos · cuando algo no es viable · quién puede decir qué | Cuatro formas tasadas de evidencia de imposibilidad. La deuda **se acuerda antes**, nunca a posteriori. Freno de dos devoluciones `DIS`↔`CON` con las dos posturas escritas | `A9` (patrón de escalado), comprobación 4 | «**Construcción no puede simplificar en silencio.** Si algo no es viable, devuelve con evidencia.» (L4-5) | «Sin comparación no hay eje evaluable, y sin eje evaluable el gate no cierra. Es la comprobación que impide que las estaciones 1 a 9 del ciclo hayan sido decorativas.» (L127-129) |
| 9 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | **íntegra** | siete conceptos · 29 campos de rol · `autoridad` · `independencia` · autoridad de rol vs de capacidad · qué NO puede declarar un rol | Cuatro verbos de autoridad sin quinto. **«Lo que no está en `decide` no se decide»** = autoridad silenciosa = defecto de conformidad. La autoridad de un rol es siempre subconjunto de la de su capacidad. **PROHIBIDO ser propietario global de un tipo de proceso: eso lo fija b.16, no el rol** | `M-5`, `M-6`, `G-2`, `B-2` | «CAPACIDAD qué SABE HACER el sistema. Vive en el catálogo. Permanente, no consume nada. Confundirla con equipo → equipos materializados sin cola (T12).» (L10-11) | «7 memoria_actualiza se escribe ANTES de soltar la custodia» (L160) |
| 10 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | **íntegra** | cuatro conceptos · asignación determinista · siete ejes · un agente varios roles · **relevo de agente** · 22 bloques `ads:perfil-agente` | Contrato de **continuidad entre agentes**: el rol no cambia, el entrante carga contrato+prompt+método+checkpoint, comprueba `based_on`, revalida sólo lo afectado y **no pide resumen al Owner**. `perfil:plataforma` prohíbe a `PLT` «tomar custodia de un paquete de producto». `perfil:seguridad` no admite degradación ni ocupación parcial | `G-1`, `G-2`, `m-3`, comprobación 3 | «**Un rol no es un modelo.** … Cambiar de proveedor no puede cambiar quién responde de qué.» (L3-5) | «ninguna. SIS modifica la fábrica; un error suyo se multiplica por todos los items. prohibido: … "declarar superada una prueba que sólo está escrita"» (`perfil:sistema`, L534-538) |
| 11 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | **íntegra** | 17 elementos · siete reglas · anatomía de un paso · cuándo se salta un paso | Elemento 8 `consultas` («a qué otras capacidades se pregunta, y con qué pregunta»), con regla 5: **toda consulta lleva pregunta cerrada**. Elemento 17 `prueba_de_reanudacion`, obligatoria y concreta. Un paso sólo se salta por condición falsa anotada o por rol no materializado, **y queda traza** | `B-2`, `M-5`, comprobación 3 | «Un método es lo que impide que cada agente invente su propia metodología. Si un método admite dos ejecuciones razonables con resultados distintos, no es un método: es un tema.» (L4-6) | «Un método que intentara especificar el contenido produciría trabajo mecánico y homogéneo — exactamente el resultado «correcto y sin alma» que el paso 3 de esta iniciativa existe para impedir.» (L148-150) |
| 12 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | **íntegra** | cinco obligaciones · regla del rebote infinito · **estructura del bloque `ads:handoff`** · qué NO viaja · devolución · cuándo interviene el Owner · handoff y checkpoint | La **forma**, no las instancias. Los doce campos del bloque. Cuatro campos obligatorios de toda devolución. La regla transfronteriza: un artefacto de una fuente **se entrega por referencia a su revisión** (`<source-id>@<sha>`), nunca copiándolo | `B-2` (núcleo), `G-1`, `G-2`, `ND-1` | «Un handoff no es «pasar el trabajo». Es una entrega con **cinco obligaciones**» (L7) | «El emisor NO explica su trabajo al receptor. El receptor lo entiende leyendo los artefactos y el checkpoint. Si no puede, ése es el defecto — y se corrige en el emisor, no con una reunión.» (L112-114) |
| 13 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3 343 | **íntegra** | §0–§116; en particular §6-§10 manifiesto, §20-§35 items/packages/Integration Set, §49-§51 adopción y migración, §88-§89 antiobjetivos, §97 `N1`-`N14`, §98 `I1`-`I10`, §99-§101 `CA-1`-`CA-17`, §106 `D1`-`D10`, §107 abiertas | **Mandato aprobado.** Cierra `D1`-`D10`. `SOURCES.toml` como fuente única de composición. Un item/package puede atravesar varias fuentes (`N11`). Checkpoint multi-source (`CA-12`). Integration Set (`CA-13`). `G29` sin una rama/PR global (`CA-14`). **§88 no autoriza crear ahora base de datos, lock service, daemon ni registry**. §107 deja abiertas: runtime distribuido, locks multiagente, scheduler, colas, release universal, despliegues parciales, mirrors, adapters completos | `A14`, `A12`, `G-1`, `M-3`, `ND-4` | «**Estado:** APROBADO PARA IMPLEMENTACIÓN … No es una propuesta para seguir investigando alternativas. La decisión de arquitectura descrita aquí está tomada y debe implementarse en ADS Kernel.» (cabecera y §0) | «Si mañana La Pesquerapp tiene frontend Next.js, backend Laravel, app móvil y repositorio de infraestructura, ¿puedo clonar/abrir sólo su repo ADS…? Si la respuesta no es claramente **sí**, todavía quedan cambios por implementar. **Fin de la decisión.**» (§116) |
| 14 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | **íntegra** | §1-§15; en particular §2 auditoría substractiva, §3 actualización, §4 unidad superior, §5 dossier vivo, §9 contratos compartidos, §12 **cuestión abierta crítica**, §15 tabla de estado | **NO es especificación cerrada.** Lo aceptado como *dirección* o *necesidad*: auditoría substractiva, actualización «detectar automáticamente, actualizar conscientemente», unidad superior a task/package (**nombre y contrato por diseñar**), dossier vivo, contratos compartidos, integración global, un ADS por producto. **Abierto y bloqueado: la materialización física multi-repo** | `ND-4`, comprobación 5 | «Estado: documento de trabajo del Owner. Este archivo **no es una especificación cerrada** ni autoriza a implementar automáticamente todos sus puntos.» (cabecera) | «\| materialización física multi-repo \| **ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO** \|» (§15) |
| 15 | `kernel/operativo/entrada/00-INDICE.md` | 28 | **íntegra** | índice de los cinco documentos · las tres frases del paso 1 | Fija el orden de lectura de la puerta de entrada y la regla dura: **ninguna expresión se convierte en trabajo por sí sola**; terminar sin item es un resultado correcto | `M-5`, `M-6` | «La puerta de entrada del sistema. Cinco documentos, en orden de lectura:» (L3) | «3 El Owner no tiene que saber redactar requisitos. El sistema le ayuda a descubrir lo que quiere: le enseña alternativas cuando preguntar no funciona.» (L26-27) |
| 16 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | **íntegra** | catorce estaciones · caminos hacia atrás · dónde termina cada clase · **quién es dueño de qué** · qué garantiza | **Autoridad de creación de items: pasos 10-13 son de `DSP`**, con «NINGUNA autoridad sobre el contenido del encuadre». Pasos 1-9 `ENC`; paso 9 Owner; paso 14 `ENC`. Freno de a.7 entre 7 y 8 | `M-5`, `M-6`, comprobación 6 | «Catorce estaciones. **No es una cadena rígida**: casi todas pueden devolver hacia atrás, y varias terminan legítimamente sin item.» (L4-5) | «[ ] cada paso deja checkpoint: un corte de sesión no borra lo comprendido» (L144) |
| 17 | `kernel/operativo/entrada/03-FORMAS.md` | 557 | **íntegra** | catorce bloques `ads:forma-conversacion` · «Cómo se elige la forma» | Catálogo completo de la conversación: orden clara, error evidente, comentario subjetivo, idea inmadura, feature, gap, cambio de dirección, problema de diseño, investigación, decisión, feedback, referencia anterior, «continúa», interrupción. **Todas se reconocen sobre la expresión del Owner.** Algoritmo de selección de once ramas con cláusula de cierre | `M-6` (núcleo), `A3`, comprobación 6 | «Catálogo. Contiene catorce bloques `ads:forma-conversacion`, uno por clase de expresión.» (L3) | «**El orden importa.** Se evalúa de arriba abajo y gana la primera que se cumple… si una expresión contiene dos cosas… **se parte en dos expresiones**» (cierre de «Cómo se elige la forma») |
| 18 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | **íntegra** | cinco ejes de incertidumbre · tabla de confirmación · umbral y margen de anclaje · qué hacer si el Owner no contesta | Grado global = máximo, no promedio. `alta` prohíbe formular y entregar. Tabla de confirmación derivada de a.8, con regla de cierre por materia. `UMBRAL_ANCLAJE = 0.60`, `MARGEN = 0.15`, **provisionales**. Distingue `esperando-owner` de `bloqueado`, `esperando-dependencia`, `aparcado` y `checkpoint` | `M-6`, comprobación 6 | «Se puntúa cada eje. **El grado global es el más alto de los cinco**, no el promedio: una sola incógnita grave basta para que el encuadre no esté listo.» (L12-13) | «Un encuadre puede quedarse esperando indefinidamente. Es un resultado normal del sistema.» (L187) |
| 19 | `kernel/operativo/entrada/05-ESCENARIOS.md` | 637 | **íntegra** | escenarios A-F · las cuatro salidas de la expresión subjetiva · `T75`-`T80`, `T154`-`T157` | Diez bloques `ads:escenario` con `dado/cuando/entonces/falla_si`. **Escenario C es el contrato de continuidad entre chats y agentes** (`T77`). `T155` ancla el cálculo del nivel de novedad a las cinco variables | `M-6`, `A3`, comprobación 3 y 6 | «Los tres adjetivos **son el dato**, no ruido a limpiar. `básica` sugiere ausencia de intención; `plana`, ausencia de jerarquía o profundidad; `sin alma`, ausencia de carácter.» (Escenario A, paso 2) | «falla_si: - "nace un item sobre una intención que nadie ha entendido" - "el sistema fabrica una tarea de estilos para tener algo que hacer"» (`T157`, cierre) |

---

### 3 · Método

1. Verificación de identidad del árbol (`git rev-parse`, `git status`) y del recuento de líneas (`wc -l`, total 8 310, coincidente).
2. Lectura íntegra secuencial de las diecinueve, sin `grep` dirigido y sin fragmentos, en el orden del encargo.
3. Formación de juicio propio **antes** de abrir el documento 16: inventario de las diecisiete instancias `ads:handoff` (`grep '^id: handoff'` sobre `kernel/` y `packs/`, ordenado), cruce contra las `capacidad_productora` de los diez procesos de `01-PROCESOS.md`, y lectura de §8.0-§8.4 y §15.7 de `11-ARQUITECTURA-INTEGRADA.md`.
4. Sólo entonces: lectura del documento 16 completo — dictamen A (§5), dictamen B (§5), adjudicación C (§4-§7).
5. Reconciliación hallazgo a hallazgo, con la regla de no mover severidad sin prueba citada.
6. Comprobación aritmética independiente del recuento adjudicado.

Lo que **no** hice: no ejecuté validadores, no ejecuté pruebas, no leí los esquemas `.yaml`, no leí `packs/`, no leí `(a)`, `(b)`, `E1` ni `E2` fuera de lo citado por otros.

---

### 4 · Las seis comprobaciones

#### Comprobación 1 · `C5` y el bloqueante `B-2`

Está desarrollada íntegra en la sección 5 de este dictamen, con su conclusión entre las cuatro posibles. Resumen: **`C5` no resuelve `B-2`.**

#### Comprobación 2 · `C1`, `C2` y `C3`

Repasé los nueve conceptos que el encargo nombra. Resultado, materia a materia:

- **Contrato de paquete.** Ni `C1`, ni `C2`, ni `C3` lo definen: `C1` define el contrato de **rol** (29 campos) y `C3` el de **método** (17 elementos). El contrato de paquete vive en `C4`. **Ningún hallazgo que afirmara la ausencia de un contrato de paquete puede resolverse aquí**, y ninguno lo afirmaba.
- **Transición.** `C3` regla 2 exige condición comprobable en todo paso condicional («Todo `si` va seguido de algo que se puede mirar y responder sí o no **sin criterio**»). Es el mismo patrón que los `condicionales` de `b.16` — y por eso `B-2` es un defecto real y no una laguna de estilo: la condición existe como forma, y lo que falta es que el proceso la declare.
- **Gate.** `C3` regla 6: «El método **no** cierra porque el agente considere que terminó. Cierra porque recorrió las comprobaciones del gate y anotó el resultado de cada una. Una comprobación no anotada es una comprobación no hecha.» Esto endurece `G-1` y `G-3`: un gate cuyo productor no existe no es un gate laxo, es un gate no recorrible.
- **Evidencia.** `C1` campo `salida` («capa depositada sin artefacto localizable» es el error que evita) y `C3` elemento 6 `artefactos`. Nada que cambie los hallazgos.
- **Composición.** `C1`: «El contrato fija el MÍNIMO; la composición puede exigir MÁS… Lo que **NO PUEDE** hacer ninguna composición es combinar dos roles que un contrato declara independientes.» `C2` enumera lo permitido y lo prohibido. Ninguno de los 29 hallazgos toca composición.
- **Autoridad.** Aquí sí hay efecto, y es el más importante de esta comprobación. `C1` L85-87: «**Regla dura:** lo que no está en `decide` **no se decide**. Un rol que actúa fuera de su lista de decisión comete autoridad silenciosa, que es un defecto de conformidad **aunque el resultado sea bueno**.» Y L33-34: «AUTORIDAD qué puede DECIDIR, PROPONER, VETAR o ESCALAR. Sin declararla → autoridad silenciosa: alguien decide sin poder hacerlo.» **`M-5` deja de ser una omisión editorial**: dos pasos del ciclo de auditoría de §5.3 sin actor nombrado son, por definición de `C1`, autoridad silenciosa, que `C1` clasifica como defecto de conformidad. Además `C1` L118-122 acota la corrección: «la autoridad de un rol es SIEMPRE un subconjunto de la de su capacidad», luego nombrar a `DSP` como actor de `APERTURA` no basta si su ficha no lo autoriza — que es exactamente lo que `M-5` denuncia. Y `C1` L140-142 prohíbe expresamente que un rol sea propietario global de un tipo de proceso («eso lo fija b.16, no el rol»), lo que refuerza `G-2` (§18 asigna a `ARQ` el propietario global de `M6`-`M7` a mano) y `B-1` (`proceso:AUD` declara su propietario «DERIVADO… NUNCA se asigna a mano»).
- **Estado.** Ninguno de los tres declara el estado persistido: eso es `b.2`/`b.4` y §2 de F4. Sin efecto.
- **Recuperación.** `C2` «Relevo de agente» es el contrato completo y **no lo había leído nadie**: el rol no cambia, el entrante carga contrato+prompt+método+checkpoint, comprueba `based_on`, revalida sólo la parte afectada, «continúa desde el paso exacto. NO reinicia y NO pide resumen al Owner». `C3` elemento 17 exige `prueba_de_reanudacion` concreta y prohíbe la fórmula «el método es reanudable por checkpoint». **Esto sostiene las cláusulas `REANUDACIÓN` de §8.1, §8.3 y §8.4**, y por tanto ningún hallazgo puede alegar que la reanudación entre agentes no tenga contrato: lo tiene. Lo que sí queda descubierto es el **contenido** del checkpoint que viaja entre `PLT`, `SIS` y `VER` — ver `ND-1`.
- **Cierre.** `C1` campo `gate` («cierre por criterio propio» es el error que evita) y `C3` regla 6. Sin cambio.

**Hallazgos que afirmaban la ausencia de un mecanismo que ya vive en estos contratos: ninguno.** Lo comprobé uno a uno sobre los 29. El más cercano era `B-2` («no tienen vehículo»), y el vehículo que podría haber vivido en `C3` —`consultas`, elemento 8— **existe pero no cubre el caso**: ver sección 5.

#### Comprobación 3 · Handoffs

- **Entrega entre capacidades.** Diecisiete instancias, verificadas por `grep '^id: handoff'`: `arq-a-con`, `cierre-a-apr`, `con-a-dis`, `con-a-ver`, `dis-a-arq`, `dis-a-con`, `dis-a-ent`, `dis-a-ver`, `dom-a-con`, `enc-a-dsp`, `ent-a-uso`, `inv-a-dis`, `prd-a-arq`, `prd-a-dis`, `seg-a-con`, `uso-a-dis`, `ver-a-ent`. **Ninguna otra en todo `kernel/` ni en `packs/`.**
- **Transferencia entre procesos.** No existe como objeto. Los handoffs son entre **capacidades**, y su campo `cuando` está anclado, en siete de las diecisiete, al criterio condicional del proceso: `C-DIS`, `C-ARQ`, `C-DOM`, `C-SEG`, `C-ENT`, `C-USO`, `C-APR`. Esto es la evidencia decisiva de la comprobación 1.
- **Estado persistido y reanudación.** Cada instancia declara `checkpoint:` con contenido específico («ARQ lee de DIS: nivel de novedad, direcciones descartadas y por qué, para no proponer una descartada como alternativa»). `C5` L107-109 lo generaliza: el receptor carga el checkpoint del emisor en la parte que le concierne, con `based_on` y `freshness`.
- **Receptor y condiciones de aceptación.** `comprueba_al_recibir` en las diecisiete, sin excepción.
- **Rechazo.** `rechaza_si` en las diecisiete. Y la regla que las atraviesa: rechazar al recibir **no** cuenta como devolución para el freno de a.7; aceptar y devolver después **sí**.
- **Evidencia.** `evidencia_de_devolucion` obligatorio, más los cuatro campos de `C5` L84-89 sin los cuales una devolución «se rechaza como devolución».
- **Continuidad entre agentes y chats.** Repartida en tres sedes coherentes: `C5` («El emisor NO explica su trabajo al receptor»), `C2` («Relevo de agente»), y `entrada/03-FORMAS` `forma:interrupcion` + `entrada/05` escenario C/`T77`. **Las tres dicen lo mismo y no se contradicen.** Es el tramo más sano de las diecinueve fuentes.
- **Relación con instalación, adopción, migración y actualización.** Aquí está el hueco. **Cero instancias con `PLT` o `SIS` como emisor o receptor**, y esas dos capacidades son las que cargan tres de los cuatro macrocircuitos (§8.1 `PLT`+`SIS`+`VER`; §8.3 `PLT`·`SIS`·`VER`; §8.4 `SIS`·`PLT`·`VER`). Ninguna entrega entre ellas tiene `comprueba_al_recibir`, `rechaza_si`, `evidencia_de_devolucion` ni `checkpoint` declarados.
- **Y el matiz que me obliga a rebajar mi propia conclusión.** `00-CIRCUITOS.md` —índice de `circuitos/`, que **no** es una de las diecinueve y que abrí para esta comprobación— cierra así: «Un par de capacidades sin handoff declarado **no está prohibido**: significa que su entrega se rige por las reglas comunes de `C5`. Los declarados son aquellos donde la experiencia —o el diseño— ha mostrado que hace falta precisión extra.» Eso **contradice literalmente** `C5` L36-37 («**Todo** handoff del sistema se declara con un bloque `ads:handoff`») y desactiva la lectura fuerte de mi hallazgo. Queda la lectura débil, que sigue siendo real y es `ND-1`.

**Conclusión de la comprobación 3:** el aparato de handoff es completo en su **forma** y en la continuidad entre agentes; es **incompleto en instancias precisamente sobre los pares que los cuatro macrocircuitos usan**; y contiene una contradicción entre `C5` y su propio índice sobre si declarar es obligatorio.

#### Comprobación 4 · `diseno/`

- **Sistema de diseño · UI · UX · coherencia visual.** Existen y están completos: `memoria:sistema-visual` (tipografía, color por rol, rejilla, ritmo, densidad), `memoria:componentes` (cinco estados obligatorios, patrones con clase y alcance, excepciones), y el eje `sistema` de la rúbrica con su evidencia («extracción de los valores usados y comparación contra el sistema declarado»).
- **Accesibilidad y responsive.** No son huecos: `memoria:adaptacion` los declara con autoridad (`DIS/diseno-interaccion`, con veto de la rúbrica de usabilidad); `rubrica:usabilidad` tiene eje `accesibilidad` con los tres niveles y su método; `gate:usabilidad` tiene la comprobación `accesibilidad-del-pack`; y `05-FIDELIDAD` incluye `RESPONSIVE` entre las ocho cosas que no se simplifican en silencio.
- **Documentación viva.** Doce ficheros declarados en `<proyecto>/docs/diseno/00-` a `11-`, con doce `ads:memoria` que declaran autoridad, actualización, consulta, caducidad y `vacio_significa`.
- **Auditoría.** `04-CICLO-DE-CALIDAD` «Dónde muere el ciclo si nadie lo defiende» enumera seis omisiones y ancla cinco a una comprobación de gate; la sexta (estación 12, dispositivo real) se **declara** como límite del kernel.
- **Armonización y componentes.** `memoria:componentes` + revisión de consistencia de `DIS/Evolucion` + eje `sistema`.
- **Relación con `O8` y la taxonomía documental.** Dos de las áreas condicionales que `M-1` enumera —«dirección visual» y «sistema de diseño»— **ya tienen sede canónica, identificador y autoridad** en `01-MEMORIA-DE-DISENO`. Esto afecta a `G-4` en las dos direcciones y se registra allí.
- **Relación con la adopción completa de PesquerApp.** `03-ESCALA-DE-NOVEDAD` calcula el nivel con cinco variables observadas sobre «el control repo y sus fuentes», y `N3 = superficie_construida and not memoria_vigente` es exactamente el caso de un producto con historia. La corrección `A-07` existe precisamente para que la Reconstrucción sea alcanzable en brownfield. §8.2 `A6` («reconstrucción: … UI/UX, sistema de diseño … REALES») descansa sobre esto correctamente **en la materia**, y defectuosamente en el **nombre** (ver `ND-2`).

**¿Algún hallazgo de documentación o adopción ignoró mecanismos ya existentes?** Sí, uno, y sólo parcialmente: **`G-4`**. Su premisa —«F6 tiene que inventar los doce [identificadores]»— es falsa para al menos dos de las doce áreas, que ya los tienen. No lo rebajo, porque el defecto duro que `C` confirmó sin matiz —doce contratos de aspecto sin identificador declarado en §4.3— sigue en pie; pero su alcance cambia, y aparece una mitad nueva. Detalle en la tabla de la sección 7.

`M-9` también se ve afectado, en menor grado: parte del contenido que un BASELINE de adopción debe responder en materia de diseño **ya está escrito** —las cinco variables de la escala, con su criterio de observación («no «hay código»: hay algo que alguien usa»), y los doce campos `vacio_significa` de la memoria—. La laguna de `M-9` es real, pero es menor de lo que su formulación sugiere.

#### Comprobación 5 · `docs/owner/`

Distingo, como el encargo exige, y me apoyo en los títulos y en la metadata de estado de cada documento.

**Lo APROBADO** (`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`, «Estado: APROBADO PARA IMPLEMENTACIÓN»):

- **Decisiones expresas del Owner**: `D1`-`D10` (§106). Repo ADS independiente; el control repo como fuente de verdad global; `SOURCES.toml` como manifiesto de composición; workspace de repos hermanos; identidad de fuente = remoto canónico + id estable; submodules fuera de la arquitectura base; un item/package puede abarcar varias fuentes; el estado global no se duplica por repo; Integration Set con revisiones exactas; adapters sobre un contrato de filesystem/Git.
- **Control repo, adopción permanente, documentación, estado, recuperación, Git, autoridad**: §4.2/§4.3 qué vive y qué no vive en el control repo; §18 no duplicar ADS en las fuentes; §19 documentación *code-adjacent* frente a documentación de producto; §25 Git independiente por fuente; §26 atomicidad **lógica**, no Git; §31 revisión de `G29`; §34 recuperación multi-source; §35 `based_on` por referencia; §80 «estado = ficheros del repo» reinterpretado como control repo; §81 tabla de autoridad (control repo / source repos / runtime / Integration Set).
- **Restricciones**: §64 nada de credenciales en el manifiesto; §88 **no autoriza crear ahora** servidor central, base de datos, registry, daemon, broker, cola, API cloud, servicio Git, lock service, submodule manager, tooling de monorepo; §89 no resolver por anticipado sincronización distribuida, commits atómicos multi-repo, mirrors, federación; §102 antiobjetivos.
- **Verificación de que `C5` cumple el mandato.** `C5` L67-72 implementa `N10`, `I2` y §35 al pie de la letra: «Un artefacto que vive en una fuente… se entrega por referencia a su revisión, nunca copiándolo al control repo ni a otra fuente… El handoff nombra la fuente por su `id` de `SOURCES.toml`.» Esto es una conformidad, no un defecto, y lo registro como tal.

**Lo PENDIENTE** (`ADS-IDEAS-PENDIENTES-MULTIREPO.md`, «documento de trabajo del Owner… **no es una especificación cerrada** ni autoriza a implementar automáticamente todos sus puntos»):

- Dirección o necesidad **aceptada**, contrato **por diseñar**: auditoría substractiva (§2); actualización de ADS en proyectos instalados con el principio «detectar automáticamente, actualizar conscientemente» (§3); **unidad de trabajo superior a task/package — «Nombre definitivo: pendiente»** (§4); dossier vivo (§5); FEA grande como FEA con ejecución ampliada (§6); contratos compartidos entre componentes (§9); integración como obligación global (§10).
- **Abierto y bloqueado**: la materialización física multi-repo (§12, «NO IMPLEMENTAR TODAVÍA»; §15, «ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO»).

**¿Convirtió F4 alguna propuesta pendiente en norma aprobada?** Lo comprobé en los dos casos con mayor riesgo y la respuesta es **no**:

1. La `iniciativa` de §3.3 **es** la «unidad de trabajo superior» de `IDEAS §4`, cuyo estado es «necesidad aceptada; nombre/contrato por diseñar». Diseñarla es exactamente lo que el Owner pidió; F4 no la presenta como decisión suya.
2. El **dossier vivo** de `IDEAS §5` está tratado como derivado, no como norma: §3.3.2 «VIVE EN `dosier.md`, que es DERIVADO ENTERO, con su `source_revision`… Un dosier que alguien mantiene a mano es una segunda verdad que envejece», y cita explícitamente que «`I5` y el §15 del documento de pendientes coinciden».

**Lo que sí encontré, y registro** (`ND-4`): los dos documentos de `docs/owner/` sostienen estatus **opuestos** sobre la misma cuestión —la materialización multirrepo— y **ninguno cita al otro**; no consta anotación de sustitución en ninguna parte del corpus. La metadata de autoridad que `O10` instituyó («la clasificación pasa a ser por **ubicación y metadata de autoridad**») resuelve la lectura para quien la conozca, pero el residuo permanece, y la última fila de la tabla de `IDEAS §15` sigue diciendo «NO IMPLEMENTAR» sobre lo que `C6`, `C7` y §10 ya implementan.

Y una **observación de proporcionalidad, que no elevo a hallazgo**: §88 del mandato aprobado excluye de la primera implementación «base de datos» y «lock service», y F4 introduce un `indice.sqlite` y un `.ads/run/lock`. F4 los declara **no canónicos y operacionales** (§2.2 L303, §2.7 L2277-2280), que es la salida correcta; pero no cita §88 en ningún punto, de modo que la conformidad es material y no está argumentada. Lo dejo como observación porque el hecho de que estén declarados no canónicos me impide llamarlo defecto sin forzar la lectura.

#### Comprobación 6 · `entrada/`

- **Taxonomía y clasificación.** Nueve clases (en `01-TAXONOMIA`, fuera de mi lote) y **catorce formas** de conversación con algoritmo de selección de once ramas, evaluado de arriba abajo, ganando la primera que se cumple.
- **Escenarios.** Seis recorridos + las cuatro salidas de la expresión subjetiva, todos con bloque `ads:escenario` y `falla_si`.
- **Apertura de trabajo.** Estación 10: `DSP` crea el item, después de que `ENC` haya entregado. `enc-a-dsp` lo confirma: «DSP crea el item y ENC informa después».
- **Órdenes.** `forma:orden-clara`: «no crea item. Produce un evento sobre lo que ya existe». Umbral 0.60 y margen 0.15, provisionales, con puntuación reproducible. Escenario D cubre la orden sobre base caducada.
- **Ideas, gaps, features.** `forma:idea-inmadura` → vivero, sin item. `forma:gap` y `forma:feature` con su tipo y su gate.
- **Documentación y continuidad.** `forma:interrupcion` + escenario C/`T77`: el agente nuevo carga checkpoint, comprueba `based_on`, revalida sólo lo afectado y no pide resumen al Owner. Coincide con `C2` «Relevo de agente».
- **Autoridad para crear items.** Nadie más que `DSP`, en el paso 10, y sólo tras el circuito. `ENC` no crea items. «Aparcar y desaparcar son las dos únicas transiciones exclusivas del Owner» (escenario F).
- **Auditorías autónomas.** **Aquí está el hueco, y es mayor de lo que `M-6` dice.** El aparato entero de entrada está construido sobre **un solo sujeto: el Owner**. Las catorce formas se reconocen por lo que el Owner dice; los cinco ejes de incertidumbre puntúan la expresión del Owner («sólo hay adjetivos, sin ningún caso»); la tabla de confirmación es sobre la autoridad del Owner; «Dónde termina cada clase de entrada» clasifica expresiones del Owner. **No hay ninguna forma que reconozca un *finding* de una auditoría**, y la cláusula de cierre del algoritmo de selección —«11 en otro caso → `forma:idea-inmadura`»— enviaría todo finding de `AUD` al vivero. §5.3 y §8.3 de F4 encargan a `ENC` clasificar findings «con las nueve clases de entrada»: el encargo no tiene rama. Esto **aumenta el alcance de `M-6`**.

---

### 5 · Resultado específico de `C5` frente a `B-2`

**Lo que `B-2` afirma.** Que los participantes declarados de los cuatro macrocircuitos no tienen vehículo en los condicionales del proceso que `D67` les asigna. Ejemplo canónico: `proceso:SIS` (`01-PROCESOS.md` L553-557) declara **exactamente dos** condicionales, `ENT` y `APR`; §8.1 L5090-5091 declara participantes `Owner`, `PLT`, `ENC`, `PRD`, `SIS`, `VER`, `ARQ`, `DOM`, `DIS`, `SEG`.

**Qué vehículo faltaba, exactamente.** No «un handoff». Lo que falta es **el mecanismo por el que una capacidad que no es obligatoria ni condicional del proceso deposita una capa dentro de la ruta de ese item, con traza, gate y evidencia**. En el kernel existen tres mecanismos candidatos, y sólo tres:

1. **Etapa condicional de ruta** — la capacidad figura en `condicionales` del proceso con su criterio `C-<CAP>`. Deposita capa, tiene gate, deja traza.
2. **Modo consulta** — la capacidad responde una pregunta cerrada sin tomar custodia. `DOM/CAPACIDAD.md` L53: «En modo consulta **no toma custodia**; en modo trabajo propio recibe paquete con custodia, gate y checkpoint.» Su sede formal es `C3` elemento 8 (`consultas`) con la regla 5 («Toda consulta lleva pregunta cerrada»).
3. **Otro item bajo la misma iniciativa** — §8.0 declara que cada macrocircuito «es una INICIATIVA con su plantilla de ruta. **No un proceso**», y §3.3 que la iniciativa lleva `items` como referencias. Un item distinto puede tener otro proceso, con otros condicionales.

**Qué proporciona `C5`, leído con los dos ficheros de handoffs delante.**

`C5` proporciona **la forma de la entrega, no la entrada en la ruta**. Lo dice él mismo, sin ambigüedad (L36-39):

> «Todo handoff del sistema se declara con un bloque `ads:handoff` conforme a `esquemas/handoff.yaml`. Los handoffs concretos entre capacidades viven en `circuitos/`, no aquí: **C5 define la forma, no las instancias.**»

Su contenido, punto por punto, contra lo que `B-2` necesita:

| lo que `B-2` necesita | qué da `C5` |
|---|---|
| **sujeto** | el paquete y sus artefactos: «Viaja un ARTEFACTO y su evidencia; el trabajo lo compone DSP» (L59) |
| **emisor** | campo `de:` — una capacidad **ya presente en la ruta** |
| **receptor** | campo `a:` — ídem |
| **contenido** | `entrega:` — artefactos concretos, localizables; nunca copia de contexto ni de contenido de una fuente |
| **persistencia** | `checkpoint:` — qué del checkpoint del emisor debe poder leer el receptor |
| **reanudación** | obligación 5: «QUÉ CHECKPOINT SOBREVIVE: el receptor debe poder reanudar sin hablar con el emisor» (L14) |
| **evidencia** | `evidencia_de_devolucion:` más los cuatro campos obligatorios de toda devolución (L84-89) |
| **gate** | **ninguno.** «UN HANDOFF NO ES UN PUNTO DE APROBACIÓN. Entre dos equipos no hay un humano validando el traspaso.» (L101-102) |
| **autoridad** | `owner:` — «Casi nunca… Interviene sólo cuando la entrega contiene una decisión de su autoridad —tabla de a.8— o cuando la devolución escala por el freno de a.7» (L96-98) |

**Su relación con los cuatro macrocircuitos, comprobada instancia a instancia.** Aquí está el resultado decisivo, y va en contra de la esperanza que `C` expresó al cerrar §7 del documento 16:

1. **Siete de las diecisiete instancias anclan su `cuando` al criterio condicional del proceso.** `prd-a-dis`: «el item cumple **C-DIS**». `dis-a-arq`: «el item cumple **C-ARQ**». `dom-a-con`: «el item cumple **C-DOM**». `seg-a-con`: «el item cumple **C-SEG**». `ver-a-ent`: «el item cumple **C-ENT**». `ent-a-uso`: «el item cumple **C-USO**». `cierre-a-apr`: «el item es un INC, o hay una revisión de circuito o una promoción». Es decir: **el handoff se dispara porque la capacidad ya está en la ruta; no es lo que la mete en ella.** En un item de `proceso:SIS`, `C-DIS`, `C-ARQ`, `C-DOM` y `C-SEG` nunca se evalúan, porque el proceso no los declara. Las instancias **confirman el mecanismo que `B-2` denuncia**; no lo suplen.
2. **Ninguna de las diecisiete tiene a `SIS` o a `PLT` como emisor o receptor.** Verificado por enumeración completa de ids sobre `kernel/` y `packs/`. Las tres capacidades que cargan tres de los cuatro macrocircuitos —`SIS`, `PLT`, `VER`— sólo aparecen en una instancia entre ellas: `con-a-ver`.
3. **La ruta de `proceso:SIS` que sí está declarada tampoco está cubierta.** Sus obligatorias son `SIS` → `CON` → `VER`. Existe `con-a-ver`; **no existe `sis-a-con`**. Lo mismo ocurre con `PRD → CON` en `FEA` y `GAP` (no existe `prd-a-con`), con `ENT → ARQ` en `INC`, y con toda la cadena de `DIR`.
4. **La cláusula de escape.** `00-CIRCUITOS.md` —índice de `circuitos/`, no una de las diecinueve— declara que «un par de capacidades sin handoff declarado **no está prohibido**: significa que su entrega se rige por las reglas comunes de `C5`». Esto contradice el «Todo handoff… se declara» de `C5` L36, y hace que los puntos 2 y 3 **no** sean por sí solos un defecto de conformidad. Lo digo aunque debilite mi propia posición.

**Y el vehículo alternativo, comprobado capacidad a capacidad.** La vía de consulta existe, pero está acotada por origen en cuatro de las seis capacidades que `B-2` nombra:

- `DIS/CAPACIDAD.md` L33: «una consulta en modo consulta **desde ENC, PRD, ARQ o USO**» — `SIS` no figura.
- `PRD/CAPACIDAD.md` L20: «**desde DIS, ARQ o ENC**» — `SIS` no figura.
- `ARQ/CAPACIDAD.md` L20: «**desde PRD, DIS o ENC**» — `SIS` no figura.
- `ENC/CAPACIDAD.md` L35-38: cuatro entradas, todas ancladas al Owner — `ENC` no es consultable en absoluto.
- `DOM/CAPACIDAD.md` L17 y `SEG/CAPACIDAD.md` L53: **no acotan el origen** → vehículo plausible. Es el matiz que `C` ya había verificado, y lo confirmo.
- **Y añado una séptima capacidad que ninguno de los tres revisó**: `PLT`. §8.1 la declara participante de `N0`, `N2` y `N6`; no es obligatoria ni condicional de `proceso:SIS`; su `entrada` (`PLT/CAPACIDAD.md` L16-19) admite «una consulta sobre **disponibilidad de entornos o dispositivos**» y nada más; y `C2` `perfil:plataforma` le prohíbe «tomar custodia de un paquete de producto». `PLT` no tiene vehículo para `N0`/`N2`/`N6` por ninguna de las tres vías.

Y aún queda un vehículo que `B-2` nombra como salida posible sin explorarlo: **partir el macrocircuito en más items**. Existe soporte: §8.0 dice que el macrocircuito es una iniciativa y no un proceso; §3.3 le da `items` como referencias; y §8.1 declara expresamente que la iniciativa «**no** nace con el conjunto de items vacío, **nace con uno**» —`SIS-001`—, lo que implica que puede acumular más. **El mecanismo existe. Lo que no existe es la declaración de que sea ése**, ni fase a fase ni macrocircuito a macrocircuito. Que es exactamente lo que `B-2` pide en su «qué exigiría cerrarlo».

**CONCLUSIÓN — la de las cuatro posibles:**

> ## `C5` **NO RESUELVE** `B-2`.

`C5` define la forma de una entrega **entre capacidades que ya están en la ruta**. No es un mecanismo de activación, no es un gate, y él mismo declara que no contiene las instancias. Las diecisiete instancias que sí existen **corroboran el diagnóstico de `B-2`**, porque siete de ellas condicionan su disparo al criterio `C-<CAP>` que el proceso debe declarar y que `proceso:SIS` no declara para ninguna de las capacidades en cuestión. La lectura del corpus completo de handoffs no encuentra el vehículo; encuentra la confirmación de que hace falta uno.

**Y `B-2` no estaba mal planteado.** Lo compruebo contra las cuatro opciones: no está mal planteado (el hueco es real y ahora tiene una segunda sede independiente), no se resuelve completamente, no se resuelve parcialmente por `C5` —lo que se resuelve parcialmente, para `DOM` y `SEG`, se resuelve por sus fichas de capacidad, no por `C5`—. Queda: **no lo resuelve**.

**Además, `B-2` gana evidencia.** `00-CIRCUITOS.md`, que es el documento que convierte las diez rutas de `b.16` en recorridos concretos, dibuja así el circuito `SIS`:

> «SIS ──► CON ──► VER ──► [ENT OBLIGATORIO si modifica el runtime] ──► [APR si C-APR]»

Ni `ENC`, ni `PRD`, ni `ARQ`, ni `DOM`, ni `DIS`, ni `SEG`, ni `PLT`. Es una **segunda sede vigente e independiente** del mismo hueco, que ningún revisor citó, y hace todavía menos sostenible la hipótesis de que el vehículo estuviera escondido en algún sitio.

**No he inventado ningún artefacto nuevo.** Apliqué `C5` primero, luego `C3`, luego las fichas de capacidad, luego `00-CIRCUITOS.md`. Ninguno lo cierra.

---

### 6 · Estado de los hallazgos tras el nivel 0

**Nota previa sobre el conjunto.** La tabla de adjudicación del documento 16 (§4) tiene **33 filas**. El encargo habla de «29 hallazgos adjudicados (4 bloqueantes, 6 graves, 13 medios, 6 menores)», que es el recuento que el propio adjudicador escribe al pie de su tabla. **Ese recuento no cuadra con la tabla que resume**, y lo demuestro en `ND-5`. Para no perder ninguno, doy estado a **las 33** y marco cuáles quedan fuera del recuento de 29.

| id | severidad adjudicada | **estado tras el nivel 0** | qué cambia, y por qué |
|---|---|---|---|
| `A1` | BLOQUEANTE | **confirmado sin cambios** | Ninguna de las diecinueve toca §3.6 ni el contrato de `evento`. Fuera de mi cobertura material |
| `A2` | BLOQUEANTE | **confirmado sin cambios** | Ídem. El predicado de transacción abierta no vive en ninguna de las diecinueve |
| `B-1` | BLOQUEANTE | **confirmado con alcance distinto** | Confirmado, y **su rama de resolución (a) deja de estar abierta**: `00-CIRCUITOS.md` da el criterio escrito para elegir entre `INV` y `AUD` — «Auditoría de conformidad de la propia organización: es un item **SIS**, no un AUD: su objeto es **la fábrica, no el producto**». El objeto de `A2`/`A3` es el producto → `AUD`. **Pero la misma rama importa un defecto nuevo**: la lista de condicionales de `proceso:AUD` que `B-1` cita contiene `DIS/Reconstruccion`, que no es una capacidad (ver `ND-2`). Severidad intacta |
| `B-2` | BLOQUEANTE (con matiz) | **confirmado, y aumentado en alcance** | El vehículo **no está en `C5`** (sección 5). Se añaden: (i) segunda sede independiente del hueco, el grafo `SIS` de `00-CIRCUITOS.md`; (ii) una **séptima capacidad sin vehículo por ninguna de las tres vías, `PLT`**, que `B-2` cita en su primera cita pero omite en su análisis y cuya vía de consulta está acotada a «disponibilidad de entornos o dispositivos»; (iii) confirmación de que siete de las diecisiete instancias de handoff anclan su disparo al criterio condicional del proceso, luego el handoff presupone la ruta y no la crea. **No cambio la severidad: sigue siendo bloqueante** |
| `A3` | GRAVE | **confirmado con alcance distinto** | Confirmado. Se añade **una sede vigente más que ningún revisor listó**: `entrada/03-FORMAS.md` `forma:continua` describe «Continúa» como «la función Estado de DSP… reconstruye, verifica, consume órdenes, selecciona y reporta» — **sin ninguna de las dos ramas transaccionales**. Es la sede que usa el catálogo de entrada del Owner, y tendrá que reanclarse junto a §7.4 y §16 L6876. Severidad intacta |
| `A4` | GRAVE | **confirmado sin cambios** | Trazabilidad de `D64`-`D68`; fuera de la materia de las diecinueve |
| `G-1` | GRAVE | **confirmado sin cambios (evidencia reforzada)** | `C2` `perfil:seguridad`, `degradacion_permitida`: «**ninguna**. Un veto duro no admite ocupación degradada: si no hay modelo que cumpla, **el paquete queda bloqueado** y se dice qué falta.» Segunda sede independiente de que la obligación de `SEG` no admite sustituto ni ocupación parcial. Y `perfil:plataforma`, `prohibido`: «tomar custodia de un paquete de producto». Refuerza; no altera severidad ni alcance |
| `G-2` | GRAVE | **confirmado sin cambios (evidencia reforzada)** | Dos sedes nuevas: `C2` L436 («PLT tiene backlog propio», segunda sede de lo que `B` tomó de `PLT/CAPACIDAD.md` L4) y `C1` L140-142 («PROHIBIDO ser propietario global de un tipo de proceso del kernel → eso lo fija b.16, no el rol»), que convierte la asignación manual de `ARQ` como propietario global en defecto de contrato y no sólo en incoherencia entre sedes |
| `G-3` | GRAVE | **confirmado sin cambios** | Ninguna de las diecinueve produce baseline ni clasificación de desconocidos críticos para la instalación |
| `G-4` | GRAVE | **confirmado, y aumentado** | Su premisa se **reduce** en un punto y el hallazgo **crece** en otro. Reduce: `01-MEMORIA-DE-DISENO.md` ya declara **doce identificadores canónicos** (`memoria:<slug>`) con autoridad, caducidad y fichero, de modo que para «dirección visual» y «sistema de diseño» F6 no parte de cero. Crece: precisamente por eso, declarar `contrato-de-aspecto:documental/direccion-visual` y `…/sistema-de-diseno` sin reconciliarlos con los `ads:memoria` existentes **crea una segunda sede editable sobre la misma materia**, que es `I5`; §4.3 no aplica ahí la disciplina de los dos relojes que §5.7 sí aplica a `responsables`. Severidad intacta |
| `A5` | MEDIO (rebajado de grave por C) | **confirmado sin cambios** | Fuera de la materia de las diecinueve |
| `A6` | MEDIO | **confirmado sin cambios** | Ídem |
| `A7` | MEDIO | **confirmado sin cambios** | Ídem. `C1` y `C2` distinguen rol, agente y autoridad pero no tocan los cinco conceptos de `a.9` |
| `A8` | MEDIO | **confirmado sin cambios** | Ídem |
| `A9` | MEDIO | **confirmado sin cambios** | Ídem. Nota: `C5` L96-98 y `diseno/05-FIDELIDAD` paso 5 dan el **patrón** que su remedio necesita —escalar con las dos posturas escritas, autoridad nombrada— pero ninguno de los dos cubre el desenlace 4b. No es cambio de estado |
| `A10` | MEDIO | **confirmado sin cambios** | Ídem |
| `A13` | MEDIO (subido de menor por C) | **confirmado sin cambios** | Segunda sede de `A7`. `C` lo mantuvo separado; lo respeto |
| `M-1` | MEDIO | **confirmado sin cambios** | Recuento de trece frente a catorce; ninguna de las diecinueve es la fuente enumerada |
| `M-2` | MEDIO | **confirmado sin cambios** | §1.3 no está en mi lote |
| `M-3` | MEDIO | **confirmado sin cambios** | El mandato del Owner no fija el gate de una actualización; §107 deja abierta la «estrategia universal de release». Nada que cambie |
| `M-4` | MEDIO | **confirmado sin cambios** | Registro de decisiones; fuera de mi lote |
| `M-5` | MEDIO | **confirmado con alcance distinto, y aumentado** | Deja de ser una omisión de redacción. `C1` L33-34 y L85-87: un actor no nombrado que decide es **autoridad silenciosa**, «un defecto de conformidad **aunque el resultado sea bueno**». `entrada/02-CIRCUITO` fija que la creación de items es de `DSP` en el paso 10 y sólo tras el circuito, y `handoff:enc-a-dsp` lo repite. `C1` L118-122 acota además la corrección: nombrar a `DSP` no basta si su ficha no lo autoriza — que es la segunda mitad de lo que `M-5` pide. **No muevo la severidad**: sostener MEDIO→GRAVE exigiría demostrar que la apertura ocurre hoy, y no está construida |
| `M-6` | MEDIO | **confirmado con alcance distinto, y aumentado** | `M-6` lo formula como una asimetría de registro (cuatro extensiones de ficha registradas, la quinta no). Con `03-FORMAS`, `02-CIRCUITO` y `04-INCERTIDUMBRE` leídos, el defecto es mayor: **el aparato entero de entrada está construido sobre un único sujeto, el Owner**, y no tiene rama para un finding. Las catorce formas se reconocen sobre «la expresión»; los cinco ejes puntúan la expresión; la tabla de confirmación es sobre la autoridad del Owner. Y la cláusula de cierre del algoritmo —«11 en otro caso → `forma:idea-inmadura`»— **mandaría todo finding de `AUD` al vivero**. Añadir una línea a `ENC/CAPACIDAD.md` no cierra esto. Severidad intacta; el «qué lo cerraría» de `M-6` es insuficiente tal como está escrito |
| `M-7` | MEDIO | **confirmado sin cambios** | Ninguna de las diecinueve trata los frenos de a.7 salvo el freno de dos devoluciones (`C5`, `diseno/05`), que no es el FRENO 3 |
| `M-8` | MEDIO | **confirmado, y aumentado** | La colisión de espacio de nombres que `M-8` registra para `R1`-`R9`/`R1`-`R8` **se repite con `N<n>`**: `C6` L29-42 declara los principios normativos `N1`-`N14` —procedentes de `…APROBADA` §97 y citados como tales por `C5-HANDOFF.md` («una **FUENTE** de `SOURCES.toml`… (C6 **N5**)»)— mientras §8.1 usa `N0`-`N7` para las fases de instalación y, en el mismo apartado, `N-5` y `N-6` como identificadores de hallazgo. El remedio de `M-8` («renombrar el conjunto») debe cubrir los dos espacios |
| `M-9` | MEDIO | **confirmado con alcance distinto** | Confirmado, con el alcance **reducido en una fracción**: para la materia de diseño, el contenido que un baseline de adopción debe establecer **ya está escrito y es comprobable** — las cinco variables de `03-ESCALA-DE-NOVEDAD` con su criterio de observación («no «hay código»: hay algo que alguien usa»; «Una memoria que describe una pantalla que ya no existe no es vigente») y los doce campos `vacio_significa` de `01-MEMORIA-DE-DISENO`. Lo que sigue sin declarar es el resto de las catorce preguntas. Severidad intacta |
| `A11` | MENOR | **absorbido por otro (`M-8`)** | El propio adjudicador lo resolvió así: «ambos ciertos, y el hallazgo unificado es el de `B`, que es estrictamente más completo». Lo registro como absorbido, no como confirmado independiente |
| `A12` | MENOR | **confirmado sin cambios** | El mandato del Owner §25/§26/§30 respalda que lo que serializa `main` es Git por fuente, no un lock; y §88 excluye un «lock service». Coherente con `A12`; no lo altera |
| `m-1` | MENOR | **confirmado sin cambios** | Fuera de mi lote |
| `m-2` | MENOR | **confirmado sin cambios** | Ídem |
| `m-3` | MENOR (confirmado como hecho; el juicio, no asumido) | **confirmado con alcance distinto** | Aparece una **tercera sede, y es de herramienta, no de misión**: `C2` `perfil:plataforma`, `herramientas`: «[configuración de CI, gestión de entornos, **observabilidad**, aislamiento de agentes]»; frente a `perfil:operacion` (ENT): «[despliegue, **lectura de logs y métricas**, ejecución de smoke tests, reversión]». `PLT` **construye** la observabilidad, `ENT` **lee** sus salidas. Refuerza la lectura de `B` sin resolverla: el aspecto sigue pudiendo juzgarlo quien opera. **Mantengo la posición de `C`: no lo asumo como defecto** |
| `m-4` | MENOR (inferencia rechazada por C) | **confirmado sin cambios** | Fuera de mi lote |
| `A14` | *fuera del recuento de 29 según `C`* | **confirmado con alcance distinto** | `C` lo excluyó como «no defecto de F4», y en eso tiene razón. **Pero su procedencia ya no es un hueco**: el mandato aprobado del Owner §6.2 elige TOML precisamente porque «Python moderno puede leerlo mediante biblioteca estándar (`tomllib`)» y «evita introducir PyYAML u otra dependencia sólo para interpretar el manifiesto», y §36 exige usar «sólo Python stdlib y Git CLI». **El suelo de Python 3.11 es consecuencia directa de una decisión aprobada del Owner**, no un descuido. Lo que falta —declarar `python_requires` y comprobar la versión antes de que el fallo suba a la capa de certificación— es implementación, con la solución determinada. Clasificación: **limitación aceptada con procedencia aprobada**, no defecto de F4 |

**Recuento de mi tabla:** 4 bloqueantes · 6 graves · 16 medios · 6 menores · 1 absorbido (`A11`) · 1 fuera del conjunto de defectos de F4 (`A14`) = **33 filas**.

---

### 7 · Hallazgos nuevos

Registro sólo lo demostrado por las diecinueve fuentes (más, donde lo declaro, `00-CIRCUITOS.md`), que afecte materialmente a `F4` y que no duplique los 29.

---

**`ND-1` · `C5` exige declarar todo handoff y su propio índice dice lo contrario; y ninguna instancia cubre a `PLT` ni a `SIS`, que cargan tres de los cuatro macrocircuitos — MEDIO**

*Clasificación:* **defecto preexistente del kernel** (la contradicción) **más defecto de `F4`** (certificar `C5` sin excepción nombrada).

`C5-HANDOFF.md` **L36-37**:

> «**Todo** handoff del sistema se declara con un bloque `ads:handoff` conforme a `esquemas/handoff.yaml`.»

`kernel/operativo/circuitos/00-CIRCUITOS.md`, párrafo de cierre:

> «Un par de capacidades sin handoff declarado **no está prohibido**: significa que su entrega se rige por las reglas comunes de `C5`. Los declarados son aquellos donde la experiencia —o el diseño— ha mostrado que hace falta precisión extra.»

Las dos frases no pueden leerse literalmente a la vez. **Y la elección entre ellas tiene consecuencia material para `F4`**, no sólo editorial: la quinta obligación de `C5` es «QUÉ CHECKPOINT SOBREVIVE: el receptor debe poder reanudar sin hablar con el emisor», y **el contenido de ese checkpoint es precisamente lo que cada instancia declara** en su campo `checkpoint:` («ARQ lee de DIS: nivel de novedad, direcciones descartadas y por qué…», «CON lee de DOM: qué consultas debe ejecutar y guardar como evidencia»). Bajo las «reglas comunes» solas, **qué debe poder leer el receptor no está declarado**.

Enumeración completa de las diecisiete instancias (`grep '^id: handoff'` sobre `kernel/` y `packs/`): **`PLT` y `SIS` no aparecen en ninguna**, ni como emisor ni como receptor. Y §8.1, §8.3 y §8.4 declaran sus `REANUDACIÓN` sobre entregas entre exactamente esas capacidades. Además, dentro de la propia ruta declarada de `proceso:SIS` —`SIS` → `CON` → `VER`— existe `con-a-ver` y **no existe `sis-a-con`**; el mismo patrón se repite en `PRD → CON` (`FEA`, `GAP`), `ENT → ARQ` (`INC`) y toda la cadena de `DIR`.

**La mitad que es defecto de `F4`:** §15.7 del entregable declara «`C5` handoff | **REUTILIZADO**», sin más. En la misma tabla, `C6` es «REUTILIZADO CON EXCEPCIÓN NOMBRADA, y su defecto REGISTRADO» y `C7` es «REUTILIZADO CON UNA CORRECCIÓN PENDIENTE, NOMBRADA». **F4 aplicó a `C6` y `C7` la disciplina de nombrar el defecto del derivado que invoca, y no la aplicó a `C5`**, invocándolo sobre pares para los que no hay instancia y sobre una cláusula de reanudación cuyo contenido depende de esas instancias. Es la misma asimetría que `M-6` denuncia para las extensiones de ficha, sobre otro objeto.

*Qué exigiría cerrarlo:* decidir cuál de las dos frases manda —`C5` L36 o el cierre de `00-CIRCUITOS.md`—; y, en cualquiera de los dos casos, declarar qué checkpoint viaja entre `PLT`, `SIS` y `VER` en los cuatro macrocircuitos, o registrar en §15.7 la excepción con la misma disciplina con que se registraron las de `C6` y `C7`.

---

**`ND-2` · `proceso:AUD` declara como capacidad condicional `DIS/Reconstruccion`, que es un método; al fijarlo, preselecciona el nivel de novedad que la escala obliga a calcular — MEDIO**

*Clasificación:* **defecto preexistente del kernel, propagado por `F4`**.

`kernel/operativo/recorrido/01-PROCESOS.md` **L433-434** (`proceso:AUD`, `condicionales`):

> ```
>   - capacidad: "DIS/Reconstruccion"
>     condicion: "C-DIS"
> ```

`kernel/operativo/circuitos/00-CIRCUITOS.md`, grafo `AUD`: «├─► [DIS/Reconstruccion si C-DIS]».

`kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` **L109-116**:

> «DIS/Fundacion … DIS/Reconstruccion … DIS/Evolucion … Cuál se ejecuta **lo decide la escala de novedad, no el criterio del agente**. Los tres son **métodos de la capacidad `DIS`** y viven, como todos los métodos del sistema, en `capacidades/DIS/metodos/`.»

`kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` **L12** y **L46-50**:

> «El nivel **no se elige**: se calcula.»
> «N4 FUNDACIÓN `dir_sustituye or (not superficie_construida and not memoria_vigente)` · N3 RECONSTRUCCIÓN `superficie_construida and not memoria_vigente` …»

**Dos defectos, uno de forma y otro material.**

*De forma:* `DIS/Reconstruccion` **no es una de las quince capacidades**. La nota al pie de §18 del propio entregable (L7003-7005) declara que «confundir el nombre de un proceso con el de una capacidad es el mismo modo de fallo que `G1` corrigió con `a.9`». Aquí se confunde el nombre de un **método** con el de una capacidad, en el campo `capacidad:` de un bloque normativo del kernel, y §8.2 L5209 lo repite literalmente («A6 activa DOM, SEG, **DIS/Reconstruccion** y PRD»).

*Material:* al fijar el método en el condicional, `proceso:AUD` **preselecciona el nivel de novedad**. Si en una adopción `dir_sustituye` es cierto —un item `DIR` aprobado sustituye expresamente la dirección anterior—, la escala da **N4, Fundación**, y el proceso obliga a Reconstrucción. `03-ESCALA-DE-NOVEDAD` cierra advirtiendo exactamente contra esto: «**Bajar el nivel es la forma más silenciosa de abaratar el diseño**».

*Por qué afecta materialmente a `F4`:* §8.2 es el macrocircuito de la adopción, y `O15` declara que la adopción de PesquerApp es **permanente y completa**. La fase `A6` reconstruye «UI/UX, sistema de diseño… REALES» con un método preseleccionado por el proceso en vez de calculado por la escala, y la justificación de §8.2 se apoya literalmente en esa lista.

*Qué exigiría cerrarlo:* sustituir `DIS/Reconstruccion` por `DIS` en el condicional de `proceso:AUD` y en el grafo de `00-CIRCUITOS.md`, dejando que la escala calcule el método; y corregir §8.2 L5209 en consecuencia. La condición `C-DIS` ya es la correcta y no cambia.

---

**`ND-3` · Colisión de espacio de nombres `N<n>` entre los principios normativos del mandato del Owner y las fases del macrocircuito de instalación — MENOR**

*Clasificación:* **problema editorial.**

`kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` L29-42 declara `N1`-`N14`, los catorce principios normativos que `…APROBADA` §97 fija. `C5-HANDOFF.md` L76 los cita como identificador: «una **FUENTE** de `SOURCES.toml`, que es un repositorio del producto (**C6 N5**)». §8.1 del entregable usa `N0`-`N7` para las ocho fases de la instalación, y **en el mismo bloque** usa `N-5` y `N-6` como identificadores de hallazgo. Tres significados de `N<n>` conviviendo, uno de ellos a cuatro líneas del otro.

Es exactamente la clase de defecto que `M-8` registra para `R1`-`R9` frente a `R1`-`R8`, y el remedio debería cubrir ambos espacios de una vez.

---

**`ND-4` · `docs/owner/` sostiene dos estatus opuestos sobre la materialización multirrepo, sin anotación de sustitución — MENOR**

*Clasificación:* **problema editorial**, mitigado por `O10`.

`ADS-IDEAS-PENDIENTES-MULTIREPO.md` §12: «**CUESTIÓN ABIERTA CRÍTICA — Materialización del proyecto multi-repo. NO IMPLEMENTAR TODAVÍA.**» §15, última fila: «materialización física multi-repo | **ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO**».

`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`, cabecera: «**Estado:** APROBADO PARA IMPLEMENTACIÓN»; §0: «No es una propuesta para seguir investigando alternativas. La decisión… está tomada y debe implementarse en ADS Kernel.»

Ninguno cita al otro. No consta anotación de sustitución en `docs/owner/`, ni en `DECISIONES-Y-CONTRADICCIONES.md`, ni en el entregable. La resolución `O10` («la clasificación pasa a ser por **ubicación y metadata de autoridad**») resuelve la lectura para quien conozca la regla, y por eso lo califico de MENOR y no de más; pero el residuo es real, y un lector que recorra `docs/owner/` en orden alfabético lee primero «APROBADO PARA IMPLEMENTACIÓN» y después «NO IMPLEMENTAR SIN DISEÑO PREVIO» sobre la misma materia.

---

**`ND-5` · El recuento de la propia adjudicación no cuadra con la tabla que resume: son 32 hallazgos y 16 medios, no 29 y 13 — MENOR (defecto del gate, no de `F4`)**

*Clasificación:* **problema editorial**, y lo registro pese a no ser defecto de `F4` porque la lista de condiciones para `F5` se construye sobre esa cifra.

Derivación, sobre la tabla de §4 del documento 16 (33 filas, enumeradas: `A1`-`A14`, `B-1`, `B-2`, `G-1`-`G-4`, `M-1`-`M-9`, `m-1`-`m-4`):

```
bloqueantes  A1 · A2 · B-1 · B-2                                   = 4    ✓ coincide
graves       A3 · A4 · G-1 · G-2 · G-3 · G-4                       = 6    ✓ coincide
             (A5 sale, rebajado a MEDIO por el propio adjudicador)
medios       A5 · A6 · A7 · A8 · A9 · A10 · A13                    = 7
             M-1 · M-2 · M-3 · M-4 · M-5 · M-6 · M-7 · M-8 · M-9   = 9
                                                            total  = 16   ✗ declara 13
menores      A11 · A12 · m-1 · m-2 · m-3 · m-4                     = 6    ✓ coincide
             (A13 sale, subido a MEDIO; A14 sale, «no es defecto de F4»)
TOTAL de defectos adjudicados                                      = 32   ✗ declara 29
```

El adjudicador escribe «13 MEDIOS confirmados (contando `A5` y `A13` reclasificados a MEDIO por mí)», pero su propia reclasificación **suma** dos a los catorce que ya había (`A6`-`A10` más `M-1`-`M-9`), dando dieciséis. La discrepancia es de tres en los medios y de tres en el total.

Es la misma clase de defecto que el gate confirma cuatro veces en el entregable —`A6` (seis fases frente a cinco), `A10` (ocho puntos frente a diez), `M-1` (catorce frente a trece), `m-1` (ocho frente a diez)—, cometida esta vez por el gate sobre sí mismo. Ninguno de los 32 hallazgos se pierde por ello, pero **la condición de entrada a `F5` está redactada sobre una cifra que su propia tabla desmiente**.

---

**Observación adyacente, que NO registro como hallazgo.** Al contrastar `B-2` encontré que `proceso:SIS` declara `condicion_de_entrada`: «Una fricción real, un incidente del sistema o **una capacidad de producto bloqueada** lo exigen», y su obligatoria `cambio-de-sistema` exige que «el item enlaza el problema real, la fricción o la capacidad de producto que justifica su existencia. **Sin ese enlace no se trabaja**» —repetido en `00-CIRCUITOS.md` y en `SIS/CAPACIDAD.md`—. El disparador de §8.1 es «el Owner quiere gobernar un producto **que todavía no existe**», donde no hay capacidad de producto que enlazar. **No lo registro** porque su demostración descansa en `01-PROCESOS.md` y `SIS/CAPACIDAD.md`, que no están entre mis diecinueve fuentes; lo dejo anotado para quien tenga ese lote.

---

### 8 · Limitaciones de mi revisión

1. **No leí `§2` ni `§3` del entregable.** Todo el bloque `A1`-`A10`, `A12`, `A13` —protocolo transaccional, contrato de `evento`, identidad, sellado— queda **fuera de mi cobertura material**. Su estado «confirmado sin cambios» significa que **las diecinueve fuentes no lo tocan**, no que yo lo haya verificado.
2. **No leí `01-TAXONOMIA.md`.** Es el primero de los cinco de `entrada/` y no está en mi lote. Mis conclusiones sobre `M-6` descansan en los otros cuatro y en la cita que `B` hace de él; el algoritmo de selección de forma que uso está en `03-FORMAS`, que sí leí íntegro.
3. **Abrí un fichero fuera de las diecinueve.** `00-CIRCUITOS.md` (240 líneas). Lo declaro en cada punto donde una conclusión depende de él: la cláusula de escape de `ND-1`, la segunda sede de `B-2`, el criterio `AUD`/`SIS` de `B-1`, y el grafo `AUD` de `ND-2`.
4. **No ejecuté nada.** Ni validadores, ni pruebas, ni `workspace check`. `A14` lo evalúo por procedencia documental, no reproduciendo el fallo.
5. **No leí los esquemas `.yaml`.** En particular `esquemas/handoff.yaml`, que `C5` invoca. Si ese esquema declara campos que las instancias omiten, no lo sé.
6. **No leí `packs/`.** `rubrica:usabilidad` y `gate:excelencia-visual` delegan en el pack instalado (matriz de entornos, criterios de accesibilidad exigibles, presupuestos de respuesta). Mi comprobación 4 se detiene en la frontera del kernel.
7. **De `…APROBADA` (3 343 líneas) leí el cien por cien, pero la contrasté selectivamente.** Comprobé la traza de `CA-10`/`CA-11`/§100 en §15.7 y la ausencia de traza de `CA-12`-`CA-14`; **no verifiqué uno a uno los diecisiete criterios de aceptación ni los diez invariantes** contra el entregable. Consideré registrar la falta de traza como hallazgo y **decidí no hacerlo**: §15.7 sí cita `CA-10`, `CA-11` y §100, y §15.2 traza el apartado 8 de la directiva a «§10 · `C6` · `C7`». La laguna existe pero es parcial, y no la sostengo con la fuerza necesaria.
8. **No consulté al Revisor E**, ni sé qué ha encontrado. Si coincidimos, es convergencia; si diferimos, no he arbitrado nada.
9. **`m-3` sigue siendo un juicio.** Aporté una sede más y no lo resolví, como no lo resolvió `C`.

---

### 9 · Qué cambia y qué no tras esta cobertura

**No emito veredicto de suficiencia.** La arquitectura no se ha corregido: los cuatro bloqueantes siguen en pie, los seis graves siguen en pie, y ninguna de las diecinueve fuentes retira ni uno solo de ellos. Emitir un veredicto ahora sería confundir haber cerrado una laguna de lectura con haber cerrado un defecto.

**Qué cambia:**

1. **La pregunta de `B-2` está contestada, y la respuesta es que no.** `C5` no contiene el vehículo. El corpus de handoffs, leído íntegro, **confirma el mecanismo que `B-2` denuncia** —siete de diecisiete instancias disparan sobre el criterio condicional que el proceso debe declarar— y añade una segunda sede independiente del hueco y una séptima capacidad afectada, `PLT`. La esperanza que el adjudicador dejó escrita al cerrar su §7 —«`C5-HANDOFF.md` y `handoffs-generales.md` son precisamente donde podría vivir el vehículo que `B` no encontró»— **queda cerrada en negativo**. Ya nadie tiene que volver a mirar ahí.
2. **`B-1` pierde una de sus dos ramas abiertas.** El criterio para elegir entre `INV` y `AUD` está escrito en `00-CIRCUITOS.md` («su objeto es la fábrica, no el producto»), y apunta a `AUD`. Lo que queda abierto es el propietario global derivado y —nuevo— el error de categoría que esa rama importa.
3. **Cuatro hallazgos crecen en alcance con prueba citada, sin que ninguno cambie de severidad:** `M-6` (el aparato de entrada no tiene sujeto distinto del Owner, y su cláusula de cierre manda los findings al vivero), `M-5` (autoridad silenciosa, por la definición literal de `C1`), `M-8` (la colisión de espacios de nombres se repite con `N<n>`), `G-4` (la mitad reducida y la mitad nueva).
4. **Tres hallazgos ganan sede o evidencia sin cambiar:** `A3` (una sexta sede, `forma:continua`), `G-1` y `G-2` (segundas sedes en `C2` y `C1`).
5. **`A14` deja de ser un cabo suelto:** su procedencia es una decisión aprobada del Owner (§6.2 y §36 del mandato), y su remedio está determinado.
6. **Aparecen cinco hallazgos nuevos**, dos de ellos con efecto material sobre `F4` (`ND-1`, `ND-2`) y tres editoriales (`ND-3`, `ND-4`, `ND-5`).
7. **El recuento del gate no cuadra:** son **32** hallazgos adjudicados y **16** medios, no 29 y 13.
8. **Se cierra la laguna de cobertura por la parte que me tocaba.** Las diecinueve fuentes están leídas íntegras, con cita comprobable de su primera y su última sección sustantiva. Lo que ninguna de ellas contiene, ya se sabe que no contiene.

**Qué no cambia:**

- Los cuatro bloqueantes: `A1`, `A2`, `B-1`, `B-2`. Ninguno retirado, ninguno rebajado.
- Los seis graves: `A3`, `A4`, `G-1`, `G-2`, `G-3`, `G-4`. Ninguno retirado, ninguno rebajado.
- **Ni una sola severidad movida en ninguna dirección.** No encontré prueba que lo justificara, y no la fabriqué.
- La condición estructural del encargo del gate —que el corpus obligatorio se cubra íntegro— sigue **sin cumplirse por completo**: quedan sin abrir `01-TAXONOMIA.md`, dieciocho de los diecinueve esquemas `.yaml`, `packs/` más allá de cabeceras, los validadores línea a línea, `tooling/tests/test_workspace.py`, y §11 y §14 del entregable. Mi lote cubre diecinueve fuentes; no cubre las demás.
- Y sobre todo: **ningún defecto se ha corregido**. Lo único que ha ocurrido es que ahora se sabe, con cita, qué dicen diecinueve documentos que nadie había abierto — y que ninguno de ellos absuelve a `F4c`.

---

## DICTAMEN DEL REVISOR E

## 1 · Identidad, procedencia y modo

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          redesign/kernel-2.0
HEAD          7c7856ccb88ea3851fb5e1fc1ec04af38d03ab96   (git rev-parse, verificado)
ÁRBOL         limpio (git status --porcelain → 0 líneas)
MODO          SÓLO LECTURA. No he modificado ningún fichero, no he hecho commits ni
              ninguna escritura de git. Mi única escritura ha sido en el scratchpad.
```

**Qué NO soy.** No escribí `F4`, ni `F4b`, ni `F4c`. No apliqué `D16`–`D70` ni redacté `O1`–`O16`. **No soy el REVISOR A ni el REVISOR B ni el ADJUDICADOR C**: no participé en el gate y no he leído sus dictámenes como verdad, sino como objeto. **No he consultado al REVISOR D, no sé qué ha leído ni qué concluye, y nada de lo que sigue supone su contenido.** No emito veredicto de suficiencia: el encargo me lo prohíbe expresamente y además la arquitectura no se ha corregido.

**Qué he tratado como objeto y no como fuente.** `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` y `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`. Cada cita que uso de ellos la he abierto en su fichero y su línea. Todo recuento que declaro lo he derivado yo.

**Un dato de anclaje que importa.** El gate se emitió sobre `a713590`. `git merge-base --is-ancestor a713590 HEAD` → cierto, y `git diff --stat a713590 HEAD` toca **seis ficheros**: `docs/evolucion/00-INDICE.md`, `16-GATE-…md`, `CHECKPOINT-ADS-NEXT.md` y tres `.txt` de evidencia. **Ninguna de las diecinueve fuentes ni `11-ARQUITECTURA-INTEGRADA.md` ha cambiado** entre el árbol que leyeron A, B y C y el que he leído yo. Mi lectura es directamente comparable con la suya, y la afirmación del doc 16 —«NINGÚN hallazgo se ha corregido en esta pasada»— es **verificable y cierta**.

---

## 2 · Evidencia de lectura de las diecinueve fuentes

Declaro, fuente por fuente, **lectura íntegra, de la primera a la última línea, por `cat`/`sed` sobre el fichero completo, no por `grep` ni por fragmentos**. Los recuentos de línea son los de `wc -l` ejecutado por mí; suman **8 310**, que coincide exactamente con el total del encargo.

### 2.1 · Cobertura, aportación y hallazgos afectados

| # | ruta exacta | líneas | lectura | secciones relevantes | qué decisiones o contratos aporta | hallazgos del doc 16 a los que afecta |
|---|---|---|---|---|---|---|
| 1 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | **161** | **ÍNTEGRA** | los siete conceptos · 29 campos de rol · `autoridad` (cuatro verbos) · `independencia` · autoridad rol⊂capacidad · qué NO puede declarar un rol | separa CAPACIDAD·EQUIPO·ROL·AGENTE·MÉTODO·HERRAMIENTAS·AUTORIDAD; prohíbe que un rol sea propietario global de un proceso; fija que autoridad de rol ⊆ autoridad de capacidad | `B-1` · `B-2` · `M-5` · `M-6` · **nuevo E-3** |
| 2 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | **539** | **ÍNTEGRA** | cuatro conceptos · asignación determinista (6 pasos) · siete ejes · combinaciones prohibidas · **relevo de agente** · 21 bloques `ads:perfil-agente` | portabilidad K0.8; relevo de agente como norma con `based_on`/`freshness`; `perfil:sistema` y `perfil:plataforma` | `m-3` (refuerzo) · continuidad entre chats · **ningún bloqueante** |
| 3 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | **150** | **ÍNTEGRA** | 17 elementos · siete reglas · anatomía de paso · cuándo se salta un paso | `consultas` como campo declarado del método (pregunta cerrada); `prueba_de_reanudacion` obligatoria; el gate es lista recorrida entera | `B-2` (vía consulta) · `M-5` · continuidad |
| 4 | `kernel/operativo/contratos/C5-HANDOFF.md` | **115** | **ÍNTEGRA** | cinco obligaciones · regla del rebote · estructura `ads:handoff` · qué NO viaja · devolución · Owner · checkpoint | **la forma del handoff, no las instancias**; custodia; devolución con cuatro campos; enlaces no copias; frontera de repositorio | **`B-2` (comprobación 1)** · `G-1` · `G-2` · `A11`/`M-8` |
| 5 | `kernel/operativo/circuitos/DIS-handoffs.md` | **247** | **ÍNTEGRA** | ocho instancias `ads:handoff` de DIS · cuatro reglas comunes | instancias `prd-a-dis`, `dis-a-arq`, `dis-a-con`, `con-a-dis`, `dis-a-ver`, `uso-a-dis`, `inv-a-dis`, `dis-a-ent` | **`B-2`** · `G-4` · **nuevo E-5** |
| 6 | `kernel/operativo/circuitos/handoffs-generales.md` | **245** | **ÍNTEGRA** | nueve instancias `ads:handoff` · regla común | `enc-a-dsp`, `prd-a-arq`, `arq-a-con`, `dom-a-con`, **`seg-a-con`**, `ver-a-ent`, `ent-a-uso`, `cierre-a-apr`, `con-a-ver` | **`G-1` (prueba directa)** · **`G-2`** · **`B-2`** · `M-5` |
| 7 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | **3 343** | **ÍNTEGRA** | §§0–116 completos; en especial §31 (G29) · §49–§51 (adopción/migración) · §55 ENT · §97 `N1`–`N14` · §98 `I1`–`I10` · §106 `D1`–`D10` · §107 abiertas | **norma aprobada**: control repo, `SOURCES.toml`, siblings, Integration Set, item multi-fuente, provider-neutral | `B-1` · `G-1` · `M-3` · `M-4` · **nuevo E-1** · **nuevo E-6** |
| 8 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | **597** | **ÍNTEGRA** | §2 auditoría substractiva · §3 actualización ADS · §4 unidad amplia · §5 dosier vivo · §12 **cuestión abierta** · §15 estado de las ideas | **NO es norma**: «necesidad aceptada», «por diseñar», «ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO» | `M-3` · `M-7` · `M-9` · **nuevo E-7** |
| 9 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | **141** | **ÍNTEGRA** | dos gates · diez motivos de rechazo · juicio en un rol · referencias · **los tres procedimientos** | la excelencia visual es requisito de kernel; `DIS/Fundacion|Reconstruccion|Evolucion` los elige la escala, no el agente | **nuevo E-2** · `B-1` |
| 10 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | **352** | **ÍNTEGRA** | tres capas · ubicación física · **doce bloques `ads:memoria`** · regla de entrada y salida | doce secciones con `autoridad`, `caducidad`, `fichero`, `vacio_significa` — el mecanismo del que §4.3 dice derivar el mapa documental | **`G-4` (alcance)** · `M-2` · `O8` |
| 11 | `kernel/operativo/diseno/02-RUBRICAS.md` | **343** | **ÍNTEGRA** | `rubrica:usabilidad` (6 ejes) · `rubrica:excelencia-visual` (9 ejes) · dos gates · **las dos pasadas** · portador de la evidencia de CON | el gate visual se evalúa en DOS pasadas: ocho ejes en la 9, `fidelidad` en la 11 | **nuevo E-5** · `m-3` |
| 12 | `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | **264** | **ÍNTEGRA** | cinco variables · cálculo booleano `N4`–`N0` · qué exige cada nivel · cinco bloques `ads:nivel-novedad` · registro obligatorio | **el nivel se calcula, no se elige**; los dos gates son obligatorios en los cinco niveles | **nuevo E-2** · `B-1` · `M-9` |
| 13 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | **130** | **ÍNTEGRA** | trece estaciones · doce retornos · dónde muere el ciclo · estaciones por nivel | los nueve ejes tienen destino de retorno; la estación 12 se declara **fuera del alcance del kernel** | `m-3` · **nuevo E-5** |
| 14 | `kernel/operativo/diseno/05-FIDELIDAD.md` | **129** | **ÍNTEGRA** | ocho cosas · artefacto de comparación · tres veredictos · cuando no es viable · quién puede decir qué | la deuda se acuerda ANTES; cuatro formas de evidencia de imposibilidad; freno de a.7 entre DIS y CON | `G-4` · **nuevo E-5** |
| 15 | `kernel/operativo/entrada/00-INDICE.md` | **28** | **ÍNTEGRA** | índice de cinco documentos · las tres frases | la literal se conserva; ninguna expresión crea trabajo por sí sola | `M-6` · `M-5` |
| 16 | `kernel/operativo/entrada/02-CIRCUITO.md` | **145** | **ÍNTEGRA** | catorce estaciones · diez retornos · dónde termina cada clase · **quién es dueño de qué** | pasos 1–9 ENC, 9 Owner, **10–13 DSP**, 14 ENC; DSP sin autoridad de contenido | **`M-5`** · `M-6` · `B-2` |
| 17 | `kernel/operativo/entrada/03-FORMAS.md` | **557** | **ÍNTEGRA** | catorce bloques `ads:forma-conversacion` · cómo se elige la forma | el **modo consulta** declarado forma a forma (DIS, ARQ, INV, VER, «la capacidad propietaria») | **`B-2`** · **`M-6`** · **nuevo E-8** |
| 18 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | **187** | **ÍNTEGRA** | cinco ejes · desenlaces · tabla de confirmación · umbral y margen · Owner que no contesta | `grado_inicial` persiste y **activa la crítica para siempre**; umbral 0.60 / margen 0.15 PROVISIONALES | **nuevo E-4** · `M-9` |
| 19 | `kernel/operativo/entrada/05-ESCENARIOS.md` | **637** | **ÍNTEGRA** | escenarios A–F · `T75`–`T80` · `T154`–`T157` | el recorrido de referencia completo; las cuatro salidas de la expresión subjetiva | **nuevo E-4** · **nuevo E-9** · `M-6` |
| | **TOTAL** | **8 310** | | | | |

> **Vigésima fuente, leída y declarada aparte.** `kernel/operativo/entrada/01-TAXONOMIA.md` (**309 líneas**, leída íntegra hasta su novena clase). No está en las diecinueve del encargo, pero la sección 7 del doc 16 la declara cubierta sólo en «dos bloques `ads:entrada` de nueve» y `M-6` depende de ella. La leí para no juzgar `M-6` sobre la misma cobertura parcial que el gate. **Cita:** L5–6 *«Entre lo que dice y lo que el sistema fabrica hay **nueve cosas distintas**»*; L20–22 *«NINGUNA CLASE DE ENTRADA CREA TRABAJO POR SÍ MISMA salvo las tres que lo declaran»*.

### 2.2 · Cita comprobable de la primera y de la última sección sustantiva de cada fuente

| # | primera sección sustantiva | última sección sustantiva |
|---|---|---|
| 1 | **C1 L10** *(«Los siete conceptos»)*: «`CAPACIDAD  qué SABE HACER el sistema. Vive en el catálogo. Permanente, no consume nada.`» | **C1 L160** *(«Cómo se lee un contrato de rol»)*: «`7  memoria_actualiza  se escribe ANTES de soltar la custodia`» |
| 2 | **C2 L10** *(«Los cuatro conceptos»)*: «`ROL  responsabilidad declarada. Vive en el kernel o en un pack. Permanente.`» | **C2 L537** *(`perfil:sistema`)*: «`- "declarar superada una prueba que sólo está escrita"`» |
| 3 | **C3 L4–5**: «Un método es lo que impide que cada agente invente su propia metodología. Si un método admite dos ejecuciones razonables con resultados distintos, no es un método: es un tema.» | **C3 L144–145**: «`EL MÉTODO DICE  explora tres direcciones distintas entre sí, y prueba que lo son` / `EL MÉTODO NO DICE  cuáles. Eso es el trabajo`» |
| 4 | **C5 L10**: «`1  QUIÉN ENTREGA QUÉ  artefactos concretos, localizables, no «el trabajo hecho»`» | **C5 L112–114**: «`El emisor NO explica su trabajo al receptor. El receptor lo entiende leyendo los artefactos y el checkpoint. Si no puede, ése es el defecto`» |
| 5 | **DIS-handoffs L22** (`handoff:prd-a-dis`): «`cuando: "el item cumple C-DIS y PRD ha depositado su capa de intención y criterio de éxito"`» | **DIS-handoffs L245–246**: «`4  EL RECHAZO AL RECIBIR no cuenta como devolución a efectos del freno de a.7, porque la capa nunca se depositó.`» |
| 6 | **handoffs-generales L7–10** (`handoff:enc-a-dsp`): «`de: ENC / a: DSP / cuando: "un encuadre alcanza el estado listo-para-dsp y pasa su gate"`» | **handoffs-generales L238**: «`EL RECEPTOR COMPRUEBA ANTES DE TOMAR CUSTODIA.`» |
| 7 | **APROBADA L36–44** (§1.1): «`PRODUCTO != REPOSITORIO GIT`» y «`ADS PROJECT != REPOSITORIO DE CÓDIGO`» | **APROBADA L3337–3339** (§116): «Si mañana La Pesquerapp tiene frontend Next.js, backend Laravel, app móvil y repositorio de infraestructura, ¿puedo clonar/abrir sólo su repo ADS, reconstruir el workspace, pedir una feature transversal…?» |
| 8 | **IDEAS L3–7**: «Estado: documento de trabajo del Owner. Este archivo **no es una especificación cerrada** ni autoriza a implementar automáticamente todos sus puntos.» | **IDEAS L597** (§15, última fila): «`| materialización física multi-repo | **ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO** |`» |
| 9 | **diseno/00 L4–6**: «**No buscamos interfaces usables. Buscamos productos con personalidad, actuales, expresivos y visualmente excelentes**» | **diseno/00 L114–116**: «Cuál se ejecuta lo decide la [escala de novedad](../../kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md), **no el criterio del agente**.» |
| 10 | **diseno/01 L16–18**: «`KERNEL  lo que es cierto en CUALQUIER producto con interfaz… No contiene un solo valor concreto`» | **diseno/01 L346–351**: «`SALIDA  ningún paquete de DIS cierra sin haber escrito en la memoria: [ ] lo decidido [ ] LO DESCARTADO Y SU PORQUÉ`» |
| 11 | **diseno/02 L9–10**: «`LA RÚBRICA ORDENA EL JUICIO. NO LO SUSTITUYE.`» | **diseno/02 L338–342**: «`[ ] en los ejes no automatizables, LA RAZÓN del nivel, en una frase que otro pueda discutir`» |
| 12 | **diseno/03 L4–5**: «`C-DIS` (b.16) decide **si** Diseño se activa. Esta escala decide **qué método ejecuta y cuánto explora**.» | **diseno/03 L262–264**: «**Bajar el nivel es la forma más silenciosa de abaratar el diseño**, y por eso el nivel se calcula con las cinco variables de arriba… en vez de elegirse.» |
| 13 | **diseno/04 L4–5**: «Trece estaciones. **No es una tubería**: seis de ellas pueden devolver hacia atrás» | **diseno/04 L128–130**: «La reducción de estaciones **no es discrecional**: la fija la escala de novedad… Saltarse una estación fuera de lo que el nivel permite es un defecto de conformidad.» |
| 14 | **diseno/05 L4–6**: «**Construcción no puede simplificar en silencio.** Si algo no es viable, devuelve con evidencia.» | **diseno/05 L127–129**: «`gate:excelencia-visual` comprueba el eje `fidelidad` **a través de este artefacto**. Sin comparación no hay eje evaluable, y sin eje evaluable el gate no cierra.» |
| 15 | **entrada/00 L7**: «`01-TAXONOMIA.md` — las nueve clases de expresión, y por qué la mayoría no produce trabajo» | **entrada/00 L26–28**: «El Owner no tiene que saber redactar requisitos. El sistema le ayuda a descubrir lo que quiere: le enseña alternativas cuando preguntar no funciona.» |
| 16 | **entrada/02 L4–5**: «Catorce estaciones. **No es una cadena rígida**: casi todas pueden devolver hacia atrás, y varias terminan legítimamente sin item.» | **entrada/02 L138–145** («Qué garantiza este circuito»): «`[ ] cada paso deja checkpoint: un corte de sesión no borra lo comprendido`» |
| 17 | **entrada/03 L14–16** (`forma:orden-clara`): «`reconoce_por: - "el objetivo es un item o paquete que ya existe"`» | **entrada/03 L554–557**: «**El orden importa.** Se evalúa de arriba abajo y gana la primera que se cumple… si una expresión contiene dos cosas… **se parte en dos expresiones**.» |
| 18 | **entrada/04 L11–12**: «**El grado global es el más alto de los cinco**, no el promedio: una sola incógnita grave basta para que el encuadre no esté listo.» | **entrada/04 L186–187**: «Un encuadre puede quedarse esperando indefinidamente. Es un resultado normal del sistema.» |
| 19 | **entrada/05 L4–6**: «No son ilustraciones: son las pruebas T75 a T84, y su estado real está en `../pruebas/REGISTRO-generado.md`.» | **entrada/05 L629–637** (`T157`): «`falla_si: - "nace un item sobre una intención que nadie ha entendido" - "el sistema fabrica una tarea de estilos para tener algo que hacer"`» |

---

## 3 · Método

1. Anclar `HEAD`, comprobar árbol limpio y **derivar** que ninguna de las 19 fuentes cambió entre `a713590` (árbol del gate) y `HEAD`.
2. Extraer del doc 16 §4 los hallazgos adjudicados **contando yo las filas**, sin fiarme del recuento declarado.
3. Leer las diecinueve íntegras, en orden: contratos → circuitos → diseño → entrada → Owner. `cat -n` / `sed -n '1,$p'` sobre el fichero completo.
4. Para cada hallazgo del doc 16, preguntarme **una sola cosa**: *¿alguna de estas diecinueve contiene el mecanismo cuya ausencia el hallazgo afirma, o cambia el sujeto sobre el que se afirma?* Sin prueba citada, el hallazgo se confirma sin cambios.
5. Recuentos derivados por mí: instancias `ads:handoff` (`grep -c '^id: handoff:'` → 8 + 9 = **17**), condicionales de `proceso:SIS` y `proceso:AUD` (lectura literal de `01-PROCESOS.md` L505–564 y L415–445), áreas condicionales de §4.3 (recuento a mano → **13**), vocabulario del campo `capacidad` de los condicionales, bloques `ads:memoria` (**12**), niveles `ads:nivel-novedad` (**5**), formas `ads:forma-conversacion` (**14**), clases `ads:entrada` (**9**), perfiles `ads:perfil-agente` (**21**).
6. Comprobar contra esquema donde el esquema existe: `esquemas/handoff.yaml`, `esquemas/memoria.yaml`, `esquemas/proceso.yaml`.
7. Ninguna escritura. `registrar_evidencia.py` y todo validador con efecto de escritura, no ejecutados.

---

## 4 · Las seis comprobaciones obligatorias

### COMPROBACIÓN 1 · `C5-HANDOFF.md` frente al bloqueante `B-2`

Su resultado completo está en la sección 5, que el encargo pide aparte. Aquí queda su lugar en el orden.

---

### COMPROBACIÓN 2 · `C1`, `C2` y `C3`

**Qué cubren, materia a materia:**

| materia | quién la fija en estos tres contratos | ¿resuelve algún hallazgo? |
|---|---|---|
| **contrato de paquete** | ninguno. `C1` fija el contrato de **rol** (29 campos); `C3`, el de **método** (19 campos). El paquete es de `b.2`/`a.1` | **no** |
| **transición** | `C3` regla 1 (`termina_cuando` por paso) y regla 2 (condición comprobable). `C1` campo `activacion`/`retirada` del rol | no las de `§2.6` |
| **gate** | `C3` regla 6: «El método **no** cierra porque el agente considere que terminó… Una comprobación no anotada es una comprobación no hecha» (L91–93). `C1` campo `gate` | refuerza `M-5` y `G-1`: un gate no se satisface por criterio |
| **evidencia** | `C1` `criterios_calidad`; `C3` `artefactos` y `critica` | no |
| **composición** | `C1` L106–110: «**El contrato fija el MÍNIMO; la composición puede exigir MÁS**… lo que **NO PUEDE** hacer ninguna composición es combinar dos roles que un contrato declara independientes». `C2` L70–78, seis reglas | no |
| **autoridad** | `C1` L118–122: «**la autoridad de un rol es SIEMPRE un subconjunto de la de su capacidad**». `C1` L141–142: «`PROHIBIDO  ser propietario global de un tipo de proceso del kernel → eso lo fija b.16, no el rol`» | **`B-1`**: cierra una salida. El `propietario_global` derivado de `proceso:AUD` **no puede** resolverse creando un rol que lo asuma |
| **estado** | `C1` `checkpoint`; `C2` relevo (L88–95); `C3` `checkpoints` | continuidad, no `§2` |
| **recuperación** | `C2` L88–95 y `C3` elemento 17 `prueba_de_reanudacion`, con `R03` como regla del validador | **positivo**, ver abajo |
| **cierre** | `C3` regla 6; `C1` `salida` + `gate` + `memoria_actualiza` | no |

**Revisión expresa de «hallazgos que afirmaron una ausencia que ya vivía aquí».** Los revisé uno a uno. **Encontré un mecanismo real y no encontré ningún hallazgo anulado por él:**

- **`consultas` de `C3`** (elemento 8, L24; regla 5, L78–85: «Toda consulta lleva pregunta cerrada») es un **vehículo declarado** para que una capacidad pregunte a otra dentro de un método. **No resuelve `B-2`**: una consulta produce una respuesta, no una **capa depositada**; el receptor no toma custodia; y el propio `C3` la separa de `salida` y de `devolucion`. Además está acotada por el campo `consulta` de la ficha receptora, que es exactamente donde el adjudicador ya comprobó que `SIS` no figura para `DIS`, `PRD`, `ARQ` ni `ENC`.
- **`veto` de `C1`** (L81: «`veta: puede DETENER algo en su materia. Exige contrato de veto de a.5`») es un vehículo por el que `DIS`, `DOM`, `SEG` y `VER` alcanzan cualquier item **para detenerlo**. **No cubre producir**: `§8.1` declara a `DIS`, `DOM` y `SEG` participantes «según discovery», y descubrir no es vetar.
- **Recuperación:** `C2` «Relevo de agente» + `C3` `prueba_de_reanudacion` + `C5` «Handoff y checkpoint» + `forma:interrupcion` + `T77` cubren **completamente** la exigencia del Owner en `APROBADA` §113 («no es aceptable que *el backend sabía X sólo porque estaba en otro chat*»). Lo digo porque `§8.4` presenta su `REANUDACIÓN` como aportación de `G5`, y el mecanismo de método y de handoff **ya existía**. No es defecto; es cobertura que el gate no vio.

**Conclusión de la comprobación 2.** `C1`, `C2` y `C3` **no anulan ni reducen ningún hallazgo de los 32**. `C1` **cierra una vía de escape de `B-1`** (el `propietario_global` no se arregla con un rol). Y los tres, leídos juntos con `01-PROCESOS.md`, hacen visible un defecto que ninguno de los tres revisores registró y que consigno como nuevo (**E-3**).

---

### COMPROBACIÓN 3 · Los dos ficheros de handoffs

**Recuento derivado por mí:** `grep -c '^id: handoff:'` → `DIS-handoffs.md` **8**, `handoffs-generales.md` **9**, `00-CIRCUITOS.md` **0**. **Diecisiete instancias en total.**

| pregunta del encargo | qué encontré |
|---|---|
| **entrega entre capacidades** | Sí, y sólo entre capacidades: `esquemas/handoff.yaml` declara `de: {tipo: ref, ref_a: capacidad}` y `a: {tipo: ref, ref_a: capacidad}`. **Un handoff no puede tener por sujeto un proceso, una fase, un macrocircuito ni al Owner.** |
| **transferencia entre procesos** | **NO EXISTE.** Ningún handoff nombra un proceso. El esquema no tiene campo para ello. |
| **estado persistido** | `checkpoint` es campo **obligatorio** del esquema y las 17 instancias lo declaran, siempre en la forma «X lee de Y: …, para …». |
| **receptor** | El campo `a`, y **el receptor comprueba antes de tomar custodia** (`C5` L20, DIS-handoffs L238, handoffs-generales L238). |
| **condiciones de aceptación** | `comprueba_al_recibir`, obligatorio, mínimo un elemento. Todas las instancias lo cumplen. |
| **rechazo** | `rechaza_si`, obligatorio. Y la distinción capital: rechazar al recibir **no gasta** una de las dos devoluciones de `a.7`; aceptar y devolver después, sí. |
| **reanudación** | Vía `checkpoint` + `C5` L107–109 («Si `based_on` cambió, revalida **sólo la parte afectada**»), coherente con `C2` paso 4 del relevo. |
| **evidencia** | `evidencia_de_devolucion`, obligatorio, y `C5` L81–92 impone **cuatro campos** a toda devolución, so pena de que «se rechaza como devolución… no contaba para el freno». |
| **continuidad entre agentes y chats** | Cubierta, y por tres piezas independientes que concuerdan: `C2` relevo, `C3` `prueba_de_reanudacion`, `C5` checkpoint. |
| **relación con instalación, adopción, migración y actualización** | **NINGUNA. Cero.** `grep -i 'adopción\|adopcion\|pesquerapp'` sobre los dos ficheros de handoffs, los seis de `diseno/` y los cinco de `entrada/` y sobre `C1`, `C2`, `C3`, `C5`: **salida vacía**. |

**El hueco estructural, derivado.** De las quince capacidades, las diecisiete instancias cubren trece: `PRD ARQ CON DOM SEG VER ENT USO INV ENC DSP APR DIS`. **`SIS` y `PLT` no aparecen ni una sola vez, ni como `de` ni como `a`.** Y `SIS` y `PLT` son exactamente el propietario global y el ejecutor de los cuatro macrocircuitos (`§18` L6990–L6999, `§8.1` L5090, `§8.4` L5440). Lo registro como nuevo hallazgo (**E-5**), porque es una ausencia de instancia, no una discrepancia de texto, y porque **agrava `B-2` en vez de cerrarlo**.

**Y una prueba directa de `G-1` que nadie tenía.** `handoffs-generales.md` **L107**:

> `cuando: "el item cumple C-SEG, y siempre en items DEP antes de construir"`

El handoff `seg-a-con` declara, en el propio catálogo del kernel, que **en todo item `DEP` `SEG` entrega a `CON` antes de construir**. `U5b` es `proceso:DEP` (`§18` L6999) y sus participantes son «`ENT`, `VER`» (`§18`) y «`SIS · PLT · VER · Owner`» (`§8.4` L5440). El handoff obligatorio de `DEP` **no tiene ni emisor ni receptor entre los participantes declarados**. `G-1` deja de apoyarse sólo en `01-PROCESOS.md` y `G28`: lo confirma también el catálogo de handoffs.

**Conclusión de la comprobación 3.** El aparato de handoffs es **coherente, completo en forma y con esquema**; y es **estructuralmente incapaz** de ser el vehículo que `B-2` echa en falta, porque su sujeto son capacidades y su disparador presupone la activación, no la produce.

---

### COMPROBACIÓN 4 · `diseno/`

| pregunta | qué fija `diseno/` |
|---|---|
| **sistema de diseño** | `memoria:sistema-visual` + `memoria:componentes` (`01-MEMORIA` L131–153 y L223–243), autoridad `DIS/sistema-de-diseno` |
| **UI · UX** | `rubrica:usabilidad` (6 ejes) y `rubrica:excelencia-visual` (9 ejes), con umbral, `juicio_humano` y `no_automatizable` declarados |
| **coherencia visual** | eje `sistema`; motivo de rechazo 5 «INCONSISTENTE»; `gate:excelencia-visual · memoria-actualizada` |
| **documentación viva** | doce bloques `ads:memoria`, capa `profile`, en `<proyecto>/docs/diseno/00-…11-…` |
| **auditoría** | `gate:excelencia-visual` (12 comprobaciones) y `gate:usabilidad` (6), con `automatizable: si|parcial|no` por comprobación |
| **accesibilidad** | eje `accesibilidad` de usabilidad + `memoria:adaptacion`; el criterio exigible **lo pone el pack**, no el kernel |
| **responsive** | `memoria:adaptacion` («puntos de adaptación reales del producto, derivados del contenido, no de dispositivos de moda») y punto 7 de `05-FIDELIDAD` |
| **componentes** | `memoria:componentes`, con los **cinco estados obligatorios** |
| **armonización** | `03-ESCALA` reglas de reutilización de ejes por nivel; `05-FIDELIDAD` los tres veredictos |

**Relación con `O8` y la taxonomía documental.** Es la parte que cambia algo. `§4.3` **L4147–4149** declara que el área 1 «se regenera **desde los bloques `ads:memoria`** de los documentos gobernados y desde las celdas de `cobertura`». Los **únicos** doce bloques `ads:memoria` que existen en el kernel son los de `diseno/01-MEMORIA-DE-DISENO.md`, y `esquemas/memoria.yaml` hace obligatorios exactamente `id · nombre · capacidad · capa · fichero · autoridad · contiene · se_actualiza_cuando · se_consulta_en · caducidad · vacio_significa` — es decir, **las cuatro cosas que `§4.3` dice que el mapa documental necesita** («qué documentos existen, cuál cubre cada área, quién responde de cada uno y cuál es su vigencia»), más tres. Esto **no anula `G-4`** —doce áreas siguen sin identificador declarado— pero **cambia su alcance**: el patrón de identidad, responsable y caducidad **ya existe, con esquema y con doce ejemplares trabajados**, y la prescripción del doc 16 («declarar los doce identificadores») debe reutilizarlo en vez de inventar una convención nueva.

**¿Algún hallazgo de documentación o adopción ignoró un mecanismo ya existente?** Sí, uno, y en la otra dirección: **`§8.2` ignora `03-ESCALA-DE-NOVEDAD`**. `§8.2` L5208–5210 fija que «`A6` activa DOM, SEG, **DIS/Reconstruccion** y PRD». `diseno/00` L114–116 dice: «Cuál se ejecuta lo decide la escala de novedad, **no el criterio del agente**», y `03-ESCALA` L46–50 lo formaliza: `DIS/Reconstruccion` es el método de `N3`, cuya condición es `superficie_construida and not memoria_vigente`. Un producto con historia **que sí tenga memoria vigente** computa `N0`, `N1` o `N2` —nunca `N3`—, y uno cuya dirección un `DIR` sustituya computa `N4`. **`§8.2` predetermina un nivel que la escala declara calculado y no elegible.** Es un hallazgo nuevo (**E-2**) y ninguno de los tres revisores podía verlo sin `diseno/`.

**Relación con la adopción completa de PesquerApp.** **Ninguna, y es un dato.** Los seis ficheros de `diseno/` no mencionan adopción, migración, instalación ni PesquerApp. `DIS/Reconstruccion` —el procedimiento que `§8.2` convoca en `A6` para reconstruir «UI/UX, sistema de diseño… REALES»— está definido en `diseno/` **sin ninguna referencia a que se ejecute dentro de un macrocircuito de adopción**, y `03-ESCALA` lo describe como un cálculo por item, no por producto. `O14`/`O15` quedan intactos: no encontré en `diseno/` nada que autorice ni que impida la adopción permanente.

---

### COMPROBACIÓN 5 · `docs/owner/`

**La diferencia de autoridad, primero, porque el encargo la subraya.**

| | `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | `ADS-IDEAS-PENDIENTES-MULTIREPO.md` |
|---|---|---|
| declaración propia | **L3:** «**Estado:** APROBADO PARA IMPLEMENTACIÓN» · **L14:** «No es una propuesta para seguir investigando alternativas. La decisión… está tomada y debe implementarse» | **L3–7:** «Estado: documento de trabajo del Owner. Este archivo **no es una especificación cerrada** ni autoriza a implementar automáticamente todos sus puntos» |
| qué cierra | §106 `D1`–`D10` **expresamente cerradas** | §15: «necesidad aceptada», «por diseñar», «dirección preferida» |
| qué deja abierto | §107: runtime distribuido, locks multi-agente, scheduler, colas, servicio cloud, release universal, despliegues parciales, mirrors, adapters completos | §12 entero: **«CUESTIÓN ABIERTA CRÍTICA… NO IMPLEMENTAR TODAVÍA»**, con 29 preguntas |

**No he convertido ninguna propuesta en norma.** Y verifiqué en la dirección contraria: **F4 tampoco lo hace en lo grueso.** `iniciativa` —que es literalmente la «unidad de trabajo amplia» cuyo «Nombre definitivo: **pendiente**» declara `IDEAS` §4— entra en la arquitectura **por `O11`**, una resolución del Owner con fecha (`DECISIONES` L277), no por lectura directa del documento de trabajo. Eso es correcto y lo digo.

**Qué fija realmente la aprobada, y a qué hallazgos toca:**

- **§31** manda revisar `G29` y retirar la relación universal «un item → una branch → un PR». Es el origen normativo de `P-04`/`PN-11`/`O16` y de la abstención de tocar `C7`. **Coherente con `D65`.** No cambia ningún hallazgo.
- **§49–§51** fijan **adopción** («la actual ruta… que copia ADS dentro de un repositorio de código debe retirarse como ruta normal») y **migración** de proyectos 1-repo. Son el mandato de `§8.2` y `§8.3`.
- **§55 ENT** le atribuye «verificar convergencia de source changes; comprobar Integration Set; coordinar migraciones; manejar integración parcial; preparar release/rollback». Es coherente con `U5b` y con `§6.7`.
- **§45–§48** fijan el **bootstrap**, origen de `§8.1`.
- **§98 `I1`–`I10`** e **§97 `N1`–`N14`** son invariantes y principios normativos **de este documento**, y de ahí salen los `N1`–`N14` de `C6`.
- **§113 «Regla de independencia de chat»** — cubierta, ver comprobación 2.

**Lo que la aprobada NO contiene, y es material.** **No dice nada sobre actualizar una versión de ADS ya instalada.** `grep -i 'versión de ADS\|actualizar ADS\|actualización de ADS\|versión instalada'` sobre sus 3 343 líneas: **salida vacía**. Ese mandato vive sólo en `IDEAS` §3, cuyo principio es literalmente «**Principio provisional:** *Detectar automáticamente; actualizar conscientemente*», y cuya tabla §15 lo clasifica «necesidad aceptada; política… **como base**». `§8.4` **L5427** lo eleva a:

> `PRINCIPIO       DETECTAR AUTOMÁTICAMENTE, ACTUALIZAR CONSCIENTEMENTE`

sin el calificativo «provisional» y sin citar su procedencia. La cadena no está rota —`09-SINTESIS.md` L638 lo registra como «ACEPTADA y FUSIONADA… El principio *«detectar automáticamente, actualizar conscientemente»* entra tal cual»— pero **el calificativo del Owner se perdió por el camino**, y `U` es precisamente el macrocircuito cuyo gate (`M-3`), participantes (`G-1`) e interacción con el freno (`M-7`) están en disputa. Nuevo hallazgo **E-7**, MENOR.

**Y una consecuencia para tres hallazgos existentes:** `IDEAS` §3 dice «**Debe estudiarse** si la actualización ADS… puede representarse mediante procesos/capacidades existentes —por ejemplo DEP/PLT/SIS— en lugar de crear automáticamente un nuevo tipo de proceso». Es decir: la elección `SIS`+`DEP` de `§18` para `U` **es coherente con una sugerencia del Owner que él dejó expresamente por estudiar**. Por tanto `G-1`, `M-3` y `M-4` **no pueden cerrarse invocando autoridad del Owner**: nadie ha decidido eso. Los tres se confirman.

**Un defecto de la propia regla `O10`.** `O10` fija «`docs/owner/` como destino canónico… La clasificación pasa a ser por **ubicación y metadata de autoridad**» (`DECISIONES` L276). La mitad de *ubicación* está implementada (`validadores/exclusiones.yaml` L100, `comprobar_fuentes.py` L67–68). **La mitad de *metadata de autoridad* no existe:** ninguno de los dos ficheros lleva bloque `ads:`, front-matter ni campo declarado; lo único que los separa es una línea de prosa distinta en cada uno. `exclusiones.yaml` L102–105 lo sabe —«decisiones aprobadas **y documentos de trabajo**»— y aun así exime a los dos por igual. Nuevo hallazgo **E-6**, MENOR: implementación ausente.

---

### COMPROBACIÓN 6 · `entrada/`

| pregunta | qué fija `entrada/` | consecuencia |
|---|---|---|
| **taxonomía** | nueve clases `ads:entrada`, todas definidas **sobre la expresión del Owner** (`01-TAXONOMIA` L5–6) | sostiene `M-6` |
| **clasificación** | `02-CIRCUITO` paso 8; catorce `ads:forma-conversacion` con árbol de decisión de once ramas (`03-FORMAS` L536–552) | ninguna rama admite un sujeto distinto del Owner |
| **escenarios** | seis recorridos + diez bloques `ads:escenario` (`T75`–`T80`, `T154`–`T157`) | ver **E-4** y **E-9** |
| **apertura de trabajo** | `02-CIRCUITO` L154–157: «`pasos 10-13  DSP  orden y ruta. NINGUNA autoridad sobre el contenido del encuadre`» | ver abajo |
| **auditorías autónomas** | **NADA.** Ninguna de las cinco menciona `AUD`, política de recurrencia ni `O7` | **confirma `M-5`** |
| **órdenes** | `forma:orden-clara` + `04-INCERTIDUMBRE` §3 (umbral 0.60 / margen 0.15, **PROVISIONALES**) + `T78` | ninguno |
| **ideas** | `forma:idea-inmadura` → VIVERO, sin item | ninguno |
| **gaps** | `forma:gap`, tipo GAP tras el gate | ninguno |
| **features** | `forma:feature`, tipo FEA tras el gate | ninguno |
| **documentación** | `memoria` de ENC, léxico del Owner, checkpoint por forma | ninguno |
| **continuidad** | `forma:interrupcion` + `T77` («Relevo de agente a mitad de conversación sin pedir resumen al Owner») | positivo |
| **autoridad para crear items** | **Dos reglas duras y sólo dos.** `01-TAXONOMIA` L20–22: «NINGUNA CLASE DE ENTRADA CREA TRABAJO POR SÍ MISMA salvo las tres que lo declaran». `02-CIRCUITO` L156: los pasos 10–13 son de `DSP`, **sin autoridad de contenido** | **decisivo para `M-5`** |

**Conclusión sobre `M-5`, que es el hallazgo que esta lectura podía haber anulado y no anula.** El ciclo de auditoría de `§5.3` deja `APERTURA` («crea un item AUD. SÓLO dentro de la política O7… el sistema PROPONE y espera») sin actor. Buscando el actor en `entrada/`, lo que encuentro es lo contrario de un remedio: **toda la autoridad de creación de items que `entrada/` declara está anclada a una expresión del Owner**, y un finding de un `AUD` no es una expresión del Owner. De modo que `M-5` y `M-6` **no son dos hallazgos independientes: son las dos caras del mismo hueco** —la taxonomía de entrada no tiene clase para un hallazgo originado por el sistema, y en consecuencia nadie está autorizado a abrir el item que de él nacería—. Ninguno se absorbe en el otro (tienen sedes y remedios distintos), pero cerrar uno sin el otro deja el circuito roto por el otro extremo. Lo hago constar en la tabla de la sección 6 como **alcance distinto** en `M-6`.

---

## 5 · Resultado específico de `C5` frente a `B-2`

### 5.1 · Qué vehículo faltaba, exactamente

`B-2` afirma que los participantes que `§8.1` declara —`PLT`, `ENC`, `PRD`, y «`ARQ DOM DIS SEG` según discovery»— **no tienen forma de entrar en la ruta** de un item `proceso:SIS`. Lo verifiqué yo, sobre la fuente, no sobre el dictamen. `01-PROCESOS.md` **L553–557**, sección completa de condicionales de `proceso:SIS`:

> `condicionales:`
> `  - capacidad: "ENT"`
> `    condicion: "el cambio modifica el runtime: activación segura y reversible"`
> `  - capacidad: "APR"`
> `    condicion: "C-APR"`

Y sus obligatorias (L522–552) son `SIS`, `CON` y `VER`. Por tanto la ruta de un item `proceso:SIS` puede contener, como máximo, **cinco capacidades**: `SIS`, `CON`, `VER`, `ENT`, `APR`. `PLT`, `ENC`, `PRD`, `ARQ`, `DOM`, `DIS` y `SEG` **quedan fuera por construcción**. El vehículo que falta es, con precisión: **un mecanismo declarado que active una capacidad en la ruta de un item cuyo proceso no la declara ni obligatoria ni condicional.**

### 5.2 · Qué proporciona `C5`, y con qué sujeto

`C5` proporciona **una forma**, no una instancia, y lo dice él mismo (**L38–39**): «Los handoffs concretos entre capacidades viven en `circuitos/`, no aquí: **C5 define la forma, no las instancias.**» La forma, contrastada contra `esquemas/handoff.yaml`:

| | qué declara `C5` / el esquema |
|---|---|
| **sujeto** | **una capacidad emisora y una capacidad receptora, y nada más.** `de: {tipo: ref, ref_a: capacidad}`, `a: {tipo: ref, ref_a: capacidad}`. No hay campo para proceso, fase, macrocircuito ni Owner |
| **emisor** | campo `de`. «El emisor NO explica su trabajo al receptor» (L112) |
| **receptor** | campo `a`. «QUIEN RECIBE COMPRUEBA ANTES DE TOMAR CUSTODIA» (L20) |
| **contenido** | `entrega`: «artefactos concretos, localizables». Y **L59**: «`NO VIAJA  una tarea. Viaja un ARTEFACTO y su evidencia; el trabajo lo compone DSP`» |
| **persistencia** | `checkpoint`, obligatorio: «qué del checkpoint del emisor debe poder leer el receptor» |
| **reanudación** | L107–109: «El receptor **carga el checkpoint del emisor**… Si `based_on` cambió, revalida **sólo la parte afectada**» |
| **evidencia** | `evidencia_de_devolucion`, obligatorio, y los cuatro campos de L84–87 |
| **gate** | **ninguno. L101–102: «`UN HANDOFF NO ES UN PUNTO DE APROBACIÓN. Entre dos equipos no hay un humano validando el traspaso.`»** |
| **autoridad** | `owner`, «`ninguna`» en la mayoría. L96–98: interviene «sólo cuando la entrega contiene una decisión de su autoridad… o cuando la devolución escala por el freno de a.7» |
| **disparador** | **`cuando`: «condición comprobable que dispara la entrega»** |

### 5.3 · Su relación con los cuatro macrocircuitos

Dos hechos, ambos derivados por mí:

**(a) El disparador de un handoff presupone la activación; no la produce.** Las diecisiete instancias reales lo demuestran sin excepción. `handoff:prd-a-dis` → `cuando: "el item cumple **C-DIS** y PRD ha depositado su capa"`. `handoff:dis-a-arq` → `"…y el item cumple **C-ARQ**"`. `handoff:dom-a-con` → `"el item cumple **C-DOM**…"`. `handoff:seg-a-con` → `"el item cumple **C-SEG**…"`. `handoff:ent-a-uso` → `"…y el item cumple **C-USO**"`. Y `C-DIS`, `C-ARQ`, `C-DOM`, `C-SEG`, `C-USO` son literalmente los valores del campo `condicion` de los **condicionales de los procesos de `b.16`** (`01-PROCESOS.md` L63–69, L123–129, L174–176, L254, L340–342, L396, L431–435, L502). **El handoff es el vehículo del trabajo entre dos capacidades que la ruta YA activó; el que las activa es el proceso.** No hay circularidad posible: si `proceso:SIS` no declara `C-DIS`, ningún handoff puede hacer que `C-DIS` sea verdadera.

**(b) No existe una sola instancia para los macrocircuitos.** Recuento propio: **17 instancias**, que cubren **trece** capacidades. **`SIS` y `PLT` no aparecen ni una vez.** Y `SIS` es el propietario global de `N0`–`N5`, `U0`–`U4` y `U5`–`U6` (`§18` L6990, L6998–6999) y `PLT` el ejecutor declarado en `§8.1`, `§8.3` y `§8.4`. Es decir: incluso si `proceso:SIS` declarase mañana a `PLT` y `ENC` como condicionales, **seguiría sin existir el handoff por el que se entregan el trabajo**, y `C5` L38–39 dice expresamente que esa instancia debe existir en `circuitos/`.

### 5.4 · CONCLUSIÓN

> ## `C5` **NO RESUELVE** `B-2`.

Y lo concluyo con las tres precisiones que el encargo exige, sin inventar ningún artefacto nuevo:

1. **No lo resuelve porque no es su materia.** `C5` gobierna la entrega entre dos capacidades **ya activadas**. `B-2` denuncia la ausencia del acto de activación. Son dos cosas distintas y `C5` lo declara: «viaja un ARTEFACTO… **el trabajo lo compone DSP**» (L59) y «UN HANDOFF NO ES UN PUNTO DE APROBACIÓN» (L101).
2. **La lectura de `C5` y de los dos ficheros de handoffs AGRAVA `B-2` en vez de aliviarlo.** Antes había un hueco (participantes sin condicional). Ahora hay dos: participantes sin condicional **y**, para los dos únicos actores que los cuatro macrocircuitos nombran en todas sus fases —`SIS` y `PLT`—, **ninguna instancia de handoff en absoluto**, cuando `C5` exige que las instancias vivan en `circuitos/`.
3. **`B-2` no estaba mal planteado, y su severidad no cambia.** Sigue siendo **BLOQUEANTE**. Lo que cambia es su **alcance**: la salida «que el vehículo exista en otra sede» queda **cerrada por lectura directa**, y el remedio 1.4 del doc 16 —«declarar por qué mecanismo entra cada participante»— debe ampliarse con **«y declarar la instancia de handoff correspondiente, que `C5` exige y `circuitos/` no tiene»**.

La sospecha explícita del adjudicador (§7: «`C5-HANDOFF.md` y `handoffs-generales.md` son precisamente donde podría vivir el vehículo que B no encontró. Nadie miró ahí.») queda **contestada: miré, y no vive ahí.**

---

## 6 · Los hallazgos adjudicados tras el nivel 0

### 6.1 · Una corrección aritmética previa, derivada por mí

El encargo me pide dictaminar sobre «los 29 hallazgos adjudicados (4 bloqueantes, 6 graves, 13 medios, 6 menores)». **Ese recuento no cuadra con la propia tabla del adjudicador**, y lo digo antes de la tabla para que nada se pierda.

`grep`/recuento manual sobre `docs/evolucion/16-…md` §4: la tabla tiene **33 filas** (`A1`–`A14` = 14, `B-1`/`B-2` = 2, `G-1`–`G-4` = 4, `M-1`–`M-9` = 9, `m-1`–`m-4` = 4). Clasificándolas por la **severidad adjudicada por C, no por la propuesta**:

```text
BLOQUEANTES  A1 · A2 · B-1 · B-2                                            =  4  ✔ coincide
GRAVES       A3 · A4 · G-1 · G-2 · G-3 · G-4                                =  6  ✔ coincide
MEDIOS       A5(reclasificado) · A6 · A7 · A8 · A9 · A10 · A13(reclasificado)
             + M-1 · M-2 · M-3 · M-4 · M-5 · M-6 · M-7 · M-8 · M-9          = 16  ✘ C declara 13
MENORES      A11 · A12 · m-1 · m-2 · m-3 · m-4                              =  6  ✔ coincide
EXCLUIDO     A14 — «no es defecto de F4» (§6 del adjudicador)               =  1
                                                                    TOTAL     33
```

**El recuento adjudicado real es 4 + 6 + 16 + 6 = 32, no 29.** Aun descontando la unificación `A11 ≡ M-8` que C resuelve «a favor de B», serían **31 distintos**. La cifra «13 MEDIOS» del párrafo de recuento **subestima en tres** lo que la propia tabla de C confirma. Lo registro como nuevo hallazgo **E-10** (defecto del doc 16, no de F4) y **doy estado a las 33 filas** para que ninguna quede sin dictamen.

### 6.2 · Tabla de estado

Cada fila lleva **exactamente uno** de los siete estados. **No he cambiado ninguna severidad**: donde no tengo prueba concreta y citada, escribo «confirmado sin cambios».

| id | severidad adjudicada | **estado tras el nivel 0** | por qué, con la prueba de las diecinueve |
|---|---|---|---|
| `A1` | BLOQUEANTE | **confirmado sin cambios** | Ninguna de las 19 toca `§2.6`/`§3.6` ni el enum de `deriva.causa`. No hay `esquemas/evento.yaml`. Fuera del alcance de mis fuentes |
| `A2` | BLOQUEANTE | **confirmado sin cambios** | Ídem. El predicado de transacción abierta no aparece en ninguna de las 19 |
| `B-1` | BLOQUEANTE | **confirmado con alcance distinto** | Confirmado y **ampliado por dos vías**. (i) `C1` **L141–142** cierra una salida: «`PROHIBIDO ser propietario global de un tipo de proceso del kernel → eso lo fija b.16, no el rol`» — el `propietario_global` DERIVADO de `AUD` no se arregla creando un rol. (ii) `diseno/00` **L114–116** y `03-ESCALA` **L46–50** demuestran que `DIS/Reconstruccion` **no es una capacidad activable ni un participante asignable**: es el método del nivel `N3`, calculado. El remedio 1.3 crece: hay que corregir también el condicional de `proceso:AUD` (ver **E-3**) |
| `B-2` | BLOQUEANTE | **confirmado con alcance distinto** | Sección 5. `C5` no lo resuelve; el disparador de todo handoff presupone `C-XXX`; y **`SIS` y `PLT` no tienen ninguna instancia de handoff**. Severidad **intacta**; el remedio 1.4 debe incluir la instancia que `C5` L38–39 exige |
| `G-1` | GRAVE | **confirmado sin cambios (con prueba nueva)** | `handoffs-generales.md` **L107**: `cuando: "el item cumple C-SEG, y siempre en items DEP antes de construir"`. El handoff obligatorio de todo `DEP` no tiene emisor (`SEG`) ni receptor (`CON`) entre los participantes de `U5b`. Severidad intacta; la evidencia deja de depender sólo de `G28` |
| `G-2` | GRAVE | **confirmado sin cambios (con prueba nueva)** | Sin `CON` en `A8`/`M6`/`M7`, no puede existir `handoff:con-a-ver` (`handoffs-generales` L203–206, único camino hacia `VER` junto a `dis-a-ver`), y el «`VER` verifica» de `§18` L6997 no tiene de quién recibir |
| `G-3` | GRAVE | **confirmado sin cambios** | Ninguna de las 19 declara qué produce el baseline ni la clasificación de desconocidos críticos en el macrocircuito `N` |
| `G-4` | GRAVE | **confirmado con alcance distinto** | El defecto duro —doce contratos de aspecto sin identificador— **se confirma**. Cambia el remedio: `diseno/01-MEMORIA` (doce bloques `ads:memoria`) y `esquemas/memoria.yaml` (`id · fichero · autoridad · caducidad` obligatorios) **ya son el patrón** que `§4.3` L4147–4149 dice usar para derivar el mapa. Declarar los doce debe **reutilizar** ese mecanismo, no inventar convención |
| `A3` | GRAVE | **confirmado sin cambios** | `§7.4`/`§2.6.9`/`PN-7`: fuera del alcance de las 19 |
| `A4` | GRAVE | **confirmado sin cambios** | `§15.8` y la cabecera: fuera del alcance de las 19 |
| `A5` | MEDIO *(reclas.)* | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `A6` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `A7` | MEDIO | **confirmado sin cambios** | `C1` L10–34 confirma que los conceptos y los campos son cosas distintas, lo que **respalda** la prescripción, pero la sede del defecto (`§2.6.10` L1917) no está en mis fuentes |
| `A8` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `A9` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `A10` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `A13` | MEDIO *(reclas.)* | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `M-1` | MEDIO | **confirmado sin cambios** | **Recontado por mí** sobre `§4.3` L4174–4178: UX e investigación · dirección visual · sistema de diseño · arquitectura de datos detallada · integraciones · cumplimiento regulatorio · modelo de amenazas avanzado · observabilidad · continuidad · analítica · dispositivos · internacionalización · gobierno de IA = **TRECE**. La tabla L4191 dice «14» |
| `M-2` | MEDIO | **confirmado sin cambios** | Ninguna de las 19 añade la fila a `§1.3`. `diseno/01` ofrece el patrón (`autoridad` + `caducidad` por bloque), no la fila |
| `M-3` | MEDIO | **confirmado sin cambios** | Y **queda cerrada la salida por autoridad del Owner**: `APROBADA` no menciona la actualización de ADS instalado (`grep` vacío sobre 3 343 líneas), e `IDEAS` §3/§15 la deja «por diseñar». Nadie ha decidido el gate de `U6` |
| `M-4` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19; el registro `D67` no lo tocan |
| `M-5` | MEDIO | **confirmado sin cambios** | **Reforzado.** `entrada/02` L154–157 da la propiedad del circuito («pasos 10-13 DSP… NINGUNA autoridad sobre el contenido») y `01-TAXONOMIA` L20–22 la regla dura. **Ninguno de los cinco ficheros de `entrada/` menciona `AUD`, `O7` ni auditoría autónoma.** El actor no existe en la única sede que podría declararlo |
| `M-6` | MEDIO | **confirmado con alcance distinto** | El alcance **crece y se prueba mejor**. No es sólo que la ficha de `ENC` no registre la extensión: **todo el aparato de entrada está definido sobre la expresión del Owner** — `01-TAXONOMIA` L5–6 («nueve cosas distintas» *entre lo que dice el Owner y lo que el sistema fabrica*), `03-FORMAS` L536–552 (árbol de once ramas, todas sobre la expresión), `entrada/02` L138–145. Un finding de un `AUD` no tiene clase, no tiene forma y no tiene rama. Severidad **intacta**; remedio mayor que «añadir una entrada a la ficha» |
| `M-7` | MEDIO | **confirmado sin cambios** | Nada en las 19 reconcilia los macrocircuitos con el FRENO 3. `C2` `perfil:despacho` y `entrada/04` §2 no lo tocan |
| `M-8` | MEDIO | **confirmado sin cambios** | Fuera del alcance de las 19. Nota: el hallazgo **E-1** que registro abajo es **de la misma clase** (colisión de espacio de nombres) y en un espacio distinto |
| `M-9` | MEDIO | **confirmado con alcance distinto** | El defecto se confirma: `§8.2` no declara el contenido del BASELINE de `A3`. **Alcance distinto:** para una de las doce materias el contenido **sí existe y es calculable** — `03-ESCALA` L16–32 fija cinco variables que se responden «**mirando el producto —el control repo y sus fuentes— y la memoria de diseño**, no interpretando». El remedio puede apoyarse en ese patrón para las demás áreas, en vez de derivar catorce preguntas del brief a mano |
| `A11` | MENOR | **absorbido por otro** *(por el propio adjudicador)* | C lo resuelve así en §5(a).1: «el hallazgo unificado es el de B», `M-8`. Lo dejo donde C lo dejó; nada de las 19 lo altera |
| `A12` | MENOR | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `m-1` | MENOR | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `m-2` | MENOR | **confirmado sin cambios** | Fuera del alcance de las 19 |
| `m-3` | MENOR | **confirmado sin cambios** | **Un dato más, y el juicio sigue sin asumirse.** `C2` `perfil:plataforma` declara `herramientas: […, observabilidad, …]` — tercera sede donde la observabilidad pertenece a `PLT`. Sigue siendo, como C dijo, una preferencia de diseño defendible en ambos sentidos. **No cambio la severidad ni asumo el juicio** |
| `m-4` | MENOR | **confirmado sin cambios** | Fuera del alcance de las 19; C ya rechazó su inferencia |
| `A14` | *(excluido por C)* | **rechazado** *(por el adjudicador, y lo mantengo)* | «No es defecto de F4»: prueba ejecutada en un entorno con Python 3.10.12 contra un tooling que exige 3.11. Nada de las 19 lo reabre |

**Resumen de mi pasada:** de los 33, **ninguno rechazado por mí**, **ninguno reducido**, **ninguno aumentado en severidad**, **cuatro confirmados con alcance distinto** (`B-1`, `B-2`, `G-4`, `M-6`, y `M-9`), **dos confirmados con prueba nueva que no cambia su severidad** (`G-1`, `G-2`), **ninguno dependiente de una fuente que antes faltaba en el sentido de quedar en suspenso**: las diecinueve **no anulan nada**.

---

## 7 · Hallazgos nuevos

Sólo los demostrados por estas diecinueve fuentes (más el doc 16 como objeto), que afecten materialmente a F4 y no dupliquen los 33.

---

### `E-1` · Colisión de espacio de nombres `N`: los principios normativos `N1`–`N14` y las fases del macrocircuito de instalación `N0`–`N7` conviven, se citan por identificador y significan cosas distintas — **MEDIO** · *defecto preexistente del kernel, heredado y agravado por F4*

**Cita 1** — `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` **§97**, L2729–2785: `### N1` … `### N14`, catorce **principios normativos** («`N5` Una source es una ubicación física versionada»).

**Cita 2** — `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` **L29–42**: los mismos catorce, adoptados literalmente como `N1`–`N14`.

**Cita 3** — `kernel/operativo/contratos/C5-HANDOFF.md` **L75–77**, dentro de mis diecinueve:

> «una **FUENTE** de `SOURCES.toml`, que es un repositorio del producto (**C6 N5**)»

**Cita 4** — `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L5090** (`§8.1`): `PARTICIPANTES  Owner · PLT (N0,N2,N6) · ENC+PRD (N1,N5) · SIS (N3) · VER (N4,N7)`; y **L6990**: «`| **N · instalación** | N0–N5 | proceso:SIS |`».

**Por qué es defecto.** `N5` significa, en el mismo corpus y ambos vigentes, «*una FUENTE es una ubicación física versionada*» (C5/C6, citado por identificador) y «*la quinta fase del macrocircuito de instalación*» (§8.1/§18, citada por identificador). `N1` significa «*un ADS Project representa un producto*» y «*la fase donde `ENC`+`PRD` participan*». Es **exactamente** el modo de fallo que `M-8` denuncia para `R1`–`R9` frente a `R1`–`R8`, en un espacio de nombres **más usado** y que **atraviesa la frontera del contrato**: `C5` cita `N5` para desambiguar una palabra, y `§8.1` cita `N5` para nombrar una fase. Un lector de `§8.1` que abra `C6` buscando `N5` encuentra otra cosa.

**Qué exigiría cerrarlo.** Renombrar uno de los dos espacios —lo natural es que las fases del macrocircuito lleven prefijo (`INS-0`…`INS-7`, como `A`, `M` y `U` ya lo llevan implícitamente)— y comprobarlo con la misma prueba que se cree para `R1`–`R9`.

---

### `E-2` · `§8.2` fija `DIS/Reconstruccion` en la fase `A6`, y `03-ESCALA-DE-NOVEDAD` declara que ese método **se calcula y no se elige** — **MEDIO** · *defecto de F4*

**Cita 1** — `11-ARQUITECTURA-INTEGRADA.md` **L5208–5210** (`§8.2`, PARTICIPANTES): «`A6 activa DOM, SEG, DIS/Reconstruccion y PRD`».

**Cita 2** — `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` **L114–116**:

> «Cuál se ejecuta lo decide la [escala de novedad](../../kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md), **no el criterio del agente**.»

**Cita 3** — `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` **L46–50**:

> `N4  FUNDACIÓN        dir_sustituye  or  (not superficie_construida and not memoria_vigente)`
> `N3  RECONSTRUCCIÓN   superficie_construida  and  not memoria_vigente`
> `N2  DIRECCIÓN NUEVA  memoria_vigente  and  not patron_cubre  and  premium_o_nuevo`

**Cita 4** — mismo fichero, **L262–264**: «**Bajar el nivel es la forma más silenciosa de abaratar el diseño**, y por eso el nivel se calcula con las cinco variables… **en vez de elegirse**.»

**Por qué es defecto.** `DIS/Reconstruccion` es el método de `N3` y sólo de `N3`. Un producto con historia cuya `memoria_vigente` sea verdadera computa `N0`, `N1` o `N2`; uno con un `DIR` que sustituya la dirección computa `N4`. `§8.2` **predetermina el nivel para todo producto adoptado**, que es precisamente la elección que `03-ESCALA` declara no discrecional, y lo hace en la fase del macrocircuito cuya justificación `B-1` ya denuncia como falsa bajo el mapeo de `§18`. En el mejor caso el texto acierta el caso típico; en el peor, obliga a `F6` a saltarse la escala o a contradecir `§8.2`.

**Qué exigiría cerrarlo.** Que `A6` diga «`DIS`, con el método que resulte de la escala de novedad calculada sobre el producto adoptado», y que declare **quién** calcula las cinco variables y **en qué fase** —candidato natural: `A2`/`A3`, que es donde el inventario y el baseline ya miran el producto—.

---

### `E-3` · El campo `capacidad` de los condicionales de `b.16` no tiene vocabulario: mezcla capacidades, formas cualificadas y **un método** — **MEDIO** · *defecto preexistente del kernel, y sede del remedio de `B-1`*

**Cita 1** — `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` **L10, L26–28** (los siete conceptos): «`CAPACIDAD  qué SABE HACER el sistema. Vive en el catálogo.`» · «`MÉTODO  PROCEDIMIENTO que el rol debe seguir… Confundirlo con rol → dos roles distintos ejecutando el mismo procedimiento genérico`».

**Cita 2** — `kernel/operativo/recorrido/01-PROCESOS.md` **L433–434** (`proceso:AUD`, condicionales):

> `  - capacidad: "DIS/Reconstruccion"`
> `    condicion: "C-DIS"`

**Cita 3** — `kernel/operativo/esquemas/proceso.yaml`: `condicionales… campos: capacidad: {tipo: texto, min: 3}` — **texto, no `ref_a: capacidad`**; y `obligatorias… capacidad_productora: {tipo: texto, min: 3}`.

**Derivación propia** sobre los valores realmente usados en `01-PROCESOS.md`:

```text
campo `capacidad` de los condicionales   APR·8  ENT·6  USO·5  DIS·4  ARQ·4  PRD·2  SEG·1  DOM·1
                                          SEG:condiciones·4  DOM:condiciones·4  CON:experimental·2
                                          ARQ:diagnostico·1        ← formas cualificadas
                                          DIS/Reconstruccion·1     ← un MÉTODO
campo `capacidad_productora`              …  OWNER·1              ← no es una de las quince
                                          «la capacidad propietaria de cada decisión sustituida»·1
```

**Por qué es defecto.** Los campos que deciden **qué entra en una ruta** admiten tres notaciones distintas y ningún tipo los comprueba. Ahí caben `DIS/Reconstruccion` (un método) y `OWNER` (que no es capacidad). Es la **raíz** del segundo defecto de `B-1` —`AUD` y `DEU` en la columna de participantes— un nivel por debajo, en el fichero derivado de `(b)` en vez de en `§18`, y por eso el remedio (c) del doc 16 («sustituir `AUD` y `DEU` por capacidades reales en las columnas de participantes») **no basta**: la misma sustitución hace falta en el condicional de `proceso:AUD`, que es justamente el que `§8.2` L5209 invoca.

**Qué exigiría cerrarlo.** Fijar el vocabulario del campo (capacidad de las quince, con sufijo `:` opcional para la variante declarada), tipar `capacidad` y `capacidad_productora` como `ref_a: capacidad` en `esquemas/proceso.yaml`, y sustituir `DIS/Reconstruccion` por `DIS` con su condición, y `OWNER` por la autoridad que corresponda.

---

### `E-4` · El escenario de referencia contradice el mecanismo que `04-INCERTIDUMBRE` acaba de crear: declara `GRADO GLOBAL = ALTA` y persiste `grado_inicial: media` — **MEDIO** · *defecto preexistente del kernel*

**Cita 1** — `kernel/operativo/entrada/05-ESCENARIOS.md` **L76** (Escenario A, paso 5):

> `GRADO GLOBAL = ALTA   →  PROHIBIDO FORMULAR. Se conversa. Crítica obligatoria después.`

**Cita 2** — mismo fichero, **L180–181** (el encuadre `ENC-001` resultante):

> `  grado: media`
> `  grado_inicial: media`

**Cita 3** — mismo fichero, **L220** (paso 8): «Obligatoria: **la incertidumbre fue alta** y el nivel de Owner es obligatorio.»

**Cita 4** — `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` **L205–207**:

> «El grado ALTA queda persistido en `incertidumbre.grado_inicial`, y eso hace la crítica independiente **OBLIGATORIA para siempre** en este encuadre, aunque la conversación baje el grado.»

**Por qué es defecto.** `grado_inicial` existe para una sola cosa —que la crítica no se pierda cuando la conversación baja el grado— y es campo obligatorio del esquema (`esquemas/encuadre.yaml` L39: `obligatorios: [grado, grado_inicial, ejes, motivo]`), con validador propio (`comprobar_contratos.py` L712–713) y prueba (`T136-T152` L266). **El único ejemplar trabajado del corpus lo rellena mal**: persiste `media` para un encuadre que su propio paso 5 declaró `ALTA`, y su paso 8 vuelve a decir «fue alta». Leído literalmente, el escenario **desactiva** la crítica que el propio escenario ejecuta. Y `05-ESCENARIOS` no es prosa: es el contrato de `T75`, con `estado: contrato-definido`. Un implementador de `F6` que derive el ejemplo reproduce exactamente el fallo que `A-19` corrigió.

**Qué exigiría cerrarlo.** `L181 → grado_inicial: alta`, conservando `grado: media` (que es el correcto tras conversar), y una comprobación en `T75` de que `grado_inicial` coincide con el grado del paso 5.

---

### `E-5` · Las instancias de handoff `dis-a-ver` exigen «los nueve ejes» y `02-RUBRICAS` declara que en esa estación sólo hay ocho — **MENOR** · *defecto preexistente del kernel*

**Cita 1** — `kernel/operativo/circuitos/DIS-handoffs.md` **L138–144** (`handoff:dis-a-ver`):

> `entrega: - "el dictamen de excelencia visual con sus **nueve ejes**"`
> `comprueba_al_recibir: - "**ambos dictámenes existen** y ningún eje está en rechazo"`

**Cita 2** — `kernel/operativo/diseno/02-RUBRICAS.md` **L214–215** (`gate:excelencia-visual`, comprobación `ocho-ejes-en-la-pasada-de-diseno`):

> «en la pasada de diseño, **los ocho ejes distintos de fidelidad** tienen nivel y evidencia, y `fidelidad` está marcado **pendiente-de-construccion**»

**Cita 3** — mismo fichero **L278–285**: «`PASADA DE DISEÑO  estación 9 · antes de entregar a Construcción · ocho ejes con nivel y evidencia`» · «`PASADA DE FIDELIDAD  estación 11 · con la capa ya construida`».

**Por qué es defecto.** `handoff:dis-a-ver` se dispara «cuando DIS cierra su capa», es decir, tras la estación 9, cuando el eje `fidelidad` está por construcción y **no puede tener nivel**. Un receptor que aplique literalmente `comprueba_al_recibir` **rechaza toda entrega de DIS**, porque el dictamen de la pasada de diseño nunca tendrá nueve ejes evaluados. Es la misma clase de defecto que `02-RUBRICAS` corrigió en el gate (hallazgo `A-20`, «era una regla que nadie podía cumplir») y que **no se propagó a la instancia de handoff**.

**Qué exigiría cerrarlo.** `DIS-handoffs.md` L139 → «el dictamen de la **pasada de diseño**, con sus ocho ejes y `fidelidad` marcado `pendiente-de-construccion`».

---

### `E-6` · `O10` clasifica el material del Owner «por ubicación **y metadata de autoridad**», y la metadata de autoridad no existe en ninguno de los dos ficheros — **MENOR** · *implementación ausente*

**Cita 1** — `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L276** (`O10`): «**`docs/owner/`** como destino canónico. La clasificación pasa a ser por **ubicación y metadata de autoridad**, en vez de una exención manual por fichero.»

**Cita 2** — `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` **L3**: «**Estado:** APROBADO PARA IMPLEMENTACIÓN» — prosa, sin bloque `ads:`, sin front-matter, sin campo.

**Cita 3** — `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` **L3**: «> Estado: documento de trabajo del Owner.» — ídem.

**Cita 4** — `kernel/operativo/validadores/exclusiones.yaml` **L100–105**: exime `ruta: docs/owner/` en bloque, con motivo «decisiones aprobadas **y documentos de trabajo** que NO son corpus operativo».

**Por qué es defecto.** La mitad de la regla que se implementó (ubicación) **borra** la distinción que la otra mitad debía preservar: en `docs/owner/` conviven una norma aprobada y un documento que dice «**NO IMPLEMENTAR TODAVÍA**», y **nada legible por máquina los distingue**. `exclusiones.yaml` sabe que son dos clases y aun así las trata igual. El riesgo es exactamente el que el encargo del nivel 0 me pidió vigilar: que una propuesta del Owner se lea como norma por vivir donde vive la norma.

**Qué exigiría cerrarlo.** Un campo declarado —bloque `ads:` o front-matter— con `autoridad: aprobada | trabajo` en cada fichero de `docs/owner/`, comprobado por el validador que ya recorre el directorio.

---

### `E-7` · `§8.4` eleva a `PRINCIPIO` de un macrocircuito un principio que el Owner declaró **provisional** en un documento de trabajo — **MENOR** · *presión normativa*

**Cita 1** — `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` §3: «**Principio provisional:** > **Detectar automáticamente; actualizar conscientemente.**» Y §15: «`| actualización ADS → proyectos | necesidad aceptada; política "detectar automáticamente, actualizar conscientemente" como base |`».

**Cita 2** — `11-ARQUITECTURA-INTEGRADA.md` **L5427** (`§8.4`): «`PRINCIPIO       DETECTAR AUTOMÁTICAMENTE, ACTUALIZAR CONSCIENTEMENTE`».

**Cita 3** — `grep -i 'versión de ADS\|actualizar ADS\|actualización de ADS\|versión instalada'` sobre las 3 343 líneas de `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` → **salida vacía**. El macrocircuito `U` **no tiene mandato en la norma aprobada**.

**Por qué es defecto, y qué no es.** No es una invención: `09-SINTESIS.md` L638 registra el tema como «ACEPTADA y FUSIONADA… El principio *«detectar automáticamente, actualizar conscientemente»* **entra tal cual**». Lo que se perdió en la cadena es la palabra **provisional**, y con ella la señal de que `U` descansa sobre un tema que el Owner dejó por diseñar. Importa porque tres hallazgos vivos (`G-1`, `M-3`, `M-7`) discuten precisamente el gate, los participantes y el freno de `U`, y ninguno puede resolverse invocando una decisión del Owner que no existe.

**Qué exigiría cerrarlo.** Que `§8.4` cite la procedencia y conserve el calificativo, o que la ausencia de mandato aprobado para `U` se registre como presión normativa, con la simetría que `§16` se impone a sí mismo.

---

### `E-8` · `03-FORMAS` declara «catorce bloques, **uno por clase de expresión**», y las clases son nueve — **MENOR** · *problema editorial*

**Cita 1** — `kernel/operativo/entrada/03-FORMAS.md` **L3**: «> Catálogo. Contiene **catorce** bloques `ads:forma-conversacion`, **uno por clase de expresión**.»

**Cita 2** — `kernel/operativo/entrada/01-TAXONOMIA.md` **L5–6**: «hay **nueve** cosas distintas»; tabla L26–36: nueve clases.

**Derivación propia:** 14 bloques `ads:forma-conversacion`, 9 bloques `ads:entrada`. La correspondencia no es 1:1 y el propio `03-FORMAS` L554–557 lo dice sin querer («se parte en dos expresiones»). Sin consecuencia normativa —el árbol de decisión de L536–552 funciona— pero es una cifra derivada falsa en la cabecera de un catálogo, y el corpus tiene ya cuatro hallazgos de esa misma clase (`M-1`, `m-1`, `A6`, `A10`).

---

### `E-9` · `05-ESCENARIOS` se declara «las pruebas T75 a T84» y contiene `T75`–`T80` y `T154`–`T157`; `T81`–`T84` viven en otro fichero — **MENOR** · *problema editorial*

**Cita 1** — `kernel/operativo/entrada/05-ESCENARIOS.md` **L5**: «No son ilustraciones: son **las pruebas T75 a T84**».

**Cita 2** — derivación propia: el fichero contiene `id: T75, T76, T77, T78, T79, T80, T154, T155, T156, T157`. `T81`–`T84` están en `kernel/operativo/pruebas/T081-T085-reanudacion-ENC.md` (verificado, existen y están en `REGISTRO-generado.md` L30–33).

**Por qué es defecto.** La cabecera del fichero declara mal su propio contenido y omite las cuatro pruebas más recientes (`T154`–`T157`), que son las que cierran las cuatro salidas de la expresión subjetiva. Sin consecuencia normativa.

---

### `E-10` · El recuento del adjudicador declara **13 medios** donde su propia tabla adjudica **16** — **MENOR** · *problema editorial, del doc 16, no de F4*

**Cita** — `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md`, párrafo de recuento tras la tabla de §4: «**13 MEDIOS confirmados** (contando `A5` y `A13` reclasificados a MEDIO por mí)».

**Derivación propia** — ver §6.1: la tabla adjudica como MEDIO a `A5, A6, A7, A8, A9, A10, A13, M-1…M-9` = **16**. El total adjudicado real es **32** (o 31 con la unificación `A11≡M-8`), no 29.

**Por qué importa.** Es un recuento **derivado** del propio gate, en la sección que fija la carga de trabajo de F5, y el encargo del nivel 0 lo hereda literalmente. Tres hallazgos medios reales quedan fuera de la cifra que un lector usa para dimensionar la corrección. Es exactamente la clase de defecto que `A6`, `A10`, `m-1` y `M-1` denuncian en F4, cometida por el documento que los denuncia.

---

### Clasificación de los diez

| id | severidad | clasificación |
|---|---|---|
| `E-1` | MEDIO | defecto preexistente del kernel *(heredado y agravado por F4)* |
| `E-2` | MEDIO | **defecto de F4** |
| `E-3` | MEDIO | defecto preexistente del kernel |
| `E-4` | MEDIO | defecto preexistente del kernel |
| `E-5` | MENOR | defecto preexistente del kernel |
| `E-6` | MENOR | implementación ausente |
| `E-7` | MENOR | presión normativa |
| `E-8` | MENOR | problema editorial |
| `E-9` | MENOR | problema editorial |
| `E-10` | MENOR | problema editorial *(del doc 16)* |

**Ninguno es «limitación aceptada».** Lo comprobé uno a uno: `E-2` y `E-4` tienen la contradicción escrita en dos sedes vigentes, no una limitación declarada; `E-6` y `E-7` son huecos que el propio corpus se compromete a llenar.

---

## 8 · Limitaciones de mi revisión

```text
1  Leí ÍNTEGRAS las diecinueve del encargo (8 310 líneas, verificadas con wc -l) más
   entrada/01-TAXONOMIA.md (309). NO he leído íntegro `11-ARQUITECTURA-INTEGRADA.md`:
   abrí de él los tramos que necesitaba para contrastar —§1.3, §4.3, §8.1, §8.2, §8.4,
   §15.2–§15.4, §18— y lo traté como OBJETO. NO afirmo nada sobre §2, §3, §6, §7, §9–§14
   ni §16–§17, que no abrí.

2  Por tanto NO he verificado por mí mismo A1, A2, A3, A4, A5, A6, A8, A9, A10, A12, A13,
   M-4, M-8, m-1, m-2 ni m-4. Los declaro «confirmados sin cambios» en el sentido exacto
   de que MIS FUENTES NO LOS TOCAN — no en el sentido de que yo los haya reproducido.

3  Tampoco leí C4, C6 ni C7 completos: de C6 abrí sólo L29–42 (los `N1`–`N14`) y de
   `esquemas/` sólo handoff.yaml, memoria.yaml, proceso.yaml y encuadre.yaml en los
   campos citados. `packs/`, `capacidades/*/roles|metodos|prompts` y `validadores/*.py`
   línea a línea siguen SIN CUBRIR por nadie.

4  NO ejecuté ningún validador ni ninguna prueba. Modo sólo lectura estricto. Todos mis
   hallazgos son sobre TEXTO y sobre esquema declarado, y ninguno lo pude confirmar ni
   desmentir con una ejecución: nada de esto está construido.

5  E-2, E-4 y E-5 son contradicciones entre dos sedes vigentes. NO afirmo cuál de las dos
   frases debe sobrevivir: afirmo que las dos no pueden ser ciertas a la vez.

6  NO he consultado al REVISOR D, no sé qué ha leído y no supongo nada de su dictamen.
   Si coincidimos, la coincidencia no está pactada; si divergimos, la divergencia es real
   y alguien deberá adjudicarla.

7  Mi corrección aritmética del recuento adjudicado (E-10) la derivé contando las filas de
   la tabla de C y clasificándolas por la severidad que C les asigna. NO reabro ninguna de
   sus adjudicaciones: sólo cuento las que él escribió.
```

---

## 9 · Qué cambia y qué no tras esta cobertura

**No emito veredicto de suficiencia.** La arquitectura no se ha corregido: entre `a713590` y `HEAD` sólo cambiaron el índice, el checkpoint, tres ficheros de evidencia y el propio doc 16. Los 32 hallazgos siguen abiertos en el texto, uno por uno.

**Qué cambia:**

1. **La laguna de cobertura del NIVEL 0 queda cerrada por mi parte.** Las diecinueve fuentes —8 310 líneas— están leídas íntegras, con cita de su primera y última sección sustantiva y con el efecto de cada una sobre los hallazgos declarado. El requisito 0.1 del doc 16 ya no puede alegarse contra mi eje.
2. **La pregunta que el adjudicador dejó abierta tiene respuesta.** `C5` **no** contiene el vehículo de `B-2`, y la razón es estructural, no accidental: el sujeto de un handoff son dos capacidades, su disparador presupone la condición del proceso (`C-DIS`, `C-SEG`, `C-ARQ`…) y el esquema no admite proceso ni fase. `B-2` sigue siendo **BLOQUEANTE**, con **el alcance ampliado**: `SIS` y `PLT` no tienen **ninguna** instancia de handoff, cuando `C5` exige que las instancias existan en `circuitos/`.
3. **Dos graves ganan prueba independiente.** `G-1` la tiene ahora en `handoffs-generales.md` L107 («siempre en items DEP antes de construir») y `G-2` en la ausencia del único camino de entrada a `VER`. Ninguno cambia de severidad; ambos dejan de depender de una sola sede.
4. **Cuatro hallazgos cambian de alcance sin cambiar de severidad:** `B-1` (crece: `C1` cierra la salida por rol, y `DIS/Reconstruccion` no es asignable), `G-4` (encoge en remedio: el patrón existe en `ads:memoria`), `M-6` (crece: el hueco es de toda la taxonomía de entrada, no de una ficha), `M-9` (encoge en parte: `03-ESCALA` ya fija cómo se establece una de las materias del baseline).
5. **Tres hallazgos quedan protegidos contra una salida falsa.** `G-1`, `M-3` y `M-4` **no pueden cerrarse invocando al Owner**: la norma aprobada no menciona la actualización de ADS instalado, y el documento que la menciona dice de sí mismo que no autoriza a implementar.
6. **Diez hallazgos nuevos**, ninguno duplicado, dos de ellos en la misma clase de los que ya bloquean (`E-1` colisión de nombres, como `M-8`; `E-3` confusión capacidad/método/proceso, como el segundo defecto de `B-1`), uno **defecto propio de F4** (`E-2`), y uno que corrige la aritmética del propio gate (`E-10`).

**Qué no cambia:**

- **Ningún hallazgo se rechaza, se reduce ni se anula.** Las diecinueve fuentes no contenían el mecanismo que el gate sospechaba. Contenían **la prueba de que ese mecanismo no está**, y dos huecos más.
- **Ningún bloqueante deja de serlo.** Los cuatro siguen en pie.
- **El patrón que A describió y C extendió se confirma también en mi eje, y con un matiz propio.** A lo formuló como «decisiones bien tomadas y aplicadas a la mitad de los sitios que las invocan». En las diecinueve fuentes el patrón aparece **al revés**: `diseno/`, `entrada/` y los handoffs contienen **mecanismos correctos, completos y con esquema** —la escala de novedad, las dos pasadas del gate visual, el `grado_inicial`, el relevo de agente, la forma del handoff— y lo que falla es que **`§8` los invoca sin leerlos** (`E-2`) o **no los invoca en absoluto** (`E-5` en el catálogo, la ausencia total de instancias para `SIS` y `PLT`). No es propagación incompleta hacia fuera: es **integración incompleta hacia dentro**.
- **Y la conclusión operativa del nivel 0, que sí puedo dar sin veredicto:** el requisito 1.4 del doc 16 —«declarar por qué mecanismo entra cada participante»— **no puede resolverse en `§8`**. Toca `01-PROCESOS.md` (los condicionales), `esquemas/proceso.yaml` (el vocabulario del campo) y `circuitos/` (las instancias que faltan). Quien lo aborde en `F5` debe saber que el trabajo no está donde `§18` lo hace parecer.

---

*Fin del dictamen del REVISOR E.*

---

## ADJUDICACIÓN DEL ADJUDICADOR F

### 1 · Identidad, procedencia y modo

**Quién soy.** Adjudicador F del NIVEL 0 del gate final de `F4c`. Repositorio `/home/jose/ads-kernel`, rama `redesign/kernel-2.0`, HEAD verificado por `git rev-parse` → `7c7856ccb88ea3851fb5e1fc1ec04af38d03ab96`, cuyo commit es `docs(f4c): gate final independiente — VEREDICTO INSUFICIENTE PARA F5`. Árbol limpio: `git status --porcelain` → **0 líneas**.

**Qué NO soy.** No escribí `F4`, ni `F4b`, ni `F4c`, ni ninguna de sus correcciones. **No soy el Revisor A, ni el Revisor B, ni el Adjudicador C**: no participé en el gate. No soy el Revisor D ni el Revisor E: recibo sus dictámenes ya cerrados y los trato como **material a verificar, no como verdad**. Donde coinciden, verifico por muestreo; donde difieren, abro el fichero.

**Qué NO hago.** **No corrijo nada.** No emito veredicto de suficiencia: la arquitectura no se ha corregido y eso está expresamente fuera de mi encargo. Cierro con qué queda y con qué condición hay para empezar la tanda de corrección.

**Modo.** **SÓLO LECTURA** sobre el repositorio. No he modificado ningún fichero, no he hecho commits, no he ejecutado ninguna escritura de git. Los únicos comandos fueron `git rev-parse`, `git status`, `git log`, `cat`, `sed`, `grep`, `awk`, `wc`, `find`, `ls` y `python3 --version`. **No he usado ni solicitado Google Calendar ni Google Drive** (ambos conectores requieren autorización que esta sesión no puede completar; no la necesito y no la pedí).

---

### 2 · Qué recibí y qué abrí yo para verificar

**Recibido, leído íntegro:**

| documento | líneas | qué aporta |
|---|---|---|
| `dictamen-D.md` (scratchpad) | 404 | seis comprobaciones · estado de 33 filas · `ND-1`…`ND-5` · nueve limitaciones |
| `dictamen-E.md` (scratchpad) | 601 | seis comprobaciones · estado de 33 filas · `E-1`…`E-10` · siete limitaciones |

**Abierto por mí en el repositorio, para verificar** (todo en modo lectura):

| fichero | qué verifiqué |
|---|---|
| `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | §4 tabla completa (L1043–1084), recuento al pie, §5, §6, §7 (L1135–1160), §8, §9, §10 (L1200–1257) |
| `kernel/operativo/contratos/C5-HANDOFF.md` | **íntegro, 115 líneas** |
| `kernel/operativo/circuitos/00-CIRCUITOS.md` | **íntegro, 240 líneas** |
| `kernel/operativo/circuitos/DIS-handoffs.md` | cabecera, grafo, `dis-a-ver`, `con-a-dis`, `dis-a-con`, reglas comunes, y los 8 `id/de/a/cuando` |
| `kernel/operativo/circuitos/handoffs-generales.md` | los 9 `id/de/a/cuando`, `cierre-a-apr` completo, `seg-a-con` L104–107 |
| `kernel/operativo/esquemas/handoff.yaml` · `proceso.yaml` · `encuadre.yaml` | **íntegros** los dos primeros; campos citados del tercero |
| `kernel/operativo/recorrido/01-PROCESOS.md` | `proceso:AUD` L415–445 · `proceso:SIS` L505–560 · `proceso:INV` L270–300 · derivación completa de los campos `capacidad` y `capacidad_productora` |
| `kernel/operativo/00-INDICE.md` | L1–130 (regla de fuente única y **mapa de fuente única**) |
| `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | L105–120 |
| `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | L40–55 |
| `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | L1–60 (trece estaciones y retornos) |
| `kernel/operativo/diseno/02-RUBRICAS.md` | L208–220 · L274–290 |
| `kernel/operativo/entrada/03-FORMAS.md` | L1–6 · `forma:continua` L468–500 · algoritmo L534–557 |
| `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | L25–40 |
| `kernel/operativo/entrada/05-ESCENARIOS.md` | L1–8 · L70–80 · L172–185 · L215–225 · `T75` L322–335 |
| `kernel/operativo/entrada/01-TAXONOMIA.md` | L1–8 y recuento de bloques |
| `kernel/operativo/contratos/C6-…md` | L25–45 (`N1`–`N14`) |
| `kernel/operativo/capacidades/{DIS,PRD,ARQ,ENC,DOM,SEG,PLT}/CAPACIDAD.md` | bloques `entrada` y `materializacion` |
| `kernel/operativo/validadores/exclusiones.yaml` · `comprobar_recuentos.py` | L95–110 · la única referencia a `handoff` |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | §8.1 L5081–5100 · §8.2 L5195–5222 · §8.4 L5420–5470 · §15.7 L6378–6390 · §18 L6985–7005 · §4.3 L4170–4195 |
| `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | cabecera · L371–372 · L1359 · `grep` de actualización |
| `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | cabecera · L79–81 · L485–487 · L589 · L597 |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | `O7`–`O14` L271–280 · `O10` **L276** |
| `tooling/workspace.py` L18–26 · `python3 --version` | procedencia de `A14` |

**Lo que NO abrí:** `§2`, `§3`, `§5` a `§7`, `§9` a `§14`, `§16`, `§17` y `§19` de `11-ARQUITECTURA-INTEGRADA.md`; `C1`, `C2`, `C3`, `C4`, `C7`; `packs/`; los validadores línea a línea; `(a)`, `(b)`, `E1`, `E2`. Donde una fila de la matriz depende de esas sedes, lo marco.

---

### 3 · Método de verificación

1. **Anclaje.** `git rev-parse` y `git status` antes de nada. Confirmado el HEAD del encargo y el árbol limpio.
2. **Recuentos derivados por mí, nunca leídos:** instancias `ads:handoff` (`grep -rn '^id: handoff' kernel/ packs/` → **17**, 8 + 9 + 0); bloques `ads:forma-conversacion` (**14**); bloques `ads:entrada` (**9**); líneas de las diecinueve fuentes (`wc -l` → **8 310**, coincidente con lo que declaran D y E); filas de la tabla §4 del documento 16 (**33**); esquemas `.yaml` (**19**); ficheros `.md` en `packs/` (**24**).
3. **Regla de prueba.** Cada cita de D y de E que sostiene una conclusión la abrí en su fichero y su línea. **Las que no cuadran las corrijo por nombre y línea**, y lo digo aunque el hallazgo sobreviva.
4. **Regla de severidad.** *Ninguna severidad se mueve sin prueba citada.* No he movido ninguna de las 33. Las severidades que fijo son sólo las de los hallazgos **nuevos**, y en cada caso digo con qué hallazgo ya adjudicado calibro.
5. **Regla de duplicado.** Dos hallazgos son el mismo si comparten **sede y remedio**. Compartir modo de fallo no basta.
6. **Regla de rechazo.** Un hallazgo se rechaza cuando su demostración falla contra la fuente, aunque el hecho citado sea cierto.

---

### 4 · Resolución de `C5` frente a `B-2`

Lo comprobé yo, sin apoyarme en ninguno de los dos dictámenes para el hecho.

**Los recuentos, derivados.** `grep -rn '^id: handoff' kernel/ packs/` da **diecisiete** instancias y ninguna más en todo el árbol: `DIS-handoffs.md` **8**, `handoffs-generales.md` **9**, `00-CIRCUITOS.md` **0**.

**Cuántas anclan su `cuando` a un criterio `C-<CAP>`.** Enumeración completa de los diecisiete campos `cuando`:

```text
ANCLA POSITIVAMENTE A UN CRITERIO C-<CAP>  ── 7 de 17
  prd-a-dis   L22   "el item cumple C-DIS y PRD ha depositado su capa…"
  dis-a-arq   L53   "…y el item cumple C-ARQ"
  prd-a-arq   L36   "el item cumple C-ARQ y PRD ha depositado su capa"
  dom-a-con   L83   "el item cumple C-DOM y las condiciones se entregan ANTES de construir"
  seg-a-con   L107  "el item cumple C-SEG, y siempre en items DEP antes de construir"
  ver-a-ent   L130  "el dosier no tiene evidencia en rojo y el item cumple C-ENT"
  ent-a-uso   L154  "el cambio está desplegado y el item cumple C-USO"

LO NOMBRA EN NEGATIVO ──────────────────── 1 de 17
  dis-a-con   L80   "…o el item no cumple C-ARQ"

NO NOMBRA NINGÚN CRITERIO ─────────────── 9 de 17
  arq-a-con · con-a-dis · dis-a-ver · uso-a-dis · inv-a-dis · dis-a-ent ·
  enc-a-dsp · cierre-a-apr · con-a-ver
```

> **Corrección a `D`.** D enumera los siete como «`C-DIS`, `C-ARQ`, `C-DOM`, `C-SEG`, `C-ENT`, `C-USO`, `C-APR`». **`C-APR` no aparece en el `cuando` de `cierre-a-apr`**: su disparador (L177–182) es «el cierre del item resuelve `learning_candidate` con un enlace, o el item es un INC, o hay una revisión de circuito o una promoción». La **cifra** de D es correcta; su **lista** no. El séptimo es `prd-a-arq`, que D omite. El hecho que D quería probar sobrevive intacto.

**`SIS` y `PLT` como emisor o receptor.** Enumeración completa de los campos `de:` y `a:` de las diecisiete instancias. Las capacidades que aparecen son trece: `PRD ARQ CON DOM SEG VER ENT USO INV ENC DSP APR DIS`. **`SIS` y `PLT` no aparecen ni una sola vez, ni como `de` ni como `a`.** Las quince capacidades del catálogo están en `kernel/operativo/00-INDICE.md`; las dos que faltan son exactamente `SIS` y `PLT`.

**Qué es y qué no es `C5`, verificado línea a línea.**

- `C5` **L36–39**: «Todo handoff del sistema se declara con un bloque `ads:handoff` conforme a `esquemas/handoff.yaml`. Los handoffs concretos entre capacidades viven en `circuitos/`, no aquí: **C5 define la forma, no las instancias.**»
- `esquemas/handoff.yaml`: `de: {tipo: ref, ref_a: capacidad}` · `a: {tipo: ref, ref_a: capacidad}`. **No existe campo para proceso, fase, macrocircuito ni Owner.** El sujeto de un handoff son dos capacidades y nada más.
- `C5` **L101–102**: «UN HANDOFF NO ES UN PUNTO DE APROBACIÓN. Entre dos equipos no hay un humano validando el traspaso.» → no aporta gate.
- `C5` **L59**: «NO VIAJA una tarea. Viaja un ARTEFACTO y su evidencia; **el trabajo lo compone DSP**.» → no aporta acto de composición de ruta.

**La ruta que `B-2` denuncia, verificada en la fuente.** `01-PROCESOS.md`, `proceso:SIS`: obligatorias `SIS` → `CON` → `VER`; condicionales **exactamente dos**, `ENT` («el cambio modifica el runtime») y `APR` (`C-APR`). §8.1 **L5090** declara participantes `Owner · PLT (N0,N2,N6) · ENC+PRD (N1,N5) · SIS (N3) · VER (N4,N7) · ARQ DOM DIS SEG según discovery`. Siete capacidades declaradas participantes quedan **fuera de la ruta por construcción**.

#### CONCLUSIÓN — confirmo la de D y E, y añado dos correcciones

> ## `C5` **NO RESUELVE** `B-2`.

**Por qué, con la razón exacta.** `C5` gobierna la entrega entre dos capacidades **que la ruta ya activó**; `B-2` denuncia la ausencia del acto de **activación**. El disparador de todo handoff **presupone** la condición del proceso: en siete de diecisiete el `cuando` cita literalmente el criterio `C-<CAP>` que el proceso debe declarar. Si `proceso:SIS` no declara `C-DIS`, ningún handoff puede hacer que `C-DIS` sea verdadera. Y el esquema no admite otro sujeto. La esperanza que `C` dejó escrita al cerrar su §7 —«`C5-HANDOFF.md` y `handoffs-generales.md` son precisamente donde podría vivir el vehículo que B no encontró. Nadie miró ahí»— **queda contestada en negativo, y no debe volver a abrirse.**

**`B-2` NO cambia de severidad. Sigue siendo BLOQUEANTE.** Su **alcance** cambia en tres puntos, dos heredados y uno mío:

1. **(D y E, confirmado)** Queda cerrada por lectura directa la salida «el vehículo vive en otra sede»: no vive en `C5`, no vive en el esquema, y no vive en las diecisiete instancias.
2. **(D y E, confirmado)** `SIS` y `PLT` —que cargan tres de los cuatro macrocircuitos— **no tienen ninguna instancia de handoff**, ni siquiera dentro de la ruta que `proceso:SIS` sí declara: existe `con-a-ver`, **no existe `sis-a-con`**.
3. **(mío, corrige a `C` y matiza a `D`)** El matiz que `C` concedió —«`DOM` L17 y `SEG` L53 **no acotan el origen**, luego para esas dos existe vehículo plausible»— **sólo se sostiene para `DOM`**. Verificado:
   - `DOM/CAPACIDAD.md` **L17**, dentro de `entrada:` → «una consulta en modo consulta: condiciones antes de construir, o revisión después». Sin acotar origen. **La salida existe.**
   - `SEG/CAPACIDAD.md` **L16–19**, `entrada:` → «un item que cumple **C-SEG**» · «un item **DEP**» · «un incidente con posible consecuencia de seguridad». Y `materializacion` **L53–54**: «Se materializa cuando un item cumple **C-SEG**, y siempre en items **DEP**.» **`SEG` no ofrece una consulta de origen libre en su `entrada`**: la frase que `C` cita («en modo consulta no toma custodia») describe un **modo**, no una **vía de entrada**. En un item `proceso:SIS`, `C-SEG` no se evalúa nunca y el item no es `DEP`.

   **Consecuencia:** el hueco de `B-2` cubre **cinco** capacidades y no cuatro — `ENC`, `PRD`, `ARQ`, `DIS` y **`SEG`** —, y sigue habiendo una sola salida plausible, `DOM`.

**Sobre `PLT`, matizo a `D`.** D afirma que «`PLT` no tiene vehículo por ninguna de las tres vías». Verificado `PLT/CAPACIDAD.md` L17–20: su `entrada` es «una carencia de maquinaria que bloquea a otra capacidad» · «un item de su backlog propio» · «una consulta sobre disponibilidad de entornos o dispositivos». La primera **no está acotada por origen** y podría leerse como cubriendo `N0`/`N2`/`N6`; la segunda abre **otro item**, que es precisamente el tercer vehículo que `B-2` deja sin explorar. Lo que sí queda demostrado, y basta, es lo que `B-2` afirma: **`PLT` no entra en la ruta de un item `proceso:SIS`**, porque ese proceso no la declara ni obligatoria ni condicional, y no hay instancia de handoff que la nombre. La formulación absoluta de D («por ninguna de las tres vías») no la sostengo.

---

### 5 · Resolución de la discrepancia D/E sobre `00-CIRCUITOS.md` y `ND-1`

Ésta es la única discrepancia material entre los dos dictámenes, y la resuelvo abriendo las dos sedes.

**Las dos frases, verificadas literalmente.**

- `kernel/operativo/contratos/C5-HANDOFF.md` **L36–37**: «**Todo** handoff del sistema se declara con un bloque `ads:handoff` conforme a `esquemas/handoff.yaml`.»
- `kernel/operativo/circuitos/00-CIRCUITOS.md` **L238–240**: «Un par de capacidades sin handoff declarado **no está prohibido**: significa que su entrega se rige por las **reglas comunes** de `C5`. Los declarados son aquellos donde la experiencia —o el diseño— ha mostrado que hace falta precisión extra.»

**¿Hay contradicción real entre las dos sedes?** **Hay una tensión literal, y no es simétrica.** `C5` L36 admite dos lecturas:

- **fuerte** — cuantificador de cobertura: *toda entrega entre capacidades debe tener bloque declarado*. Bajo ella, la frase de `00-CIRCUITOS` la contradice.
- **débil** — regla de forma: *cuando hay un bloque, se ajusta al esquema*. Bajo ella, no hay contradicción.

**Cuál manda — tres pruebas, y las tres van en el mismo sentido.**

1. **El propio `C5` se autolimita en la frase siguiente.** L38–39: «Los handoffs concretos entre capacidades viven en `circuitos/`, **no aquí**: **C5 define la forma, no las instancias.**» Un documento que declara no contener las instancias no puede, dos líneas antes, fijar cuántas instancias deben existir.
2. **El mapa de fuente única del kernel asigna la materia a `circuitos/`, no a `C5`.** `kernel/operativo/00-INDICE.md`, tabla «Mapa de fuente única»: **`| entregas entre capacidades | circuitos/00-CIRCUITOS.md |`**. Y la regla que la encabeza: «**Una verdad vive en un fichero. Los demás la enlazan.** Repetirla es un defecto de conformidad.» La verdad *«qué pares entregan y cuáles hace falta declarar»* vive, por regla escrita del propio kernel, en `00-CIRCUITOS.md`.
3. **Ningún validador exige cobertura.** `grep -rl 'handoff' kernel/operativo/validadores/` devuelve un solo fichero, `comprobar_recuentos.py`, y su única referencia (L81) es `"handoffs": n("handoff")` — un **recuento**, no una comprobación de cobertura. Nada en el árbol comprueba que un par tenga bloque.

> **Resolución: manda `00-CIRCUITOS.md` L238.** La lectura fuerte de `C5` L36 **no es sostenible**, y **D tiene razón contra E**. La ausencia de instancias `sis-a-con`, `prd-a-con`, `ent-a-arq` y las de `PLT` **no es, por sí sola, un defecto de conformidad**. E sostuvo la lectura fuerte sin haber abierto `00-CIRCUITOS.md`, y lo declara en su limitación 3; su posición no sobrevive a la lectura.

**¿Queda `ND-1` como defecto, y con qué severidad?** Sí, **reformulado y rebajado**, por dos residuos que la resolución anterior **no** disuelve:

- **Residuo material.** La quinta obligación de `C5` (L14) es «QUÉ CHECKPOINT SOBREVIVE: el receptor debe poder reanudar sin hablar con el emisor», y `esquemas/handoff.yaml` hace `checkpoint` **obligatorio** en cada instancia — es el campo que dice *qué* del checkpoint del emisor concierne al receptor («ARQ lee de DIS: nivel de novedad, direcciones descartadas y por qué…»). Las «reglas comunes» de `C5` L107–109 sólo dicen «carga el checkpoint del emisor **en la parte que le concierne**», sin decir cuál es esa parte. **§8.1, §8.3 y §8.4 declaran cláusulas `REANUDACIÓN` sobre entregas entre `PLT`, `SIS` y `VER`, y para esos pares no hay ninguna instancia que declare qué parte concierne.** Ese hueco es real bajo cualquiera de las dos lecturas.
- **Residuo editorial, verificado.** Las dos frases siguen escritas y siguen siendo incompatibles en su lectura literal. Un lector que llegue a `C5` L36 sin conocer el mapa de fuente única concluirá lo contrario que un lector que llegue a `00-CIRCUITOS` L238.

**La segunda mitad de `ND-1` —«defecto de `F4`»— la verifiqué y la sostengo, aunque debilitada.** `11-ARQUITECTURA-INTEGRADA.md` §15.7, tabla `C1`–`C7`: **L6386** «`C5` handoff | REUTILIZADO», a secas; **L6387** `C6` «REUTILIZADO **CON EXCEPCIÓN NOMBRADA**, y su defecto REGISTRADO»; **L6388** `C7` «REUTILIZADO CON **UNA CORRECCIÓN PENDIENTE, NOMBRADA**». La asimetría es literal y verificable. Ahora bien: resuelta la contradicción a favor de `00-CIRCUITOS`, lo que `F4` tenía que haber nombrado no es «`C5` incumplido», sino «`C5` invocado sobre pares sin instancia, cuya cláusula de reanudación depende de esas instancias». Eso rebaja la mitad de `F4` de defecto de conformidad a **omisión de registro**.

> **Veredicto sobre `ND-1`:** **sobrevive reformulado, severidad MENOR** (baja desde el MEDIO que D propuso, por caída de su premisa fuerte). Identificador consolidado: **`F-05`**. Clasificación: **problema editorial** (las dos frases) **+ implementación ausente** (el checkpoint de `SIS`/`PLT`/`VER` sin declarar). Su parte material se cierra **dentro** del remedio 1.4 de `B-2`, no aparte.

---

### 6 · Consolidación de los hallazgos nuevos

Quince en bruto. **Tres fusiones, ninguna rechazada en bloque, dos reformuladas a la baja, y una extensión de hallazgo existente rechazada.** Doce identificadores supervivientes, `F-01`…`F-12`.

#### 6.1 · Los duplicados, fundidos

| nuevo id | funde | por qué es el mismo defecto | severidad | clasificación |
|---|---|---|---|---|
| **`F-01`** | `ND-2` + `E-2` | Misma sede raíz y mismo remedio: el nombre de un **método** ocupa el campo `capacidad`. `ND-2` cubre las tres sedes (`01-PROCESOS.md` L434, `00-CIRCUITOS.md` L166, §8.2 L5209); `E-2` cubre sólo §8.2 y aporta la demostración del daño material | **MEDIO** | defecto preexistente del kernel **propagado por F4** |
| **`F-03`** | `ND-3` + `E-1` | Misma colisión de espacio de nombres `N<n>`, mismas cuatro citas | **MEDIO** | defecto de F4 sobre espacio preexistente |
| **`F-12`** | `ND-5` + `E-10` | Mismo descuadre aritmético del documento 16, misma derivación | **MENOR** | problema editorial (**del documento 16, no de F4**) |

**`F-01`, verificado en las tres sedes:**
- `kernel/operativo/recorrido/01-PROCESOS.md` **L433–434**, `proceso:AUD` → `- capacidad: "DIS/Reconstruccion"` / `condicion: "C-DIS"`. Literal.
- `kernel/operativo/circuitos/00-CIRCUITOS.md` **L166** → `├─► [DIS/Reconstruccion si C-DIS]`. Literal.
- `11-ARQUITECTURA-INTEGRADA.md` **L5209** → «A6 activa DOM, SEG, **DIS/Reconstruccion** y PRD». Literal.
- `diseno/00-SISTEMA-DE-EXCELENCIA.md` **L109–116** → «Los tres son **métodos de la capacidad `DIS`**… Cuál se ejecuta lo decide la escala de novedad, **no el criterio del agente**.» Literal.
- `diseno/03-ESCALA-DE-NOVEDAD.md` **L44–50** → `N3 RECONSTRUCCIÓN  superficie_construida and not memoria_vigente`; `N4 FUNDACIÓN  dir_sustituye or …`. Literal. **El nivel se calcula.** Fijar el método en el condicional lo preselecciona.
- Nota al pie de §18 **L7003–7005**: «confundir el nombre de un proceso con el de una capacidad es el mismo modo de fallo que `G1` corrigió con `a.9`». Aquí se confunde el de un **método**.

**`F-03`, verificado en las cuatro sedes:**
- `contratos/C6-…md` **L29–42**: `N1`…`N14`, principios normativos («`N5 una FUENTE es una ubicación física versionada`»).
- `contratos/C5-HANDOFF.md` **L76**: «un repositorio del producto (**C6 N5**)» — cita por identificador, **a través de la frontera del contrato**.
- `11-ARQ` **L5090** (§8.1): `PLT (N0,N2,N6) · ENC+PRD (N1,N5) · SIS (N3) · VER (N4,N7)` — `N5` es una **fase**.
- `11-ARQ` **L6990** (§18): `| N · instalación | N0–N5 | proceso:SIS |`.

> **Adjudico la severidad entre D (MENOR) y E (MEDIO): MEDIO.** El dato que decide es de D, no de E: `C5` L76 cita `N5` **para desambiguar una palabra en un contrato**, mientras §8.1 cita `N5` para nombrar una fase. Es el mismo daño que `C` adjudicó MEDIO en `M-8` (`R1`–`R9` frente a `R1`–`R8`), agravado porque cruza la frontera del contrato. **No es una severidad movida: es una severidad fijada para un hallazgo nuevo, calibrada contra `M-8`.**

#### 6.2 · Los reformulados a la baja

| id | de | qué rechazo | qué sobrevive | severidad |
|---|---|---|---|---|
| **`F-05`** | `ND-1` | **La lectura fuerte** («`C5` exige declarar todo handoff, luego faltan instancias = defecto de conformidad»). Cae por la §5 de esta adjudicación | (i) las dos frases incompatibles siguen escritas; (ii) el `checkpoint` que viaja entre `PLT`, `SIS` y `VER` no está declarado en ninguna parte, y §8.1/§8.3/§8.4 declaran `REANUDACIÓN` sobre esas entregas; (iii) §15.7 L6386 no registra la excepción con la disciplina que sí aplicó a `C6` y `C7` | **MENOR** (baja desde MEDIO) |
| **`F-06`** | `E-5` | **La demostración**: «un receptor que aplique literalmente `comprueba_al_recibir` **rechaza toda entrega de DIS**». No se sigue. `02-RUBRICAS` **L287–289** dice «El gate **no cierra definitivamente hasta la segunda pasada**», y `handoff:dis-a-ver` L137 se dispara «cuando **DIS cierra su capa**». Bajo la lectura natural —la capa cierra tras la pasada de fidelidad, estación 11— los nueve ejes **sí** tienen nivel y no hay contradicción | El hecho subyacente: `04-CICLO-DE-CALIDAD` L7–48 enumera **trece estaciones** y **ninguna es la entrega a `VER`** (la 10 es a `CON`, la 11 fidelidad, la 12 dispositivo, la 13 aprendizaje). El disparador de `dis-a-ver` **no está anclado a ninguna estación**, y por tanto de qué pasada procede el dictamen queda indeterminado — y una de las dos lecturas hace la comprobación insatisfacible | **MENOR** (baja desde MENOR de E, pero cambia de naturaleza: de contradicción a ambigüedad) |

#### 6.3 · La extensión rechazada

| pieza rechazada | de | motivo, con la fuente |
|---|---|---|
| **`A3` gana una sexta sede en `entrada/03-FORMAS.md` `forma:continua`, que «tendrá que reanclarse junto a §7.4 y §16 L6876»** | `D`, estado de `A3` | **RECHAZADO.** Abrí `03-FORMAS.md` **L468–497** íntegro. `forma:continua` **no afirma la formulación retirada por `D69`**: no menciona reversión, ni ramas, ni `abandonada`. Dice «TODO: es la función Estado de DSP» y remite a «los pasos 1 a 4 de **b.14**» y «el paso 5 de **b.14**». Bajo la regla de fuente única del propio kernel (`00-INDICE.md`: «Una verdad vive en un fichero. Los demás la **enlazan**»), **enlazar a `b.14` en vez de repetir sus ramas es el comportamiento correcto**, no una sede que reanclar. `A3` queda **confirmado sin cambios**, como sostiene E |

#### 6.4 · Los diez restantes, verificados uno a uno

| id | origen | verificación mía | severidad | clasificación |
|---|---|---|---|---|
| `F-02` | `E-3` | **Confirmado y reforzado.** `esquemas/proceso.yaml`: `condicionales.campos.capacidad: {tipo: texto, min: 3}` y `obligatorias.campos.capacidad_productora: {tipo: texto, min: 3}` — **texto, no `ref_a: capacidad`**, a diferencia de `handoff.yaml`, que sí usa `ref_a`. Derivé yo la distribución completa de valores y coincide con la de E **exactamente**: `APR·8 ENT·6 USO·5 DIS·4 ARQ·4 PRD·2 SEG·1 DOM·1` · formas cualificadas `SEG:condiciones·4 DOM:condiciones·4 CON:experimental·2 ARQ:diagnostico·1` · un método `DIS/Reconstruccion·1`; y en `capacidad_productora`, `OWNER·1` y «la capacidad propietaria de cada decisión sustituida»·1 | **MEDIO** | defecto preexistente del kernel |
| `F-04` | `E-4` | **Confirmado; corrijo la cita de E.** `05-ESCENARIOS.md` **L76** «GRADO GLOBAL = ALTA»; **L180–181** `grado: media` / `grado_inicial: media`; **L219** «la incertidumbre fue alta»; `T75` **L332** exige «la incertidumbre se declara **alta**». `esquemas/encuadre.yaml` **L39** hace `grado_inicial` obligatorio. **La cita de E a `04-INCERTIDUMBRE…md` L205–207 es imposible: el fichero tiene 187 líneas.** El texto está en **L31–34** del mismo fichero. Hallazgo intacto; referencia corregida | **MEDIO** | defecto preexistente del kernel |
| `F-07` | `E-6` | **Confirmado.** `DECISIONES-Y-CONTRADICCIONES.md` **L276** (`O10`): «La clasificación pasa a ser por **ubicación y metadata de autoridad**». `ADS-ARQUITECTURA-…APROBADA.md` **L3**: «**Estado:** APROBADO PARA IMPLEMENTACIÓN» — prosa. `ADS-IDEAS-…md` **L3**: «> Estado: documento de trabajo del Owner» — prosa. **Ni bloque `ads:`, ni front-matter, ni campo, en ninguno de los dos.** `validadores/exclusiones.yaml` **L100–105** exime `docs/owner/` en bloque, con motivo «decisiones aprobadas **y documentos de trabajo**» | **MENOR** | implementación ausente |
| `F-08` | `ND-4` | **Confirmado, y NO es duplicado de `F-07`.** `IDEAS` **L485** «12. CUESTIÓN ABIERTA CRÍTICA — Materialización del proyecto multi-repo», **L487** «**NO IMPLEMENTAR TODAVÍA**», **L597** «materialización física multi-repo \| **ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO**», frente a `APROBADA` L3 «APROBADO PARA IMPLEMENTACIÓN». Ninguno cita al otro. Remedio distinto del de `F-07`: `F-07` se cierra con un campo declarado; `F-08` exige una **nota de sustitución o de vigencia** sobre la materia. Un campo `autoridad:` no retira la frase «NO IMPLEMENTAR» sobre algo que `C6`, `C7` y §10 ya implementan | **MENOR** | problema editorial |
| `F-09` | `E-7` | **Confirmado.** `IDEAS` **L79–81**: «**Principio provisional:** > **Detectar automáticamente; actualizar conscientemente.**»; **L589** tabla §15 «necesidad aceptada; política… **como base**». `11-ARQ` **L5427** (§8.4): «`PRINCIPIO       DETECTAR AUTOMÁTICAMENTE, ACTUALIZAR CONSCIENTEMENTE`», sin calificativo y sin procedencia. `grep -i 'versión de ADS\|actualizar ADS\|actualización de ADS\|versión instalada'` sobre las 3 343 líneas de `APROBADA` → **salida vacía**: `U` no tiene mandato en la norma aprobada | **MENOR** | presión normativa |
| `F-10` | `E-8` | **Confirmado, derivado por mí.** `03-FORMAS.md` **L3**: «Contiene **catorce** bloques `ads:forma-conversacion`, **uno por clase de expresión**». `grep -c '^```yaml ads:forma-conversacion'` → **14**. `01-TAXONOMIA.md` **L5–6**: «hay **nueve** cosas distintas»; `grep -c '^```yaml ads:entrada'` → **9**. La cifra 14 es correcta; **la aposición «uno por clase de expresión» es falsa** | **MENOR** | problema editorial |
| `F-11` | `E-9` | **Confirmado, derivado por mí.** `05-ESCENARIOS.md` **L5**: «son las pruebas **T75 a T84**». `grep -n '^id: T'` sobre el fichero → `T75 T76 T77 T78 T79 T80 T154 T155 T156 T157`. `T81`–`T85` viven en `kernel/operativo/pruebas/T081-T085-reanudacion-ENC.md`, que existe | **MENOR** | problema editorial |
| `F-12` | `ND-5` + `E-10` | **Confirmado, y le añado una segunda instancia derivada por mí.** Además del 32/16 frente a 29/13 (§7 de esta adjudicación), el §7 del documento 16 escribe «Son **dieciocho** fuentes obligatorias intactas» y su propio requisito 0.1 enumera **diecinueve** ficheros (2 handoffs + 6 `diseno/` + 4 contratos + 2 `docs/owner/` + 5 `entrada/`). Tercera cifra derivada del gate que su propio texto desmiente | **MENOR** | problema editorial (**del documento 16**) |

#### 6.5 · Clasificación de los doce, y por qué ninguno es «limitación aceptada»

```text
DEFECTO DE F4                          F-03  (introduce N0–N7 sobre un N1–N14 vigente)
DEFECTO PREEXISTENTE DEL KERNEL        F-02 · F-04 · F-06
DEFECTO PREEXISTENTE PROPAGADO POR F4  F-01
PRESIÓN NORMATIVA                      F-09
IMPLEMENTACIÓN AUSENTE                 F-07 · (mitad material de F-05)
PROBLEMA EDITORIAL                     F-08 · F-10 · F-11 · F-12 · (mitad textual de F-05)
LIMITACIÓN ACEPTADA                    ninguno
```

Lo comprobé uno a uno, como hizo E: `F-01`, `F-02` y `F-04` son contradicciones entre **dos sedes vigentes**, no límites declarados; `F-07` y `F-09` son huecos que el propio corpus se compromete a llenar (`O10` y §16). **La única «limitación aceptada» del conjunto es `A14`**, y no es un hallazgo nuevo — ver §8.

---

### 7 · El recuento real, derivado

**Conté yo las 33 filas de la tabla §4 del documento 16 y las clasifiqué por la severidad que `C` les asigna, no por la que propuso su revisor.**

```text
FILAS DE LA TABLA §4 ────────────────────────────────────────────────── 33
  A1…A14 = 14  ·  B-1, B-2 = 2  ·  G-1…G-4 = 4  ·  M-1…M-9 = 9  ·  m-1…m-4 = 4

BLOQUEANTES  A1 · A2 · B-1 · B-2                                     =  4   ✔ C declara 4
             (B-2 «CONFIRMADO CON MATIZ», y C escribe que sigue siendo bloqueante)

GRAVES       A3 · A4 · G-1 · G-2 · G-3 · G-4                         =  6   ✔ C declara 6
             (A5 SALE: C escribe «Rebajo a MEDIO» en su propia celda)

MEDIOS       A5 ↓reclasificado por C  ·  A6 · A7 · A8 · A9 · A10
             A13 ↑reclasificado por C («es MEDIO, no menor»)         =  7
             M-1 · M-2 · M-3 · M-4 · M-5 · M-6 · M-7 · M-8 · M-9     =  9
                                                             TOTAL   = 16   ✘ C declara 13

MENORES      A11 · A12 · m-1 · m-2 · m-3 · m-4                       =  6   ✔ C declara 6
             (A13 SALE, subido; A14 SALE, «No es defecto de F4»)

EXCLUIDO     A14 — §6 de C: «No es defecto de F4»                    =  1

DEFECTOS ADJUDICADOS  4 + 6 + 16 + 6                                 = 32
DEFECTOS DISTINTOS    32 − 1 (A11 ≡ M-8, unificado por el propio C en §5(a).1) = 31
FILAS TOTALES         32 + 1 (A14)                                   = 33
```

**Dónde está el error de `C`.** Su párrafo de recuento dice «**13 MEDIOS confirmados** (contando `A5` y `A13` reclasificados a MEDIO por mí)». El paréntesis es la trampa: `A5` y `A13` **se suman** a los catorce que ya había (`A6`–`A10` = 5, más `M-1`–`M-9` = 9), dando **dieciséis**. `C` los contó como si estuvieran **dentro** de trece. La desviación es de **tres en los medios y de tres en el total**.

> **La cifra correcta es 32 hallazgos adjudicados como defectos de `F4` — 4 bloqueantes, 6 graves, 16 medios, 6 menores — sobre 33 filas, más `A14` excluido. Descontando la unificación `A11 ≡ M-8` que el propio `C` ordenó, los defectos distintos son 31.**
>
> **La cifra de 29 que el encargo original heredó es errónea.** No pierde ningún hallazgo —los 32 tienen fila y cita—, pero **dimensiona la tanda de corrección tres medios por debajo de lo que la propia tabla del gate confirma**, y la sección 10 del documento 16 está escrita sobre ella. Registrado como **`F-12`**.

**Convergencia:** D y E llegaron por separado a 32 y 16. Lo verifiqué contando las filas yo mismo y **coincido con los dos**.

**Recuento consolidado tras el nivel 0:**

```text
DEL GATE (defectos de F4)      4 BLOQ · 6 GRAVE · 16 MEDIO · 6 MENOR   = 32
NUEVOS DEL NIVEL 0 (F-01…F-12) 0 BLOQ · 0 GRAVE ·  4 MEDIO · 8 MENOR   = 12
                                                              ─────────────
TOTAL ABIERTO                  4 BLOQ · 6 GRAVE · 20 MEDIO · 14 MENOR  = 44
FILAS DE LA MATRIZ             44 + A14 (excluido, no defecto de F4)   = 45
DISTINTOS (A11 absorbido en M-8)                                       = 43
```

---

### 8 · La matriz consolidada

Una fila por hallazgo. `sev` = severidad adjudicada. **Ninguna severidad de las 33 se ha movido.** Las severidades de `F-01`…`F-12` son fijaciones nuevas, calibradas contra hallazgos ya adjudicados. Donde la fuente está fuera de lo que abrí, lo digo con `†` (verificación heredada de `C`, no reverificada por mí).

| id | sev | causa | fuente exacta (fichero · línea) | estado tras el nivel 0 | decisión que lo condiciona | nivel doc 16 | dependencias | ¿decisión nueva del Owner? | condición comprobable de cierre |
|---|---|---|---|---|---|---|---|---|---|
| `A1` | BLOQ | defecto de F4 (contrato) | `11-ARQ` L3659 · L3622 · L3745 · L2203‑2212 † | confirmado sin cambios | `D16`–`D22` | **1** · 1.1 | ninguna | no | `deriva.causa` declarado con **tres** valores en **una sola** sede (§3.6), y §2.6.11 remite en vez de redeclarar |
| `A2` | BLOQ | defecto de F4 (protocolo) | `11-ARQ` L2514 · §2.6.1 L544‑546 · L5018 † | confirmado sin cambios | `D16`–`D22` | **1** · 1.2 | condiciona `A3` (2.3) | no | existe un predicado único y nombrado de transacción abierta, referenciado desde las siete sedes; «único terminal» retirado de L449, L986, L2514 |
| `B-1` | BLOQ | defecto de F4 (arquitectura) | §8.2 **L5208‑5210** · §18 **L6993** · `01-PROCESOS` **L429‑437** y **L419** | **confirmado, alcance ampliado por dos vías** | `D67` | **1** · 1.3 | **`F-01`, `F-02`** | no | `A2`–`A7` tiene **un** proceso, coherente en §8.2 y §18; si es `AUD`, su `propietario_global` derivado resuelto; `AUD` y `DEU` retirados de las columnas de participantes |
| `B-2` | BLOQ | defecto de F4 (arquitectura) | `01-PROCESOS` **L521‑557** · §8.1 **L5090** | **confirmado, alcance ampliado en tres puntos** (§4) | `D67` | **1** · 1.4 | **`F-05`** (mitad material) | no | cada participante de cada fase de los cuatro macrocircuitos tiene **mecanismo declarado** de entrada en ruta; si no existe en `b.16`, registrado como presión normativa |
| `G-1` | GRAVE | defecto de F4 | `01-PROCESOS` **L369‑377** · §18 **L6999** · §8.4 **L5440** · **prueba nueva:** `handoffs-generales.md` **L107** | confirmado sin cambios, **con dos pruebas nuevas independientes** | `G28`, `D67` | **2** · 2.1 | ninguna | no | `SEG` y `CON` figuran entre los participantes de `U5b` en §8.4 y §18, o se justifica y reasigna el proceso |
| `G-2` | GRAVE | defecto de F4 | §18 **L6994**/**L6997** · §8.3 L5295 † · `01-PROCESOS` L322‑325 | confirmado sin cambios, con evidencia reforzada | `D67` | **2** · 2.2 | ninguna | no | §8.3 y §18 coinciden e incluyen `ARQ`; `cambio-construido` tiene capacidad productora nombrada en `A8`, `M6` y `M7` |
| `G-3` | GRAVE | defecto de F4 | §8.1 **L5081‑5097** · §9.4 L5685‑5686 † | confirmado sin cambios | `O12` | **2** · 2.6 | ninguna | **sólo si** se reinterpreta `O12`; no si se registra como presión | una fase de `N` declara productor del baseline y de la clasificación de desconocidos críticos, o consta la reinterpretación de `O12` como `PN` |
| `G-4` | GRAVE | defecto de F4 → contrato derivado | §4.3 **L4124‑4148** · L4428‑4613 † | **confirmado con alcance modificado en las dos direcciones** (D: crece; E: el remedio encoge). Severidad intacta | `O8`, `D68` | **2** · 2.5 | `M-1`, `M-2` | no | las doce áreas tienen identificador `documental/<area>` declarado, **derivado del patrón `ads:memoria` + `esquemas/memoria.yaml` ya existente**, sin crear segunda sede editable (`I5`) |
| `A3` | GRAVE | defecto de F4 | `11-ARQ` L5008‑5013 · L1643 · L6717‑6722 · **L6876** · **L1458** † | **confirmado sin cambios** — rechazo la sexta sede que D propone (§6.3) | `D69`, `PN-7` | **2** · 2.3 | `A2` (1.2) | no | §7.4 reescrito con las dos ramas y el predicado de 1.2; §16 L6876 alineado con el cuerpo de `PN-7`; L1458 corregido |
| `A4` | GRAVE | defecto de F4 (trazabilidad) | §15.8 L6521‑6530 · cabecera L12, L59‑62 · L7073, L7079‑7082 † | confirmado sin cambios | `D64`–`D68` | **2** · 2.4 | ninguna | no | bloque `D64`–`D68` presente en §15.8; cabecera y §19 sin contradicción sobre la tercera revisión |
| `A5` | MEDIO *(rebajado por C)* | defecto de F4 | `11-ARQ` L1632‑1640 · L3654 † | confirmado sin cambios | `D16`–`D22` | **3** · 3.10 | `A13` | no | L1639 reformulado sobre el sujeto correcto (ningún **fichero canónico**; el evento `preparada` sí conserva los suyos) |
| `A6` | MEDIO | defecto de F4 (recuento) | `11-ARQ` L513 · L544‑551 · L3327‑3328 · L3637‑3640 † | confirmado sin cambios | — | **4** · 4.3 | ninguna | no | L513 → «cinco fases, dos rutas, dos cierres»; L3327‑3328 y L3637‑3640 → 5 fases, 6 estados, 7 filas |
| `A7` | MEDIO | defecto de F4 → contrato derivado | `11-ARQ` L1915‑1917 · L3290‑3294 † | confirmado sin cambios | `G1`/`a.9` | **3** · 3.1 | `A13` (misma raíz) | no | §2.6.10 L1917 dice «los cinco **campos** de procedencia», no «los cinco conceptos de `a.9`» |
| `A8` | MEDIO | defecto de F4 (justificación) | `11-ARQ` L1372‑1373 · L1394‑1400 · L1690‑1693 † | confirmado sin cambios | — | **3** · 3.8 | ninguna | no | existe artefacto derivado legible sin herramienta para los `deriva` sin reparar, o la justificación del marcador se rehace sobre lo que de verdad compra |
| `A9` | MEDIO | defecto de F4 | `11-ARQ` L1856‑1858 · L1771‑1776 · L1296 · L1457 · **L1681‑1682 / L1878‑1880** (cita corregida por C) † | confirmado sin cambios | — | **3** · 3.9 | ninguna | no | una autoridad nombrada puede cerrar el desenlace `4b`, o `X58`/L1457 dicen bloqueo acotado **por acto de autoridad** |
| `A10` | MEDIO | defecto de F4 (recuento) | `11-ARQ` L100 · L6871 · L7073 † | confirmado sin cambios | `O15` | **4** · 4.4 | `m-1` (misma raíz, dos sedes) | no | L100 → «DIEZ puntos» |
| `A11` | MENOR | prueba escrita | `11-ARQ` L2816 · L7060 · L968/L1348/L1439 † | **absorbido por `M-8`** (unificación del propio `C`, §5(a).1) | `D64` | **4** · 4.2 | `M-8` | no | se cierra con `M-8`; no tiene condición propia |
| `A12` | MENOR | defecto de F4 | `11-ARQ` L2041‑2043 · L2277‑2279 · L2312 · L1936‑1942 † | confirmado sin cambios | §88 `APROBADA` | **4** · 4.6 | ninguna | no | «un único escritor» retirado de L2041 y L1929 de la lista de protecciones de la rama canónica |
| `A13` | MEDIO *(subido por C)* | contrato derivado | `11-ARQ` L3654 † | confirmado sin cambios | `G1`/`a.9` | **3** · 3.2 | `A7` (misma raíz) | no | fila `preparada` de §3.6 L3654 corregida |
| `M-1` | MEDIO | defecto de F4 (recuento) | §4.3 **L4174** (enumera 13, dice «CATORCE») · tabla **L4191** («14») — **verificado por mí** | confirmado sin cambios | `O8`, `D68` | **4** · 4.1 | `G-4` | no | L4174 y L4191 dicen **TRECE**, o se declara cuál es la decimocuarta |
| `M-2` | MEDIO | defecto de F4 | §1.3 L183‑205 · L4156 · `PN-12` L6862‑6863 † | confirmado sin cambios | `PN-12` | **3** · 3.4 | `G-4` | no | §1.3 tiene la fila del mapa documental, o L4156 y `PN-12` dejan de invocarla |
| `M-3` | MEDIO | defecto de F4 | §18 **L6999** · §8.4 **L5464‑5466** | confirmado sin cambios; **cerrada la salida por autoridad del Owner** (§5 de E, verificada por mí: `grep` vacío en `APROBADA`) | `O12`, `D67` | **3** · 3.3 | `F-09` | no | `U6` tiene **un** gate, coherente en §18 y §8.4 |
| `M-4` | MEDIO | defecto de F4 vs registro | `DECISIONES` L236 · §18 **L7012**, **L7018‑7020** | confirmado sin cambios | `D67` | **4** · 4.5 | ninguna | no | el resumen de `D67` en el registro dice «propagar a las fuentes, `proceso:DEP`» |
| `M-5` | MEDIO | defecto de F4 (autoridad silenciosa) | §5.3 L4327‑4340 † · **prueba nueva:** `entrada/*.md` sin una sola mención de `AUD`, `auditoría` ni `O7` (`grep` mío, salida vacía) · `entrada/02-CIRCUITO` L154‑157 | **confirmado con alcance ampliado.** Severidad MEDIO **intacta** — sostener GRAVE exigiría demostrar que la apertura ocurre hoy, y nada está construido | `O7` | **3** · 3.5 | `M-6` (dos caras del mismo hueco) | no | `APERTURA` y `CAMPAÑA` tienen actor nombrado en §5.3, **y** la ficha de esa capacidad lo autoriza (`C1`: autoridad de rol ⊆ autoridad de capacidad) |
| `M-6` | MEDIO | defecto de F4 | `ENC/CAPACIDAD.md` **L35‑38** (cuatro entradas, **todas ancladas al Owner**) · §5.2 L4296‑4305 † · **prueba nueva:** `03-FORMAS` **L552** «11 en otro caso → `forma:idea-inmadura`» | **confirmado con alcance ampliado.** Severidad intacta. El remedio 3.11 del doc 16 («añadir una línea a la ficha») es **insuficiente**: todo el aparato de entrada tiene un solo sujeto, el Owner | `O7` | **3** · 3.11 | `M-5` | no | existe clase, forma **y rama del algoritmo** para un finding originado por el sistema, y la extensión de ficha de `ENC` queda registrada en §5.2 y §17 |
| `M-7` | MEDIO | defecto de F4 | `a.7` L549‑563 · `11-ARQ` L6197 † | confirmado sin cambios | `a.7` FRENO 3 | **3** · 3.7 | ninguna | no | §8 declara cómo interactúa cada macrocircuito con el FRENO 3, **y** cuántos items compone cada uno |
| `M-8` | MEDIO | defecto de F4 + prueba escrita | §19 L7060 · §2.9 L2816 · §2.1 L269‑283 † | **confirmado sin cambios.** Rechazo la absorción que D propone: la colisión `N<n>` es sede y remedio distintos → `F-03` | `D64` | **4** · 4.2 | absorbe `A11`; **el remedio 4.2 se amplía con `F-03`** | no | `R1`–`R9` retiradas de §19 L7060 y §2.9 L2816, y el conjunto retirado renombrado |
| `M-9` | MEDIO | defecto de F4 | §8.2 **L5199**, **L5219** · `BRIEF` §6.2 L435‑451 † · §15.2 L6289 † | **confirmado con alcance reducido en una fracción** (D y E coinciden): para la materia de diseño el contenido ya existe y es calculable (`03-ESCALA` L16‑50). Severidad intacta | `O8`, `O12`, `O14` | **3** · 3.6 | `G-3`, `G-4` | no | las preguntas que `A3` debe responder están declaradas, o §8.2 remite explícitamente al §6.2 de la directiva como su contrato |
| `m-1` | MENOR | defecto de F4 (cifra derivada) | `DECISIONES` L366 · §16 L6871 · §19 L7073 † | confirmado sin cambios | `O15` | **4** · 4.4 | `A10` | no | nota al pie de `O15` que reancle la cifra sin tocar la resolución |
| `m-2` | MENOR | editorial | `DECISIONES` **L271‑280**, L282‑312, L313 | confirmado sin cambios | `O7`–`O14`, `O16` | **4** · 4.7 | ninguna | no | la nota de procedencia de `O7`–`O14` precede a la sección de `O16` |
| `m-3` | MENOR | asimetría; **el juicio, no asumido** | §5.2 L4269 † · `PLT/CAPACIDAD.md` **L11‑13** | confirmado sin cambios. D aporta una tercera sede (`C2 perfil:plataforma`, no reverificada por mí) y **no lo resuelve**, como no lo resolvió `C` | — | — (sin remedio en doc 16) | ninguna | **sí, si se quisiera convertir en defecto**: es preferencia de diseño | ninguna exigible: el hecho está confirmado y el juicio no se asume |
| `m-4` | MENOR | editorial (inferencia rechazada por C) | §8.4 L5435‑5438 † · §18 **L6999** | confirmado sin cambios | `D67` | **4** · 4.7 | ninguna | no | §18 rotula `U5a` |
| `A14` | *(excluido: no es defecto de F4)* | **limitación aceptada con procedencia aprobada** + implementación ausente | `tooling/workspace.py` **L18‑22** · `APROBADA` **L371‑372** y **L1359** · entorno **Python 3.10.12** · `grep python_requires` → **vacío** (todo verificado por mí) | **excluido, y su procedencia documentada.** Adjudico entre D (amplía) y E (mantiene la exclusión): **ambos tienen razón** — sigue fuera del conjunto de defectos de F4, y la aportación de D es correcta y verificable | `APROBADA` §6.2, §36 | **4** · 4.8 | ninguna | no | `python_requires ≥ 3.11` declarado en el tooling y comprobado antes de correr, para que `T148`/`T159` no suban a certificación |
| **`F-01`** | **MEDIO** | preexistente propagado por F4 | `01-PROCESOS` **L433‑434** · `00-CIRCUITOS` **L166** · §8.2 **L5209** · contra `diseno/00` **L109‑116** y `03-ESCALA` **L44‑50** | **nuevo, consolidado** (`ND-2` + `E-2`) | `D67`; §18 nota **L7003‑7005** | **1** *(1.3 lo nombra literalmente)* | `B-1`, `F-02` | no | `DIS/Reconstruccion` sustituido por `DIS` en el condicional de `proceso:AUD`, en el grafo de `00-CIRCUITOS` y en §8.2 L5209; la condición `C-DIS` no cambia; el método lo calcula la escala |
| **`F-02`** | **MEDIO** | preexistente del kernel | `esquemas/proceso.yaml` (`capacidad: {tipo: texto}`) · `01-PROCESOS` distribución completa derivada por mí | **nuevo** (`E-3`), confirmado y reforzado | `D67`; remedio (c) de 1.3 | **1** *(parte de sustitución)* + **3** *(parte de tipado — nuevo 3.12)* | raíz de `B-1` y de `F-01` | no | vocabulario del campo fijado y declarado; `capacidad` y `capacidad_productora` tipados como `ref_a: capacidad` en `esquemas/proceso.yaml`; `DIS/Reconstruccion` → `DIS` y `OWNER` → la autoridad que corresponda |
| **`F-03`** | **MEDIO** | defecto de F4 sobre espacio preexistente | `C6` **L29‑42** · `C5` **L76** · §8.1 **L5090** · §18 **L6990** | **nuevo, consolidado** (`ND-3` + `E-1`). Severidad adjudicada entre D (MENOR) y E (MEDIO) | `D64` (remedio 4.2) | **4** *(amplía 4.2)* | `M-8` | no | uno de los dos espacios `N<n>` renombrado (natural: fases → prefijo, `INS-0`…`INS-7`), comprobado con la misma prueba que se cree para `R1`–`R9` |
| **`F-04`** | **MEDIO** | preexistente del kernel | `05-ESCENARIOS` **L76**, **L180‑181**, **L219**, `T75` **L332** · contra `04-INCERTIDUMBRE` **L31‑34** · `encuadre.yaml` **L39** | **nuevo** (`E-4`), confirmado; **cita de E corregida** (no L205‑207) | `A-19` (hallazgo previo) | **3** *(nuevo 3.13)* | ninguna | no | `05-ESCENARIOS` L181 → `grado_inicial: alta`, conservando `grado: media`; y `T75` comprueba que `grado_inicial` coincide con el grado del paso 5 |
| **`F-05`** | **MENOR** | editorial + implementación ausente | `C5` **L36‑37** vs `00-CIRCUITOS` **L238‑240** · `C5` **L14** y **L107‑109** · `handoff.yaml` (`checkpoint` obligatorio) · §15.7 **L6386** | **nuevo, reformulado a la baja** (`ND-1`). Lectura fuerte **desactivada** (§5) | `O10` no aplica; §15.7 | **1** *(mitad material, dentro de 1.4)* + **4** *(mitad editorial)* | `B-2` | no | (i) una de las dos frases cede, o `C5` L36 se acota expresamente a la forma; (ii) queda declarado qué checkpoint viaja entre `PLT`, `SIS` y `VER` en los cuatro macrocircuitos; (iii) §15.7 registra la excepción de `C5` con la disciplina de `C6` y `C7` |
| **`F-06`** | **MENOR** | preexistente del kernel (ambigüedad) | `DIS-handoffs` **L137**, **L139**, **L144** · `02-RUBRICAS` **L214‑215**, **L277‑289** · `04-CICLO` **L7‑48** | **nuevo, reformulado a la baja** (`E-5`). **Rechazo la demostración de E** (§6.2) | `A-20` (hallazgo previo) | **4** | ninguna | no | el `cuando` de `dis-a-ver` queda anclado a una estación del ciclo, y la entrega nombra la pasada de la que procede el dictamen |
| **`F-07`** | **MENOR** | implementación ausente | `DECISIONES` **L276** (`O10`) · `docs/owner/*` **L3** de cada uno · `exclusiones.yaml` **L100‑105** | **nuevo** (`E-6`), confirmado | `O10`, `P-07` | **4** | `F-08` | no | cada fichero de `docs/owner/` lleva campo declarado `autoridad: aprobada \| trabajo`, comprobado por el validador que ya recorre el directorio |
| **`F-08`** | **MENOR** | editorial | `IDEAS` **L485**, **L487**, **L597** · `APROBADA` **L3** | **nuevo** (`ND-4`), confirmado; **no duplicado de `F-07`** | `O10` | **4** | `F-07` | no | consta anotación de vigencia o de sustitución que reconcilie el «NO IMPLEMENTAR SIN DISEÑO PREVIO» de `IDEAS` §15 con lo que `C6`, `C7` y §10 ya implementan |
| **`F-09`** | **MENOR** | presión normativa | `IDEAS` **L79‑81**, **L589** · §8.4 **L5427** · `grep` vacío sobre `APROBADA` | **nuevo** (`E-7`), confirmado | `O12`; `09-SINTESIS` L638 | **4** | `G-1`, `M-3`, `M-7` (los tres discuten `U`) | **no** para registrarlo como presión; **sí** para convertirlo en norma | §8.4 cita la procedencia y conserva el calificativo «provisional», **o** la ausencia de mandato aprobado para `U` queda registrada como presión normativa con la simetría que §16 se impone |
| **`F-10`** | **MENOR** | editorial | `03-FORMAS` **L3** (14 bloques, verificado) vs `01-TAXONOMIA` **L5‑6** (9 clases, verificado) | **nuevo** (`E-8`), confirmado y derivado por mí | — | **4** | ninguna | no | la cabecera de `03-FORMAS` deja de afirmar «uno por clase de expresión» |
| **`F-11`** | **MENOR** | editorial | `05-ESCENARIOS` **L5** vs sus `id:` reales (`T75`–`T80`, `T154`–`T157`) y `pruebas/T081-T085-…md` | **nuevo** (`E-9`), confirmado y derivado por mí | — | **4** | ninguna | no | la cabecera enumera las pruebas que el fichero contiene de verdad |
| **`F-12`** | **MENOR** | editorial **del documento 16** | doc 16 §4 (33 filas) vs su párrafo de recuento; **y** §7 «dieciocho» vs requisito 0.1 (diecinueve) | **nuevo, consolidado** (`ND-5` + `E-10` + instancia mía) | — | **0** *(nuevo 0.2)* | condiciona la sección 10 entera | no | el documento 16 declara **32 y 16** (y 31 distintos), y **diecinueve** fuentes; la sección 10 se redimensiona sobre esas cifras |

#### Recuentos al pie, derivados de los identificadores de la columna `id`

```text
POR SEVERIDAD (defectos de F4 abiertos)
  BLOQUEANTE  A1 · A2 · B-1 · B-2                                              =  4
  GRAVE       A3 · A4 · G-1 · G-2 · G-3 · G-4                                  =  6
  MEDIO       A5 · A6 · A7 · A8 · A9 · A10 · A13
              M-1 · M-2 · M-3 · M-4 · M-5 · M-6 · M-7 · M-8 · M-9
              F-01 · F-02 · F-03 · F-04                                        = 20
  MENOR       A11 · A12 · m-1 · m-2 · m-3 · m-4
              F-05 · F-06 · F-07 · F-08 · F-09 · F-10 · F-11 · F-12            = 14
                                                                       TOTAL   = 44
  EXCLUIDO    A14                                                              =  1
  FILAS                                                                        = 45
  DISTINTOS   44 − 1 (A11 absorbido en M-8)                                    = 43

POR ESTADO TRAS EL NIVEL 0
  confirmados sin cambios                                                      = 21
    A1 A2 A3 A4 G-1 G-2 G-3 A5 A6 A7 A8 A9 A10 A12 A13 M-1 M-2 M-3 M-4 M-7 M-8
  confirmados sin cambios, con prueba nueva citada                             =  2  (G-1, G-2 — contados arriba)
  confirmados con alcance ampliado o modificado                                =  6
    B-1 · B-2 · G-4 · M-5 · M-6 · M-9
  confirmados sin cambios (menores)                                            =  4  (m-1 m-2 m-3 m-4 — contados arriba)
  absorbidos por otro                                                          =  1  (A11 → M-8)
  excluidos del conjunto de defectos de F4                                     =  1  (A14)
  NUEVOS                                                                       = 12  (F-01…F-12)
  rechazados por mí                                                            =  0  hallazgos completos
                                                                                  3  PIEZAS: la lectura fuerte de ND-1,
                                                                                     la demostración de E-5, y la sexta
                                                                                     sede de A3 que D propone
  SEVERIDADES MOVIDAS                                                          =  0

POR CAUSA (los 44 abiertos)
  defecto de F4                                                                = 34
  defecto preexistente del kernel                                              =  3  (F-02 · F-04 · F-06)
  preexistente propagado por F4                                                =  1  (F-01)
  implementación ausente                                                       =  1  (F-07)  + mitad de F-05
  presión normativa                                                            =  1  (F-09)
  problema editorial                                                           =  4  (F-08 · F-10 · F-11 · F-12) + mitad de F-05
  limitación aceptada                                                          =  0  (la única, A14, está excluida)

EXIGEN DECISIÓN NUEVA DEL OWNER
  ninguno de los cuatro bloqueantes ni de los seis graves, con dos salvedades:
    G-3  sólo si se elige reinterpretar O12 en vez de registrar la presión
    F-09 sólo si se elige elevar a norma el principio provisional de U
  m-3  seguiría exigiéndola si alguien quisiera convertirlo en defecto     ── TOTAL condicional: 3
```

---

### 9 · Niveles 1–4 actualizados

La sección 10 del documento 16 sigue siendo válida en su estructura. Lo que sigue es **qué entra, qué sale y qué cambia de nivel** tras el nivel 0. Todo lo que no aparece aquí queda **exactamente como el documento 16 lo dejó**.

#### NIVEL 0 — actualizado

| # | qué tiene que ocurrir | estado |
|---|---|---|
| **0.1** | Cubrir las diecinueve fuentes obligatorias no leídas, con `C5-HANDOFF.md` leído **antes** de cerrar `B-2` | **SATISFECHO.** Ver §10 |
| **0.2** | **ENTRA.** Reanclar las cifras derivadas del propio gate: **32 defectos adjudicados / 16 medios** (31 distintos), y **diecinueve** fuentes obligatorias, no dieciocho. La sección 10 se redimensiona sobre esas cifras | **abierto** — cierra `F-12` |
| **0.3** | **ENTRA.** Transcribir al documento 16 las dos resoluciones del nivel 0, para que nadie las reabra: **(a)** `C5` **no** resuelve `B-2`, y la razón es estructural (§4); **(b)** en la tensión `C5` L36 / `00-CIRCUITOS` L238 **manda `00-CIRCUITOS`**, por el mapa de fuente única del kernel (§5) | **abierto** |

#### NIVEL 1 — los cuatro bloqueantes

| # | cambio | detalle |
|---|---|---|
| **1.1** | sin cambios | `A1` |
| **1.2** | sin cambios | `A2` |
| **1.3** | **CRECE** | `B-1` **+ `F-01` + la parte mínima de `F-02`**. El remedio (c) del documento 16 —«sustituir `AUD` y `DEU` por capacidades reales en las columnas de participantes»— **no basta**: la misma sustitución hace falta en el **condicional de `proceso:AUD`** (`01-PROCESOS.md` L434) y en el **grafo de `00-CIRCUITOS.md`** (L166), que son las sedes que §8.2 L5209 invoca. Y `OWNER` como `capacidad_productora` cae en el mismo saco |
| **1.4** | **CRECE** | `B-2` **+ la mitad material de `F-05`**. Se añaden tres precisiones probadas: **(i)** el hueco cubre **cinco** capacidades —`ENC`, `PRD`, `ARQ`, `DIS` y **`SEG`**—, no cuatro: la salida por consulta de origen libre sólo existe para `DOM`; **(ii)** ninguna instancia de handoff nombra a `SIS` ni a `PLT`, luego declarar el mecanismo de entrada **no basta si no se declara también qué checkpoint viaja**; **(iii)** el trabajo **no está en §8**: toca `01-PROCESOS.md` (condicionales), `esquemas/proceso.yaml` (vocabulario) y `circuitos/` (checkpoint), y §18 lo hace parecer lo contrario |
| — | **NO ENTRA** | La obligación de crear las instancias que faltan. `00-CIRCUITOS` L238 la desactiva (§5). Lo que entra es el **contenido del checkpoint**, no el bloque |

#### NIVEL 2 — los seis graves

| # | cambio | detalle |
|---|---|---|
| **2.1** | **evidencia reforzada, remedio intacto** | `G-1` deja de apoyarse en una sola sede: `handoffs-generales.md` **L107** declara que en **todo item `DEP`** `SEG` entrega a `CON` antes de construir, y ni `SEG` ni `CON` figuran entre los participantes de `U5b` |
| **2.2** | evidencia reforzada, remedio intacto | `G-2` |
| **2.3** | **SE ESTRECHA** | `A3`. **Sale** la sexta sede que D propone (`forma:continua`): rechazada (§6.3). Las sedes siguen siendo §7.4 L5008‑5013, §16 L6876 y §2.6.9 L1458 |
| **2.4** | sin cambios | `A4` |
| **2.5** | **CAMBIA DE MÉTODO, NO DE ALCANCE** | `G-4`. El remedio deja de ser «inventar doce identificadores»: **debe reutilizar** el patrón `ads:memoria` + `esquemas/memoria.yaml`, que ya declara `id · fichero · autoridad · caducidad · vacio_significa` con **doce ejemplares trabajados**, porque §4.3 L4147‑4149 dice derivar de ahí. Y debe hacerlo **sin crear una segunda sede editable** sobre «dirección visual» y «sistema de diseño», que ya tienen sede canónica (`I5`) |
| **2.6** | sin cambios | `G-3` |

#### NIVEL 3 — los medios

| # | cambio | detalle |
|---|---|---|
| 3.1 – 3.4 | sin cambios | `A7` · `A13` · `M-3` · `M-2` |
| **3.5** | **CRECE en exigencia, no en severidad** | `M-5`. Nombrar el actor **no basta**: `C1` fija que la autoridad de un rol es siempre subconjunto de la de su capacidad, luego nombrar a `DSP` exige que su ficha lo autorice. Y `grep` sobre los cinco ficheros de `entrada/` no encuentra ni una mención de `AUD`, `auditoría` ni `O7` |
| **3.6** | **SE APOYA EN ALGO QUE YA EXISTE** | `M-9`. Para la materia de diseño, el contenido del baseline **ya está escrito y es calculable**: las cinco variables de `03-ESCALA` L16‑50, observadas «mirando el producto —el control repo y sus fuentes—, no interpretando». El remedio puede derivar de ese patrón en vez de escribir catorce preguntas a mano |
| 3.7 – 3.10 | sin cambios | `M-7` · `A8` · `A9` · `A5` |
| **3.11** | **EL REMEDIO ESCRITO ES INSUFICIENTE** | `M-6`. «Añadir `capacidades/ENC/` a las extensiones de ficha» **no cierra** el hallazgo: el aparato entero de entrada tiene un solo sujeto, el Owner —nueve clases sobre su expresión, catorce formas sobre su expresión, cinco ejes sobre su expresión— y la cláusula de cierre del algoritmo (`03-FORMAS` **L552**, «11 en otro caso → `forma:idea-inmadura`») **manda todo finding de un `AUD` al vivero**. Hace falta clase, forma y **rama** |
| **3.12** | **ENTRA** | `F-02`, parte de tipado: fijar el vocabulario del campo `capacidad` y tipar `capacidad` y `capacidad_productora` como `ref_a: capacidad` en `esquemas/proceso.yaml`, declarando qué formas cualificadas (`SEG:condiciones`, `CON:experimental`, `ARQ:diagnostico`) son legales |
| **3.13** | **ENTRA** | `F-04`: `05-ESCENARIOS` L181 → `grado_inicial: alta`, y `T75` comprueba la coincidencia con el grado del paso 5 |

#### NIVEL 4 — recuentos, citas y sedes

| # | cambio | detalle |
|---|---|---|
| 4.1, 4.3 – 4.8 | sin cambios | `M-1` · `A6` · `A10`+`m-1` · `M-4` · `A12` · `m-2`+`m-4` · `A14` |
| **4.2** | **CRECE** | `M-8` ≡ `A11` **+ `F-03`**: el renombrado debe cubrir **dos** espacios de nombres colisionados, `R1`–`R9`/`R1`–`R8` **y** `N1`–`N14`/`N0`–`N7`, con una prueba común |
| **4.9** | **ENTRA** | `F-05`, mitad editorial: acotar `C5` L36 a la forma, o retirar la frase de `00-CIRCUITOS` L238; y registrar en §15.7 la excepción de `C5` con la disciplina de `C6` y `C7` |
| **4.10** | **ENTRA** | `F-06`: anclar el `cuando` de `dis-a-ver` a una estación del ciclo y nombrar la pasada de la que procede el dictamen |
| **4.11** | **ENTRA** | `F-07`: campo `autoridad: aprobada \| trabajo` en cada fichero de `docs/owner/`, comprobado por validador |
| **4.12** | **ENTRA** | `F-08`: nota de vigencia o de sustitución sobre la materialización multirrepo |
| **4.13** | **ENTRA** | `F-09`: §8.4 cita procedencia y conserva «provisional», o la ausencia de mandato aprobado para `U` se registra como presión normativa |
| **4.14** | **ENTRA** | `F-10` y `F-11`: cabeceras de `03-FORMAS` y `05-ESCENARIOS` reancladas a su contenido real |

**Resumen del movimiento:** entran **dos puntos al nivel 0**, **dos ampliaciones al nivel 1**, **cero al nivel 2** (dos cambian de método y uno se estrecha), **dos puntos nuevos al nivel 3** más dos ampliaciones de exigencia, y **seis puntos nuevos al nivel 4** más una ampliación. **Ningún punto sale de su nivel. Ningún hallazgo baja de severidad. Ningún hallazgo sube.**

---

### 10 · Cobertura: ¿está cerrado el nivel 0?

**Requisito 0.1, literal:** *«Cubrir las dieciocho fuentes obligatorias no leídas: `circuitos/DIS-handoffs.md`, `circuitos/handoffs-generales.md`, los seis de `diseno/`, `C1`, `C2`, `C3`, `C5`, los dos de `docs/owner/`, y `entrada/00`, `02`, `03`, `04`, `05`. Con `C5-HANDOFF.md` leído antes de cerrar `B-2`, porque puede contener su vehículo.»*

**Cuento la enumeración: 2 + 6 + 4 + 2 + 5 = diecinueve ficheros.** La prosa dice dieciocho. Verifiqué el total con `wc -l` sobre las diecinueve: **8 310 líneas**, exactamente la cifra que D y E declaran por separado.

> ## El requisito **0.1** está **SATISFECHO**.

**Con qué prueba.** D y E declaran cada uno lectura íntegra de las diecinueve, con cita comprobable de su primera y su última sección sustantiva y con el recuento de líneas derivado. Yo no reproduje las 8 310 líneas —no es mi encargo—, pero **verifiqué por muestreo dirigido a los puntos donde la lectura tenía que morder**, y en todos los casos la cita existía donde el dictamen la sitúa: `C5` íntegro, los diecisiete `id/de/a/cuando`, las condicionales de `AUD`, `SIS` e `INV`, `diseno/00` L109‑116, `03-ESCALA` L44‑50, `02-RUBRICAS` L214‑289, `04-CICLO` L7‑48, `03-FORMAS` L3/L468‑497/L534‑557, `04-INCERTIDUMBRE` L25‑40, `05-ESCENARIOS` L5/L76/L180‑181/L219/L332, las siete fichas `CAPACIDAD.md`, y los dos de `docs/owner/`. **De todas las citas que abrí, una sola no estaba donde su dictamen la ponía** —la de E a `04-INCERTIDUMBRE` L205‑207, en un fichero de 187 líneas— y su texto existe en L31‑34 del mismo fichero, de modo que el hallazgo (`F-04`) sobrevive con la referencia corregida.

**Y la cláusula condicional del requisito se cumplió en el orden que exige:** los dos leyeron `C5-HANDOFF.md` **antes** de pronunciarse sobre `B-2`, y D declara además haberlo leído antes de abrir el documento 16. La sospecha de `C` —«nadie miró ahí»— **está contestada, y en negativo**.

**Cobertura suplementaria que el nivel 0 cerró sin que el requisito lo pidiera:**

- `kernel/operativo/entrada/01-TAXONOMIA.md` (**309 líneas**), que §7 del documento 16 daba por cubierto sólo en «dos bloques `ads:entrada` de nueve» y del que `M-6` depende: **E lo leyó íntegro**. Verifiqué su recuento: **nueve** bloques `ads:entrada`. Esa cobertura parcial deja de existir.
- `kernel/operativo/circuitos/00-CIRCUITOS.md` (**240 líneas**): **D lo leyó íntegro**, lo declaró por delante, y sin él la discrepancia de §5 no se habría podido resolver. **Yo lo leí íntegro también.**

#### Qué sigue sin abrir en el corpus obligatorio

El requisito 0.1 no agota la tabla §7 del documento 16. Lo que sigue **sin cubrir por nadie** —ni A, ni B, ni C, ni D, ni E, ni yo—:

| fuente | estado real hoy |
|---|---|
| `packs/` más allá de cabeceras | **sin abrir.** Doc 16 dice «11 ficheros `.md`»; `find packs -name '*.md' \| wc -l` da hoy **24**. `rubrica:usabilidad` y `gate:excelencia-visual` **delegan en el pack instalado** la matriz de entornos, los criterios de accesibilidad exigibles y los presupuestos de respuesta |
| `kernel/operativo/esquemas/*.yaml` | **19 en total.** E abrió campos citados de `handoff`, `memoria`, `proceso`, `encuadre`; yo abrí `handoff.yaml` y `proceso.yaml` íntegros. **Quince siguen sin leerse** |
| `(a)`, `(b)`, `E1`, `E2` completos | **tramos y `grep` dirigido.** Y son la especificación **normativa** de la que todo lo demás deriva |
| `C4`, `C6`, `C7` completos | **parciales.** De `C6` sólo se han leído L29‑42; `C7` sólo por cita |
| `capacidades/<COD>/roles/`, `metodos/`, `prompts/` | **sin abrir**, quince capacidades |
| `validadores/*.py` línea a línea | **ejecutados por A, nunca auditados** |
| `tooling/tests/test_workspace.py` | **existe** y sigue **sin leerse ni ejecutarse** (`pytest` no instalado) |
| `11-ARQUITECTURA-INTEGRADA.md` §11 y §14 | **sin leer en detalle por nadie** |
| `K-1` (`KERNEL.md`) | **localizado, no leído** |
| `recorrido/` más allá de los tramos citados de `01-PROCESOS.md` | **parcial** |

> **Conclusión de cobertura.** El **requisito 0.1 está cerrado**; la **regla general del encargo del gate** —que el corpus obligatorio se cubra íntegro— **sigue sin cumplirse**. Son dos cosas distintas y el documento 16 las mezcló al escribir 0.1 sobre una lista más corta que su propia tabla §7. **El nivel 0, tal como está definido, queda cerrado. La laguna de cobertura del corpus, no.**

---

### 11 · Limitaciones de mi adjudicación

```text
1  NO rehice ninguna de las dos revisiones. Verifiqué las citas que sostienen una
   conclusión, no las 8 310 líneas de las diecinueve fuentes. Cuando escribo
   «confirmado», significa que la cita está donde el dictamen la pone y dice lo que
   el dictamen dice — no que yo haya releído la fuente entera.

2  Las filas marcadas con † en la matriz descansan en la verificación de C, no en la
   mía. Son todo el bloque A1–A13, A4, G-2 (§8.3), G-3 (§9.4), M-2, M-7, M-8, M-9
   (BRIEF y §15.2), m-1 y m-3. NO abrí §2, §3, §5–§7, §9–§14, §16, §17 ni §19 de
   `11-ARQUITECTURA-INTEGRADA.md`, ni C1, C2, C3, C4, C7, ni (a)/(b)/E1/E2. Su estado
   «confirmado sin cambios» significa que NADA de lo leído en el nivel 0 los toca.

3  Las pruebas nuevas que D aporta desde C1 y C2 —`perfil:seguridad`, `perfil:plataforma`,
   C1 L85-87, L118-122, L140-142— NO las reverifiqué: no abrí esos ficheros. Las registro
   como aportadas por D y E, que coinciden en ellas por caminos independientes, y las
   marco como refuerzo, no como base de ningún cambio de severidad. Ninguna conclusión
   mía depende de ellas.

4  NO ejecuté ningún validador ni ninguna prueba, salvo `python3 --version` para A14.
   Modo sólo lectura estricto. Nada de este corpus está construido: todos los hallazgos
   son sobre TEXTO y sobre esquema declarado.

5  Mi resolución de §5 descansa en tres pruebas convergentes, y la segunda —el mapa de
   fuente única de `00-INDICE.md`— es la decisiva. Si alguien sostiene que ese mapa no
   tiene autoridad sobre un contrato de `contratos/`, la resolución cambia y `ND-1`
   vuelve a su lectura fuerte. NO he encontrado en el kernel ninguna regla de precedencia
   explícita entre `contratos/` y el mapa de fuente única: `grep` de «prevalece»,
   «precedencia», «en caso de conflicto» sobre `kernel/operativo/*.md`, `contratos/*.md`
   y `circuitos/*.md` devuelve un solo resultado pertinente (`C4` L31, sobre otra materia).
   Lo digo porque es el punto más débil de esta adjudicación.

6  La severidad MEDIO de F-03 la fijé por calibración contra M-8, no por una regla escrita.
   D proponía MENOR. Es la única decisión de severidad en la que me aparto de uno de los
   dos revisores, y su justificación es un dato de D, no mío.

7  Mi rechazo de la demostración de E-5 descansa en leer «DIS cierra su capa» como
   posterior a la estación 11. NO hay en el corpus una frase que lo fije. Por eso no
   rechazo el hallazgo entero: lo reformulo como ambigüedad, que es lo único que la
   fuente sostiene.

8  NO he verificado el hallazgo §6(d) que C añadió por su cuenta (L1458), ni las cinco
   piezas que C rechazó, salvo la de B-2, que sí verifiqué y corregí (SEG).

9  NO emito veredicto de suficiencia y no lo insinúo. Ninguno de los cuatro bloqueantes
   ni de los seis graves se ha corregido; ni uno solo se ha retirado ni rebajado.
```

---

### 12 · Condición exacta para comenzar la tanda de corrección

**Sin veredicto de suficiencia.** El veredicto del gate —`INSUFICIENTE PARA F5`— es de `C` y no me corresponde tocarlo. Lo que declaro es qué hace falta para que la **tanda de corrección** pueda empezar.

> **La tanda de corrección puede comenzar cuando, y sólo cuando, se cumplan estas cuatro condiciones, todas comprobables y ninguna de ellas una corrección:**
>
> **C1 · Que el requisito 0.1 conste cerrado.** Lo está: las diecinueve fuentes obligatorias —**8 310 líneas**, verificadas— están leídas íntegras por dos revisores independientes, con cita de su primera y su última sección sustantiva, y `C5-HANDOFF.md` fue leído antes de pronunciarse sobre `B-2`. **Esta condición ya se cumple con esta adjudicación.**
>
> **C2 · Que la carga de trabajo se redimensione sobre las cifras derivadas, no sobre las declaradas.** Son **32 hallazgos adjudicados como defectos de `F4`** —4 bloqueantes, 6 graves, **16** medios, 6 menores—, **31 distintos** tras la unificación `A11 ≡ M-8`, más **12 hallazgos nuevos** del nivel 0 —4 medios y 8 menores—: **44 abiertos, 43 distintos**. No 29. Quien abra la tanda sobre la cifra de 29 dejará **tres medios del gate y cuatro medios nuevos** fuera del plan (`F-12`).
>
> **C3 · Que las dos resoluciones del nivel 0 queden escritas antes de tocar nada, para que no se reabran a mitad de la corrección:**
> **(a)** `C5` **no** resuelve `B-2`, y no lo resuelve por razón estructural: el sujeto de un handoff son dos capacidades, su disparador cita el criterio `C-<CAP>` que el proceso debe declarar, y el esquema no admite proceso ni fase. **Nadie tiene que volver a mirar ahí.**
> **(b)** En la tensión entre `C5` L36 y `00-CIRCUITOS` L238 **manda `00-CIRCUITOS`**, por el mapa de fuente única del propio kernel. **La ausencia de instancias de handoff no es, por sí sola, un defecto de conformidad.** Lo que sí queda abierto es el **contenido del checkpoint** entre `PLT`, `SIS` y `VER`, y eso se cierra dentro del remedio 1.4.
>
> **C4 · Que la corrección arranque por el nivel 1 con sus dos ampliaciones incorporadas**, porque son las que cambian **dónde** está el trabajo:
> **1.3** ya no se cierra sólo en §8.2 y §18: toca también el condicional de `proceso:AUD` (`01-PROCESOS.md` L434) y el grafo de `00-CIRCUITOS.md` (L166).
> **1.4** ya no se cierra en §8 en absoluto: toca `01-PROCESOS.md` (los condicionales), `esquemas/proceso.yaml` (el vocabulario del campo) y `circuitos/` (el checkpoint que falta). **§18 hace parecer que el trabajo está donde no está**, y quien empiece por ahí perderá la tanda.

**Y una condición que NO hace falta, y conviene decirlo porque ahorra una consulta.** **La tanda de corrección no requiere ninguna decisión nueva del Owner para empezar.** Lo verifiqué sobre los diez hallazgos de nivel 1 y 2 y sobre los doce nuevos: todos se cierran propagando decisiones que el corpus ya tomó correctamente en otra sede. Sólo **tres** puntos abrirían consulta al Owner, y los tres son **electivos y no bloquean el arranque**:

- **`G-3`**, únicamente si se elige **reinterpretar `O12`** en instalación en vez de registrar la presión normativa;
- **`F-09`**, únicamente si se elige **elevar a norma** el principio «detectar automáticamente, actualizar conscientemente», que el Owner declaró **provisional** en un documento de trabajo y que la norma aprobada no menciona;
- **`m-3`**, únicamente si alguien quisiera convertir en defecto lo que `C`, D y yo dejamos declarado como juicio no asumido.

**Lo que sigue exactamente igual que antes del nivel 0.** Los cuatro bloqueantes —`A1`, `A2`, `B-1`, `B-2`— y los seis graves —`A3`, `A4`, `G-1`, `G-2`, `G-3`, `G-4`— siguen en pie. **Ninguno retirado, ninguno rebajado, ninguna severidad movida en ninguna dirección.** Lo único que ha ocurrido en el nivel 0 es que ahora se sabe, con cita y con línea, qué dicen diecinueve documentos que nadie había abierto — y que **ninguno de ellos absuelve a `F4c`**: contienen la prueba de que el mecanismo que el gate sospechaba no está, doce defectos más, y una sola cláusula —la de `00-CIRCUITOS` L238— que retira una obligación que nadie había leído bien.
