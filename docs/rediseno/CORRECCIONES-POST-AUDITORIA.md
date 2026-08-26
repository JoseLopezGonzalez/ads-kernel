# CORRECCIONES POST-AUDITORÍA — resolución de los 33 hallazgos

> Fase de corrección posterior a la auditoría independiente. **Ningún hallazgo se cierra
> por haber cambiado la prosa**: cada uno tiene evidencia proporcional a su naturaleza, y
> los que se corrigieron con código llevan además una **infracción deliberada** que
> demuestra que su prueba falla cuando debe fallar.

## 1 · Rama base, commit base y procedencia

```text
rama base        origin/main   (rama por defecto de origin, detectada, no supuesta)
commit base      f5cf2bbf71fa063ee7b13a5f80ebf312fb77b871
                 «Merge pull request #1 …/claude/kernel-operativo-equipos-roles-s4dzfq»
                 su árbol es idéntico al de 953b8aa, el commit auditado
rama de trabajo  claude/kernel-operativo-correcciones-post-auditoria

auditoría        docs/rediseno/AUDITORIA-INDEPENDIENTE-LOCAL.md
                 recogida por `git cherry-pick -x b7a2ceb 4bc8aee`, que tocan ESE ÚNICO
                 fichero. Ambos commits llevan su línea «(cherry picked from commit …)»,
                 de modo que la procedencia queda escrita en el historial. No se hizo
                 merge de la rama antigua, ni reset, ni force push.
```

### Recuento de commits, derivado de Git

**La cifra no se escribe aquí: se deriva.** La entrega anterior escribió «18 commits» a
mano mientras la lista adjunta sumaba 19 y GitHub mostraba 19. Lo que se fija es el
desglose por clase, que sí es invariante, y el comando que da el total en cada momento:

```bash
git rev-list --count origin/main..HEAD                                # total sobre main
git log --format='%s' origin/main..HEAD | grep -c '^audit(kernel)'    # de auditoría
git rev-list --count HEAD..origin/main                                # por detrás  → 0
```

```text
2   commits de AUDITORÍA, incorporados por cherry-pick con su procedencia escrita
     — su prefijo es `audit(kernel)`, y es lo que los distingue
resto  commits de CORRECCIÓN, posteriores
0   commits por detrás de main
```

Escribir el total a mano aquí lo dejaría desactualizado en el commit siguiente, que es
exactamente el defecto que esta entrada corrige.

## 2 · Decisiones del Owner aplicadas

| | decisión | cómo se aplicó |
|---|---|---|
| **3.1** | `ENC` es la decimoquinta capacidad base | enmienda **E1** a la sección (a) |
| **3.2** | frontera exacta `ENC` / `DSP` | E1.1, más las prohibiciones recíprocas en ambas fichas |
| **3.3** | `ENC` **no** es equipo permanente | E1.2 · su ficha pasa a materialización bajo demanda · C4 sustituye «los dos equipos que no se retiran nunca» —que enumeraba tres— por la distinción de los tres conceptos |
| **3.4** | enmienda normativa controlada | documento propio, aviso de cabecera en (a) y siete marcas `[E1]` en los puntos exactos. **(a) no se reescribe.** (b) no se enmienda: b.7 sigue siendo cierta con E1.1 |
| **9.1** | dos gates independientes, crítica con autoridad real | conservado y **reforzado**: los dos gates son obligatorios en los cinco niveles; un rechazo por personalidad, actualidad o alma vuelve a exploración |
| **9.2** | umbrales 0.60 y 0.15 provisionales | declarados PROVISIONALES y calibrables por uso real |
| **9.3** | ninguna estadística inventada | «la mayoría de las expresiones terminan sin item» sustituida en los tres sitios donde aparecía |
| **9.4** | «básica, plana y sin alma» no produce dos items siempre | las cuatro salidas declaradas según el anclaje, con prueba cada una (T154–T157) |
| **9.5** | español como idioma canónico | declarado en `esquemas/00-LENGUAJE.md`, con la excepción de los identificadores técnicos estables. Comprobado por T153 |

### La enmienda E1, en concreto

`docs/rediseno/a-ENMIENDA-E1-ENC.md`. Sustituye por enumeración explícita: los recuentos de
a.0, a.3 y a.4; la función *Encuadre* de `DSP` en a.3; y la propiedad del *índice de lo
existente*. Confirma expresamente que **los equipos permanentemente activos siguen siendo
dos**, para que ningún contrato derivado añada un tercero. Deja intacto todo lo demás:
autoridad, vetos, frenos, paralelismo, checkpoint y las pruebas T01–T25.

## 3 · Matriz de resolución de los 33 hallazgos

Estado: **corregido** · **aceptado-como-deuda** · **sustituido** · **abierto**.

| id | gravedad | descripción comprobada | causa raíz | corrección realizada | prueba | negativo | estado |
|---|---|---|---|---|---|---|---|
| **A-01** | crítico | `ENC` era una 15ª capacidad sin encaje normativo, con el índice de lo existente y un tercer equipo permanente | (a) no la contemplaba y la decisión estaba pendiente | enmienda **E1** aprobada por el Owner; ficha de ENC, C4 y `packs/00-QUE-ES-UN-PACK` alineados | T151 (recuentos) | N151 | **corregido** |
| **A-02** | crítico | `./tooling/new-project.sh mi-web-app pack-web-app,pack-design-led` terminaba con código 3 | la documentación citaba packs retirados y el script validaba después de crear | script valida antes de crear, descubre packs por disco, lista los instalables al fallar; README y START_HERE corregidos; se envía `docs/rediseno/` con el kernel. **T148 ejecuta los tres packs sueltos y la combinación `wear-os,mobile-app`** que el checkpoint documenta como siguiente comando del piloto | **T148** | N148 | **corregido** |
| **A-03** | crítico | T131 en `prueba-superada` afirmando un comportamiento que su validador no ejecutaba | se leyó la salida del validador, no su código | T131 pasa al enunciado que sí sostiene; el comportamiento se demuestra en **T149** con fixtures | T131 · **T149** | N149 · N149b · N149c · N149d | **corregido** |
| **A-04** | grave | `kernel-status.sh` no veía los `.py`: un fork de los validadores era indetectable | la huella se calculaba sobre `.md` y `.yaml` | `huella.py` define la huella una vez: kernel, packs y tooling, con `.md .yaml .py .sh` | **T150** | N150 · N150b · N150c | **corregido** |
| **A-05** | grave | T134 pasaba por coincidencia de nombre; 119 de 188 ficheros exentos de hecho | la comprobación buscaba el basename como subcadena | `comprobar_referencias.py` construye el grafo por ruta normalizada; exclusiones explícitas con motivo | **T147** *(sustituye a T134)* | N147 · N147b · N147c · N147d | **corregido** |
| **A-06** | grave | DIS y DOM se arbitraban un veto que a.5 reserva al Owner | la cláusula `colision` se escribió sin contrastar con a.5 | los cuatro contratos de veto escalan al Owner; nuevo campo `levantable` que hace la regla comprobable | **T136** | N136 · N136b | **corregido** |
| **A-07** | grave | la rama N3 era inalcanzable: la Reconstrucción no se elegía nunca | N4 preguntaba «¿no existe memoria?», cierto también para brownfield | cinco variables del encuadre de diseño y condiciones **formales**; `memoria_vigente` exige fiable, no obsoleta y representativa | **T138** | N138 · N138b | **corregido** |
| **A-08** | grave | N0 y N1 se saltaban gates que el sistema declara obligatorios; tres documentos discrepaban | dos textos independientes sobre la misma verdad | una sola fuente: los bloques `ads:nivel-novedad`. Los dos gates son obligatorios en los cinco niveles; lo que cambia es la evidencia reutilizable | **T139** | N139 · N139b | **corregido** |
| **A-09** | grave | obligaciones, huérfanas y cierre sin portador operativo | el vocabulario de b.3/b.4/b.10 nunca se materializó | `recorrido/` con los seis conceptos, `gate:cierre-de-item`, los diez procesos canónicos y `plantillas/CIERRE.md` | **T140** | N140 · N140b · N140c | **corregido** |
| **A-10** | grave | los frenos de a.7 y b.9 sin ejecutor; la Supervisión de DSP sin materializar | se citaron en prosa y nadie los contaba | `DSP/supervision` y `DSP/Supervision`, independientes de quien recompone; tres comprobaciones nuevas en `gate:despacho-coherente` | **T141** | N141 · N141b · N141c · N141d | **corregido** |
| **A-11** | grave | el encuadre no podía declarar `esperando-owner`, y tenía `aparcado` como estado propio | un vocabulario de estados paralelo al de b.2 | dos campos: `estado` (madurez) y `estado_paquete` (b.2); las cuatro distinciones escritas | **T142** | N142 · N142b | **corregido** |
| **A-12** | grave | tres versiones para el mismo artefacto; el árbol del README era el de 1.3.0 | no había política de versiones, y ads_lint no miraba la portada | `kernel/VERSIONES.md` distingue cuatro versiones de cosas distintas; release a 2.0.0-alpha.2 | **T152** | N152 · N152b | **corregido** |
| **A-13** | grave | `gate:usabilidad` decía aplicarse a CON y nada lo vinculaba | el `aplica_a` se escribió sin portador | `gate:implementacion-completa` gana `superficie-usable`, con quién produce y quién juzga | **T144** | — | **corregido** |
| **A-14** | grave | la crítica de encuadre obligatoria podía evaporarse al bajar el grado | el gate miraba el grado FINAL | se persiste `grado_inicial`; el gate exige el dictamen por grado inicial, nivel de Owner o materialización | **T145** | N145 · N145b | **corregido** |
| **A-15** | medio | `ENC/Critica` existía, se usaba y se probaba, y su ficha no lo declaraba | T90 sólo cruzaba capacidades con roles | declarado en la ficha; **T90 pasa a cruzar también los métodos** | T90 | N90 | **corregido** |
| **A-16** | medio | C4 invocaba `composicion:dis-fundacion`, que no existe | el ejemplo se escribió antes que las composiciones | el ejemplo recorre las diez composiciones reales en su orden real | T147 *(enlaces)* | — | **corregido** |
| **A-17** | medio | constante muerta, rama inalcanzable y una comprobación declarada que no existía | el validador no se leyó, sólo su salida | código muerto eliminado; la comprobación de gates que SUMAN existe y encontró un choque real (`cinco-estados`) | T132 | — | **corregido** |
| **A-18** | medio | T86 verificaba sólo el veto y su nombre prometía toda la autoridad | la prueba se nombró por la intención, no por lo que hacía | T86 renombrada a lo que verifica; **T146** cubre lo mecánicamente comprobable y declara qué NO comprueba | T86 · **T146** | N146 · N146b | **corregido** |
| **A-19** | medio | la incertidumbre ALTA tenía dos consecuencias incompatibles, y una tercera en otra tabla | tres textos sobre la misma condición | un solo desenlace: activa la crítica y detiene la entrega | T145 | N145 | **corregido** |
| **A-20** | medio | el eje `fidelidad` se exigía cuando aún no hay construcción que comparar | el gate no declaraba sus dos pasadas | las dos pasadas declaradas: ocho ejes en diseño, `fidelidad` en la de fidelidad | T139 | — | **corregido** |
| **A-21** | medio | `intencion` y `jerarquia` podían rechazar sin destino de retorno | la tabla de retornos cubría siete de nueve ejes | los nueve tienen destino, en 04-CICLO y en el prompt del crítico | T153 | — | **corregido** |
| **A-22** | medio | `handoff:cierre-a-apr` con emisor USO, que es condicional; sin `handoff:con-a-ver` | el emisor se eligió por el circuito típico, no por el disparador | emisor pasa a DSP con el motivo escrito; se declara `handoff:con-a-ver` | T147 | — | **corregido** |
| **A-23** | medio | `DSP/estado` **decidía** una cancelación, que b.7 le niega | el texto se copió de b.8 sin contrastar con b.7 | la cancelación sale de `decide` y entra en `propone`; nuevo límite y nueva comprobación de gate | **T137** | N137 | **corregido** |
| **A-24** | medio | once recuentos en prosa contradecían al corpus | las cifras se escribían a mano | `comprobar_recuentos.py` deriva 26 cifras y comprueba una tabla explícita de dónde se afirman | **T151** | N151 | **corregido** |
| **A-25** | medio | «lo más restrictivo gana» no era computable | faltaba la dirección de monotonía de cada propiedad | `propiedades_medibles` con `direccion`, `unidad` y `valor` sólo cuando es del medio; resolutor puro | **T149** | N149 | **corregido** |
| **A-26** | medio | 04-CICLO afirmaba que las seis omisiones tienen gate; la 12 no lo tiene | la afirmación se escribió sin recorrerla | cinco se nombran con su comprobación; la estación 12 se declara como límite del kernel | — *(documental)* | — | **corregido** |
| **A-27** | menor | exención de vocabulario por fichero completo: 19 exentos | la exención se diseñó como marca de cabecera | exención por RANGO y por línea, con motivo; al retirar las 19, sólo DOS la necesitaban | ads_lint | — | **corregido** |
| **A-28** | menor | ads_lint dejaba fuera README, START_HERE, KERNEL.md, plantillas y docs | el ámbito por defecto eran dos directorios | enlaces y vocabulario en los 217 documentos del repositorio; 10 exentos de vocabulario con motivo. **Encontró un caso real**: una fórmula no comprobable en `AGENTS_EXAMPLE` para decidir cuándo interviene el Owner | ads_lint · T147 | — | **corregido** |
| **A-29** | menor | el pack `wear-os` se identifica por una plataforma concreta | el identificador nombra la clase por su ejemplo más reconocible | **decisión declarada** en el propio PACK.md, con qué la haría revisable | — *(documental)* | — | **corregido** |
| **A-30** | menor | profundidad muy asimétrica: DIS con 11 roles frente a 1–3 de las demás. **La asimetría existe y es real** | DIS se construyó deliberadamente como patrón de calidad, no como plantilla mecánica | **no se corrige en esta fase**, por decisión: la profundidad de las demás capacidades crecerá con el uso real, no antes. Se registra para que «equipos y métodos de las demás capacidades» no se lea como paridad de profundidad | — | — | **aceptado-como-deuda** |
| **A-31** | menor | el umbral de anclaje cambia de capa entre (b) y el kernel | (b) los sitúa en el runtime, que no existe | declarados PROVISIONALES, con dónde viven mientras no haya runtime y quién los calibra | — *(documental)* | — | **corregido** |
| **A-32** | medio | `CHECKPOINT-OPERATIVO.md` desactualizado respecto al commit que declaraba terminado | se actualizó antes del último commit, no después | reescrito por completo, con las cifras derivadas y el punto exacto de continuación | T151 | — | **corregido** |
| **A-33** | menor | la decisión O3 citaba `entrada/03-CLASIFICACION.md`, que no existe | la ruta cambió y la cita no | corregida a `entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` §3; O1 marcada RESUELTA por E1 | ads_lint *(ámbito ampliado)* | — | **corregido** |

**Resumen:**

```text
32  corregidos con evidencia
 1  ACEPTADO COMO DEUDA no bloqueante — A-30, la asimetría de profundidad, que existe y
    no desaparece: se acepta y se registra, no se cierra
 0  hallazgos sin disposición
 0  bloqueos abiertos
```

`aceptado-como-deuda` **no es** «no reproducible». La asimetría es real y comprobable; lo
que se decide es no corregirla ahora. Presentarla como desaparecida sería exactamente el
defecto que esta fase existe para no repetir.

## 3.b · Defecto de la propia entrega: la evidencia publicada estaba corrupta

> El Owner contrastó la rama publicada y encontró que **ocho de diez ficheros de evidencia
> del commit `68b3383` contenían `python3: can't open file`**, mientras el informe afirmaba
> «todos EXIT 0», «evidencia reproducible» y «27 pruebas superadas». Es el defecto más
> grave de esta fase, porque no estaba en el corpus: estaba en lo que demostraba el corpus.

**Causa exacta.** El bucle de shell que archivó las salidas construía el nombre del script
**sin la extensión `.py`**:

```bash
case $v in contratos) f=comprobar_contratos;; ... esac      # ← falta el .py
python3 kernel/operativo/validadores/$f > .../$v-salida.txt 2>&1
```

Tres fallos que se sumaron, y ninguno solo habría bastado:

```text
1  EL NOMBRE SIN EXTENSIÓN     python3 no encontraba el fichero y abortaba
2  `2>&1`                      el error del intérprete se escribía DENTRO del fichero de
                               evidencia, sobrescribiendo evidencia que era válida
3  SIN COMPROBAR EL CÓDIGO     se publicaba primero y no se comprobaba después: publicar y
                               verificar eran el mismo gesto, y ninguno verificaba nada
```

`lint-salida.txt` e `integridad-salida.txt` se salvaron porque se escribieron en
invocaciones separadas que sí llevaban `.py`. Los otros ocho quedaron con el mensaje de
error como único contenido.

**Ficheros reparados** —los ocho, republicados por el runner desde una ejecución real:

```text
arranque-salida.txt · contratos-salida.txt · negativos-salida.txt · packs-salida.txt
prompts-salida.txt · recuentos-salida.txt · referencias-salida.txt · versiones-salida.txt
```

**Qué impide que vuelva a ocurrir.** No se han editado los `.txt` a mano: eso habría
escondido la causa.

```text
validadores/validadores.yaml        el manifiesto CANÓNICO: qué hay en validadores/, de
                                    qué tipo, qué evidencia produce, y qué firma de éxito
                                    y qué identificadores debe contener esa evidencia

validadores/registrar_evidencia.py  el runner ÚNICO. Descubre del manifiesto, invoca por
                                    ruta completa terminada en .py y comprueba que el
                                    fichero existe ANTES de ejecutar; captura stdout,
                                    stderr y código POR SEPARADO; escribe en temporal y
                                    publica con os.replace (atómico) SÓLO si el código fue
                                    cero; termina con código no cero si algo falla

validadores/comprobar_evidencia.py  T158. Comprueba lo publicado: que exista, que no
                                    contenga errores de invocación ni trazas, que lleve
                                    cabecera de procedencia con su orden y su código, que
                                    la orden invoque un `.py`, que el código sea cero, que
                                    contenga la firma de éxito y los identificadores de SU
                                    validador, que no sea la evidencia de otro, y que todo
                                    `.py` de validadores/ esté en el manifiesto
```

Cada evidencia lleva ahora su cabecera, y el `stderr` —cuando lo hay— se conserva
**identificado**, nunca mezclado con la salida:

```text
# evidencia de: contratos
# orden:        python3 kernel/operativo/validadores/comprobar_contratos.py
# codigo:       0
```

**Seis infracciones deliberadas** demuestran que T158 falla cuando debe: se archiva una
invocación sin `.py` (el defecto exacto), una evidencia afirma éxito sin la salida que lo
respalda, la evidencia de un validador ocupa el fichero de otro, se publica una ejecución
con código no cero, falta un fichero exigido, y un validador nuevo queda fuera del
manifiesto.

**Lo que esto cambia en el informe anterior:** los validadores **sí** estaban en verde —lo
que fallaba era el archivado—, pero **el informe no tenía derecho a afirmarlo**, porque su
propia evidencia decía lo contrario. La afirmación se sostiene ahora sobre una ejecución
publicada por el runner y comprobada por T158.

## 4 · Hallazgos nuevos encontrados durante la corrección

Ninguno de estos estaba en el informe. Los cuatro se encontraron **ejecutando**, no leyendo.

| | qué | cómo apareció | resolución |
|---|---|---|---|
| **N-01** | **un proyecto recién creado no era conforme**: once enlaces rotos | ejecutar `ads_lint` DENTRO del proyecto que `new-project.sh` acababa de crear | el kernel se envía con `docs/rediseno/`; el índice y `00-QUE-ES-UN-PACK` dejan de enlazar packs que pueden no estar instalados |
| **N-02** | T131 fallaba en un proyecto instalado: exigía que el otro pack EXISTIERA | el mismo experimento | la compatibilidad pasa a comprobarse por **simetría cuando ambos están presentes**, no por existencia |
| **N-03** | `gate:web-estados-de-red` repetía la comprobación `cinco-estados` del kernel con otro significado | la comprobación de A-17 al implementarse de verdad | renombrada a `cinco-estados-de-red` |
| **N-04** | la plantilla `AGENTS_EXAMPLE` remitía el gate del Owner a una fórmula no comprobable | ampliar el ámbito de ads_lint (A-28) | sustituida por las cinco filas de a.8 |

Ninguno exigió una decisión estratégica no autorizada, y por eso ninguno detuvo la fase.

## 5 · Cambios por área

```text
docs/rediseno/     enmienda E1 · aviso y siete marcas en (a) · O1 resuelta · O3 corregida

kernel/            VERSIONES.md nuevo · VERSION a 2.0.0-alpha.2 · CHANGELOG con entrada
                   nueva y con la corrección de las cifras de la anterior
                   templates/AGENTS_EXAMPLE corregido

kernel/operativo/  recorrido/ NUEVO — obligaciones, cierre y los diez procesos
                   esquemas/ — nivel-novedad y proceso nuevos; veto gana `levantable`;
                     encuadre gana `estado_paquete` y `grado_inicial`; pack gana
                     `propiedades_medibles`; ads_lint gana el tipo `numero`
                   capacidades/ — ENC (E1, ENC/Critica) · DSP (supervisión, cancelación)
                     · DIS (crítica en dos pasadas y modo reutilización) · CON (usabilidad)
                     · DIS/DOM/SEG/VER (colisión de vetos)
                   diseno/ — escala de novedad formal · gates por nivel · dos pasadas ·
                     retornos de los nueve ejes · estación 12 declarada
                   entrada/ — estados del encuadre · incertidumbre alta · umbrales
                     provisionales · las cuatro salidas de la expresión subjetiva
                   circuitos/ — handoff:con-a-ver nuevo · cierre-a-apr retipado
                   plantillas/ — CIERRE.md nuevo · ENCUADRE actualizado
                   prompts/ — los 42, con su bloque «Cómo cierras» y su enlace al método
                   validadores/ — SIETE nuevos: huella, integridad, referencias, arranque,
                     versiones, recuentos, prompts, composicion_packs y negativos
                   pruebas/ — T136 a T157 · fixtures · RECUENTOS-generado

packs/             propiedades_medibles en los tres · COMPOSICION con P1 computable ·
                   00-QUE-ES-UN-PACK con quince códigos · wear-os con la decisión A-29 ·
                   web-app con la comprobación renombrada

tooling/           new-project.sh valida antes de crear y envía la especificación ·
                   kernel-status.sh llama a huella.py en vez de recalcular
```

## 6 · Revisión individual de las 42 unidades de instrucción

**Vocabulario, fijado para que no contradiga el recuento canónico:**

```text
36  PROMPTS CANÓNICOS con fichero propio, en capacidades/<COD>/prompts/
     ← es lo que cuenta el recuento canónico `prompts: 36`
 6  UNIDADES DE INSTRUCCIÓN EMBEBIDAS, como sección del contrato de un rol de pack
42  UNIDADES DE INSTRUCCIÓN revisadas en total
```

Llamar «42 prompts» al conjunto contradecía el recuento derivado, que cuenta 36 ficheros de
prompt y 42 roles. La entrega anterior lo hacía, y se corrige aquí, en el validador, en la
prueba T153 y en la salida archivada.

> La auditoría revisó a fondo **una** de las unidades y de ese único contraste salieron dos
> hallazgos. Su advertencia fue explícita: «no es prudente suponer que los otros treinta y
> cuatro estén limpios». Se han revisado **las 42**, cada una contra su contrato, su método,
> su capacidad y la autoridad normativa.

**El hallazgo transversal.** No fue una unidad mala: fue que **casi ninguna nombraba el gate
contra el que cierra ni cuándo escribir checkpoint**, y muchas no decían qué entregan ni
cuándo devuelven. Una unidad de instrucción es lo único que el agente carga: lo que no está
en ella, no ocurre. Las 42 ganan un bloque **«Cómo cierras»** derivado de su propio contrato
—salida, gate, checkpoint, devolución, bloqueo y escalado, con las palabras del contrato—, y
las 36 con fichero propio ganan el enlace a su método, que no tenían.

**La comprobación mecánica** la ejecuta `comprobar_prompts.py` (**T153**) sobre nueve puntos:
quién la declara, enlaces de cabecera, conversación con el Owner sin autoridad, gate,
salida, devolución, checkpoint, atribución de lo que la capacidad escala, e idioma. Salida
completa en `pruebas/evidencia/prompts-salida.txt`.

> **T153 es ESTRUCTURAL Y HEURÍSTICA, y su enunciado se acotó a eso.** Antes afirmaba «cada
> prompt es coherente con su contrato, su método y su capacidad», que es más de lo que
> puede demostrar: comprueba enlaces, presencia de señales textuales y comparaciones
> aproximadas de autoridad y de idioma. Su enunciado es ahora:
>
> ```text
> «Cada unidad de instrucción declara y enlaza las señales estructurales que su
>  contrato exige»
> ```
>
> La coherencia **semántica** —si enseña de verdad a hacer el trabajo, si su tono induce a
> inventar— no la decide ninguna medida de texto. Es la tabla de abajo, y es una **revisión
> humana documentada**, no algo que T153 certifique.

**La lectura individual**, que es lo que ninguna medida de texto puede hacer:

| unidad | qué comprueba su lectura | resultado |
|---|---|---|
| `ENC/interlocutor` | conserva la literal antes de interpretar; persiste antes de preguntar; no crea items | **conforme**; le faltaba el enlace a sus cuatro métodos |
| `ENC/anclaje` | tres términos antes de decir que algo no existe; busca lo que contradice; no interpreta ni propone | **conforme**, es de los más precisos del corpus |
| `ENC/critica-de-encuadre` | lee la literal ANTES que la interpretación ajena, para no ser un eco | **conforme** |
| `PRD/definicion` | empieza por el fuera de alcance; separa problema de solución; **propone** prioridad, no la fija | **conforme** |
| `PRD/criterio-de-exito` | criterio verificable por un tercero; fracaso ≠ negación del éxito; no disfraza juicio de medición | **conforme** |
| `ARQ/encaje` | mide y no estima; dos alternativas con coste; devuelve a DIS **con** alternativa; seis condiciones de paralelismo | **conforme**, ejemplar |
| `ARQ/diagnostico` | reproduce antes de explicar; la causa cubre TODOS los síntomas; distingue defecto de gap | **conforme** |
| `DOM/modelo` | condiciones antes de construir; busca consumidores en el repositorio; veto con evidencia mínima; **la pérdida la decide el Owner** | **conforme** |
| `DOM/migracion` | una reversión no ejecutada no es una reversión; datos reales; ventana de incompatibilidad declarada | **conforme** |
| `CON/implementacion` | no redecide: devuelve; lee buscando huecos de autoridad | **conforme** |
| `CON/experimental` | criterio de descarte **antes**; no integra: propone item nuevo | **conforme** |
| `VER/dosier` · `VER/decision` | evidencia que viaja, no un sí/no; `VER:decisión` no sustituye la preferencia del Owner | **conforme** |
| `ENT/despliegue` | comprobar la vuelta antes de ir; la publicación es materia reservada, sin excepción por contexto | **conforme** |
| `ENT/observacion` | los cinco requisitos del rollback, uno a uno; atribuye antes de revertir | **conforme** |
| `USO/validacion` | el Owner es UNA fuente de siete; por lotes; registra comportamiento, no opinión | **conforme** |
| `INV/investigacion` | no empieza sin consumidor; contesta la pregunta que le hicieron; puede declarar que no se puede decidir | **conforme** |
| `SEG/condiciones` | veto duro con alcance estrecho y evidencia exacta; llega antes | **conforme** |
| `PLT/maquinaria` | empieza por un bloqueo, no por una idea; lo que sólo funciona en su máquina no existe | **conforme** |
| `APR/promocion` | la regla de las dos ocurrencias; «sin aprendizaje promovible» es resultado normal; una regla sin comprobación no cambia nada | **conforme** |
| `SIS/coherencia` | **no escribe contenido por nadie**: crea item y enruta | **conforme** |
| `SIS/evolucion` | exige la justificación de producto; recuerda el freno de racha; **no toca las secciones aprobadas** | **conforme** |
| `DSP/enrutamiento` | autoridad total sobre orden, ninguna sobre contenido; traza de lo no activado; seis condiciones | **conforme** |
| `DSP/estado` | «Continúa» es trabajar, no informar; las órdenes no se pierden | **corregido**: preguntaba por esperas no viables y **no decía qué hacer**. Ahora declara las tres salidas de b.8 y cuál no es suya |
| `DSP/supervision` | **nuevo** (A-10): los cuatro contadores con sus umbrales aprobados; la inanición se ve y no se arregla | **nuevo** |
| `DIS/direccion-artistica` | lee la memoria antes de proponer; no pregunta en abstracto: enseña | **conforme** |
| `DIS/critica-visual` | no propone, juzga; sin «conforme con reservas» | **corregido**: le faltaban las **dos pasadas** del gate, el **modo reutilización de N0** y el destino de `intencion` y `jerarquia` |
| `DIS/diseno-visual` | el número de direcciones lo fija el nivel; distintas en dos de cinco dimensiones | **conforme** |
| `DIS/diseno-interaccion` | empieza por el error, no por el camino feliz | **conforme** |
| `DIS/investigacion-visual` | referencia con enlace, autor, fecha y principio; citar de memoria es material inventado | **conforme** |
| `DIS/investigacion-ux` | consigue los datos reales, incluido el caso que rompe la composición | **conforme** |
| `DIS/movimiento` | el movimiento no se juzga leyendo su descripción: se graba | **conforme** |
| `DIS/prototipado` | declara qué es real y qué está simulado antes de empezar; nunca entra en el producto | **conforme** |
| `DIS/sistema-de-diseno` | un sistema gobierna, no describe; forma completa de declarar un patrón | **conforme** |
| `DIS/revision-de-fidelidad` | las ocho cosas que se simplifican en silencio; duración medida sobre la grabación | **conforme** |
| `DIS/validacion-de-uso` | no lee la especificación antes de recorrer, para no validar su memoria | **conforme** |
| `web:DIS/densidad-y-tablas` · `web:CON/estados-de-red` | densidad sin perder legibilidad; los cinco estados de red | **conforme** |
| `mob:DIS/interaccion-tactil` · `mob:CON/ciclo-de-vida` | pulgar y alcance; terminación forzada sin perder trabajo | **conforme** |
| `wear:DIS/lectura-de-un-vistazo` · `wear:CON/energia-y-estados` | un dato, una acción; el ambiental es superficie, no apagado | **conforme** |

**Resultado:** 42 unidades revisadas —36 prompts canónicos y 6 embebidas— · 39 conformes
tras añadirles el bloque de cierre · **2 corregidas por contenido** (`DSP/estado` y
`DIS/critica-visual`) · 1 nueva (`DSP/supervision`). Ninguna se atribuía autoridad ajena,
ninguna instruía hablar con el Owner sin poder, y ninguna confundía producir evidencia con
emitir veredicto.

Esta tabla es **revisión humana de un solo lector**, y así se declara en las limitaciones.

## 7 · Reevaluación de las once pruebas que figuraban como superadas

> «No confíes en que un validador verde demuestra lo que su nombre afirma.»

| prueba | qué AFIRMABA | qué EJECUTABA de verdad | ¿basta la evidencia? | estado final |
|---|---|---|---|---|
| **T86** | «la autoridad de un rol no excede la de su capacidad» | sólo la contención del **veto**; nada sobre `decide` | **no** para el enunciado | **renombrada** a «Ningún rol veta lo que su capacidad no veta» · superada |
| **T87** | ninguna composición combina roles que ella declara independientes | exactamente eso, sobre los 38 bloques | sí | superada |
| **T88** | todo rol apunta a un prompt que existe | existencia del fichero y del ancla | sí | superada |
| **T89** | toda prueba de reanudación cita un escenario que existe | eso, admitiendo T01–T74 como referencias válidas | sí, **con límite declarado**: citar un escenario `contrato-definido` es suficiente | superada · límite escrito |
| **T90** | capacidades y roles se referencian sin huérfanos | sólo capacidad↔rol; **A-15 fue un método huérfano y no lo vio** | **no** | **reforzada**: cruza también los métodos · superada · negativo N90 |
| **T91** | todo paso de todo método declara cuándo termina | eso, sobre los 35 métodos | sí | superada · negativo N91 |
| **T92** | ningún contrato exige una marca | sólo ficheros `.md`: esquemas y validadores quedaban fuera | **no** | **reforzada** a `.yaml` y `.py` · superada · negativo N92 |
| **T131** | «lo más restrictivo gana entre dos packs» | que `compatible_con` resolviera y `precedencia` no estuviera vacío | **no** — prueba estructural presentada como de comportamiento | **renombrada**; el comportamiento pasa a **T149**, con fixtures y cuatro negativos |
| **T132** | tres afirmaciones, incluida «los gates de pack SUMAN» | dos de las tres; la tercera tenía una rama **inalcanzable** | **no** | **reforzada**: la comprobación existe y encontró un choque real |
| **T134** | «ningún documento del corpus existe para nadie» | coincidencia de **nombre base**: 119 de 188 exentos de hecho | **no** | **sustituida** por **T147**, por ruta normalizada · cuatro negativos |
| **T135** | ninguna composición rebaja la independencia de un contrato | exactamente eso | sí | superada |

**Cuatro de las once no sostenían su enunciado.** Ninguna se ha conservado como superada
para mantener una cifra: dos se renombraron a lo que verifican, dos se reforzaron hasta
demostrarlo, y una fue sustituida.

### Estado del registro, derivado

```text
CONTRATO DEFINIDO       54
VALIDADOR IMPLEMENTADO   0
PRUEBA EJECUTADA         0
PRUEBA SUPERADA         27
PRUEBA FALLIDA           0
total                   81
```

Las superadas se ejecutan en **once validadores**, y **49 infracciones deliberadas**
demuestran que cada una falla cuando debe fallar. Las 54 en `contrato-definido` siguen
siéndolo por la misma razón de siempre: exigen un proyecto real, hardware físico, juicio
humano o el runtime.

## 8 · Comandos ejecutados y códigos de salida

```bash
# posicionamiento
git status --short --branch ; git fetch --all --prune
git symbolic-ref refs/remotes/origin/HEAD        # → refs/remotes/origin/main
git remote show origin                            # HEAD branch: main
git diff --stat 953b8aa origin/main               # vacío: el árbol auditado ES el de main
git show --stat b7a2ceb 4bc8aee                   # ambos tocan SÓLO el informe
git checkout -b claude/kernel-operativo-correcciones-post-auditoria origin/main
git cherry-pick -x b7a2ceb 4bc8aee
git push -u origin claude/kernel-operativo-correcciones-post-auditoria

# validación final: UNA orden, que regenera, ejecuta, comprueba y publica
python3 kernel/operativo/validadores/registrar_evidencia.py    # EXIT 0
./tooling/kernel-status.sh                                     # LIMPIO
```

Ya no hay un bucle de shell que archive salidas: **archivar la evidencia es lo que hace el
runner**, y hacerlo mal es lo que la fase anterior demostró que es fácil. La salida vive en
`kernel/operativo/pruebas/evidencia/`, un fichero por validador, cada uno con su cabecera de
procedencia. Reproducirla es ejecutar esa orden.

## 9 · Pruebas negativas

**49 infracciones deliberadas**, cada una sobre una **copia temporal** del repositorio. El
corpus real no se toca en ningún momento: no hay restauración que pueda salir mal porque no
hay nada que restaurar.

```text
A-02  1   la documentación vuelve a citar un pack derogado
A-03  4   resolución menos restrictiva · sin motivo · dependiente del orden · conflicto silencioso
A-04  3   validador editado · tooling editado · huella estrechada
A-05  4   huérfano con nombre repetido · enlace a la carpeta equivocada · exclusión sin motivo · exclusión caducada
A-06  2   veto levantable que arbitra · colisión que no escala
A-07  2   N3 inalcanzable · escala no total
A-08  2   estaciones sin los dos gates · nivel sin gate obligatorio
A-09  3   gate de cierre sin obligaciones · DSP retira · informe que suma
A-10  4   sin ejecutor · sin gate · supervisor no independiente · umbral inventado
A-11  2   estado que falta · aparcado como estado propio
A-12  2   release que nadie sigue · línea histórica igualada al release
A-14  2   crítica por grado final · sin grado inicial
A-15  1   método que su capacidad deja de declarar
A-18  2   decide lo que su capacidad escala · decide materia ajena
A-23  1   DSP vuelve a decidir una cancelación
A-24  1   cifra escrita a mano que ya no cuadra
A-13  2   vínculo CON↔gate:usabilidad roto · vínculo sin declarar quién juzga
T158  6   invocación archivada sin .py · éxito sin salida que lo respalde · evidencia de
          otro validador · código no cero publicado · evidencia que falta · validador
          fuera del manifiesto
—     5   paso sin condición de salida · marca en un esquema · unidad sin gate ·
          unidad que habla con el Owner sin poder · unidad sin método
```

## 10 · Limitaciones reales

```text
1  NINGÚN PROYECTO REAL. Nada ha pasado por gym-wear, PesquerApp ni ningún otro. Las 54
   pruebas en `contrato-definido` lo siguen siendo porque exigen un proyecto, hardware,
   juicio humano o runtime. Esta fase no las mueve, y no debe parecer que las mueve.

2  EL RUNTIME SIGUE SIN EXISTIR. Lo construido es el contenido que ese runtime consumirá,
   y las obligaciones, los frenos y el cierre están declarados como CONTRATO ejecutable,
   no como código que se ejecute hoy.

3  T146 NO COMPRUEBA LA CONTENCIÓN SEMÁNTICA FINA de la autoridad de un rol. Atrapa las
   tres formas groseras y lo declara expresamente. Que un rol decida algo compatible con
   su capacidad sin compartir una palabra es lectura humana, y ninguna medida de texto lo
   decide. Es una limitación consciente, no un descuido.

4  LA REVISIÓN DE LAS UNIDADES DE INSTRUCCIÓN ES DE UN SOLO LECTOR. Mecánicamente son 42
   de 42, y eso lo comprueba T153 — que es ESTRUCTURAL Y HEURÍSTICA y no demuestra
   coherencia semántica. La lectura cualitativa la ha hecho quien escribió esta fase. Un
   segundo lector independiente encontraría cosas, igual que la auditoría las encontró
   sobre el trabajo anterior, y como el propio Owner encontró la corrupción de evidencia
   que ninguna de las dos vio.

8  LA EVIDENCIA DEMUESTRA QUE LOS VALIDADORES CORRIERON Y EN QUÉ TERMINARON. No demuestra
   que cada validador compruebe lo que su nombre dice: eso lo demuestran sus 49
   infracciones deliberadas, y sólo en la medida en que esas infracciones cubran los modos
   de fallo reales. Es una cobertura, no una garantía.

5  LOS UMBRALES SON PROVISIONALES. 0.60 y 0.15 no están calibrados con uso real, y así se
   declaran. Los frenos —2, 2, 3 y 3— vienen de (a) y (b) y tampoco se han observado.

6  LA SECCIÓN (g) SIGUE ABIERTA. Disposición física del estado, atomicidad multiarchivo,
   event log y recuperación. T25 permanece abierta por diseño.

7  NO SE HA EJECUTADO NINGUNA PRUEBA DE COMPORTAMIENTO DE DISEÑO. Que las rúbricas
   discriminen de verdad entre un producto con carácter y uno sin él exige aplicarlas a
   una interfaz real.
```

## 11 · Pendientes no bloqueantes

```text
· el piloto real, que es lo único que convierte `contrato-definido` en `prueba-ejecutada`
· reescribir KERNEL.md como índice delgado sobre kernel/operativo cuando el runtime exista
  (decisión O2, con su condición de revisión ya escrita)
· calibrar los umbrales de anclaje con el primer uso real
· las secciones (c) a (i), que se diseñan como items SIS dentro de un proyecto, no como
  bloque previo
· A-30: la profundidad de las capacidades distintas de DIS crecerá con el uso, no antes
```

## 12 · Condiciones de aprobación

| condición que impediría aprobar | estado |
|---|---|
| queda abierto un hallazgo crítico o grave | **ninguno abierto** |
| el arranque documentado sigue fallando | **funciona**, con los tres packs, verificado por T148 |
| una prueba superada sin demostrar su afirmación | **ninguna**: cuatro se renombraron, reforzaron o sustituyeron en la ronda anterior, y **T153 se acotó** en ésta a lo que demuestra mecánicamente |
| la evidencia publicada no respalda lo que el informe afirma | **T158 lo comprueba**, con seis infracciones deliberadas |
| algún hallazgo grave sin infracción deliberada | **ninguno**: A-13 era el último y ya tiene N144 y N144b |
| no se han revisado individualmente los prompts | **42 de 42**, con registro individual |
| persisten referencias rotas conocidas | **cero**, en los 217 documentos |
| siguen existiendo recuentos manuales incompatibles | **cero**: se derivan y se comprueban |
| ENC y DSP conservan autoridad solapada | **frontera declarada** en E1.1, con prohibiciones recíprocas |
| ENC queda materializada permanentemente | **no**: bajo demanda, y los permanentes siguen siendo dos |
| DSP puede decidir cancelaciones semánticas | **no**: propone y ejecuta, nunca decide |
| N3 sigue siendo inalcanzable | **alcanzable**, comprobado sobre las 32 combinaciones |
| el cierre puede ocurrir con obligaciones huérfanas | **no**: `gate:cierre-de-item` lo impide |
| DIS o DOM arbitran silenciosamente vetos | **no**: ambos detienen y escalan al Owner |
| los frenos siguen sin ejecutor | **DSP/supervision**, con su método y sus gates |
| la auditoría o su matriz no están en la rama | **ambas presentes** |
| el árbol no queda limpio | **limpio** |
| la evidencia no permite repetir las pruebas | **un fichero por validador** en `pruebas/evidencia/` |
