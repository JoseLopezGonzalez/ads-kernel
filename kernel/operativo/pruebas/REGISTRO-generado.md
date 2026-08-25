# REGISTRO DE PRUEBAS — generado

<!-- GENERADO por validadores/registro_pruebas.py. No editar a mano. -->
<!-- source_revision: 57a3cad8726b7f2c -->

Fuente: los bloques `ads:escenario` de `kernel/operativo/` y `packs/`.
Los cuatro estados y qué autoriza a decir cada uno: [`REGISTRO.md`](REGISTRO.md).

## Recuento

| estado | pruebas |
|---|---|
| CONTRATO DEFINIDO | 11 |
| VALIDADOR IMPLEMENTADO | 0 |
| PRUEBA EJECUTADA | 0 |
| PRUEBA SUPERADA | 7 |
| PRUEBA FALLIDA | 0 |
| **total** | **18** |

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
| [T86](T086-T092-contratos.md) | La autoridad de un rol no excede la de su capacidad | C1 · a.1 AUTORIDAD · autoridad silenciosa | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T87](T086-T092-contratos.md) | La independencia gana siempre a la combinación | C4 paso 5 · C2 combinaciones prohibidas · G13 | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T88](T086-T092-contratos.md) | Todo rol es materializable porque su prompt existe | C1 campo prompt · regla R02 · C4 prohibiciones | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T89](T086-T092-contratos.md) | Ninguna reanudación se declara posible sin prueba que la respalde | C3 regla 7 · regla R03 · a.10 | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T90](T086-T092-contratos.md) | Capacidades y roles se referencian mutuamente sin huérfanos | a.1 · C1 · C4 | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T91](T086-T092-contratos.md) | Ningún paso de ningún método dura lo que el agente decida | C3 regla 1 · esquemas/metodo.yaml | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
| [T92](T086-T092-contratos.md) | El kernel es portable porque ningún contrato exige una marca | K0.8 · C2 regla de portabilidad | validador-estructural | **PRUEBA SUPERADA** | evidencia/T086-T092-salida.txt |
