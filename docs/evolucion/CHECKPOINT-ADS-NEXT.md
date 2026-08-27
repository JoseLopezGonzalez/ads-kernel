# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/08 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · F4 ARQUITECTURA INTEGRADA ENTREGADA, NO CERTIFICADA
based_on:    docs/evolucion/09-SINTESIS.md@56ea196 + su addendum
             docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md@56ea196
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O7–O14 y D16–D22
             kernel/VERSION@2.0.0-alpha.9 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: se autoriza F4 en exclusiva, y se entrega la arquitectura integrada
             (2026-08-27)
procedencia_de_la_critica: los hallazgos y el veredicto de la crítica de F3 los EMITIÓ un
             revisor independiente que no participó en ella. El fichero que los recoge lo
             TRANSCRIBIÓ Y APLICÓ el autor de F3. Aplicar una crítica NO equivale a
             autocertificarse
resuelto:
  · LA PRIMERA DECISIÓN, que H2 ordenaba primero: DISPOSICIÓN FÍSICA DEL ESTADO.
    Ficheros canónicos + DIARIO DE EVENTOS append-only + MANIFIESTO DE TRANSACCIÓN +
    derivados deterministas. SQLite canónico y event sourcing puro comparados y
    DESCARTADOS por romper «el estado ES los ficheros, legibles sin informe intermedio»;
    sólo ficheros, descartado por no cumplir la atomicidad que a.9 exige. SQLite queda
    como índice compilado NO canónico, en el plano operacional
  · el diario ES el JOURNAL que a.11 dejó PENDIENTE. Cierra G26
  · DURABLE frente a OPERACIONAL: `estado/` versionado · `.ads/run/` no versionado y
    reconstruible. El criterio, en una pregunta: ¿sobrevive a un clon nuevo?
  · CUATRO TIPOS NUEVOS Y NI UNO MÁS: `iniciativa` `adaptador` `cobertura` `evento`.
    Todo lo demás compone, deriva o reutiliza — findings son items, campañas son
    iniciativas, la certificación es cobertura, la matriz es una vista
  · CI-1 aplicado: el sujeto auditable es referencia tipada (clase, ancla, ruta), con el
    componente de C6 como ANCLA. SOURCES.toml no se toca
  · CI-2 resuelto por COMPOSICIÓN: `memoria` gobierna, `cobertura` da vigencia. Cero
    campos duplicados. Las tres vías comparadas
  · CI-5 aplicado: cuatro macrocircuitos con disparador, fases, gates, rollback,
    reanudación y certificación PROPIOS. El motor es común; las rutas no se aplanan
  · CI-6 aplicado: adaptador en cuatro piezas — definición canónica, proyecciones donde
    cada proveedor las DESCUBRE, huella con validador de deriva, y prueba de humo
  · P-08 con solución general diseñada: entradas declaradas por validador, huella de
    entradas en la evidencia, y las cuatro preguntas separadas — integridad, procedencia,
    éxito y VIGENCIA
  · doce escenarios extremo a extremo recorridos. NINGUNO EJECUTADO
  · D16–D22 registradas con su alternativa descartada
owner_captado: "Queda AUTORIZADA exclusivamente F4 — ARQUITECTURA INTEGRADA" (2026-08-27)
pregunta_pendiente: ninguna. Las cinco presiones normativas son materia de F5, no preguntas
siguiente:   CRÍTICA INDEPENDIENTE DE F4, por quien no la escribió. Después F5
falta_para_cerrar_la_capa:
  · F4 NO ESTÁ CERTIFICADA. La escribe quien la propone, y el plan exige crítica
    independiente antes de F5. El precedente: 33 hallazgos en la iteración anterior
  · CINCO PRESIONES NORMATIVAS. PN-1 —la sección (g) no existe y §2 la escribe— BLOQUEA
    todo el estado durable. PN-2 y PN-3 son la misma y sólo bloquean que el sistema abra
    auditorías solo. PN-4 probablemente no exija nada. PN-5 es consecuencia de PN-3
  · NADA CONSTRUIDO: ni kernel, ni runtime, ni tooling, ni esquemas, ni adaptadores
  · el piloto O14 sigue seleccionado y NO ejecutado. La columna de uso real, vacía
  · ningún adaptador existe, y por tanto ninguno está certificado
  · X1 y P-05 siguen deferidas. Ninguna decisión de F4 cruza esa línea
  · dos dimensiones de auditoría sin propietario declarado: rendimiento y resiliencia, y
    dependencias y cadena de suministro. NO se asignan por comodidad
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
F4  ARQUITECTURA INTEGRADA   ENTREGADA y NO CERTIFICADA — 11-ARQUITECTURA-INTEGRADA.md
F4c CRÍTICA INDEPENDIENTE    siguiente. Su puerta la pasa quien NO escribió F4
F5  ENMIENDAS                cinco presiones normativas enumeradas y sin redactar
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
1  CRÍTICA INDEPENDIENTE DE F4   por quien NO la escribió. Es la puerta que el plan fija
                                 para F4, y F4 no la pasa sola. Sin ella, F5 no arranca.

2  QUÉ MIRAR PRIMERO             §2, la disposición física del estado. Es la decisión de
                                 la que dependen la certificación operativa, la iniciativa
                                 y la matriz de cobertura, y la única que bloquea el orden
                                 de construcción entero.

3  QUÉ LLEVAR AL OWNER           las cinco presiones normativas de §16. Sólo PN-1 bloquea
                                 de verdad: la sección (g) no existe y §2 la escribe.
                                 PN-2 y PN-3 son la misma pregunta por dos caminos.

4  QUÉ VIGILAR                   la tentación de leer «diseñado» como «hecho». Cuatro
                                 tipos nuevos, cuatro macrocircuitos y doce escenarios
                                 salen de F4 con CERO líneas construidas y CERO
                                 escenarios ejecutados.

5  DÓNDE PARAR                   antes de redactar una enmienda. Eso es F5, y su puerta es
                                 la aprobación explícita del Owner.
```
