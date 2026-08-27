# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/05 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · F3 SÍNTESIS ENTREGADA
based_on:    docs/evolucion/06-CONTRASTE.md@910d1d3
             docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md@43c627f
             kernel/VERSION@2.0.0-alpha.7 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: el Owner entrega el documento de pendientes —principios aceptados,
             propuestas abiertas y problemas por sintetizar— y ordena ejecutar F3 (2026-08-27)
resuelto:
  · SEIS HALLAZGOS, que son el resultado de la fase:
    H1 los cuatro macrocircuitos —instalación, adopción, migración, actualización— son UNA
       composición sobre procesos existentes, no cuatro diseños. Comprobado fase a fase:
       A2/A3/A6 son `AUD`, y los condicionales que AUD ya declara son la lista de
       participantes que el documento escribe
    H2 el ESTADO PERSISTIDO es el cuello de botella: cinco de los seis bloques del documento
       dependen de él, y a.9 delega su disposición física desde el principio
    H3 el ADAPTADOR es una PROYECCIÓN COMPILADA, no una capa de conocimiento. Cierra X3,
       da contenido a P-01 y su huella cierra P-06 — sin tocar K-1
    H4 el sujeto que le faltaba a P-03 ya existe y es canónico: el COMPONENTE de C6. Las
       doce dimensiones del §20.3 son capacidades que ya tienen propietario
    H5 el contrato documental del §5.23 es el esquema `memoria` con DOS campos más
    H6 el documento se contradice consigo mismo: máxima documentación contra mínima
       complejidad. Registrado como X7
  · PUERTA DE F3 SUPERADA: X1 deferida con su línea escrita · X2 resuelta por lectura, y su
    parte de Owner acotada a una pregunta · X3 RESUELTA · X4 RESUELTA: la minería es un AUD
    con SIS como consumidor · X5 resuelta en su forma
  · TRES CONTRADICCIONES NUEVAS, registradas con las dos posturas y sin resolver:
    X6 la auditoría autónoma crea trabajo y ninguna entrada del Owner lo autoriza
    X7 el mínimo documental obligatorio contra el control de crecimiento
    X8 organización preestructurada contra «no se materializan equipos permanentes» (R04)
  · P-01, P-02, P-03, P-06 y P-07 quedan RESUELTOS EN SU FORMA y entran en F4. P-05 sigue
    deferido, y ahora comparte condición de reapertura con X4. P-04 está cerrado en
    arquitectura y abierto en evidencia: exige runtime y piloto
  · Q9 y Q10 RESPONDIDAS. Q10 devuelve un criterio operable en vez de una lista: no se
    sustituye lo que tiene CICATRIZ ESCRITA, que es la lente L7 del propio protocolo
  · siete de los veintinueve candidatos convergen en UNA pieza: el contrato de adaptador
  · descartado: crear el fichero EVOLUTION.md. KERNEL_CHANGELOG y VERSIONES ya son el
    ledger, con política escrita y validador. Otro sería la segunda verdad que el §26.24
    dice querer evitar
  · descartado: un tipo de proceso nuevo para adopción, migración, actualización, minería
    o auditoría del propio ADS. Los diez de b.16 los cubren
  · descartado, por ahora: el esquema `candidato`. Se justifica con la segunda minería
owner_captado: "material de evolución, no normativa vigente ni autorización para
             implementar directamente todo su contenido" (2026-08-27)
pregunta_pendiente: nueve, listadas en 09-SINTESIS. La más cara de aplazar es la novena:
             qué producto real se usa para el piloto
siguiente:   F4 ARQUITECTURA INTEGRADA, que NO la certifica quien la escribe
falta_para_cerrar_la_capa:
  · la síntesis no ha pasado por crítica independiente. Es la puerta de F4, no de F3
  · nada de lo resuelto «en su forma» está construido. Cinco problemas resueltos en forma
    son cinco contratos por escribir, no cinco piezas que funcionen
  · sigue sin haber piloto. La columna de uso real está vacía desde F0
  · T169 y T170 en contrato-definido · CA-10 y CA-11 dependen de runtime · el §100 como
    DESCUBRIMIENTO exige un agente y un producto real
  · leer el manifiesto exige Python 3.11 o superior: `tomllib` es estándar desde ahí. En
    3.10 fallan comprobar_fuentes, comprobar_arranque y las pruebas de workspace, diciendo
    por qué. Es una limitación declarada del entorno, no un defecto del corpus
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
F4  ARQUITECTURA INTEGRADA   siguiente. Su puerta es la CRÍTICA INDEPENDIENTE
F5  ENMIENDAS                no iniciada
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
1  F4 ARQUITECTURA INTEGRADA   una sola propuesta que explique juntos organización, kernel,
                               packs, profile, adaptadores, estado, runtime, Git,
                               instalación, adopción, actualización, aprendizaje,
                               documentación y pruebas. No una colección de subsistemas.

2  EMPEZAR POR                 el ORDEN que la síntesis concluye, y que no es el del BLOQUE G
                               del documento: la disposición física del estado va primero,
                               porque la certificación operativa, la unidad amplia y la
                               matriz de cobertura se apoyan las tres en ella. Construirlas
                               antes fabricaría tres almacenes paralelos — modo de fallo (a)
                               de a.7.

3  LLEVAR A LA MESA            las nueve preguntas del Owner de 09-SINTESIS. Cuatro de ellas
                               —X6, X7, X8 y la ubicación de P-07— cambian qué se construye,
                               no sólo cuándo.

4  QUÉ VIGILAR                 la tentación de leer «resuelto en su forma» como «hecho».
                               Cinco problemas salen de F3 con forma propuesta y CERO
                               líneas construidas. Y la puerta de F4 no la pasa quien la
                               escribe: la iteración anterior dejó el precedente con
                               treinta y tres hallazgos de una auditoría independiente.

5  DÓNDE PARAR                 antes de tocar (a), (b), E1 o E2. Eso es F5, y su puerta es
                               la aprobación explícita del Owner.
```
