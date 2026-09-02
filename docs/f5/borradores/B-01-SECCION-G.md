# BORRADOR · `B-01` · La sección `(g)` y su apartado de gobierno Git del control repo

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-01
ENTREGABLES: F5-B · F5-C
PRESIONES: PN-1 · PN-11
FILAS DE LA MATRIZ: F5-OB-01 · F5-OB-02
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Es el esqueleto de una sección normativa que
> **no existe todavía**. Su forma exacta depende de `D-01`, que el Owner no ha respondido.
> Ninguna parte de este fichero puede citarse como vigente, y su zona lo clasifica como
> `NO_APLICABLE_A_IMPLEMENTACION` en el registro de sedes canónicas.

---

## 1 · Qué falta exactamente, y por qué sólo el Owner puede ponerlo

La especificación aprobada delega la disposición física del estado durable a una sección
`(g)` **que nunca se escribió**, y declara además una regla de diario PENDIENTE «hasta
diseñar memoria, eventos y recuperación en la sección `(g)`, no ahora por inferencia».

El diseño de esa materia **existe y es extenso**, pero vive en un documento **derivado**, y
un derivado no puede autoconcederse la autoridad que su fuente reservó a otra sección. Ésa
es la presión, literalmente, y no se resuelve leyendo mejor: se resuelve con un acto.

## 2 · Las materias que `(g)` tiene que cubrir

**Derivadas de tres fuentes que coinciden, no escritas a mano.** El criterio de aceptación
`A3` exige que `(g)` «cubra las materias que su fuente le reservó», y ésta es la lista
reconstruida a partir de la delegación de `(a)`, de la ampliación que la presión declara, y
de la resolución que fijó la sede del gobierno Git.

```text
 1  cuántos ficheros y cómo se fragmentan                      delegado por (a)
 2  transacciones y protocolo transaccional                     delegado por (a)
 3  el diario de eventos, que es la regla declarada PENDIENTE   delegado por (a)
 4  recuperación, con sus dos ramas y sin mezclas parciales     delegado por (a)
 5  qué es durable y qué es operacional, y qué vive en Git      delegado por (a)
 6  el escalonado de sincronización y sus tres puntos           ampliación de PN-1
 7  que nunca se confirma con una transacción abierta           ampliación de PN-1
 8  la semántica completa del sellado                           ampliación de PN-1
 9  el esquema de identidad direccionado por contenido          ampliación de PN-1
10  concurrencia, bloqueo y orden entre emisores                materia de la disposición
11  versionado y migración de esquema                           materia de la disposición
12  el apartado de GOBIERNO GIT DEL CONTROL REPO                sede fijada por `O16`
13  el apartado de RAÍZ EXTERNA, si `D-02` elige esta sede      condicionado a `D-02`
```

> **ADVERTENCIA DE MÉTODO, y se declara en vez de ocultarse.** Ninguna sede publica esta
> lista cerrada. Está **reconstruida** a partir de tres textos, y el acto del Owner debería
> fijar el perímetro exacto para que `A3` sea verificable de forma mecánica y no por
> lectura. Es un límite de este borrador, no un hallazgo.

## 3 · Lo que YA está fijado, y que `(g)` no puede contradecir

**Esto no se decide en `D-01`: ya es autoridad vigente**, y `(g)` lo instancia sin
contradecirlo.

```text
· los seis invariantes del estado, aprobados en (a)
· que el estado ES los ficheros del repositorio ADS de control, precisado por E2
· que toda transición multiarchivo es recuperable e idempotente, y que lo incompleto se
  detecta y se termina o se revierte SIN INVENTAR ESTADO
· el determinismo: ningún derivado lleva hora de pared, duración ni identidad de proceso
· un solo ejecutor de mutaciones canónicas
· que el estado global REFERENCIA revisiones de otras fuentes y NUNCA las copia
· que la reanudación se reconstruye desde el estado canónico, sin conversación
· que un item multi-fuente no cierra sin su conjunto de integración
· que la autoridad normativa del gobierno Git del control repo vive en (g), que su contrato
  derivado lo materializa F6, y que el contrato de fuentes NO se toca            —`O16`
· que el valor por defecto de la política de publicación es «esperando-owner», y que la
  ausencia de política NUNCA significa «publica»
· que ninguna política autoriza publicar una recuperación, ni autoriza forzar referencias
```

## 4 · Esqueleto de la sección, por opción

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

### Si `D-01` = `A` · ratificación íntegra por remisión

```text
g.0   ACTO DE ADOPCIÓN. La disposición física del estado durable diseñada en «PENDIENTE-DECISION-DEL-OWNER: D-01»
      queda adoptada como sección (g), del mismo grado normativo que (a) y (b).
g.1   PERÍMETRO ADOPTADO. Las trece materias de §2 de este borrador.
g.2   PARÁMETROS QUE SALEN DEL USO REAL, declarados como calibrables y NO como omisiones.
g.3   TRASLADO DE SEDE. El texto adoptado se traslada a docs/rediseno/, porque su sede
      actual es un directorio que el corpus ordena retirar tras F6.
```

### Si `D-01` = `B` · `(g)` normativa breve + contrato derivado ← recomendada

```text
g.0   LA REGLA DE FRONTERA, escrita ANTES que nada:
      «es NORMA todo lo que, si cambiara, obligaría a reaprobar (a), (b) o una enmienda;
       es MECANISMO todo lo demás».
g.1   LA FORMA ELEGIDA. Canónico en ficheros + diario de eventos con transacciones +
      derivados. Y por qué se descartan las otras tres, con su motivo escrito.
g.2   LOS INVARIANTES que la disposición debe cumplir.
g.3   LA RELACIÓN ESTADO ↔ DIARIO. El estado se LEE del fichero y NUNCA se reproyecta; el
      evento explica el cambio. Prohibición de un tercer artefacto que compita con los dos.
g.4   RECUPERACIÓN: las dos ramas, y que ninguna cierra dejando mezcla parcial publicable.
g.5   GOBIERNO GIT DEL CONTROL REPO: la tabla de propiedad y las decisiones que presupone.
g.6   LO QUE BAJA AL CONTRATO DERIVADO, nombrado una a una para que no quede materia
      huérfana: el autómata de fases, la clasificación de ficheros en recuperación, el
      escalonado de sincronización, la forma del identificador y la matriz adversarial.
g.7   LO QUE (g) DEJA EXPRESAMENTE ABIERTO, con su condición de cierre.
```

### Si `D-01` = `C` · `(g)` acotada al desbloqueo

```text
g.1   Instantánea, evento y protocolo transaccional con sus dos ramas de reanudación.
g.2   DIFERIDO EXPRESO, con condición de cierre nombrada: sellado, migración de esquema,
      orden entre máquinas y bloqueo distribuido.
g.3   DECLARACIÓN DE COBERTURA PARCIAL, que es lo que esta opción debe hacer explícito
      para no chocar en silencio con los criterios A1 y A3.
```

<!-- ads-lint-ignore-end -->

## 5 · El apartado de gobierno Git del control repo · `F5-C`

**La sede ya no se pregunta: la fijó `O16`.** Lo que este apartado recoge está determinado, y
su contenido no depende de `D-01` salvo en su extensión.

```text
· la tabla de PROPIEDAD del control repo: quién crea, confirma, publica, abre rama, integra,
  ejecuta la verificación continua, revierte y retira rama
· la rama canónica, y que la regla Git de las fuentes NO se le aplica
· la unidad aislada de trabajo, que es la transacción y no la rama
· que las peticiones de integración NO se usan para el estado
· que la rama canónica NUNCA contiene estado parcial
· la concurrencia entre máquinas, resuelta por comparación e intercambio de Git
· que forzar referencias está PROHIBIDO, sin excepción automática
```

**Y lo que NO entra aquí:** el contrato derivado. Lo materializa `F6`, y no se crea ahora.

## 6 · Trazabilidad

| presión | fila de la matriz | decisión | qué desbloquea al aprobarse |
|---|---|---|---|
| `PN-1` | `F5-OB-01` | `D-01` | el estado durable, el runtime, la iniciativa, la cobertura y el corte de estado mínimo |
| `PN-11` | `F5-OB-02` | `D-01` | el contrato derivado de gobierno Git del control repo, en `F6` |

**Prueba prevista:** que `(g)` exista como sede vigente, que cubra las materias de §2, y que
el primer nodo del orden de construcción deje de estar declarado bloqueado.
