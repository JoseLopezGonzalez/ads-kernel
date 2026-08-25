# REGISTRO DE PRUEBAS — generado

<!-- GENERADO por validadores/registro_pruebas.py. No editar a mano. -->
<!-- source_revision: 8b9db502028fe3d2 -->

Fuente: los bloques `ads:escenario` de `kernel/operativo/` y `packs/`.
Los cuatro estados y qué autoriza a decir cada uno: [`REGISTRO.md`](REGISTRO.md).

## Recuento

| estado | pruebas |
|---|---|
| CONTRATO DEFINIDO | 11 |
| VALIDADOR IMPLEMENTADO | 0 |
| PRUEBA EJECUTADA | 0 |
| PRUEBA SUPERADA | 0 |
| PRUEBA FALLIDA | 0 |
| **total** | **11** |

## Detalle

| id | prueba | cubre | ejecución | estado | evidencia |
|---|---|---|---|---|---|
| [T75](../entrada/05-ESCENARIOS.md) | El comentario subjetivo no se traduce a tarea técnica | paso 1.6 · forma:comentario-subjetivo · gate:encuadre-listo · gate:anclaje-completo | requiere-juicio-humano | **CONTRATO DEFINIDO** | — |
| [T76](../entrada/05-ESCENARIOS.md) | Deíctico resuelto sin preguntar y sin desaparcar | forma:referencia-anterior · b.13 desambiguación · a.2 aparcado | guion-manual | **CONTRATO DEFINIDO** | — |
| [T77](../entrada/05-ESCENARIOS.md) | Relevo de agente a mitad de conversación sin pedir resumen al Owner | forma:interrupcion · a.10 checkpoint · ENC/Escucha · T01 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T78](../entrada/05-ESCENARIOS.md) | Orden emitida sobre base que dejó de ser vigente | ENC/Orden · gate:orden-emitida · a.9 protocolo de órdenes · T24 | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T79](../entrada/05-ESCENARIOS.md) | Un comentario sin objetivo no genera ningún artefacto de trabajo | 01-TAXONOMIA · a.7 modo de fallo (b) · b.15 regla dura | guion-manual | **CONTRATO DEFINIDO** | — |
| [T80](../entrada/05-ESCENARIOS.md) | Duplicado con item aparcado se convierte en propuesta de retomar | ENC/Anclaje · gate:anclaje-completo · a.2 aparcado · T10 | guion-manual | **CONTRATO DEFINIDO** | — |
| [T81](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Anclaje sin repetir búsquedas | ENC/Anclaje · a.10 checkpoint · gate:anclaje-completo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T82](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Maduracion sin repetir alternativas rechazadas | ENC/Maduracion · forma:idea-inmadura · a.10 checkpoint | guion-manual | **CONTRATO DEFINIDO** | — |
| [T83](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Orden sin aplicar dos veces el mismo evento | ENC/Orden · gate:orden-emitida · a.9 idempotencia por id | requiere-runtime | **CONTRATO DEFINIDO** | — |
| [T84](T081-T085-reanudacion-ENC.md) | Reanudación de ENC/Formulacion desde campos parcialmente escritos | ENC/Formulacion · gate:encuadre-listo | guion-manual | **CONTRATO DEFINIDO** | — |
| [T85](T081-T085-reanudacion-ENC.md) | La crítica no se reanuda si su lectura independiente no se escribió | ENC/Critica · gate:critica-de-encuadre · G13 | guion-manual | **CONTRATO DEFINIDO** | — |
