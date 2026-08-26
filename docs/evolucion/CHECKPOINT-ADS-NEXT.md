# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

```text
CHECKPOINT — ADS-NEXT/03 · SIS/evolucion
actualizado: 2026-08-26
metodo:      SIS/Evolucion · fase F2 de F6 (CONTRASTE) · entregada
based_on:    docs/evolucion/ADS-NEXT-OWNER-BRIEF.md@b80cde2
             docs/rediseno/a-CAPACIDADES-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/b-RECORRIDO-APROBADA.md@aprobada-2026-08-25
             docs/rediseno/a-ENMIENDA-E1-ENC.md@aprobada-2026-08-26
             kernel/KERNEL.md@1.3.0 · G29 G30 G52 K0.8 K0.10 K0.11
             kernel/VERSION@2.0.0-alpha.3
             ~/projects/lapesquerapp-frontend@main · -backend@main, leídos 2026-08-26
freshness:   vigente
last_meaningful_event: el Owner retira gym-wear de la minería por fuente contaminada
             y ordena continuar con F2 (2026-08-26)
resuelto:
  · F0 y F1 entregadas. F2 entregada: 29 veredictos y seis problemas arquitectónicos
  · Q1 NO RESPONDIDA ni en positivo ni en negativo, y X1 DEFERIDA — no bloqueada.
    PesquerApp es la única fuente externa madura, y sus dos repos son un solo producto
  · Q3 RESPONDIDA: una skill es el disparador de un proveedor sobre un método que ya
    existe. El contenido vive en el workflow neutral
  · seis candidatos ya estaban resueltos en ADS, y en cuatro de ellos ADS es MÁS ESTRICTO
  · el contraste desmintió tres afirmaciones propias, corregidas en su documento:
    C-1 el gobierno Git no estaba ausente · C-2 los ledgers sí tienen campos ·
    C-3 el mecanismo de zonas ya existe en a.9
  · descartado: la nota de 1 a 10 y el veredicto «aprobado con observaciones». ADS los
    rechaza por diseño, y el contraste confirmó por qué
  · descartado: diseñar la cuarta capa. Orden expresa del Owner, y ahora regla 6 de
    03-INVARIANTES
owner_captado: "No diseñes una cuarta capa por intuición ni fuerces los candidatos de
             PesquerApp para justificarla." (2026-08-26)
pregunta_pendiente: ninguna. F3 no depende de nada externo
siguiente:   F3 síntesis: decidir la FORMA de los dos candidatos de pack y los cuatro de
             kernel, y llevar los seis problemas a preguntas de arquitectura
falta_para_cerrar_la_capa:
  · Q9 y Q10 sin abordar
  · P-01 a P-06 registrados y sin resolver, por diseño
  · ninguna decisión arquitectónica tomada, que es donde el Owner ordenó detenerse
```

## Estado de las fases

```text
F0  BASELINE Y MAPA          ENTREGADA
F1  MINERÍA                  CERRADA — PesquerApp. gym-wear RETIRADO por el Owner
F2  CONTRASTE                ENTREGADA
F3  SÍNTESIS                 siguiente
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
1  F3 SÍNTESIS   NO empezar por los seis problemas. Empezar por lo cerrado: los dos
                 candidatos de MEJORA PACK —captura de fidelidad y gancho con
                 degradación— son los únicos cuya forma no depende de ninguna pregunta
                 abierta.

2  LUEGO         los cuatro de MEJORA KERNEL: registro derivado del estado, entrada
                 mínima para herramienta sin adaptador, prueba de humo de arranque, y
                 frontera de escritura entre ejecutores. Decidir su FORMA, no todavía su
                 ubicación: tres de los cuatro tocan P-01.

3  LOS PROBLEMAS van a la síntesis como PREGUNTAS con evidencia. P-05 no se toca.

4  QUÉ VIGILAR   la tentación de resolver P-01 creando un tipo canónico «adaptador» sin
                 haber decidido dónde vive. Dónde vive toca K-1, y K-1 está bajo P-05.

5  DÓNDE PARAR   antes de cerrar cualquier decisión arquitectónica irreversible y antes
                 de cualquier implementación amplia. Orden expresa del Owner.
```
