# C5 — El handoff entre capacidades


> El formato de entrega entre equipos es una de las cosas que a.11 declaró **ausentes por
> completo** en el kernel 1.3.0. Esto lo cierra en su forma operativa.

Un handoff no es «pasar el trabajo». Es una entrega con **cinco obligaciones**:

```text
1  QUIÉN ENTREGA QUÉ            artefactos concretos, localizables, no «el trabajo hecho»
2  QUÉ COMPRUEBA QUIEN RECIBE   antes de tomar custodia, no después de empezar
3  QUÉ LO HACE RECHAZABLE       condiciones escritas, no impresión de calidad
4  QUÉ EVIDENCIA ACOMPAÑA UNA DEVOLUCIÓN   una devolución sin evidencia es una opinión
5  QUÉ CHECKPOINT SOBREVIVE     el receptor debe poder reanudar sin hablar con el emisor
```

## La regla que evita el rebote infinito

```text
QUIEN RECIBE COMPRUEBA ANTES DE TOMAR CUSTODIA.

Si rechaza, el paquete NO cambia de custodia: sigue en el emisor, con el motivo escrito.
Eso NO cuenta como devolución a efectos del freno de a.7, porque la capa nunca se
depositó.

Si acepta y DESPUÉS descubre que la capa anterior es insuficiente, entonces sí es
DEVOLUCIÓN, y cuenta para el freno de dos.
```

Esta distinción es la que impide que un equipo acepte trabajo malo por cortesía y luego lo
devuelva, gastando una de las dos devoluciones disponibles en algo que era comprobable de
entrada.

## Estructura de un handoff

Todo handoff del sistema se declara con un bloque `ads:handoff` conforme a
[`esquemas/handoff.yaml`](../esquemas/handoff.yaml). Los handoffs concretos entre
capacidades viven en [`circuitos/`](../circuitos/), no aquí: **C5 define la forma, no las
instancias.**

```yaml
de: <CAP emisora>
a:  <CAP receptora>
cuando: <condición comprobable que dispara la entrega>
entrega: [<artefacto 1>, <artefacto 2>]
comprueba_al_recibir: [<comprobación 1>, …]
rechaza_si: [<condición 1>, …]
devolucion: <qué ocurre y con qué evidencia>
evidencia_de_devolucion: [<qué acompaña obligatoriamente>]
owner: <qué parte de esto pertenece a la decisión del Owner, o «ninguna»>
checkpoint: <qué del checkpoint del emisor debe poder leer el receptor>
```

## Qué NO viaja en un handoff

```text
NO VIAJA   una copia del contexto: se enlaza el origen y su versión (based_on)
NO VIAJA   una decisión tomada por el emisor en materia del receptor
NO VIAJA   una tarea. Viaja un ARTEFACTO y su evidencia; el trabajo lo compone DSP
NO VIAJA   una conversación con el Owner. Viaja lo que decidió, citado, con fecha
NO VIAJA   el contenido de una FUENTE. Viaja su revisión exacta: `<source-id>@<sha>`
```

> **Enlaces, no copias.** Es la misma regla del checkpoint de a.10, y por el mismo motivo:
> una copia envejece en silencio y nadie sabe cuál de las dos manda.

**A través de la frontera de un repositorio, la regla es la misma y aprieta más.** Un
artefacto que vive en una fuente —código, esquema, contrato de API— se entrega por
referencia a su revisión, nunca copiándolo al control repo ni a otra fuente: eso crearía la
segunda copia editable que `I5` prohíbe, y esta vez sin nadie que la vea envejecer. El
handoff nombra la fuente por su `id` de `SOURCES.toml`, y el receptor la materializa si la
necesita.

> **Cuidado con la palabra «fuente».** En este corpus significa dos cosas: el *origen* de
> una información —«la fuente de esta decisión»— y una **FUENTE** de `SOURCES.toml`, que es
> un repositorio del producto (C6 N5). Cuando el sentido no se deduzca del contexto, se
> escribe «fuente del manifiesto» o se cita su `id`.

## Devolución: qué evidencia es obligatoria

Una devolución **DEBE** llevar, sin excepción:

```text
[ ] QUÉ falta, en la capa concreta, no en el trabajo en general
[ ] POR QUÉ es insuficiente para la capa del receptor: qué no puede hacer con ella
[ ] QUÉ LA CERRARÍA: la comprobación o el artefacto concreto que resolvería el hueco
[ ] LA EVIDENCIA que sostiene el hallazgo, del tipo que exija el handoff
    (captura, medición, traza, grabación, salida de test, enlace al contrato roto)
```

Una devolución sin los cuatro campos **se rechaza como devolución** y el paquete vuelve al
receptor: no cuenta para el freno, porque no era una devolución.

## Cuándo interviene el Owner en un handoff

**Casi nunca.** El campo `owner` de la mayoría de handoffs es `ninguna`. Interviene sólo
cuando la entrega contiene una decisión de su autoridad —tabla de a.8— o cuando la
devolución escala por el freno de a.7 con las dos posturas escritas.

```text
UN HANDOFF NO ES UN PUNTO DE APROBACIÓN.
Entre dos equipos no hay un humano validando el traspaso.
```

## Handoff y checkpoint

El receptor **carga el checkpoint del emisor** en la parte que le concierne: `based_on`
con versiones, `freshness`, y las decisiones del Owner captadas. Si `based_on` cambió,
revalida **sólo la parte afectada** (a.10).

```text
El emisor NO explica su trabajo al receptor.
El receptor lo entiende leyendo los artefactos y el checkpoint.
Si no puede, ése es el defecto — y se corrige en el emisor, no con una reunión.
```
