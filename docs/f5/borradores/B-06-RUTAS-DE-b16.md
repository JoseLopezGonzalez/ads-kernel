# BORRADOR · `B-06` · Las tres enmiendas a la tabla de rutas, en un solo acto

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-06
PENDIENTE-DECISION-DEL-OWNER: D-07
PENDIENTE-DECISION-DEL-OWNER: D-09
ENTREGABLE: F5-A
PRESIONES: PN-8 · PN-13 · PN-14
FILAS DE LA MATRIZ: F5-OB-11 · F5-OB-12 · F5-OB-13
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Son **tres decisiones distintas** —el Owner puede
> responderlas de forma diferente— que se **aplican en una sola enmienda** porque tocan la
> misma tabla. Agruparlas en un acto es más barato y evita tres pasadas sobre material
> aprobado; **no** las convierte en una sola pregunta.

---

## 1 · Las tres, y por qué son distintas

```text
D-06 · PN-8    a la ruta de AUDITORÍA le falta el productor del dictamen de verificación
D-07 · PN-13   dos procesos no admiten dominio, seguridad ni diseño, y el paso de
               descubrimiento de un producto NUEVO tiene que entrar por uno de ellos
D-09 · PN-14   se nombra un MÉTODO donde va una CAPACIDAD, en dos puntos aprobados
```

**La sede lo dice de la primera y la segunda:** no son la misma presión —«otra fila, otra
capacidad y otro remedio»—. Y la tercera no es una cuestión de rutas: es un identificador
mal puesto que **predetermina** lo que otra regla prohíbe predeterminar.

## 2 · Esqueleto de la enmienda única

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
ENMIENDA E<n> A LAS SECCIONES (a) Y (b) · composición de rutas

  identificador   E<n>
  enmienda a      docs/rediseno/b-RECORRIDO-APROBADA.md
                  docs/rediseno/a-CAPACIDADES-APROBADA.md
  fecha           PENDIENTE-DECISION-DEL-OWNER: D-06
  autoridad       Owner
  estado          PENDIENTE-DECISION-DEL-OWNER: D-06

  E<n>.1 · la ruta de AUDITORÍA                                  depende de D-06
     SI A  AMPLÍA la fila: verificación entra como participante CONDICIONAL, con su
           condición declarada
     SI B  PRECISA que la celda auditada NO exige dictamen de verificación, y NOMBRA la
           capacidad que lo produce en su lugar

  E<n>.2 · los procesos de sistema e investigación               depende de D-07
     SI A  AMPLÍA las dos filas: dominio, seguridad y diseño entran como CONDICIONALES,
           cada uno con su condición
     SI B  PRECISA que el descubrimiento de dominio y diseño de un producto NUEVO no
           pertenece a ese paso, y NOMBRA dónde pertenece

  E<n>.3 · el método nombrado como participante                  depende de D-09
     SI A  SUSTITUYE, en los DOS puntos aprobados, la cadena del método por la CAPACIDAD
           con su condición; y PRECISA que el método concreto lo calcula la escala de
           novedad, no la ruta
     SI B  PRECISA que las dos cadenas designan al mismo participante, sin tocar el texto

  E<n>.4 · IMPACTO
     sobre las composiciones que la tabla deriva · sobre el gate de «listo para
     construir» · sobre los derivados del kernel, que actualiza F6 y NO F5

  E<n>.5 · ORDEN
     esta enmienda se aplica ANTES de la renumeración editorial, porque puede introducir
     referencias nuevas al recorrido aprobado
```

<!-- ads-lint-ignore-end -->

## 3 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-8` | `F5-OB-11` | `D-06` | que una casilla de cobertura alcance «verificado» CON EVIDENCIA |
| `PN-13` | `F5-OB-12` | `D-07` | que el paso de descubrimiento abra con dominio y diseño, y que el arranque incorpore el dictamen de seguridad |
| `PN-14` | `F5-OB-13` | `D-09` | que la composición de esa ruta sea verificable mecánicamente contra la fuente |

**Nota sobre la tercera:** es la mitad `F5` de un hallazgo externo cuya otra mitad —
actualizar los derivados del kernel— es de `F6`. **`F5` toca la fuente; `F6` toca el
derivado, y en ese orden.**
