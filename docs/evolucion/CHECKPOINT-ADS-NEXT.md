# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/01 · SIS/evolucion
actualizado: 2026-08-26
metodo:      SIS/Evolucion · fase F0 de F6 (BASELINE Y MAPA)
based_on:    docs/evolucion/ADS-NEXT-OWNER-BRIEF.md@b80cde2
             docs/rediseno/a-CAPACIDADES-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/b-RECORRIDO-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/a-ENMIENDA-E1-ENC.md@aprobada-2026-08-26
             kernel/VERSION@2.0.0-alpha.2 (el release pasa a alpha.3 en esta misma fase)
freshness:   vigente
last_meaningful_event: el Owner incorpora la directiva ADS NEXT al repositorio (2026-08-26)
resuelto:
  · F0 entregada: baseline con evidencia ejecutada, mapa de los 23 apartados con
    veredicto, registro de invariantes y plan de investigación con diez preguntas
  · la iniciativa es trabajo SIS legítimo y sostenido: el freno de racha de a.7 declara
    su propia excepción cuando el objetivo explícito es construir el kernel o su runtime
  · el orden minería → piloto queda decidido y motivado, no por preferencia
  · descartado: proponer arquitectura en F0. La directiva lo prohíbe en su apartado 23
  · descartado: enmendar (a) o (b) desde aquí. Se registra la presión, no se resuelve
owner_captado: "Tu misión es evolucionar ADS hacia esa visión utilizando, en la medida
             que el propio estado actual lo permita, ADS para trabajar sobre ADS."
             (2026-08-26)
pregunta_pendiente: qué repositorios se ponen a disposición para la minería, y en qué ruta
siguiente:   ejecutar F1 sobre el primer repositorio que el Owner indique, recorriendo las
             ocho lentes y produciendo fichas en 05-CANDIDATOS.md
falta_para_cerrar_la_capa:
  · F1 minería: sin material
  · Q1 y Q3 sin respuesta, y bloquean la arquitectura
  · X1 (cuarta capa) y X4 (proceso de minería) abiertas
```

## Estado de las fases

```text
F0  BASELINE Y MAPA          ENTREGADA
F1  MINERÍA                  BLOQUEADA — espera rutas de repositorio
F2  CONTRASTE                no iniciada
F3  SÍNTESIS                 no iniciada
F4  ARQUITECTURA INTEGRADA   no iniciada
F5  ENMIENDAS                no iniciada
F6  DESCOMPOSICIÓN Y EJECUCIÓN  no iniciada
```

## Lo que cambió en el repositorio durante F0

```text
docs/evolucion/00-INDICE.md               nuevo — punto de entrada de la iniciativa
docs/evolucion/01-BASELINE-ADS.md         nuevo — 23.1
docs/evolucion/02-MAPA-DIRECTIVA.md       nuevo — 23.2
docs/evolucion/03-INVARIANTES.md          nuevo — lo que no se toca en silencio
docs/evolucion/04-PLAN-DE-INVESTIGACION.md nuevo — preguntas, protocolo y fases
docs/evolucion/05-CANDIDATOS.md           nuevo — inventario, sin material
validadores/exclusiones.yaml              los dos documentos del Owner, exentos de
                                          vocabulario con su motivo escrito
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.3 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio
README.md                                 enlaza la iniciativa

NO se ha tocado (a), (b), E1, ningún contrato, esquema, rol, método, gate, prompt,
pack ni validador. El corpus operativo queda intacto y sus cifras derivadas no cambian.
```

## Cómo se comprueba que esto sigue en pie

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # vacío: los generados son deterministas
```

## Siguiente acción exacta

```text
1  PEDIR        al Owner la ruta de lectura de cada repositorio a minar.
                Es lo único que bloquea, y no es una decisión técnica: es acceso.

2  MINAR        el primero, por las ocho lentes L1..L8 de 04-PLAN, no por su árbol de
                directorios. Una ficha por candidato, con origen y evidencia de uso.

3  NO INSTALAR  la minería LEE. Nada se escribe en el proyecto minado. La adopción es
                otro circuito y va después.

4  QUÉ VIGILAR  Q1 y Q3. Si al terminar el primer proyecto no hay evidencia sobre
                conocimiento repetido entre proyectos ni sobre skills reales, la minería
                se ha hecho por el árbol de directorios y hay que repetirla por lentes.

5  QUÉ SE GANA  la respuesta a X1 —si existe una cuarta capa— deja de ser una opinión
                arquitectónica y pasa a ser una conclusión.
```
