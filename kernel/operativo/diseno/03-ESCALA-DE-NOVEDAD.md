# La escala de novedad: cuánta exploración exige cada trabajo


`C-DIS` (b.16) decide **si** Diseño se activa. Esta escala decide **qué método ejecuta y
cuánto explora**. Son dos preguntas distintas y la segunda no puede quedar al criterio del
agente: si queda, una corrección de espaciado acaba convocando el mismo procedimiento que
una pantalla nueva, o —lo que es peor— una pantalla nueva se resuelve con el esfuerzo de
una corrección de espaciado.

## Las cinco variables del encuadre de diseño

El nivel **no se elige**: se calcula. Y para calcularlo hacen falta cinco cosas que se
responden **mirando el producto —el control repo y sus fuentes— y la memoria de diseño**,
no interpretando:

```text
superficie_construida     existe producto o superficie REAL, en uso o utilizable, que
                          merece preservarse. No «hay código»: hay algo que alguien usa.

memoria_vigente           existe dirección de diseño ESCRITA que además es FIABLE, no está
                          obsoleta y REPRESENTA lo implementado. Las cuatro cosas. Una
                          memoria que describe una pantalla que ya no existe no es vigente.

dir_sustituye             un item DIR aprobado sustituye EXPRESAMENTE la dirección
                          anterior. Es una decisión registrada, no una impresión.

patron_cubre              existe un patrón VIGENTE cuyo alcance cubre este caso y cuyos
                          criterios comprobables se cumplen — el test de a.8, literal.

premium_o_nuevo           la superficie está declarada premium, O introduce una interacción
                          o un movimiento que el producto no tenía.
```

> **Por qué `memoria_vigente` y no «existe memoria».** Preguntar sólo si la memoria existe
> hacía **inalcanzable el nivel N3**: un producto construido sin dirección escrita responde
> «no existe memoria» y caía en N4, de modo que la Reconstrucción no se elegía nunca y un
> brownfield recibía el método de fundación. Es el hallazgo **A-07**, y esta es su
> corrección.

## Cómo se calcula el nivel

Se evalúan los cinco niveles **en orden**. Gana el primero cuya condición es verdadera. Las
condiciones son **expresiones booleanas sobre las cinco variables**, no frases:

```text
N4  FUNDACIÓN        dir_sustituye  or  (not superficie_construida and not memoria_vigente)
N3  RECONSTRUCCIÓN   superficie_construida  and  not memoria_vigente
N2  DIRECCIÓN NUEVA  memoria_vigente  and  not patron_cubre  and  premium_o_nuevo
N1  CASO NUEVO       memoria_vigente  and  not patron_cubre  and  not premium_o_nuevo
N0  EXTENSIÓN        memoria_vigente  and  patron_cubre
```

**La cobertura es total y los cinco niveles son alcanzables**, y no por argumento: T138
enumera las treinta y dos combinaciones posibles de las cinco variables y comprueba que
cada una produce **exactamente un** nivel, y que **ningún nivel queda sin combinación que
lo alcance**.

Los cinco casos que el Owner nombró expresamente, resueltos por la misma tabla:

| situación real | variables | nivel |
|---|---|---|
| proyecto realmente en blanco | nada construido, sin memoria | **N4** |
| proyecto vivo sin memoria de diseño | construido, sin memoria | **N3** |
| proyecto vivo con memoria obsoleta | construido, memoria no vigente | **N3** |
| dirección sustituida por un DIR aprobado | `dir_sustituye` | **N4** |
| memoria vigente y patrón que cubre el caso | vigente, cubre | **N0** |

> **Un proyecto no se clasifica por anticipado.** El nivel sale de mirar lo que hay. Si un
> proyecto tiene aplicación o interfaz real, lo más probable es N3 — pero lo decide la
> evidencia, no la expectativa.

## Qué exige cada nivel

> **Nivel pequeño NO significa sin verificación.** Lo que un nivel bajo elimina es la
> EXPLORACIÓN, nunca la comprobación. Los dos gates de Diseño son **obligatorios en los
> cinco niveles**; lo que cambia entre niveles es **cuánta de su evidencia puede
> reutilizarse** de la del patrón vigente que se está aplicando.

Cuatro cosas distintas, y ninguna es «se omite»:

```text
GATE OBLIGATORIO            hay que pasarlo. En los cinco niveles, los dos.

EVIDENCIA REUTILIZADA       un eje se satisface con la evidencia YA VIGENTE del patrón que
                            se aplica, enlazándola. No se vuelve a producir.

EVIDENCIA PROPIA            un eje NUNCA se reutiliza: depende de esta aplicación concreta
                            y hay que producirla otra vez.

OMISIÓN                     no existe. Ningún nivel omite un gate. Si alguna vez hiciera
                            falta, sería un override declarado en el PROFILE (K0.7), no una
                            tabla de niveles.
```

**Qué demuestra que un patrón previo sigue siendo aplicable** — sin esto, la reutilización
es una excusa:

```text
[ ] el patrón está VIGENTE: su clase no es expired_or_superseded (a.8)
[ ] su ALCANCE declarado cubre este caso
[ ] se cumplen TODOS sus criterios comprobables
[ ] no se introduce ningún elemento fuera de su alcance
[ ] su evidencia enlazada existe y se puede abrir
[ ] su condición de caducidad NO se ha cumplido
```

Los seis son el test de «extiende un patrón aprobado» de a.8, y se anotan en el dictamen.

Los cinco niveles, en forma canónica:

```yaml ads:nivel-novedad
id: N4
nombre: Fundación
orden: 1
metodo: DIS/Fundacion
condicion_formal: "dir_sustituye or (not superficie_construida and not memoria_vigente)"
condicion_legible: >
  No hay superficie construida que merezca preservarse y tampoco dirección de diseño
  vigente; o un DIR aprobado sustituye expresamente la dirección anterior.
exploracion_minima: "sin techo de sesiones; mínimo tres territorios creativos con moodboard"
gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]
ejes_reutilizables: []
ejes_nunca_reutilizables:
  [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, acabado, fidelidad, alma]
evidencia_de_vigencia:
  - "no aplica: no hay patrón previo del que reutilizar nada"
critica_visual: completa
owner: obligatorio
estaciones: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

```yaml ads:nivel-novedad
id: N3
nombre: Reconstrucción
orden: 2
metodo: DIS/Reconstruccion
condicion_formal: "superficie_construida and not memoria_vigente"
condicion_legible: >
  Existe producto o superficie real, pero la memoria de diseño falta, es poco fiable, está
  obsoleta o no representa lo implementado.
exploracion_minima: "inventario completo antes de proponer; mínimo dos propuestas de evolución"
gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]
ejes_reutilizables: []
ejes_nunca_reutilizables:
  [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, acabado, fidelidad, alma]
evidencia_de_vigencia:
  - "no aplica: lo que se reconstruye es precisamente la dirección que falta"
critica_visual: completa
owner: obligatorio
estaciones: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
```

```yaml ads:nivel-novedad
id: N2
nombre: Dirección nueva en una superficie
orden: 3
metodo: DIS/Evolucion
condicion_formal: "memoria_vigente and not patron_cubre and premium_o_nuevo"
condicion_legible: >
  Hay dirección vigente, ningún patrón cubre este caso, y la superficie es premium o
  introduce una interacción o un movimiento que no existía.
exploracion_minima: "mínimo tres direcciones distintas entre sí, rama DIVERGENTE"
gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]
ejes_reutilizables: []
ejes_nunca_reutilizables:
  [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, acabado, fidelidad, alma]
evidencia_de_vigencia:
  - "el sistema de diseño vigente y su versión, para comprobar que la dirección nueva no lo rompe"
critica_visual: completa
owner: obligatorio
estaciones: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

```yaml ads:nivel-novedad
id: N1
nombre: Caso nuevo dentro del sistema
orden: 4
metodo: DIS/Evolucion
condicion_formal: "memoria_vigente and not patron_cubre and not premium_o_nuevo"
condicion_legible: >
  Hay patrones vigentes, pero ninguno cubre este caso con su alcance declarado, y la
  superficie no es premium ni introduce interacción o movimiento nuevos.
exploracion_minima: "mínimo dos alternativas comparadas contra los principios, rama de EXTENSIÓN"
gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]
ejes_reutilizables: [personalidad, actualidad, alma]
ejes_nunca_reutilizables: [intencion, jerarquia, sistema, respuesta, acabado, fidelidad]
evidencia_de_vigencia:
  - "la entrada del patrón vecino cuyo lenguaje se extiende, con su clase y su alcance"
  - "el dictamen anterior del que se reutiliza el eje, enlazado y con su fecha"
critica_visual: completa
owner: opcional-acumulada
estaciones: [1, 4, 5, 6, 7, 8, 9, 10, 11, 13]
```

```yaml ads:nivel-novedad
id: N0
nombre: Extensión de patrón vigente
orden: 5
metodo: DIS/Evolucion
condicion_formal: "memoria_vigente and patron_cubre"
condicion_legible: >
  Un patrón vigente cubre el caso, se cumplen sus criterios comprobables y no se introduce
  nada fuera de su alcance. Es el test de a.8, literal.
exploracion_minima: "ninguna: se aplica el patrón y se registra que se aplicó"
gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]
ejes_reutilizables: [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, alma]
ejes_nunca_reutilizables: [acabado, fidelidad]
evidencia_de_vigencia:
  - "la entrada del patrón aplicado: clase, alcance, criterios comprobables y caducidad"
  - "la evidencia enlazada del patrón, comprobada como abrible y no caducada"
  - "la comprobación de los seis puntos del test de vigencia, anotada en el dictamen"
critica_visual: de-reutilizacion
owner: ninguna
estaciones: [1, 8, 9, 10, 11, 13]
```

> **La crítica visual `de-reutilizacion` de N0 es más corta, no inexistente.** El dictamen
> existe igual, y lo que comprueba es que el patrón está vigente, que la aplicación cae
> dentro de su alcance, y que `acabado` y `fidelidad` —los dos ejes que nunca se
> reutilizan— se cumplen en esta superficie concreta. Sin ese dictamen,
> `gate:excelencia-visual` no cierra en ningún nivel.

### «Distintas entre sí» es comprobable

Dos direcciones son distintas si difieren en **al menos dos** de estas cinco dimensiones:

```text
[ ] estructura de la composición          dónde vive cada cosa
[ ] jerarquía                             qué domina y cómo se consigue que domine
[ ] sistema tipográfico                   familia, escala o uso del peso
[ ] tratamiento del color                 rol del color en la jerarquía, no la paleta
[ ] densidad y ritmo                      cuánto cabe y cómo respira
```

Tres propuestas que sólo cambian la paleta **son una sola dirección con tres pinturas**, y
el gate las rechaza por no cumplir el mínimo de exploración. Esta comprobación es del rol
`DIS/critica-visual`, y la ejecuta en la fase divergente, **antes** de la convergencia.

## Por qué N0 existe

Sin N0, cada ajuste dentro de un patrón aprobado convocaría exploración: eso es ceremonia
inútil y es el modo de fallo (b) de a.7. Con N0, el sistema **aplica lo aprobado sin volver
a discutirlo**, que es justamente para lo que sirve tener un sistema de diseño.

```text
N0 NO SIGNIFICA trabajo barato, acabado inferior ni verificación reducida.
   Los DOS gates se pasan igual. Lo que N0 elimina es la EXPLORACIÓN.
   Y los ejes `acabado` y `fidelidad` NUNCA se reutilizan: son de esta superficie.
```

## Registro obligatorio

Todo paquete de DIS declara en su checkpoint:

```text
nivel_de_novedad: N0 | N1 | N2 | N3 | N4
motivo:           la pregunta de la escala que se respondió «sí», citada
```

Un paquete de DIS sin nivel declarado no puede cerrar: `gate:excelencia-visual` lo
comprueba en su comprobación `nivel-declarado`, junto con la evidencia de vigencia cuando
el nivel reutiliza algún eje. **Bajar el nivel es la forma más silenciosa de abaratar el
diseño**, y por eso el nivel se calcula con las cinco variables de arriba y se cita la
condición que resultó verdadera, en vez de elegirse.
