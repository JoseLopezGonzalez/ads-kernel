# Las cinco entregas que `11-ARQ` §8.0 declara

> **Añadidas por `F6`, macrobloque 3.** `11-ARQ` §8.0 las escribe una a una en su bloque
> «`SIS` y `PLT`, dicho aparte» y remite su materialización a este directorio: «Son
> instancias, no norma: no requieren decisión del Owner, y su ausencia hoy NO bloquea la
> composición, sólo la entrega». Forma: [`C5`](../contratos/C5-HANDOFF.md).


```yaml ads:handoff
id: handoff:sis-a-plt
de: SIS
a: PLT
cuando: "el alcance del paquete declara fuentes que no están materializadas en el workspace y `C7:82` atribuye la materialización a PLT"
entrega:
  - "la SOLICITUD DE MATERIALIZACIÓN de las fuentes del alcance, por su `id` de SOURCES.toml y su `path` declarado"
  - "la revisión exacta que el paquete necesita de cada fuente, `<source-id>@<sha>`"
comprueba_al_recibir:
  - "cada fuente solicitada está declarada en SOURCES.toml con `id` y `path`"
  - "ninguna ruta de destino escapa del workspace ni cae dentro del control repo"
  - "la solicitud NO incluye rama, commit, push ni PR: eso es de la capacidad con custodia y no de PLT (`C7:83`-`C7:86`)"
rechaza_si:
  - "la solicitud pide a PLT una operación que `C7` no le atribuye"
  - "el destino está ocupado por otro repositorio o el remoto no corresponde"
devolucion: >
  PLT devuelve a SIS cuando la solicitud nombra una fuente que el manifiesto no declara, o pide una operación fuera de `C7:82`.
  El paquete queda esperando-dependencia y NO se despacha.
evidencia_de_devolucion:
  - "el `id` de la fuente que el manifiesto no declara, o la operación pedida y la fila de `C7` que la atribuye a otro"
owner: "ninguna: materializar una fuente declarada no es materia del Owner."
checkpoint: "SIS lee de PLT: qué fuentes quedaron materializadas y en qué revisión, para no volver a pedirlas."
```

```yaml ads:handoff
id: handoff:sis-a-con
de: SIS
a: CON
cuando: "un paquete declara `escribe_fuentes` y la obligación `cambio-construido` del proceso está sin satisfacer"
entrega:
  - "el SOURCE CHANGE: el paquete con su `lee_fuentes` y su `escribe_fuentes`"
  - "la custodia de rama, commit, push, PR y CI POR FUENTE bajo `C7:83`-`C7:86`"
  - "la capa de SIS que declara qué cambia en la fábrica y por qué"
comprueba_al_recibir:
  - "cada fuente de escritura está justificada por el objetivo del paquete"
  - "las fuentes del alcance están materializadas: `gate:workspace-conforme` pasa"
  - "la capa de SIS enlaza el problema real que justifica el cambio"
rechaza_si:
  - "hay una fuente en `escribe_fuentes` que el objetivo del paquete no justifica"
  - "el paquete no declara `lee_fuentes` ni `escribe_fuentes` y toca código"
devolucion: >
  CON devuelve a SIS cuando lo declarado por SIS no se puede construir sin ampliar el alcance.
  La devolución cuenta para el freno de `a.7` sólo si CON ya había tomado custodia.
evidencia_de_devolucion:
  - "qué parte de la capa de SIS no es construible y qué alcance haría falta"
owner: "la autorización de retirada POR FUENTE, cuando el cambio retira algo heredado (`A8`, `M6`)."
checkpoint: "CON lee de SIS: la justificación de producto enlazada y las decisiones del Owner captadas, para no volver a preguntarlas."
```

```yaml ads:handoff
id: handoff:sis-a-ver
de: SIS
a: VER
cuando: "el cambio de la fábrica está construido y hay que proponer un nivel de certificación con su evidencia"
entrega:
  - "el dosier de certificación: las celdas de cobertura del sujeto"
  - "la evidencia ejecutada, con el estado real de cada prueba"
  - "el nivel PROPUESTO, que VER verifica y no decide"
comprueba_al_recibir:
  - "cada celda propuesta trae la evidencia que la sostiene, ejecutada"
  - "ninguna prueba se declara superada sin haberse ejecutado"
  - "el sujeto de la certificación trae sus identificadores resueltos"
rechaza_si:
  - "hay una celda propuesta sin evidencia enlazada"
  - "el nivel propuesto presupone otro nivel que no está verificado y vigente"
devolucion: >
  VER devuelve a SIS con la celda concreta cuya evidencia falta o no sostiene lo que afirma.
  VER verifica y NO certifica.
evidencia_de_devolucion:
  - "la celda concreta, qué evidencia falta y qué comprobación la cerraría"
owner: "ninguna: verificar no es aprobar, y el nivel lo emite SIS."
checkpoint: "VER lee de SIS: el sujeto con sus identificadores y la huella de la evidencia, para poder contrastar sin reproducirla entera."
```

```yaml ads:handoff
id: handoff:con-a-ent
de: CON
a: ENT
cuando: "el cambio está construido en una o varias fuentes y hay que declarar convergencia (`C7:88`-`C7:89`)"
entrega:
  - "el RESULTADO POR FUENTE: qué quedó construido en cada `<source-id>@<sha>`"
  - "el estado de CI por fuente, que verifica push y PR"
comprueba_al_recibir:
  - "cada fuente del alcance trae su resultado, sin huecos"
  - "CI está en verde en cada fuente, o consta por qué no aplica"
  - "ninguna fuente quedó con trabajo a medias sin declararlo"
rechaza_si:
  - "falta el resultado de alguna fuente del alcance"
  - "hay una fuente con CI en rojo y sin motivo escrito"
devolucion: >
  ENT devuelve a CON nombrando la fuente sin resultado o con CI en rojo.
  Mientras no converjan todas, ENT sostiene el estado INTEGRACIÓN PARCIAL, que no es un fallo: es un estado declarado.
evidencia_de_devolucion:
  - "el `id` de la fuente, su revisión y la salida de CI que lo sostiene"
owner: "materia reservada en el merge, el release y el rollback irreversible, donde `C7` la exige."
checkpoint: "ENT lee de CON: la revisión exacta de cada fuente, nunca una copia de su contenido (`C5`)."
```

```yaml ads:handoff
id: handoff:ent-a-ver
de: ENT
a: VER
cuando: "ENT ha declarado la convergencia y ha emitido el Integration Set"
entrega:
  - "la convergencia declarada, con su Integration Set"
  - "la revisión de cada fuente que entra en el conjunto"
comprueba_al_recibir:
  - "el Integration Set nombra todas las fuentes del alcance y ninguna más"
  - "cada fuente entra por una revisión exacta y no por una rama"
  - "`gate:convergencia-de-fuentes` consta superado"
rechaza_si:
  - "el Integration Set deja fuera una fuente del alcance"
  - "alguna fuente entra por una referencia móvil en vez de por su revisión"
devolucion: >
  VER devuelve a ENT cuando el conjunto no es verificable: falta una fuente, o una entra por una referencia que puede moverse.
evidencia_de_devolucion:
  - "el conjunto recibido y la fuente que falta o la referencia móvil concreta"
owner: "el release, donde `C7` reserva la decisión al Owner."
checkpoint: "VER lee de ENT: el Integration Set con sus revisiones, para poder reproducir el conjunto sin hablar con ENT."
```
