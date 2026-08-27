# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/04 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · mandato multi-repositorio EJECUTADO · pasada correctiva de F2
based_on:    ADS-ARQUITECTURA-MULTIREPO-APROBADA.md@fd741e8
             docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md@aprobada-2026-08-26
             kernel/VERSION@2.0.0-alpha.6 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: el Owner resuelve que ARQUITECTURA sustituye el bloqueo de IDEAS
             para la materialización multi-repo, y ordena implementarla (2026-08-26)
resuelto:
  · ADS PROJECT != REPOSITORIO. Implementado en corpus, modelo, tooling, arranque,
    adopción, capacidades, validadores y pruebas — no como capa añadida al lado
  · enmienda E2 a (a) y (b), por sustitución explícita y sin reescribirlas
  · C6 y C7: los contratos transversales pasan de cinco a siete. C7 cierra el problema
    P-04 que el propio contraste F2 había registrado
  · SOURCES.toml, workspace.py y sus 57 pruebas con repos Git locales y SIN RED —Git sólo
    admite el transporte `file`, y una prueba lo comprueba—; comprobar_fuentes valida el
    ADS Project SIN tocar el disco, para que la CI no necesite credenciales
  · nueve de los diecisiete CA están EJECUTADOS por prueba automática; cinco son
    estructurales, dos son contrato y uno es estructural parcial. La matriz, criterio a
    criterio y con qué artefacto lo sostiene, en `08-EVIDENCIA-MULTIREPO.md`
  · del §100 está comprobada la CONDICIÓN NECESARIA —cada uno de los diez tiene un sitio
    declarado donde leerse, y T171 lo comprueba—, no el descubrimiento, que exige piloto
  · la reconstrucción de un producto de CUATRO fuentes deja de ser un test mental y pasa a
    ser `test_42`: cuatro repos Git locales, se borran los cuatro, y el workspace se
    reconstruye desde el control repo y su manifiesto con las mismas revisiones
  · descartado: crear una capacidad de Git. El 8.2 avisa de que repartir Git entre PLT,
    ENT, DSP y CON es el problema; una capacidad más lo repartiría otra vez
  · descartado: tipos canónicos para source y component. Duplicarían el manifiesto
owner_captado: "todo ADS debe dejar de asumir que proyecto ADS y repositorio Git son la
             misma cosa" (2026-08-26)
pregunta_pendiente: ninguna
siguiente:   F3 síntesis de los candidatos de PesquerApp, que el mandato interrumpió
falta_para_cerrar_la_capa:
  · T169 y T170 en contrato-definido: exigen runtime y un guion con dos repos reales.
    Siguen ahí, y no se cuentan como demostradas
  · CA-10 y CA-11 dependen de runtime para poder comprobarse de verdad
  · el §100 como DESCUBRIMIENTO —no como cobertura estructural— exige un agente y un
    producto real
  · nada de esto ha pasado todavía por un producto real. Sigue sin haber piloto
  · leer el manifiesto exige Python 3.11 o superior: `tomllib` es estándar desde ahí. En
    3.10 el manifiesto no se lee y tres validadores fallan diciéndolo
  · P-01, P-02, P-03, P-05, P-06 y P-07 siguen registrados y sin resolver
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
F3  SÍNTESIS                 siguiente, con el material de F1 y F2 intacto
F4  ARQUITECTURA INTEGRADA   no iniciada
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

(a), (b) y E1 siguen ÍNTEGRAS y sin reescribir: E2 las enmienda por sustitución
explícita, que es la única vía que admite la regla 1 de 03-INVARIANTES.
Los dos documentos del Owner —ARQUITECTURA e IDEAS— tampoco se han tocado.
NADA se ha escrito en los proyectos minados.
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
resto     commits de la pasada correctiva de F2, posteriores a a224c36
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
1  F3 SÍNTESIS   retomar donde el mandato la interrumpió. El material de F1 y F2 está
                 intacto: 29 candidatos y los seis problemas de 06-CONTRASTE, más P-07,
                 que registró la decisión multi-repo.

2  EMPEZAR POR   los dos candidatos de MEJORA PACK —captura de fidelidad y gancho con
                 degradación—, los únicos cuya forma no depende de ninguna pregunta
                 abierta.

3  RECONSIDERAR  P-01 y P-04 a la luz de lo implementado. P-04 queda cerrado por C7.
                 P-01 sigue abierto, y ahora con un contrato sobre el que apoyarse: D10
                 del mandato decide adapters sobre filesystem y Git.

4  QUÉ VIGILAR   la tentación de dar por probado el modelo multi-repo. Está comprobado
                 CONTRA SÍ MISMO —13 validadores y 57 pruebas de workspace—, nueve de los
                 diecisiete CA están ejecutados y el resto son estructurales o contrato.
                 No ha pasado por un producto real: la columna de uso real sigue vacía.
                 Y verde no es lo mismo que correcto: los ocho bloqueantes de workspace.py
                 convivieron con una batería entera en verde.

5  DÓNDE PARAR   antes de cerrar cualquier decisión arquitectónica irreversible.
```
