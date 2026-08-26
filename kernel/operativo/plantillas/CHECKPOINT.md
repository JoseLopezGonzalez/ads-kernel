# PLANTILLA — CHECKPOINT

Formato normativo en [a.10](../../../docs/rediseno/a-CAPACIDADES-APROBADA.md). Esta
plantilla no lo redefine: lo hace copiable, y añade el recordatorio de los errores que
convierten un checkpoint en un log inútil.

```text
CHECKPOINT — <ITEM-ID>/<nn> · <CAP>/<rol>
actualizado: <ISO 8601>
metodo:      <CAP>/<Metodo> · paso <n> de <N> (<NOMBRE DEL PASO>)
based_on:    <fuente>@<versión> · <fuente>@<versión>
             <source-id>@<sha> · <contrato>@<versión>      ← ver «multi-fuente» abajo
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

## Multi-fuente: un paquete que toca código de varios repositorios

Reanudar un trabajo repartido **no puede depender de «abre la rama»**: hay varias, en
repositorios distintos, y ninguna sabe de las demás. Lo que lo sabe es esto:

```text
sources:
  <source-id>:  rama <ref> · commit <sha> · push <sí|no> · PR <ref|ninguno> · CI <estado>
  <source-id>:  rama <ref> · commit <sha> · push <sí|no> · PR <ref|ninguno> · CI <estado>
```

Y `based_on` referencia la revisión exacta de la que se partió:

```text
based_on:    backend@a1b2c3d
             api-contract@v4
```

> **Se REFERENCIA, no se copia.** Volcar en el checkpoint el contenido de otra fuente crea
> una segunda copia que envejece en silencio. Es la regla 1 de abajo aplicada a través de
> la frontera del repositorio.

`E2.3` y [`C7`](../contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) fijan el contrato; su prueba
es **T170**.

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
