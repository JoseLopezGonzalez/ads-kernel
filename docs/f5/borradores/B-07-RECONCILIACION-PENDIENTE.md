# BORRADOR · `B-07` · El productor del aviso de reconciliación pendiente

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-03
ENTREGABLE: F5-A
PRESION: PN-17
FILA DE LA MATRIZ: F5-OB-15
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Las tres salidas son **incompatibles entre sí** y
> **cada una toca una sede distinta**. Este borrador prepara las tres y no elige ninguna.

---

## 1 · El defecto, con precisión

La especificación aprobada dice que agotar los reintentos de escritura concurrente **deja
todas las órdenes sin consumir**, **no modifica el estado canónico** y **registra
«reconciliación pendiente»**. Una prueba de conformidad aprobada exige lo mismo.

El aviso, sin embargo, está definido como un predicado que **se deriva** del diario de
transacciones, con exactamente **dos disyuntos**, y los dos son sobre el diario. **El
agotamiento de reintentos no emite ningún evento de diario** — el propio diseño lo declara
fuera de esa materia y ordena no modificar el estado canónico.

**Consecuencia mecánica y triple:**

```text
1  la prueba de conformidad NO ES SATISFACIBLE por esta arquitectura
2  el freno del despacho NUNCA DISPARA para este caso
3  el aviso NO TIENE PRODUCTOR por la vía que la especificación le manda tener uno
```

Y lo agrava que el mecanismo escriba «registra reconciliación pendiente» en su salida,
veintiséis líneas antes de que la definición del predicado declare que **se deriva** y que
**no hay bandera que escribir**.

## 2 · Las tres salidas, preparadas

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
SI D-03 = A · tercer disyunto en el predicado derivado
   el predicado pasa a tener un tercer disyunto que cubre el agotamiento de reintentos.
   SEDE  la definición del predicado, en el diseño
   COSTE el disyunto necesita algo DURABLE que lo sostenga, y la especificación aprobada
         PROHÍBE expresamente modificar el estado canónico en ese punto. Hay que resolver
         esa tensión ANTES, y este borrador no la resuelve

SI D-03 = B · un registro que NO es estado canónico            ← recomendada
   el agotamiento deja rastro en un registro OPERATIVO —fuera del estado canónico, sin
   abrir transacción— y el predicado lo lee.
   SEDE  la salida del mecanismo, y la definición del predicado
   HAY QUE DECLARAR, con precisión y por escrito:
     · que ese registro NO es estado canónico, luego la prohibición se cumple LITERALMENTE
     · que NO exige abrir transacción, que es lo que cerró el problema anterior de esta
       misma familia — registrar lo que impide registrar
     · su ciclo de vida: quién lo escribe, quién lo consume y cuándo se retira
   NO ENMIENDA material aprobado

SI D-03 = C · enmendar la prueba de conformidad
   se acota qué significa «registrar» en la especificación y en su prueba.
   SEDE  material APROBADO: la especificación de capacidades y su prueba
   COSTE es la salida más cara: gasta una enmienda sobre (a) y sobre una prueba que el
         Owner aprobó
```

<!-- ads-lint-ignore-end -->

## 3 · Lo que NO alcanza, y se acota para que nadie lo ensanche

```text
NO ALCANZA  al resto de la definición del predicado: sus dos ramas siguen siendo correctas
            para el conflicto y para la deriva
NO BLOQUEA  el diario de transacciones, ni el mecanismo de escritura concurrente, que sigue
            deteniendo el ciclo y dejando las órdenes intactas
NO DEPENDE  de la sección (g), ni la bloquea
```

## 4 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-17` | `F5-OB-15` | `D-03` | la conformidad de la prueba, el freno del despacho para el canal de órdenes, y cualquier prueba de `F6` que quiera verificarla en verde |

**Prueba prevista:** que la prueba de conformidad sea satisfacible por alguna ruta de la
arquitectura, y que el freno dispare para el caso del canal de órdenes.
