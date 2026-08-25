# PLANTILLA — CHECKPOINT

Formato normativo en [a.10](../../../docs/rediseno/a-CAPACIDADES-APROBADA.md). Esta
plantilla no lo redefine: lo hace copiable, y añade el recordatorio de los errores que
convierten un checkpoint en un log inútil.

```text
CHECKPOINT — <ITEM-ID>/<nn> · <CAP>/<rol>
actualizado: <ISO 8601>
metodo:      <CAP>/<Metodo> · paso <n> de <N> (<NOMBRE DEL PASO>)
based_on:    <fuente>@<versión> · <fuente>@<versión>
freshness:   vigente | requiere revalidación | obsoleto
last_meaningful_event: <qué pasó y cuándo>
resuelto:
  · <qué quedó decidido, y qué quedó descartado con su motivo>
owner_captado: "<sus palabras exactas>" (<fecha>)
pregunta_pendiente: <la pregunta exacta, o «ninguna»>
siguiente:   <UNA acción concreta>
falta_para_cerrar_la_capa:
  · <lo que el gate todavía no tiene>
```

## Las cuatro cosas que lo estropean

```text
1  TRANSCRIPCIÓN     copiar la conversación. Un checkpoint que crece con cada turno es un
                     log, y los logs no se releen. ENLACES, no copias.
2  SIGUIENTE VAGO    «continuar con el diseño» no es una acción. «explorar la segunda
                     dirección y compararla contra los principios» sí lo es.
3  BASED_ON SIN      sin versión, no se puede saber si la fuente cambió, y la reanudación
   VERSIÓN           continúa sobre supuestos obsoletos sin enterarse.
4  DESACTUALIZADO    seguir trabajando sin escribirlo es un DEFECTO DEL SISTEMA, no una
                     omisión menor. El gate de suspensión no se cumple.
```

## Cuándo se escribe

Los seis momentos obligatorios están en a.10. El que más se incumple:

> **Antes de formular la siguiente pregunta importante, y no después.** Si el corte llega
> justo tras la pregunta, lo comprendido ya está a salvo.
