# SECCIÓN (g) — ESTADO DURABLE, GOBIERNO GIT DEL CONTROL REPO Y RAÍZ EXTERNA

**ESTADO: APROBADA** por el Owner el 2026-09-02, mediante la resolución
[`O23`](../owner/ADS-OWNER-RESOLUCIONES.md) §2, §3 y §4.

> ## QUÉ ES ESTA SECCIÓN
>
> **Es NORMA, del mismo grado que `(a)` y `(b)`.** La especificación aprobada delegó a una
> sección `(g)` la disposición del estado durable, y esa sección no existía. Ésta la ocupa.
>
> **Es NORMA BREVE.** Fija componentes obligatorios, invariantes observables y condiciones
> de aceptación. **No fija mecanismo**: rutas, nombres de fichero, serialización,
> algoritmos, bloqueos y herramientas pertenecen a los CONTRATOS DERIVADOS que `F6`
> construye, y `g.17` los nombra uno a uno.
>
> **Lo que esta sección NO hace:** no implementa nada, no inicia `F6`, no declara construido
> ningún contrato, no desbloquea PesquerApp y no cierra `F5`.

**Precedencia.** Por encima: las resoluciones del Owner. Al mismo nivel: `(a)`, `(b)` y sus
enmiendas — esta sección **no las contradice, las completa** en la materia que le
reservaron. Por debajo: los contratos y esquemas del kernel, que la instancian.

---

## `g.0` — La frontera entre NORMA y MECANISMO

**Ésta es la regla que decide, para cualquier materia futura, si pertenece aquí o al
contrato derivado.** La fija `O23` §2.

```text
ES NORMA        componentes obligatorios del estado durable · invariantes semánticos ·
                atomicidad · durabilidad · integridad · concurrencia · diario ·
                recuperación · reconciliación · versionado · migración · propiedad y
                autoridad de escritura · auditabilidad · relación con el gobierno Git del
                control repo · frontera con la raíz externa de confianza · condiciones
                observables de aceptación

ES MECANISMO    rutas físicas · nombres concretos de ficheros · formato de serialización ·
                estructuras auxiliares · algoritmos · implementación de bloqueos ·
                estrategia concreta de escritura · herramientas · detalles internos de
                migración
```

**El mecanismo PUEDE evolucionar sin otra decisión del Owner**, y sólo bajo estas cinco
condiciones, que se comprueban juntas. **`O23` §2 enuncia TRES.** Las condiciones 3 y 4 **no
son precisiones nuevas del Owner y no se le atribuyen**: son **consecuencias explícitas de la
condición 1** sobre las invariantes de esta misma sección —durabilidad `g.4`, integridad
`g.5`, recuperación `g.8`, auditabilidad `g.13` e `I-g7`—, y se enuncian aparte porque son
las que más fácilmente se erosionan sin que nadie lo note:

```text
1  preserva TODAS las invariantes normativas de esta sección
2  mantiene compatibilidad, o declara una migración explícita
3  NO rebaja durabilidad, integridad, auditabilidad ni recuperación
4  conserva la separación entre estado canónico, registros auxiliares y evidencia
5  supera las pruebas positivas y negativas de su contrato
```

**Y la consecuencia, dicha para que nadie la invierta:** convertir un detalle puramente
mecánico en norma permanente es un defecto de esta sección, y omitir una materia que sus
fuentes le reservaron también lo es.

## `g.1` — Componentes obligatorios del estado durable

**Son TRES, y son materias diferenciadas. Ninguna implementación puede colapsarlas en una
sola estructura por comodidad.**

```text
ESTADO CANÓNICO    la verdad vigente del producto: items, paquetes, iniciativas, cobertura,
                   memoria y conjuntos de integración. Se LEE directamente, sin reproyectar

DIARIO CANÓNICO    la secuencia de eventos que EXPLICA cómo el estado llegó a ser lo que es,
                   y que sostiene el protocolo transaccional y la recuperación

REGISTRO OPERATIVO el rastro auxiliar durable que produce el runtime cuando una operación
AUXILIAR           se agota sin poder tocar el estado canónico. NO es estado canónico y NO
                   es diario canónico. Su materia está en `g.9`
```

**Y un cuarto plano que NO es estado durable, y se nombra para que no se confunda:** lo
OPERACIONAL —bloqueos, cachés e índices compilados— no se versiona, es reconstruible, y su
desaparición no pierde ninguna verdad.

**Los tres componentes durables viven en el REPOSITORIO DE CONTROL**, y el estado global
**referencia** revisiones de otras fuentes: **nunca las copia**.

## `g.2` — Invariantes semánticos

**Se cumplen siempre, y una implementación que los rompa es defectuosa aunque pase sus
pruebas.**

```text
I-g1  el estado canónico es LEGIBLE sin herramienta: se lee el fichero y se sabe el estado.
      Ninguna lectura del estado exige reproyectar el diario
I-g2  toda transición multiarchivo es RECUPERABLE e IDEMPOTENTE, y lo incompleto se DETECTA
      y se termina o se revierte SIN INVENTAR ESTADO
I-g3  DETERMINISMO: ningún artefacto derivado lleva hora de pared, duración, número de
      ejecución ni identidad de proceso. Mismo estado canónico produce bytes idénticos
I-g4  hay UN SOLO ejecutor de mutaciones canónicas
I-g5  el estado global NO se copia en las fuentes
I-g6  la reanudación se reconstruye DESDE EL ESTADO CANÓNICO, sin conversación y sin el Owner
I-g7  el estado canónico, el diario canónico y el registro auxiliar permanecen SEPARADOS, y
      ninguno se deriva del otro por conveniencia de implementación
```

## `g.3` — Atomicidad

**Una transición multiarchivo es una TRANSACCIÓN**, y se observa como tal: o se ve entera,
o no se ve.

```text
· ninguna transacción deja una mezcla parcial PUBLICABLE
· nunca se confirma en Git con una transacción ABIERTA
· la ventana en que una transacción está incompleta es DETECTABLE, y detectarla no depende
  de haber presenciado el fallo
```

> **Lo que esta sección NO afirma, y se dice contra su propio interés:** no se afirma
> aislamiento de lecturas. Lo que se garantiza es recuperabilidad, idempotencia y
> detectabilidad de la ventana.

## `g.4` — Durabilidad

```text
· lo confirmado como durable SOBREVIVE a un corte, a un reinicio y a un fallo del proceso
· la sincronización con el medio es ESCALONADA, y sus puntos obligatorios son norma; el
  cuándo exacto y el cómo son mecanismo
· una operación que no puede alcanzar durabilidad FALLA de forma visible, y no se declara
  completada
```

## `g.5` — Integridad

```text
· la identidad de un objeto durable se DERIVA DE SU CONTENIDO, y no de su posición ni de un
  contador
· toda corrupción o truncamiento se DETECTA al leer, y produce fallo CERRADO
· ningún resumen calculado por el propio árbol basta como prueba de la integridad de ese
  árbol. Esa prueba pertenece a la raíz externa de `g.15`
```

## `g.6` — Concurrencia

```text
· los escritores concurrentes se SERIALIZAN, y el mecanismo de serialización es del contrato
· un conflicto de escritura se DETECTA, y se detiene el ciclo dejando las órdenes intactas
· agotar los reintentos NO modifica el estado canónico, y produce el registro de `g.9`
· la bifurcación entre máquinas se DETECTA. Su resolución NO se decide en esta sección, y
  queda declarada como materia calibrable del contrato derivado
```

## `g.7` — Diario

**El diario canónico existe, y es norma que exista.** Ocupa la regla que la especificación
aprobada dejó PENDIENTE «hasta diseñar memoria, eventos y recuperación en la sección `(g)`».

```text
· registra los eventos que explican cada transición, con orden reconstruible
· sostiene el protocolo transaccional y la recuperación de `g.8`
· NO es la sede del estado: el estado se lee de su propio fichero
· el SELLADO compacta el diario conservando lo que el estado y la auditabilidad exigen; su
  umbral es parámetro CALIBRABLE del contrato derivado
· retirar el cuerpo de un evento sellado exige una transición explícita y auditable
```

## `g.8` — Recuperación

**Dos ramas, y no hay una tercera.**

```text
COMPLETAR   todo casa con su base o con su resultado → se aplica lo que falte en el orden
            declarado, y se regeneran los derivados

MARCAR      algo no casa NI con la base NI con el resultado → conflicto, con copia íntegra
            de lo divergente. La salida la decide LA AUTORIDAD, no el runtime

NINGUNA de las dos cierra dejando una mezcla parcial publicable.
LO PUBLICADO NO SE RESTAURA NUNCA de forma automática. La reversión está acotada a lo
ESPECULATIVO LOCAL, y se verifica byte a byte antes de emitirse.
NINGUNA política de publicación autoriza publicar una RECUPERACIÓN.
```

## `g.9` — Reconciliación

**Materia fijada por `O23` §4.** Al agotarse los reintentos se escribe un **REGISTRO
OPERATIVO AUXILIAR DURABLE**, y sus propiedades son norma:

```text
· vive en el CONTROL REPO, como materia administrada por el runtime
· SOBREVIVE a reinicios
· es APPEND-ONLY, o tiene semántica equivalente auditable
· identifica PRODUCTO, REPOSITORIO, ITEM, INTENTO, CAUSA y MOMENTO
· su existencia permite deducir de forma INEQUÍVOCA `reconciliacion_pendiente`
· NO modifica por sí mismo el estado canónico
· desaparece ÚNICAMENTE mediante una transición explícita y auditable de reconciliación
```

**Y la separación es norma, no preferencia:** este registro **no es** estado canónico y **no
es** diario canónico. Colapsarlo en cualquiera de los dos rompe `I-g7`.

**Su ruta y su serialización concretas pertenecen al contrato derivado**, y esta sección no
las fija.

## `g.10` — Versionado

```text
· todo objeto durable declara la VERSIÓN DE ESQUEMA con la que fue escrito
· un lector que encuentra una versión que no entiende FALLA CERRADO, y no adivina
· subir de versión exige la migración declarada de `g.11`
```

## `g.11` — Migración

```text
· toda migración es EXPLÍCITA, declarada y auditable. No hay migración implícita al leer
· una migración es RECUPERABLE: interrumpida, se detecta y se termina o se revierte
· los detalles internos de una migración son MECANISMO, y viven en el contrato derivado
```

## `g.12` — Propiedad y autoridad de escritura

```text
· UN SOLO ejecutor muta el estado canónico                                          `I-g4`
· el diario lo escribe ese mismo ejecutor, dentro de la transacción que explica
· el registro auxiliar de `g.9` lo escribe el RUNTIME, fuera del estado canónico
· la RAÍZ EXTERNA de `g.15` NO tiene permiso de escritura sobre lo que verifica
· la autoridad de PUBLICACIÓN es del Owner por defecto, y la ausencia de política declarada
  NUNCA significa «publica»
```

## `g.13` — Auditabilidad

```text
· todo cambio del estado canónico es explicable por el diario
· la evidencia de verificación NO vive dentro del árbol verificado                  `g.15`
· ningún actor puede modificar a la vez el CORPUS, la BATERÍA y el RESULTADO
  — es la separación de poderes del contrato del verificador externo, y entra aquí
    por `I-g7` y por la condición 4 de `g.0`, no por atribución al Owner
· una afirmación sobre el estado se COMPRUEBA contra el estado, y no contra un informe
```

## `g.14` — Gobierno Git del REPOSITORIO DE CONTROL

**Sede fijada por la resolución `O16`**, que resolvió que la autoridad normativa de esta
materia vive aquí, que su contrato derivado lo materializa `F6`, y que el contrato de
gobierno Git **de las fuentes NO se toca y sigue acotado a ellas**.

```text
· la rama canónica del control repo NO se rige por la regla Git de las fuentes
· la unidad aislada de trabajo es la TRANSACCIÓN, no la rama
· las peticiones de integración NO se usan para el estado
· la rama canónica NUNCA contiene estado parcial
· la concurrencia entre máquinas se SERIALIZA por un mecanismo que fija el contrato
  derivado, y la bifurcación se DETECTA
· FORZAR REFERENCIAS ESTÁ PROHIBIDO. Sin excepción automática, y sin que ninguna política
  pueda autorizarlo
· la política de publicación tiene valor por defecto «esperando-owner»
```

**La tabla de propiedad del control repo —quién crea, confirma, publica, abre rama, integra,
verifica, revierte y retira rama— es materia de esta sección y la instancia su contrato
derivado**, que `g.17` nombra. **No se copia aquí la tabla del contrato de fuentes: el sujeto
es distinto.**

## `g.15` — Frontera con la RAÍZ EXTERNA DE CONFIANZA

**Materia fijada por `O23` §3, sobre la obligación que `O18` estableció y `O19` ratificó en
su proyección.** Es NORMA de esta sección, con contrato derivado propio para `F6`.

```text
· se EJECUTA FUERA del repositorio verificado
· usa una IDENTIDAD SIN PERMISO DE ESCRITURA sobre ese repositorio, y distinta de la
  identidad de escritura del runtime
· recibe DESDE FUERA su configuración y su política de admisión: su autoridad NO puede
  depender del árbol que verifica
· sus ENTRADAS son verificadas
· produce EVIDENCIA fuera del árbol verificado, trazable y vinculada a la revisión exacta
· FALLA CERRADO ante entrada inválida, truncamiento o estructura inesperada
· declara sus CONDICIONES DE CERTIFICACIÓN
· PesquerApp permanece BLOQUEADA mientras la raíz externa no esté IMPLEMENTADA y
  CERTIFICADA
```

**La tecnología, el despliegue, las claves y su custodia, las rutas y los mecanismos
concretos pertenecen al contrato de `F6`**, y esta sección **no los elige**.

## `g.16` — Condiciones observables de aceptación

**Una implementación satisface esta sección cuando las nueve se demuestran sobre un árbol
real, y no por argumento.**

```text
G-A1  el estado canónico se lee sin reproyectar, y sin herramienta            `I-g1`
G-A2  una transacción interrumpida se DETECTA, y termina en COMPLETAR o en MARCAR, sin
      dejar mezcla parcial publicable                                        `g.3` `g.8`
      **Cubre `T25`**, incluida su cualificación: alcanza también a las transiciones
      multiarchivo NO originadas en el tablero, que es lo que su fuente reservó a `(g)`
G-A3  un corte durante la escritura no pierde lo declarado durable                  `g.4`
G-A4  una corrupción o un truncamiento producen FALLO CERRADO al leer               `g.5`
G-A5  dos escritores concurrentes se serializan; agotar reintentos deja las órdenes
      intactas y produce el registro auxiliar                               `g.6` `g.9`
G-A6  `reconciliacion_pendiente` se deduce INEQUÍVOCAMENTE del registro auxiliar, y su
      retirada exige una transición explícita                                       `g.9`
G-A7  una versión de esquema desconocida produce FALLO CERRADO, y no una adivinanza `g.10`
G-A8  forzar una referencia del control repo es imposible por política, y detectable si se
      intenta                                                                      `g.14`
G-A9  un veredicto falseado DESDE DENTRO del árbol es DESMENTIDO por la atestación
      externa                                                                      `g.15`
```

**Cada una tiene escenario POSITIVO y escenario NEGATIVO, y ambos son obligatorios.** Un
verde sin su negativo no demuestra nada, y esta sección no lo acepta como prueba.

## `g.17` — Los contratos derivados que `F6` debe construir

**Se NOMBRAN aquí, y NO se escriben aquí. Ninguno existe, ninguno está implementado y
ninguno está certificado.**

| contrato derivado | qué materia instancia | estado |
|---|---|---|
| **contrato de ESTADO DURABLE** | `g.1`–`g.13`: rutas, nombres, serialización, algoritmos, bloqueos y migración | **NO CONSTRUIDO** · `F6` |
| **contrato de GOBIERNO GIT DEL CONTROL REPO** | `g.14`, incluida su tabla de propiedad. Contrato NUEVO e independiente del de fuentes, según `O16` | **NO CONSTRUIDO** · `F6` |
| **contrato de RAÍZ EXTERNA DE CONFIANZA** | `g.15`: tecnología, despliegue, claves y su custodia, rutas y mecanismos | **NO CONSTRUIDO** · `F6` |

**Parámetros declarados CALIBRABLES**, que el contrato derivado fija y ajusta sin volver al
Owner, bajo las cinco condiciones de `g.0`:

```text
· el umbral de sellado del diario
· el formato concreto del diario
· la estrategia de bloqueo entre máquinas
· la resolución de la bifurcación entre máquinas
· la política de retirada de cuerpos sellados
```

> **Y una precisión que evita una dependencia circular:** estos parámetros son calibrables
> **por el contrato derivado y su propia evidencia**, y **NO dependen de una primera
> adopción real**. PesquerApp está BLOQUEADA hasta que `F6` implemente y certifique, de modo
> que hacer depender un parámetro normativo de ese piloto lo dejaría inalcanzable.

## `g.18` — Lo que esta sección NO hace

```text
NO IMPLEMENTA   ni una línea de runtime, verificador, adaptador ni estado persistido
NO ELIGE        tecnología, formato, base de datos, servicio, lenguaje ni despliegue
NO CONSTRUYE    ninguno de los tres contratos derivados que `g.17` nombra
NO CERTIFICA    nada. Declarar una condición de aceptación no es demostrarla
NO DESBLOQUEA   PesquerApp. La cadena pasa obligatoriamente por `F6` y su certificación
NO CIERRA       `F5`, que sólo se cierra por acto posterior y expreso del Owner
```

---

## Anexo · Cobertura del perímetro que `O23` §2 le reserva

**`O23` §2 exige que el perímetro incluya íntegramente las materias que las fuentes vigentes
reservaron a `(g)` y que `F5` reconstruyó en `B-01`.** Esta tabla es esa correspondencia, y
existe para que la cobertura se compruebe y no se lea.

| # | materia reservada | origen | dónde se cubre |
|---|---|---|---|
| 1 | cuántos ficheros y cómo se fragmentan | delegado por `(a)` | `g.1` · detalle al contrato por `g.0` |
| 2 | transacciones y protocolo transaccional | delegado por `(a)` | `g.3` |
| 3 | el diario de eventos | regla declarada PENDIENTE en `(a)` | `g.7` |
| 4 | recuperación, con sus dos ramas | delegado por `(a)` | `g.8` |
| 5 | qué es durable y qué es operacional | delegado por `(a)` | `g.1` |
| 6 | escalonado de sincronización | ampliación de `PN-1` | `g.4` |
| 7 | nunca confirmar con transacción abierta | ampliación de `PN-1` | `g.3` |
| 8 | semántica del sellado | ampliación de `PN-1` | `g.7` |
| 9 | identidad direccionada por contenido | ampliación de `PN-1` | `g.5` |
| 10 | concurrencia, bloqueo y orden entre emisores | materia de la disposición | `g.6` |
| 11 | versionado y migración de esquema | materia de la disposición | `g.10` · `g.11` |
| 12 | gobierno Git del control repo | sede fijada por `O16` | `g.14` |
| 13 | raíz externa de confianza | sede fijada por `O23` §3 | `g.15` |

**Y las materias que `O23` §2 nombra directamente**, todas con apartado propio: componentes
obligatorios `g.1` · invariantes `g.2` · atomicidad `g.3` · durabilidad `g.4` · integridad
`g.5` · concurrencia `g.6` · diario `g.7` · recuperación `g.8` · reconciliación `g.9` ·
versionado `g.10` · migración `g.11` · propiedad y autoridad de escritura `g.12` ·
auditabilidad `g.13` · gobierno Git `g.14` · frontera con la raíz externa `g.15` ·
condiciones observables de aceptación `g.16`.
