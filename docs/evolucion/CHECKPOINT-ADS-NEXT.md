# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/02 · SIS/evolucion
actualizado: 2026-08-26
metodo:      SIS/Evolucion · fase F1 de F6 (MINERÍA) · primera pasada cerrada
based_on:    docs/evolucion/ADS-NEXT-OWNER-BRIEF.md@b80cde2
             docs/rediseno/a-CAPACIDADES-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/b-RECORRIDO-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/a-ENMIENDA-E1-ENC.md@aprobada-2026-08-26
             kernel/VERSION@2.0.0-alpha.3
             ~/projects/lapesquerapp-frontend@main (1839 commits, leído 2026-08-26)
             ~/projects/lapesquerapp-backend@main (2433 commits, leído 2026-08-26)
freshness:   vigente
last_meaningful_event: el Owner señala PesquerApp como primer proyecto a minar (2026-08-26)
resuelto:
  · F0 entregada: baseline con evidencia ejecutada, mapa de los 23 apartados, invariantes
    y plan con diez preguntas
  · F1 primera pasada: 29 candidatos con procedencia, tres de ellos evidencia NEGATIVA
  · Q3 RESPONDIDA con evidencia: una skill es el disparador de un proveedor sobre un
    método neutral que ya existe. No es un tipo de contenido nuevo
  · X3 resuelta en la práctica: el proyecto ya construyó núcleo neutral + adaptadores,
    con degradación explícita y prueba de humo. No hubo que diseñarlo, hubo que encontrarlo
  · la iniciativa es trabajo SIS legítimo: el freno de racha de a.7 declara su excepción
  · descartado: proponer arquitectura antes de la síntesis. La directiva lo prohíbe
  · descartado: enmendar (a) o (b) desde aquí. Se registra la presión, no se resuelve
  · descartado: concluir Q1 con PesquerApp. Sus dos repositorios son UN producto, y la
    repetición entre ellos demuestra copia, no reutilización
owner_captado: "Tu misión es evolucionar ADS hacia esa visión utilizando, en la medida
             que el propio estado actual lo permita, ADS para trabajar sobre ADS."
             (2026-08-26)
pregunta_pendiente: ninguna que bloquee. Para cerrar Q1 hace falta minar un proyecto
             INDEPENDIENTE de PesquerApp — gym-wear está en ~/dev/gym-wear
siguiente:   minar gym-wear por las mismas ocho lentes, buscando específicamente qué
             mecanismos de PesquerApp reaparecen allí sin haberse copiado
falta_para_cerrar_la_capa:
  · Q1 sin conclusión, y bloquea la cuarta capa (X1)
  · Q9 y Q10 sin abordar
  · ningún candidato contrastado todavía contra el corpus, uno a uno (F2)
```


## Estado de las fases

```text
F0  BASELINE Y MAPA          ENTREGADA
F1  MINERÍA                  PesquerApp ENTREGADA · gym-wear pendiente
F2  CONTRASTE                no iniciada
F3  SÍNTESIS                 no iniciada
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
docs/evolucion/04-PLAN-DE-INVESTIGACION.md estado de las diez preguntas

NO se ha tocado (a), (b), E1, ningún contrato, esquema, rol, método, gate, prompt,
pack ni validador. El corpus operativo queda intacto y sus cifras derivadas no cambian.
NADA se ha escrito en los proyectos minados.
```

## Cómo se comprueba que esto sigue en pie

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # vacío: los generados son deterministas
```

## Siguiente acción exacta

```text
1  MINAR         ~/dev/gym-wear por las ocho lentes L1..L8 de 04-PLAN.

2  QUÉ BUSCAR    NO un inventario nuevo. Buscar CONVERGENCIA: qué mecanismos de los 24
                 candidatos de PesquerApp reaparecen allí sin haberse copiado. Eso, y
                 sólo eso, cierra Q1 y decide si la cuarta capa de X1 existe.

3  NO INSTALAR   la minería LEE. Nada se escribe en el proyecto minado.

4  QUÉ VIGILAR   la tentación de dar Q1 por respondida. Con un solo producto minado, la
                 respuesta honesta sigue siendo «indicios». Si gym-wear no comparte nada,
                 la conclusión correcta es que la cuarta capa NO está justificada, y hay
                 que escribirla igual.

5  QUÉ SE GANA   F2 puede empezar: contrastar los 29 candidatos contra el corpus, uno a
                 uno, por identificador.
```
