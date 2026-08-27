# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

> **Estado de la fase, en una línea:**
> **F4 corregida por devolución independiente; pendiente de segunda revisión.**
>
> Los hallazgos los EMITIÓ un revisor independiente que no escribió F4. Las correcciones
> las APLICÓ el autor material de F4. **Aplicar una crítica no prueba que esté bien
> resuelta**, y por eso `F4c` no se declara cerrada aquí.

```text
CHECKPOINT — ADS-NEXT/09 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · F4 CORREGIDA POR DEVOLUCIÓN INDEPENDIENTE; PENDIENTE DE
             SEGUNDA REVISIÓN
based_on:    docs/evolucion/09-SINTESIS.md@56ea196 + su addendum
             docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md@56ea196
             docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   corregida
             docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O7–O14 · D16–D22 · D23–D33
             kernel/VERSION@2.0.0-alpha.9 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: un revisor independiente devuelve F4 con nueve bloques de hallazgos,
             y sus correcciones quedan aplicadas (2026-08-27)
procedencia_de_la_critica: los hallazgos y el veredicto de las críticas de F3 y de F4 los
             EMITIÓ un revisor independiente que no las escribió. Los ficheros que los
             recogen los TRANSCRIBIÓ Y APLICÓ el autor material de esas fases. Aplicar una
             crítica NO equivale a autocertificarse, y NO prueba que esté bien resuelta
resuelto_en_la_devolucion_de_f4:
  · A · EL PROTOCOLO TRANSACCIONAL, reescrito para ser EJECUTABLE. El manifiesto de
    transacción se pliega en `evento` como una `fase`: una transacción es una secuencia de
    eventos INMUTABLES con `tx` común, y ya no hay fichero que se reescriba ni que se borre.
    Hash POSTERIOR esperado por fichero — el dato que faltaba—, tres cajas de clasificación
    en recuperación, ONCE ventanas de caída, SEIS garantías de durabilidad separadas con sus
    tres puntos de `fsync` obligatorio, semántica completa del sellado, e ids DIRECCIONADOS
    POR CONTENIDO. Se RETIRA la afirmación falsa de que dos emisores concurrentes no
    colisionan jamás. Tabla adversarial de DIECISIETE filas, para convertirse en pruebas F6
  · B · `cobertura.dimension` se parte en `sujeto` · `aspecto` con namespace tipado ·
    `responsables` · `criterio`. Una capacidad deja de sustituir a las dimensiones de las
    que responde: accesibilidad y responsive de una pantalla ya son dos celdas. Rendimiento,
    resiliencia y cadena de suministro dejan de estar sin dueño, asignadas a capacidades que
    YA EXISTEN. Tres celdas completas sobre el mismo contrato
  · C · la matriz de fuentes de verdad, rehecha: prioridad y aparcado en `02-control.md`, la
    zona ÓRDENES como CANAL DE COMANDOS, y el tablero deja de declararse derivado entero
  · D · el estado de iniciativa pasa a FUNCIÓN TOTAL con precedencia Q0–Q9, con su totalidad
    demostrada sobre los diez estados de b.4. No se persiste en ningún canónico
  · E · `memoria` SE GENERALIZA, y se dice. `ultima_verificacion_real` queda en UNA sola
    fuente. `capa` pasa a condicional y nace `plano`, sin fabricar la cuarta capa
  · F · `adaptador.nivel` desaparece como campo: el nivel alcanzado es DERIVADO y caduca.
    §6.7 resuelve el descubrimiento con control repo y fuentes hermanos, sin copiar la
    organización ADS y sin depender de nada no versionado
  · G · migración con secuencia única M5 certifica · M6 retira · M7 verifica. Rollback con
    remoto separado de lo local y SIN eliminación remota automática. Certificación Integrada
    con aplicabilidad para 0, 1 y N fuentes. Actualización con compatibilidad y rollback DEL
    ESTADO, y punto de no retorno declarado en U3
  · H · P-08 con TRES huellas y clave de caché por CONTENIDO, nunca el SHA de Git. Raíz de
    confianza declarada sin circularidad, y el suelo que queda abierto, dicho
  · I · D23–D33 registradas, cada una diciendo qué decisión anterior revisa. D16–D22
    CONSERVAN SU TEXTO. Tipos RECALCULADOS: cuatro de estado, uno de clase, y el manifiesto
    de transacción deja de serlo. Presiones revisadas: PN-4 retirada, PN-5 fusionada en
    PN-3, PN-6 nueva. CUATRO vigentes, sin renumerar ninguna
resuelto_en_la_entrega_de_f4:
  # HISTORIA. Es lo que F4 resolvió AL ENTREGARSE. Lo marcado [CORREGIDO] lo revisó la
  # devolución independiente, y su forma vigente está en el bloque de arriba.
  · LA PRIMERA DECISIÓN, que H2 ordenaba primero: DISPOSICIÓN FÍSICA DEL ESTADO.
    Ficheros canónicos + DIARIO DE EVENTOS append-only + derivados deterministas. SQLite
    canónico y event sourcing puro comparados y DESCARTADOS por romper «el estado ES los
    ficheros, legibles sin informe intermedio»; sólo ficheros, descartado por no cumplir
    la atomicidad que a.9 exige. SQLite queda como índice compilado NO canónico, en el
    plano operacional
    [CORREGIDO] la entrega contaba además un MANIFIESTO DE TRANSACCIÓN como pieza aparte.
    D23 lo pliega en `evento` como una `fase`
  · el diario ES el JOURNAL que a.11 dejó PENDIENTE. Cierra G26
  · DURABLE frente a OPERACIONAL: `estado/` versionado · `.ads/run/` no versionado y
    reconstruible. El criterio, en una pregunta: ¿sobrevive a un clon nuevo?
  · [CORREGIDO] la entrega decía «CUATRO TIPOS NUEVOS Y NI UNO MÁS», que era una CUOTA
    fijada antes de aplicar la prueba. El recuento se CALCULA: cuatro tipos de estado, un
    esquema de clase, y el manifiesto de transacción deja de ser tipo. §3.8
  · CI-1 aplicado: el sujeto auditable es referencia tipada (clase, ancla, ruta), con el
    componente de C6 como ANCLA. SOURCES.toml no se toca
  · CI-2 resuelto por COMPOSICIÓN: `memoria` gobierna, `cobertura` da vigencia
    [CORREGIDO] la composición era real y la generalización de `memoria` también, y sólo
    se contaba una. D27 sustituye a D20 y declara las dos. «Cero campos duplicados» no era
    cierto: `ultima_verificacion_real` estaba en los dos sitios, y ahora está en uno
  · CI-5 aplicado: cuatro macrocircuitos con disparador, fases, gates, rollback,
    reanudación y certificación PROPIOS. El motor es común; las rutas no se aplanan
    [CORREGIDO] dos de los cuatro declaraban secuencias imposibles. D32 y D33
  · CI-6 aplicado: adaptador en cuatro piezas — definición canónica, proyecciones donde
    cada proveedor las DESCUBRE, huella con validador de deriva, y prueba de humo
    [CORREGIDO] `adaptador.nivel` era una segunda verdad, y «donde cada proveedor las
    descubre» no resolvía el caso de control repo y fuentes hermanos. D28 y §6.7
  · P-08 con solución general diseñada: entradas declaradas por validador, huella de
    entradas en la evidencia, y las cuatro preguntas separadas — integridad, procedencia,
    éxito y VIGENCIA
    [CORREGIDO] la caché se claveaba por revisión de Git y era ciega al árbol sucio. D31
  · doce escenarios extremo a extremo recorridos. NINGUNO EJECUTADO
  · D16–D22 registradas con su alternativa descartada. D23–D33 las revisan sin
    reescribirlas
owner_captado: "Autoriza aplicar la crítica independiente de F4 y corregir su
             arquitectura. NO autoriza F5 ni F6" (2026-08-27)
pregunta_pendiente: ninguna. Las cuatro presiones normativas vigentes son materia de F5,
             no preguntas
siguiente:   SEGUNDA REVISIÓN INDEPENDIENTE de F4 corregida, por quien NO la escribió y NO
             aplicó estas correcciones. Después F5
falta_para_cerrar_la_capa:
  · F4 CORREGIDA POR DEVOLUCIÓN INDEPENDIENTE; PENDIENTE DE SEGUNDA REVISIÓN. Las
    correcciones las aplicó QUIEN LAS RECIBIÓ, y eso no prueba que estén bien resueltas.
    F4c NO está cerrada
  · CUATRO PRESIONES NORMATIVAS VIGENTES. PN-1 —la sección (g) no existe y §2 la escribe—
    BLOQUEA todo el estado durable, y ahora decide MÁS que antes: `fsync`, regla de commit
    de Git, sellado e identidad. PN-2 y PN-3 son la misma y sólo bloquean que el sistema
    abra auditorías solo; PN-3 absorbe lo que era PN-5. PN-6 es NUEVA: qué significa
    «Integrada» para un producto de 0 o 1 fuente, y reinterpreta O12. PN-4 queda RETIRADA
    con su motivo escrito, y F5 puede reinstaurarla
  · NADA CONSTRUIDO: ni kernel, ni runtime, ni tooling, ni esquemas, ni adaptadores, ni
    plantillas, ni packs, ni validadores, ni migraciones. Las correcciones son DISEÑO
    CORREGIDO, no diseño implementado
  · NADA PROBADO: las 17 filas de la tabla adversarial de §2.6.7, los 10 escenarios
    negativos de §11.5 y los 12 escenarios de §14 están ESCRITOS. Ninguno ejecutado
  · el piloto O14 sigue seleccionado y NO ejecutado. La columna de uso real, vacía
  · ningún adaptador existe, y por tanto ninguno está certificado
  · X1 y P-05 siguen deferidas. Ninguna decisión de F4 cruza esa línea, y D27 resuelve
    `capa` precisamente para no cruzarla
  · el SUELO DE P-08: si el runner miente, nada dentro del repositorio lo detecta.
    Declarado en §11.4, no resuelto
  · ORDEN TOTAL ENTRE MÁQUINAS: la cadena de eventos da orden total por transacción y
    parcial entre emisores concurrentes. La bifurcación se DETECTA; resolverla es runtime
    distribuido, y E2.7 ya lo dejó abierto
  · leer el manifiesto exige Python 3.11 o superior
```

> **Qué está demostrado y qué no**, criterio a criterio y con el artefacto que lo sostiene:
> [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md). Ningún criterio se cuenta como
> verificado por estar escrito.


## Estado de las fases

```text
F0  BASELINE Y MAPA          ENTREGADA
F1  MINERÍA                  CERRADA — PesquerApp. gym-wear RETIRADO por el Owner
F2  CONTRASTE                ENTREGADA
M   MANDATO MULTI-REPO       EJECUTADO — interrumpió F3 por orden del Owner
F3  SÍNTESIS                 ENTREGADA — 09-SINTESIS.md. Puerta X1..X5 superada
F3c PUERTA CORRECTIVA        CERRADA y después CORREGIDA — crítica independiente aplicada,
                             O7–O14 registradas, T158 corregido en dos pasadas, y los cuatro
                             defectos que la revisión encontró en la propia puerta resueltos.
                             10-CRITICA-INDEPENDIENTE-F3.md · release 2.0.0-alpha.9
F4  ARQUITECTURA INTEGRADA   ENTREGADA, NO CERTIFICADA, y después CORREGIDA por
                             devolución independiente — 11-ARQUITECTURA-INTEGRADA.md
F4c CRÍTICA INDEPENDIENTE    NUEVE bloques de hallazgos EMITIDOS por un revisor que no
                             escribió F4, TRANSCRITOS y APLICADOS por su autor material.
                             12-CRITICA-INDEPENDIENTE-F4.md · D23–D33
                             NO CERRADA: la puerta la pasa una SEGUNDA revisión
                             independiente que compruebe estas correcciones
F5  ENMIENDAS                cuatro presiones normativas vigentes, enumeradas y sin
                             redactar. NO INICIADA
F6  DESCOMPOSICIÓN Y EJECUCIÓN  no iniciada
```

## Lo que cambió en el repositorio

```text
F0
docs/evolucion/00-INDICE.md               nuevo — punto de entrada de la iniciativa
docs/evolucion/01-BASELINE-ADS.md         nuevo — 23.1
docs/evolucion/02-MAPA-DIRECTIVA.md       nuevo — 23.2
docs/evolucion/03-INVARIANTES.md          nuevo — lo que no se toca en silencio
docs/evolucion/04-PLAN-DE-INVESTIGACION.md nuevo — preguntas, protocolo y fases
validadores/exclusiones.yaml              los dos documentos del Owner, exentos de
                                          vocabulario con su motivo escrito
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.3 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio
README.md                                 enlaza la iniciativa

F1
docs/evolucion/05-CANDIDATOS.md           29 candidatos con procedencia y evidencia

F2
docs/evolucion/06-CONTRASTE.md            29 veredictos · 6 problemas arquitectónicos
docs/evolucion/01-BASELINE-ADS.md         corrección C-1 — gobierno Git
docs/evolucion/02-MAPA-DIRECTIVA.md       corrección C-1 — el apartado 8 pasa a PARCIAL
docs/evolucion/05-CANDIDATOS.md           correcciones C-2 y C-3
docs/evolucion/03-INVARIANTES.md          regla 6 — ninguna capa nueva sin evidencia
docs/evolucion/04-PLAN-DE-INVESTIGACION.md estado de las diez preguntas
docs/evolucion/07-DECISION-MULTIREPO.md   la contradicción, y su resolución por el Owner

MANDATO MULTI-REPOSITORIO
docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md  enmienda a (a) y (b)
kernel/operativo/contratos/C6 · C7        los dos contratos nuevos
kernel/operativo/esquemas/integration-set.yaml
kernel/operativo/plantillas/SOURCES.toml · INTEGRATION-SET.md
kernel/operativo/pruebas/T159-T170-multirepo.md
kernel/operativo/validadores/comprobar_fuentes.py
tooling/workspace.py · tooling/tests/test_workspace.py
kernel/KERNEL.md 1.4.0 · README · START_HERE · BOOTSTRAP · PROJECT · PROFILE
capacidades DSP · ENT · PLT · SIS · ARQ · DOM · ENC · VER · SEG · C2
release 2.0.0-alpha.5

PASADA CORRECTIVA DE F2
tooling/workspace.py                      los ocho bloqueantes, cada uno con su prueba
tooling/tests/test_workspace.py           29 → 57 pruebas: batería adversarial,
                                          reconstrucción de cuatro fuentes y red cerrada
tooling/new-project.sh                    el control repo nace en la rama que documenta
kernel/operativo/validadores/
  comprobar_fuentes.py                    T161 deja de ser tres literales
  comprobar_arranque.py                   T168 ampliada · T171 nueva
  comprobar_negativos.py                  N161–N161g · N171 · N171b
kernel/operativo/pruebas/fixtures/formulaciones-retiradas.yaml
kernel/KERNEL.md 1.5.0                    K0.6 · K0.8 · G04 · G12 · C0 · G26 · G27 ·
                                          G38 · G39 · G46 · G48
capacidades ARQ · ENC · DSP · SEG · CON · contratos C2 · C5 · C6 · 00-INDICE
docs/evolucion/08-EVIDENCIA-MULTIREPO.md  qué está demostrado y qué no
START_HERE.md                             cinco preguntas, y el checklist decía cuatro
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.6 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio

F3 SÍNTESIS
docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md
                                          entra como MATERIAL TEMPORAL de evolución, en su
                                          propio commit y sin copiarse en ningún otro
                                          fichero. Release 2.0.0-alpha.7
kernel/operativo/validadores/exclusiones.yaml
                                          quinta exención de vocabulario para un documento
                                          en voz del Owner. La medida de P-07
docs/evolucion/09-SINTESIS.md             nuevo — el entregable de F3
docs/evolucion/00-INDICE.md               23.4 entregada · el documento nuevo enlazado · y
                                          dos cifras que se habían quedado atrás
docs/evolucion/04-PLAN-DE-INVESTIGACION.md Q9 y Q10 respondidas · puerta de F3 superada ·
                                          la ficha de candidato registra su aplazamiento

PUERTA CORRECTIVA PRE-F4
docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md  nueva — la crítica, sus seis hallazgos, las
                                          ocho resoluciones y el defecto de T158
docs/evolucion/09-SINTESIS.md             addendum + marca en cada sección revisada. El
                                          texto original se conserva íntegro
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  O7–O14, sin reescribir O1–O6
kernel/operativo/validadores/
  comprobar_evidencia.py                  contrato de vigencia: falla cerrado, sin
                                          circularidad, y va el último para no enmascarar
                                          el motivo de otras mutaciones
  comprobar_fuentes.py                    corpus_recorrido() y ficheros_recorridos():
                                          definición ÚNICA del recorrido de T161
  comprobar_negativos.py                  N158g y N158h
  validadores.yaml                        bloque `vigencia` de `fuentes`
  exclusiones.yaml                        clasificación POR UBICACIÓN: docs/owner/
kernel/operativo/pruebas/T136-T152-post-auditoria.md  qué no veía T158, y su alcance
docs/owner/                               nuevo — los dos documentos multi-repo del Owner,
                                          movidos con git mv y sus referencias al día
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.8 — HISTÓRICO. Fue el estado
kernel/VERSIONES.md · .upstream-hash      final de esta pasada, y NO es la base vigente:
                                          la corrección de abajo lo sustituye

CORRECCIÓN DE LA PUERTA — cuatro defectos que la revisión independiente encontró en ella
docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md  procedencia: quién EMITE la crítica y quién
                                          ESCRIBIÓ el fichero dejan de confundirse
docs/evolucion/09-SINTESIS.md             O13 deja de dar por certificado lo que no lo está ·
                                          la vía de autoridad pasa de C4 a a.4
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  O9 y O13 corregidas en su registro canónico
kernel/operativo/validadores/
  comprobar_evidencia.py                  validación TIPADA del contrato `vigencia`, sin
                                          `except Exception`
  comprobar_negativos.py                  N158i–N158o · el arnés exige el diagnóstico
                                          esperado y rechaza la traza como detección
kernel/operativo/pruebas/T136-T152-post-auditoria.md  el manifiesto inválido se rechaza con
                                          un fallo, nunca con una traza
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.9 — ESTADO VIGENTE, con su
kernel/VERSIONES.md · .upstream-hash      entrada y la huella reanclada sobre el cambio

F4 ARQUITECTURA INTEGRADA
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  nueva — el entregable de F4
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D16–D22, sin reescribir D1–D15 ni O1–O14
docs/evolucion/00-INDICE.md               23.5 entregada
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado en F4. Ninguna enmienda.

F4c DEVOLUCIÓN INDEPENDIENTE — nueve bloques de hallazgos, aplicados
docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md  nueva — la crítica, su procedencia, los
                                          nueve bloques y qué se corrigió en cada uno
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  §1.3 matriz de fuentes de verdad · §2.5–§2.9
                                          protocolo transaccional reescrito · §3.2–§3.8
                                          tipos, contratos y recuento · §4.1–§4.3 contrato
                                          documental · §5.2 aspectos y §5.6 tres celdas ·
                                          §6.5 nivel derivado y §6.7 puntero en fuente ·
                                          §8.1–§8.4 los cuatro recorridos · §9.2 y §9.5
                                          certificación · §11.2–§11.5 P-08 · §15.8 · §16
                                          presiones · §17 · §18 · §19
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D23–D33, SIN reescribir D1–D22 ni O1–O14
docs/evolucion/00-INDICE.md               la crítica de F4, enlazada
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado en F4c, salvo la evidencia
DERIVADA que el runner republica. Ninguna enmienda. (a), (b), E1, E2, K-1 y C4 intactos.

(a), (b) y E1 siguen ÍNTEGRAS y sin reescribir: E2 las enmienda por sustitución
explícita, que es la única vía que admite la regla 1 de 03-INVARIANTES.
Los documentos del Owner tampoco se han tocado: el de pendientes entra literal.
NADA se ha escrito en los proyectos minados.
NADA de kernel/operativo/, packs/ ni docs/rediseno/ ha cambiado en F3.
```

### El recuento de commits se deriva, no se escribe

Esta sección llegó a decir «MANDATO MULTI-REPOSITORIO — tres commits» y se quedó
desactualizada en el commit siguiente, que es el mismo defecto que
[`CORRECCIONES-POST-AUDITORIA`](../rediseno/CORRECCIONES-POST-AUDITORIA.md) ya había
corregido para la entrega anterior. Lo que se fija es el punto de partida y el comando:

```bash
git rev-list --count 910d1d3..HEAD     # cuántos commits desde el cierre de F2
git log --oneline 910d1d3..HEAD        # cuáles son
```

```text
910d1d3   último commit de F2 (contraste)
5         commits de la implementación multi-repo: a4475a2 · fd741e8 · a8e2273 ·
          06a93ba · a224c36. NO tres, y NO seis
entre     a224c36 y 4cf9b8d, la pasada correctiva de F2
después   43c627f entra el documento de pendientes; a partir de ahí, F3
7e450cf   F3 síntesis · f59d9eb su evidencia derivada
8b6727a   primer cierre de la puerta correctiva — release 2.0.0-alpha.8, HISTÓRICO
8403d23   corrección de la puerta tras la revisión del SHA remoto — release
          2.0.0-alpha.9, ESTADO VIGENTE
```

Escribir el total a mano aquí lo dejaría mal en la siguiente confirmación. **El historial
no se reescribe**: la cifra se corrige contándola, no rehaciendo los commits.

## Cómo se comprueba que esto sigue en pie

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py   # exige Python 3.11+
git status --short          # vacío: los generados son deterministas
```

**Verde no basta.** Los ocho bloqueantes de `workspace.py` —escape por enlace simbólico,
fuentes dentro del control repo, repositorios anidados, `init` mutando con el manifiesto
roto, secretos en la salida, SSH confundido con credenciales, normalización que igualaba
repositorios distintos y tipos de TOML que reventaban— convivieron con los trece
validadores en verde y con veintinueve pruebas pasando. Lo que cerró cada uno fue una
prueba ADVERSARIAL que falla contra el código anterior, no el color del resumen.

## Siguiente acción exacta

```text
1  SEGUNDA REVISIÓN INDEPENDIENTE  por quien NO escribió F4 y NO aplicó estas
   DE F4 CORREGIDA                 correcciones. Aplicar una crítica no es superarla:
                                   quien la aplicó es quien la recibió. Sin esta segunda
                                   revisión, F4c no se cierra y F5 no arranca.

2  QUÉ MIRAR PRIMERO             §2.6, el protocolo transaccional. Es lo que la primera
                                 devolución declaró NO EJECUTABLE, y lo que más ha
                                 cambiado. La comprobación concreta: coger la tabla
                                 adversarial de §2.6.7 e intentar ejecutar cada fila
                                 CONTRA EL TEXTO — si una fila no se puede resolver con
                                 los datos que §2.6.2 escribe, sigue sin ser ejecutable.

3  QUÉ MIRAR DESPUÉS             §3.5 y §5.6: que las tres celdas de ejemplo caben de
                                 verdad en el mismo contrato, sin campos vacíos de
                                 conveniencia y sin campos que signifiquen cosas distintas
                                 en cada una. Y §3.3.1: que la función Q0–Q9 es total y
                                 disjunta sobre los diez estados de b.4, comprobado
                                 recorriéndolos, no leyendo la afirmación.

4  QUÉ LLEVAR AL OWNER           las CUATRO presiones normativas vigentes de §16. Sólo
                                 PN-1 bloquea de verdad: la sección (g) no existe y §2 la
                                 escribe. PN-2 y PN-3 son la misma pregunta por dos
                                 caminos. PN-6 es nueva y es UNA FRASE, pero sin ella todo
                                 producto de un solo repositorio queda bloqueado para
                                 empezar a programar.

5  QUÉ VIGILAR                   la tentación de leer «corregido» como «resuelto». Nueve
                                 bloques de hallazgos salen de F4c con CERO líneas
                                 construidas, CERO escenarios ejecutados y CERO
                                 comprobaciones independientes de las correcciones.

6  DÓNDE PARAR                   antes de redactar una enmienda. Eso es F5, y su puerta es
                                 la aprobación explícita del Owner.
```
