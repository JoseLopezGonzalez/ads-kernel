# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/04 · SIS/evolucion
actualizado: 2026-08-26
metodo:      SIS/Evolucion · mandato multi-repositorio EJECUTADO
based_on:    ADS-ARQUITECTURA-MULTIREPO-APROBADA.md@fd741e8
             docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md@aprobada-2026-08-26
             kernel/VERSION@2.0.0-alpha.5 · kernel/KERNEL.md@1.4.0
freshness:   vigente
last_meaningful_event: el Owner resuelve que ARQUITECTURA sustituye el bloqueo de IDEAS
             para la materialización multi-repo, y ordena implementarla (2026-08-26)
resuelto:
  · ADS PROJECT != REPOSITORIO. Implementado en corpus, modelo, tooling, arranque,
    adopción, capacidades, validadores y pruebas — no como capa añadida al lado
  · enmienda E2 a (a) y (b), por sustitución explícita y sin reescribirlas
  · C6 y C7: los contratos transversales pasan de cinco a siete. C7 cierra el problema
    P-04 que el propio contraste F2 había registrado
  · SOURCES.toml, workspace.py y sus 29 pruebas con repos Git locales; comprobar_fuentes
    valida el ADS Project SIN tocar el disco, para que la CI no necesite credenciales
  · CA-1 a CA-17 verificados, y los diez criterios de descubrimiento del §100
  · test mental final superado: borradas las cuatro fuentes, el workspace se reconstruye
    desde el repositorio ADS y su manifiesto
  · descartado: crear una capacidad de Git. El 8.2 avisa de que repartir Git entre PLT,
    ENT, DSP y CON es el problema; una capacidad más lo repartiría otra vez
  · descartado: tipos canónicos para source y component. Duplicarían el manifiesto
owner_captado: "todo ADS debe dejar de asumir que proyecto ADS y repositorio Git son la
             misma cosa" (2026-08-26)
pregunta_pendiente: ninguna
siguiente:   F3 síntesis de los candidatos de PesquerApp, que el mandato interrumpió
falta_para_cerrar_la_capa:
  · T169 y T170 en contrato-definido: exigen runtime y un guion con dos repos reales
  · nada de esto ha pasado todavía por un producto real. Sigue sin haber piloto
  · P-01, P-02, P-03, P-05, P-06 y P-07 siguen registrados y sin resolver
```


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

MANDATO MULTI-REPOSITORIO — tres commits: a4475a2 · fd741e8 · a8e2273
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

(a), (b) y E1 siguen ÍNTEGRAS y sin reescribir: E2 las enmienda por sustitución
explícita, que es la única vía que admite la regla 1 de 03-INVARIANTES.
NADA se ha escrito en los proyectos minados.
```

## Cómo se comprueba que esto sigue en pie

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # vacío: los generados son deterministas
```

## Siguiente acción exacta

```text
1  F3 SÍNTESIS   retomar donde el mandato la interrumpió. El material de F1 y F2 está
                 intacto: 29 candidatos y siete problemas registrados.

2  EMPEZAR POR   los dos candidatos de MEJORA PACK —captura de fidelidad y gancho con
                 degradación—, los únicos cuya forma no depende de ninguna pregunta
                 abierta.

3  RECONSIDERAR  P-01 y P-04 a la luz de lo implementado. P-04 queda cerrado por C7.
                 P-01 sigue abierto, y ahora con un contrato sobre el que apoyarse: D10
                 del mandato decide adapters sobre filesystem y Git.

4  QUÉ VIGILAR   la tentación de dar por probado el modelo multi-repo. Está verificado
                 CONTRA SÍ MISMO —13 validadores, 29 pruebas, 17 criterios— y no ha
                 pasado por un producto real. La columna de uso real sigue vacía.

5  DÓNDE PARAR   antes de cerrar cualquier decisión arquitectónica irreversible.
```
