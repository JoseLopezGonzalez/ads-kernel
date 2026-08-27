# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/06 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · PUERTA CORRECTIVA PRE-F4 CERRADA
based_on:    docs/evolucion/09-SINTESIS.md@7e450cf + su addendum
             docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md@515e94c
             kernel/VERSION@2.0.0-alpha.8 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: F3 pasa por CRÍTICA INDEPENDIENTE —que no la escribió quien la
             escribió—, el Owner resuelve las ocho materias que quedaban suyas, y una
             ejecución destapa que T158 daba por buena una evidencia caducada (2026-08-27)
resuelto:
  · SEIS HALLAZGOS DE LA CRÍTICA, aplicados sin borrar nada de F3:
    CI-1 H4 REVISADO. El componente de C6 es ámbito principal, NO sujeto único: no puede
         cargar con pantallas, formularios, migraciones, pipelines, agentes ni adaptadores.
         La matriz pasa a `sujeto auditable × dimensión`. No autoriza un tipo nuevo
    CI-2 H5 DEGRADADO a reutilización candidata. `memoria` no cubre procedencia, revisiones
         examinadas, relaciones, aplicabilidad, gaps ni contradicciones. Tres vías para F4
    CI-3 X8 CERRADA POR LECTURA: C4 y E1 ya la respondían. Preguntas 3 y 4 retiradas
    CI-4 X7 CERRADA: doce ÁREAS SEMÁNTICAS, no doce ficheros — y tampoco «lo necesario para
         reanudar», que era la salida que propuso la síntesis y se quedaba corta
    CI-5 H1 conservado: compartir motor de composición NO aplana las rutas
    CI-6 H3 conservado, desglosado en cuatro piezas con dueño distinto
  · OCHO RESOLUCIONES DEL OWNER, registradas como O7–O14 en DECISIONES-Y-CONTRADICCIONES:
    política de auditoría revocable · mínimo documental · catálogo frente a equipo ·
    docs/owner/ · la unidad amplia se llama `iniciativa` · gate de arranque ·
    matriz agentic · piloto en PesquerApp
  · CERO preguntas abiertas del conjunto que F3 elevó al Owner: siete resueltas, dos
    retiradas por lectura
  · T158 CORREGIDO. Reproducido primero contra el código anterior: corpus 282, evidencia
    280, cabecera y firma válidas, T158 SUPERADA. Contrato `vigencia` declarativo, con el
    recorrido IMPORTADO de quien lo define, que falla cerrado y no se acepta a sí mismo.
    Regresiones N158g y N158h, con la cifra derivada del propio fichero
  · P-07 cerrado en su ubicación: docs/owner/, y la exención pasa a ser POR UBICACIÓN.
    Cinco exenciones manuales para la misma clase eran la señal de que faltaba la clase
owner_captado: "antes debes cerrar una puerta correctiva pre-F4 derivada de la crítica
             independiente de F3" (2026-08-27)
pregunta_pendiente: ninguna
siguiente:   F4 ARQUITECTURA INTEGRADA — autorizable, y NO iniciada
falta_para_cerrar_la_capa:
  · P-08 NUEVO: la vigencia de la evidencia sólo está garantizada para T161. Los otros doce
    validadores publican cifras que pueden envejecer igual y nada lo detecta. La solución
    general exige declarar las ENTRADAS de cada validador: es materia de F4
  · nada de lo resuelto «en su forma» está construido. O7–O14 fijan dirección y no
    implementan: la iniciativa, los adaptadores, la certificación y el sistema de auditoría
    siguen sin una línea
  · el piloto está SELECCIONADO y no ejecutado. Mientras no se ejecute, T169, T170, CA-10,
    CA-11 y el §100 como descubrimiento siguen sin demostrarse
  · ningún adaptador certificado. O13 fija la matriz objetivo; certificar exige prueba de
    humo, y la prueba de humo exige adaptador
  · X1 y P-05 siguen deferidas. Nada de esta puerta las toca
  · la directiva, su prompt y el documento de pendientes siguen fuera de docs/owner/, con
    su exención propia y su migración declarada pendiente
  · leer el manifiesto exige Python 3.11 o superior: `tomllib` es estándar desde ahí. Es la
    limitación de entorno que destapó el defecto de T158
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
F3c PUERTA CORRECTIVA        CERRADA — crítica independiente aplicada, O7–O14 registradas
                             y T158 corregido. 10-CRITICA-INDEPENDIENTE-F3.md
F4  ARQUITECTURA INTEGRADA   AUTORIZABLE, y no iniciada
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
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.8 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio

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
1  F4 ARQUITECTURA INTEGRADA   ya es autorizable: la puerta correctiva está cerrada y no
                               queda ninguna pregunta del Owner abierta.

2  EMPEZAR POR                 el orden de la síntesis, que la crítica no cambia: la
                               disposición física del estado va primero. Y con lo que la
                               crítica añade: el contrato de SUJETO AUDITABLE (CI-1) y la
                               vía del contrato documental (CI-2) son ahora decisiones de
                               F4, no conclusiones heredadas de F3.

3  LO QUE F4 HEREDA RESUELTO   O7–O14. No son propuestas: son dirección fijada. La
                               `iniciativa` tiene nombre, el gate de arranque tiene nivel,
                               la matriz agentic tiene primera fila y el piloto tiene
                               producto.

4  QUÉ VIGILAR                 P-08. La vigencia de la evidencia está garantizada para T161
                               y para nada más, y decirlo es la mitad de la corrección. La
                               tentación es escribir «la evidencia está verificada» y dejar
                               que se lea como si cubriera los trece validadores.

5  DÓNDE PARAR                 antes de tocar (a), (b), E1, E2 o K-1. Eso es F5, y su
                               puerta es la aprobación explícita del Owner.
```
