# BORRADOR · `B-10` · La nota de vigencia en el documento de trabajo del Owner

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: R-03
ENTREGABLE: F5-F
FILA DE LA MATRIZ: F5-OB-22
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Y aquí la advertencia pesa más que en los demás
> borradores: **este texto está escrito para el documento del Owner, y la nota es suya.** Se
> propone para que él la adopte, la corrija o la sustituya por su propia redacción. **No se
> ha insertado en su documento, y ningún agente lo hará sin su acto.**

---

## 1 · El problema, en claro

El documento de trabajo del Owner sobre la arquitectura multirrepositorio dice, en **cuatro
sitios distintos**, que esa materia está abierta y que **no se debe implementar**. Mientras
tanto, los contratos multirrepositorio **ya la implementan**, y el propio Owner la aprobó por
otra vía, en un documento distinto marcado como decisión aprobada para implementación.

**La contradicción está REGISTRADA**, con las dos posturas escritas, y su reconciliación
tiene propietario declarado —el Owner— y está inscrita como deuda.

**Y lo que la precedencia ya resuelve, para que no se lea de más:** manda la decisión
aprobada, y los contratos son su instanciación. **No es una contradicción entre dos
autoridades vigentes**: lo que queda vivo es una **nota de vigencia pendiente** en el
documento de trabajo, no una elección sin hacer.

## 2 · Las cuatro sedes, y por qué son cuatro y no una

El hallazgo que ordena la nota **nombra sólo una**. Pero las otras tres dicen lo mismo con
otras palabras, y **una nota que tocara una sola dejaría vivas tres afirmaciones idénticas**.

```text
1  el bloque de estado de cabecera: «no es una especificación cerrada ni autoriza a
   implementar automáticamente todos sus puntos»
2  la sección de cuestión abierta crítica: «NO IMPLEMENTAR TODAVÍA»
3  la sección de instrucción para futuras implementaciones: «hasta que el Owner cierre la
   decisión multi-repo … no se debe imponer una materialización física definitiva»
4  la fila de estado de las ideas: «ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO»
```

> **Éste es un aporte de este macrobloque y se declara como tal**, en vez de presentarlo
> como si la sede lo dijera: la sede nombra la cuarta. Las otras tres las localizó la
> lectura de este encargo, y se traen porque cerrarlas juntas es el único modo de que la
> nota haga lo que promete.

## 3 · Texto propuesto para la nota

> **PROPUESTA DE REDACCIÓN, EN VOZ DEL OWNER, PARA QUE EL OWNER LA ADOPTE O LA CAMBIE.**
> Si el Owner prefiere otra redacción, la suya sustituye a ésta sin discusión: es su
> documento.

<!-- ads-lint-ignore-start: propuesta de texto pendiente de adopción por el Owner -->

```text
NOTA DE VIGENCIA

  Las afirmaciones de este documento que dicen «no implementar», «no implementar
  todavía» o «no implementar sin diseño previo» sobre la materialización física
  multi-repositorio quedan SUSTITUIDAS en ese punto concreto, y por este orden:

  1  la decisión multi-repositorio está CERRADA y APROBADA PARA IMPLEMENTACIÓN en el
     documento del Owner que la recoge, que es la sede que manda sobre esta materia;
  2  su instanciación son los contratos de producto, fuentes y workspace, y de gobierno
     Git multi-fuente, más la enmienda que los incorporó a la especificación aprobada;
  3  este documento CONSERVA su carácter de documento de trabajo para todo lo demás, y
     sigue sin autorizar a implementar sus otros puntos por sí mismo.

  Lo que esta nota NO hace: no aprueba ninguna otra idea de este documento, no cierra
  ninguna otra cuestión declarada abierta, y no altera el estado de ninguna fase.
```

<!-- ads-lint-ignore-end -->

## 4 · Lo que la nota NO resuelve, y se dice

```text
NO RESUELVE  el campo de autoridad de los ficheros del Owner. Es otro remedio, con otra
             fase, y la sede advierte expresamente que un campo de autoridad NO retira la
             frase: son remedios distintos
NO RESUELVE  ninguna otra cuestión declarada abierta en ese documento
NO CIERRA    ningún hallazgo vivo
```

## 5 · Trazabilidad

| origen | fila | decisión | qué cierra |
|---|---|---|---|
| el hallazgo externo con propietario «el Owner» y fase `F5` | `F5-OB-22` | `R-03` | la deuda de coherencia entre el documento de trabajo y lo que los contratos ya implementan |

**Prueba prevista:** que ninguna de las cuatro afirmaciones quede viva sin nota, y que la
contradicción registrada deje de tener las dos posturas abiertas.
