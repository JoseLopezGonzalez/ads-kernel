# CRÍTICA INDEPENDIENTE DE F4, Y SU APLICACIÓN

> **Quién emitió esta crítica y quién escribió este fichero no son la misma parte.** Se dice
> con precisión, y no con una frase que suene mejor.
>
> ```text
> LOS HALLAZGOS Y EL VEREDICTO   proceden de un REVISOR INDEPENDIENTE que NO escribió F4 y
>                                la revisó después de entregarse.
>
> ESTE FICHERO                   lo creó, transcribió e integró el AUTOR MATERIAL DE F4.
>                                Transcribir no es emitir, y aplicar no es certificar.
>
> APLICAR LA CRÍTICA NO PRUEBA   que esté correctamente resuelta. Quien la aplicó es quien
> QUE ESTÉ RESUELTA              la recibió, y no puede dar fe de su propia suficiencia.
>
> F4c NO QUEDA CERRADA           hasta una SEGUNDA REVISIÓN INDEPENDIENTE que compruebe
>                                estas correcciones. Este fichero no es esa revisión.
> ```
>
> **ESA SEGUNDA REVISIÓN YA SE HA HECHO, y este documento se conserva tal como se escribió.**
> Su resultado está en
> [`13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md`](13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md):
> **veredicto de INSUFICIENCIA**, con dos hallazgos BLOQUEANTES, siete GRAVES y catorce
> nuevos. **Dos de ellos son defectos que las correcciones de ESTE documento introdujeron o
> no vieron** — la omisión del `fsync` de directorio en los canónicos, y un `conflicto`
> terminal que nunca emitía `reconciliacion-pendiente`. El texto de abajo no se retoca: es la
> prueba de qué se corrigió entonces y con qué argumento, y de que aplicar una crítica no
> equivale a superarla.

## Cómo se lee

```text
LO QUE DICE LA CRÍTICA     procede del REVISOR INDEPENDIENTE. Se transcribe sin suavizarlo
                           y sin reescribirlo para que encaje con lo que F4 ya había
                           concluido.

LO QUE SE HA CORREGIDO     es trabajo del autor de F4 sobre este repositorio. Va marcado
                           como tal, y su corrección NO está comprobada por nadie
                           independiente todavía.

QUÉ NO ACREDITA ESTO       que F4 esté certificada, ni que las correcciones sean
                           suficientes, ni que estén bien resueltas. Ninguna de las tres.

QUÉ SE CONSERVA            la historia. `D16`–`D22` NO se reescriben: las revisan
                           decisiones posteriores que dicen qué queda revisado y por qué.
                           Git y este documento conservan la procedencia.
```

**Por qué el texto de F4 sí se reescribe y las decisiones no.** F4 **no estaba aprobada**.
Un documento de arquitectura que conserva sus contradicciones dentro del texto deja de ser
una fuente legible y pasa a ser un archivo de versiones. Las **decisiones**, en cambio, son
un registro con identidad: `D16`–`D22` se conservan enteras y se revisan por `D23`–`D33`.

---

# El veredicto del revisor

**F4 no es válida como base tal cual está entregada.** No por su dirección —que el revisor
acepta— sino porque **su pieza central, el protocolo transaccional, no es ejecutable**: una
recuperación real no puede llevarse a cabo con lo que §2 escribe, y varias de sus
afirmaciones de seguridad son falsas. A eso se suman una colisión semántica en el tipo del
que depende toda la auditoría, tres contradicciones internas que se contradicen entre
secciones del mismo documento, y dos macrocircuitos cuya secuencia declarada es imposible.

**Ese veredicto es del revisor, no del autor de F4**, y se transcribe sin matizarlo.

```text
NUEVE BLOQUES DE HALLAZGOS   A protocolo transaccional · B cobertura y certificación ·
                             C fuentes de verdad · D iniciativa · E contrato documental ·
                             F adaptadores · G macrocircuitos · H P-08 · I trazabilidad

LO QUE NO SE DISCUTE         la dirección de F4, sus cuatro macrocircuitos como recorridos
                             distintos, el sujeto auditable como referencia tipada, y la
                             negativa a crear una cuarta capa. Eso sobrevive entero.
```

---

# `A` · El protocolo transaccional no es ejecutable

## `A.1` · Lo que dice la crítica

**Causa.** §2.6 describe cinco pasos y cuatro casos de recuperación, y ninguno de los cuatro
puede resolverse con los datos que los cinco pasos escriben. La recuperación necesita saber
**a qué resultado exacto debía llegar cada fichero**, y el manifiesto sólo declara el hash
**previo**. Sin hash posterior esperado no existe la clasificación que hace falta, y el
sistema no puede distinguir «ya aplicado» de «lo tocó otro».

Los ocho defectos concretos que el revisor enumera:

```text
1  EL EVENTO SE EMITE ANTES     el paso 1 crea un evento que declara «qué se va a cambiar».
   DE QUE OCURRA NADA           Una caída tras el paso 1 deja en el diario, para siempre,
                                un evento que afirma un cambio que nunca ocurrió. El diario
                                deja de ser una historia y pasa a ser una lista de deseos.

2  FALTA EL HASH POSTERIOR      sin él, un fichero que no casa con el previo puede ser «ya
                                aplicado» o «modificado por otro», y el sistema no puede
                                distinguirlos. Los dos casos exigen lo contrario.

3  EL MANIFIESTO SE BORRA       el paso 4 lo borra, y §3.6 da al evento un campo `tx` que
                                apunta a él. Un evento del diario apunta a un artefacto que
                                ya no existe.

4  IDS MONOTÓNICOS SIN          §2.8 declara `EV-<nnnnnn>` monotónico y §2.7 afirma que
   SERIALIZACIÓN                «dos emisores concurrentes no colisionan jamás» porque cada
                                evento es un fichero nuevo. Es falso: dos emisores que
                                calculan «el mayor más uno» eligen el mismo número. Que el
                                fichero sea nuevo no genera el nombre.

5  VENTANAS DE CAÍDA SIN        §2.6 cubre tres momentos. Faltan: antes de preparar,
   CUBRIR                       durante la regeneración de derivados, y antes y después del
                                commit de Git. Ninguno es raro.

6  DURABILIDAD CONFUNDIDA       §2.6 usa la atomicidad de `rename` como si fuera
   CON ATOMICIDAD               durabilidad. Un `rename` atómico puede perderse entero en un
                                corte de corriente si nadie sincronizó el directorio.
                                Atomicidad, caída de proceso, caída de máquina, commit
                                local, push y clon nuevo son SEIS garantías distintas, y el
                                documento las trata como una.

7  SELLADO SIN SEMÁNTICA        §2.9 dice que al cerrar un item sus eventos «se compactan».
                                No dice qué se conserva, qué puede retirarse, cómo se
                                verifica la integridad y el orden de lo retirado, ni cómo
                                sigue siendo append-only un registro del que se quita algo.

8  SIN TABLA ADVERSARIAL        no hay ninguna enumeración de qué se observa en cada ventana
                                y qué se hace. Sin ella, F6 no tiene pruebas que escribir, y
                                la recuperación se queda en una intención.
```

**Y una pregunta que F4 no se hizo.** El manifiesto de transacción es un artefacto con
identidad propia (`TX-<nnnnnn>`), ciclo propio (se abre, se marca, se borra) y contenido
propio. **Eso es un tipo**, y F4 lo declaró fuera de la cuenta mientras defendía «cuatro
tipos y ni uno más». La cuota se fijó antes que la decisión, que es el orden inverso al que
exige la prueba del §3.1.

## `A.2` · Lo que se ha corregido

**§2.5–§2.9 reescritas enteras.** El resultado está en
[`11-ARQUITECTURA-INTEGRADA.md`](11-ARQUITECTURA-INTEGRADA.md) §2.5 a §2.9, y lo que sigue
es el resumen de qué cambió, hallazgo a hallazgo.

```text
1  EL MANIFIESTO DEJA DE SER UN ARTEFACTO PROPIO. Una transacción es una SECUENCIA DE
   EVENTOS INMUTABLES con una `fase` y un `tx` común. No hay fichero que se edite ni que se
   borre: cada fase es un evento nuevo. Resuelve 1, 3 y 7 a la vez, y responde a la
   pregunta del tipo: el manifiesto NO es un quinto tipo, y no lo es por una razón
   demostrada, no por una cuota.

2  EL EVENTO `preparada` DICE «PREPARADA», NO «HECHO». Un lector del diario nunca lee una
   intención como un hecho, porque la fase está en el propio registro.

3  CADA FICHERO LLEVA HASH PREVIO Y HASH POSTERIOR ESPERADO. La recuperación clasifica cada
   fichero en tres cajas —casa con previo, casa con posterior, no casa con ninguno— y la
   tercera NUNCA se resuelve sola.

4  IDS DIRECCIONADOS POR CONTENIDO, no monotónicos. Se retira la afirmación falsa de §2.7.

5  SEIS GARANTÍAS DE DURABILIDAD SEPARADAS, con los tres puntos donde `fsync` es
   obligatorio y por qué.

6  ONCE VENTANAS DE CAÍDA, incluidas las de derivados y las de Git.

7  SELLADO CON SEMÁNTICA COMPLETA: qué se conserva, qué puede retirarse, cómo se verifica
   la cadena y por qué sigue siendo append-only.

8  TABLA ADVERSARIAL DE RECUPERACIÓN de diecisiete filas, escrita para convertirse en
   pruebas de F6 sin traducción.
```

> **No está probado.** Ninguna de las diecisiete filas se ha ejecutado. La tabla es el
> contrato de lo que F6 debe demostrar, y **no es su demostración**.

---

# `B` · `cobertura.dimension` colisiona con tres cosas distintas

## `B.1` · Lo que dice la crítica

**Causa.** §3.5 define `dimension` como *«ref a capacidad · la dimensión es la capacidad que
la posee»*. Ese único campo se usa después para tres universos que no comparten semántica:

```text
CAPACIDAD           §5.2 · `DIS` cubre a la vez UI, UX, diseño visual, sistema de diseño,
                    responsive y accesibilidad. Con un solo campo, «auditar la accesibilidad
                    de una pantalla» y «auditar su responsive» son LA MISMA CELDA. No se
                    pueden registrar por separado, ni vencer por separado, ni tener
                    responsables distintos. La dimensión desaparece dentro de su capacidad.

ÁREA DOCUMENTAL     §4.3 · las doce áreas de `O8` se declaran «dimensiones», y una de ellas
                    —`decisiones`, `dominio y glosario`— no es ninguna capacidad. Entran en
                    el mismo campo sin namespace y sin contrato que las distinga.

NIVEL DE            §9.2 · `dimension: el nivel`. Estructural, Operativo, Integrado y
CERTIFICACIÓN       Completo tampoco son capacidades ni áreas. Tercer universo, mismo campo.
```

**Tres namespaces en un campo sin tipo es una colisión semántica**, no una economía de
diseño. El sistema no puede validar que una celda es coherente, ni derivar la matriz, ni
decir qué venció.

**Y `D21` no se sostiene tal como está escrita.** Afirma que la certificación es `cobertura`
por tener *«el mismo sujeto, el mismo ciclo y la misma caducidad»*. Pero un nivel de
certificación necesita además **qué pruebas exige, quién es su propietario, quién es su
crítico, qué nivel presupone y qué lo invalida**, y nada de eso cabe en una celda sin
deformarla: son propiedades **de la clase**, no del sujeto evaluado.

**Y dos dimensiones se dejaron sin dueño.** §5.2 declara que **rendimiento y resiliencia** y
**dependencias y cadena de suministro** no tienen propietario evidente, y las aparca. Una
arquitectura que se llama **integrada** no puede terminar con dos materias sin responsable y
llamarlo honestidad: la honestidad es decir **quién responde** o **qué norma hay que
enmendar para que alguien responda**.

## `B.2` · Lo que se ha corregido

```text
EL CAMPO SE PARTE EN CUATRO    `sujeto` (qué se audita) · `aspecto` (qué propiedad se
                               juzga, con namespace tipado) · `responsables` (qué
                               capacidades responden) · `criterio` (contra qué se juzga).
                               Una capacidad deja de sustituir a una dimensión.

`aspecto` LLEVA FAMILIA        `aspecto:calidad/<nombre>` · `aspecto:documental/<area>` ·
                               `aspecto:certificacion/<nivel>`. Tres namespaces declarados,
                               con contrato distinto cada uno, y validables por separado.

`D21` SE CONFIRMA Y SE         la certificación SIGUE siendo `cobertura` —el revisor acepta
CORRIGE EN SU FUNDAMENTO       la conclusión—, pero exige una definición de CLASE del nivel,
                               `nivel-certificacion`, que aloja pruebas, propietario,
                               crítico, jerarquía e invalidación. La celda guarda ESTADO; la
                               clase guarda NORMA. Es `D26`.

LAS DOS DIMENSIONES            rendimiento → `ARQ` (diseño) + `ENT` (observado, líder) ·
HUÉRFANAS SE ASIGNAN           resiliencia → `ENT` (líder) + `ARQ` · dependencias y cadena
                               de suministro → `PLT` (líder) + `SEG` (con veto). Las cuatro
                               capacidades EXISTEN y la materia ya está en su alcance. NO
                               genera presión normativa: genera una extensión de ficha, que
                               es trabajo de F6, y queda nombrada fichero a fichero.

TRES EJEMPLOS COMPLETOS        una pantalla en accesibilidad, un documento en una familia
                               documental y una instalación en un nivel de certificación,
                               los tres SOBRE EL MISMO CONTRATO. Está en §5.6.
                               [errata corregida: decía §5.7]
```

---

# `C` · La matriz de fuentes de verdad se contradice con `a.9` y consigo misma

## `C.1` · Lo que dice la crítica

**Causa.** §1.3 declara que la fuente única de **prioridad y aparcado** es *«la zona de
órdenes del tablero»*. Es falso por tres vías a la vez:

```text
CONTRA `a.9`        `a.9` fija `02-control.md` con `autoridad OWNER · prioridad · aparcado`
                    como el sitio del campo canónico, y declara que el tablero es un CANAL
                    DE ÓRDENES cuya escritura «NUNCA es una escritura canónica».

CONTRA `I5`         si el canal fuera la fuente, una orden `- [ ]` sin consumir ya sería
                    estado del item. Entonces una orden inválida, una en conflicto `- [!]` o
                    una que espera confirmación `- [?]` serían estado — y `a.9` dice
                    expresamente que ni se aplican ni se borran.

CONTRA §2.3 DE      el propio F4, doce líneas más abajo, dibuja `02-control.md autoridad
F4 MISMO            OWNER prioridad · aparcado`. El documento se contradice consigo mismo
                    en la misma página.
```

**Y hay una segunda fila igual de rota.** La última dice que **tableros** se regeneran y su
autoridad es «nadie». Pero el tablero de `a.9` tiene **dos zonas y dos escritores por
diseño**: `COLA` es derivada y `ÓRDENES` la escribe el Owner. Declarar el tablero entero
derivado autoriza a regenerar encima de una orden no consumida, que es exactamente lo que
`a.9` prohíbe.

## `C.2` · Lo que se ha corregido

La matriz se rehace entera y se revisa fila a fila contra `a.9` e `I5`. Los cambios:

```text
prioridad y aparcado         →  `estado/items/<ID>/02-control.md` · autoridad Owner ·
                                ejecutor runtime
FILA NUEVA                   →  «órdenes del Owner pendientes de consumo»: la zona ÓRDENES
                                del tablero. Es un CANAL DE COMANDOS, no estado. Su ejecutor
                                de mutación es «ninguno: no hay mutación hasta consumirla»
tableros                     →  se parte: la zona COLA es derivada; la zona ÓRDENES no lo es
estado del item              →  se parte por zona, porque `a.9` da autoridad distinta a
                                `00-encuadre`, `01-ruta`, `02-control` y `03-integracion`
nivel de calidad             →  «la capacidad RESPONSABLE DEL ASPECTO», tras la corrección B
```

**La regla que cierra la matriz gana su tercera frase:** una orden **pendiente, inválida o
no consumida NO es todavía estado del item**, y el **runtime es el único ejecutor de la
mutación canónica**.

---

# `D` · El estado de la iniciativa no es una función total ni disjunta

## `D.1` · Lo que dice la crítica

**Causa.** §3.3 lista cinco estados con definiciones que se solapan y dejan huecos:

```text
SE SOLAPAN      «abierta: tiene items vivos» es cierta a la vez que «bloqueada: todos sus
                items vivos están bloqueados». Con todos los items bloqueados, la función
                devuelve DOS resultados. `b.4` resuelve esto con precedencia mecánica; §3.3
                no tiene ninguna.

FALTAN CASOS    iniciativa sin items · items activos junto a items esperando junto a items
                bloqueados · cancelaciones · obligaciones no satisfechas · desacuerdos ·
                reconciliación pendiente en un item.

`lista-cierre`  la diferencia se escribe como «además, su gate está cumplido», y no se dice
FRENTE A        qué pasa si el gate NO se cumple nunca, ni si una obligación quedó huérfana
`cerrada`       —que es el caso que `b.4` P10 trata con más cuidado que ningún otro.

NO SE DICE SI   un estado derivado escrito dentro de `00-iniciativa.md`, que es un fichero
SE PERSISTE     canónico y editable, sería una segunda verdad sobre lo que ya calculan los
                items. `D22` afirma que es derivado y no dice DÓNDE aparece.
```

**Y la instalación se contradice.** §8.1 declara `ESTADO: estado/ nace en N3. La iniciativa
de instalación nace en N0`. Una iniciativa que nace en N0 y cuyo soporte durable no existe
hasta N3 **no está persistida**: vive en el chat. Y `REANUDACIÓN: por checkpoint desde N3;
antes, repitiendo el paso` lo confirma — entre N0 y N3 el recorrido depende de la
conversación, que es exactamente lo que el apartado 19 de la directiva prohíbe.

## `D.2` · Lo que se ha corregido

```text
FUNCIÓN TOTAL CON            diez reglas `Q0`–`Q9` evaluadas en orden, con la misma forma
PRECEDENCIA MECÁNICA         que `b.4`. Gana la primera que se cumple, y por construcción
                             ninguna combinación produce dos resultados ni ninguno. La
                             totalidad se demuestra recorriendo los diez estados globales
                             de `b.4`, no afirmándola.

LOS CASOS QUE FALTABAN       `abierta-sin-items` · `en-desacuerdo` · `cancelando` ·
                             `cancelada` · `aparcada` · `reconciliacion-pendiente` ·
                             obligación de la iniciativa no resuelta.

`lista-cierre` FRENTE A      `lista-cierre` = todos los items terminales, obligaciones
`cerrada`                    resueltas, GATE PENDIENTE. `cerrada` = lo mismo con el gate
                             CUMPLIDO. Una obligación huérfana NUNCA llega a ninguna de las
                             dos: devuelve `bloqueada`, como en `b.4` P10.

PERSISTENCIA RESUELTA        el estado derivado NO se escribe en `00-iniciativa.md`. Vive
                             sólo en `dosier.md`, que es derivado entero. Si alguna vez
                             tuviera que aparecer en un canónico, sería en una zona
                             regenerable y no editable con su `source_revision`. Es `D29`.

LA INSTALACIÓN SE CORRIGE    `estado/` nace en **N0**, con su soporte durable mínimo: la
                             iniciativa, el diario y el checkpoint. N3 deja de crear
                             `estado/` y hace lo que `O9` ya decía que hace: especializar y
                             verificar lo que la distribución YA trae. REANUDACIÓN pasa a
                             ser «por checkpoint desde N0». Es `D30`.
```

---

# `E` · El contrato documental se contradice entre §3.7 y §4

## `E.1` · Lo que dice la crítica

**Causa.** Cuatro contradicciones, y una afirmación que no es cierta.

```text
DOS FUENTES PARA LO MISMO   §3.7 añade `ultima_verificacion_real` a `memoria.yaml`.
                            §4.2 coloca la misma verdad en `cobertura.ultima_revision_real`.
                            Es `I5` incumplido por el mismo documento en dos páginas, y
                            además contradice el «CERO CAMPOS DUPLICADOS» que §4.2 proclama
                            tres líneas después de la tabla que los duplica.

`memoria` SE GENERALIZA     §3.7 dice que la descripción de `memoria` «se amplía de sección
EN SILENCIO                 del corpus de un equipo a documento gobernante en general».
                            ESO ES LA VÍA 1, que §4.1 comparó y DESCARTÓ, y que `D20`
                            declara descartada. F4 hace la vía 1 y la llama vía 3.

`capa` NO ADMITE EL         `memoria.capa` es un enum de tres valores: kernel, pack,
SUJETO NUEVO                profile. Un documento cuyo sujeto es la arquitectura REAL de
                            ESTE producto no es ninguno de los tres. El campo es
                            obligatorio, luego el tipo generalizado no valida.

CADUCIDAD CONFUNDIDA        `memoria.caducidad` y `cobertura.caducidad` responden preguntas
                            distintas —cuándo el documento deja de ser exigible, y cuándo
                            deja de valer la última comprobación— y F4 no las distingue.
                            Un documento vigente con una verificación caducada es el caso
                            NORMAL, y el diseño no puede representarlo.
```

## `E.2` · Lo que se ha corregido

```text
UNA SOLA FUENTE             `ultima_verificacion_real` vive SÓLO en `cobertura`, como
                            `verificacion.ultima_real`. Se RETIRA de la ampliación de
                            `memoria.yaml` que §3.7 proponía.

LA GENERALIZACIÓN SE        `memoria` SE GENERALIZA, y se dice. Su sujeto pasa de «una
DECLARA COMO DECISIÓN       sección del corpus persistente de un equipo» a «cualquier
                            documento gobernado». `D27` SUSTITUYE a `D20`, que queda
                            registrada como revisada y NO se borra.

`capa` SE RESUELVE SIN      `capa` conserva sus tres valores de `K-1` y pasa a ser
FABRICAR UNA CUARTA CAPA    CONDICIONAL: sólo la declara un documento que sea conocimiento
                            que viaja con un release. Se añade `plano`, OBLIGATORIO, con los
                            cinco planos de §1.2. Un documento del producto tiene
                            `plano: especializacion` y NO tiene `capa`. `X1` sigue deferida,
                            y no se cruza por la puerta de atrás.

DOS RELOJES SEPARADOS       `memoria.caducidad` es NORMATIVA —cuándo el documento debe
                            reescribirse—. `cobertura.caducidad` es VIGENCIA DE UNA
                            VERIFICACIÓN. Se declaran los cuatro cruces posibles.

DUPLICACIONES ELIMINADAS    `vacio_significa` y `motivo_no_aplicable` dejan de solaparse:
                            uno explica un documento VACÍO, el otro un aspecto que NO APLICA
                            a un sujeto. `memoria.estado` se define como ciclo NORMATIVO del
                            documento —`vigente | sustituida | retirada`, la forma de `b.3`—
                            y NO como estado de verificación, que es de la celda.
```

---

# `F` · `adaptador.nivel` es una segunda verdad sobre la certificación

## `F.1` · Lo que dice la crítica

**Causa.** §3.4 declara `nivel` como campo del bloque `ads:adaptador`, con valores
`soportado | compatible | generico | desconocido`. §6.5 declara que `soportado` **exige**
adaptador más prueba de humo **ejecutada** más certificación **Integrada**.

```text
LO MISMO, DOS VECES    `soportado` es a la vez un campo que alguien ESCRIBE en el adaptador
                       y una CONCLUSIÓN que se deriva de evidencia. Editable y derivado a la
                       vez es la definición de segunda verdad que `I5` prohíbe.

Y ADEMÁS NO CADUCA     un campo editable no vence. Un nivel derivado de certificación SÍ:
                       §9.3 declara qué lo invalida. Con el campo editable, un adaptador
                       puede seguir diciendo `soportado` después de que su certificación
                       haya sido invalidada por un cambio de arranque.
```

**Y una pregunta que F4 no responde.** §6.2 dice que las proyecciones van *«donde CADA
PROVEEDOR las descubre»*. Con la topología de `C6` —control repo y fuentes como
**hermanos**— un entorno abierto sobre `frontend/` no descubre nada de `ads/`. F4 no dice
cómo se resuelve, y las dos salidas fáciles están prohibidas: copiar la organización ADS a
cada fuente lo prohíbe `C6`, y un fichero no versionado no sobrevive a un clon nuevo.

## `F.2` · Lo que se ha corregido

```text
`nivel` DESAPARECE COMO      se parte en tres, y sólo dos son campos:
CAMPO DEL ADAPTADOR            `compatibilidad_declarada`   lo que el adaptador AFIRMA.
                                                            Editable. Es una intención.
                               `capacidades_del_entorno`    lo que el entorno OFRECE.
                                                            Editable. Es una observación.
                               `nivel_alcanzado`            DERIVADO. NO es campo. Es el
                                                            estado de las celdas
                                                            `aspecto:certificacion/*` cuyo
                                                            sujeto es el adaptador. Sale de
                                                            evidencia y CADUCA. Es `D28`.

EL DESCUBRIMIENTO SE         la entrada canónica es el control repo, y `C6` ya lo dice.
RESUELVE CON UN PUNTERO      Para el caso inevitable de un entorno que sólo puede abrirse
                             sobre la fuente, el adaptador proyecta en ella UN ÚNICO fichero
                             puntero: versionado, generado, con huella, que declara la
                             IDENTIDAD REMOTA del control repo y NADA MÁS. Sin reglas, sin
                             memoria, sin estado. Se resuelve por identidad y no por ruta
                             —`C6` N9—, y sobrevive a un clon nuevo porque está versionado.

LÍMITE DECLARADO             que un entorno concreto HONRE el puntero es exactamente lo que
                             mide la prueba de humo. El diseño NO puede afirmarlo.
```

---

# `G` · Dos macrocircuitos declaran secuencias imposibles

## `G.1` · Lo que dice la crítica

```text
1  MIGRACIÓN: M5 Y M6 EN ORDEN CONTRADICTORIO
   FASES dice     M5 retirar del repositorio técnico · M6 validar y certificar
   ROLLBACK dice  «M5 es el único destructivo, y va DESPUÉS de M6 en el orden real de
                  seguridad: no se retira nada hasta que lo nuevo esté certificado»
   El documento declara las dos secuencias y son incompatibles. Un lector no puede saber
   cuál ejecuta, y una de las dos retira material antes de certificar el sustituto.

2  ROLLBACK DE INSTALACIÓN Y ADOPCIÓN: BORRAR LO LOCAL NO REVIERTE LO PUBLICADO
   §8.1 N0 dice «crear y PUBLICAR control repo». §8.1 ROLLBACK dice «N0–N2 se deshacen
   BORRANDO EL WORKSPACE». §8.2 dice «revertir es borrar el control repo». Un remoto ya
   publicado sigue existiendo, con su historia y sus clones. Y no se dice quién tiene
   autoridad para eliminarlo — que es una operación destructiva sobre infraestructura del
   Owner.

3  CERTIFICACIÓN INTEGRADA: OBLIGA A UNA PRUEBA QUE PUEDE SER IMPOSIBLE
   §9.1 exige para Integrada «trabajo multi-fuente mínimo verificado como conjunto».
   `C6` N4 dice que un producto tiene **0..N** fuentes. Un producto de una sola fuente NO
   PUEDE satisfacerla nunca. Y `O12` exige Integrada para empezar a programar. Luego un
   producto de un repositorio queda bloqueado para siempre por una prueba que no le aplica.

4  ACTUALIZACIÓN: FIJA LA COMPATIBILIDAD DE LA DISTRIBUCIÓN Y NO LA DEL ESTADO
   §8.4 dice «ROLLBACK: volver a la versión anterior CON SU ESTADO». Si U4 ejecutó una
   migración de esquema, el estado quedó en el esquema nuevo y volver la distribución
   atrás produce lo que §2.8 declara ERROR EXPLÍCITO: leer un fichero con esquema mayor que
   el soportado. El rollback declarado no es ejecutable.
```

## `G.2` · Lo que se ha corregido

```text
1  SECUENCIA ÚNICA DE MIGRACIÓN, de M0 a M7, con la retirada DESPUÉS de la certificación
   y una verificación posterior que la retirada exige:
       M5 CERTIFICAR lo nuevo con lo viejo todavía en pie   ← certificación PREVIA
       M6 RETIRAR, único paso destructivo, con autorización del Owner
       M7 VERIFICAR que nada dependía de lo retirado         ← verificación POSTERIOR
   Las dos son necesarias y responden a preguntas distintas: M5 prueba que lo nuevo
   funciona; M7 prueba que lo viejo ya no hacía falta. Es `D33`.

2  ROLLBACK CON REMOTO SEPARADO DE LOCAL, y sin eliminación automática:
       LOCAL      borrar el workspace deshace lo local y NADA MÁS
       REMOTO     un control repo publicado NO se revierte borrando el local
       COMMITS    permanecen. Un rollback NO reescribe historia publicada
       AUTORIDAD  NINGUNA ELIMINACIÓN REMOTA AUTOMÁTICA. ADS propone —archivar, marcar
                  abandonado, conservar, eliminar— y sólo el OWNER ejecuta la eliminación
       LO QUE SÍ  ADS emite el evento de abandono y lo escribe en el control repo, para
       HACE SOLO  que un clon posterior no lo lea como instalación viva

3  APLICABILIDAD DE LA PRUEBA MULTI-FUENTE POR NÚMERO DE FUENTES:
       0 FUENTES   no aplica, y tampoco `workspace check` sobre fuentes ni CI
       1 FUENTE    no aplica: con una fuente no hay conjunto que converger
       N ≥ 2       OBLIGATORIA
   Una prueba no aplicable se registra con `aplicabilidad: no-aplicable`, su
   `motivo_no_aplicable` y su EVIDENCIA de inaplicabilidad —el recuento de fuentes del
   manifiesto—. Nunca bloquea, y nunca se omite en silencio. Añadir una segunda fuente
   invalida la Integrada, y ahora eso tiene consecuencia real: la prueba pasa a aplicar.
   Es `D32`, y genera la presión `PN-6`, porque reinterpreta `O12`.

4  COMPATIBILIDAD Y ROLLBACK DEL ESTADO EN LA ACTUALIZACIÓN:
       U2 compara `esquema_estado` instalado contra el que exige la candidata
       IGUAL              U4 no toca `estado/`
       CANDIDATA MAYOR    migración hacia delante. U3 NO se aprueba sin migrador inverso o
                          sin instantánea previa del estado
       CANDIDATA MENOR    NO se aplica: es un downgrade de esquema, y §2.8 lo declara error
       ROLLBACK CON       ejecuta el migrador inverso, o restaura la instantánea, y VERIFICA
       MIGRACIÓN          equivalencia con el mismo rigor que M3
       PUNTO DE NO        se declara en U3: desde qué paso el rollback deja de ser
       RETORNO            automático y pasa a ser decisión del Owner
```

---

# `H` · La caché de `P-08` no detecta lo que `P-08` existe para detectar

## `H.1` · Lo que dice la crítica

**Causa.** §11.3 dice que la huella *«se CACHEA en `.ads/run/cache/` por revisión de Git»*.

```text
LA CLAVE ES CIEGA AL       un árbol sucio tiene el MISMO `HEAD` y contenido distinto. Con la
ÁRBOL SUCIO                revisión de Git como clave, la caché sirve un veredicto calculado
                           sobre otro contenido. `P-08` existe porque una evidencia intacta
                           y caducada pasó por válida; esta caché reproduce el defecto por
                           otro camino, y en el trabajo normal —editar y comprobar— es el
                           caso PERMANENTE, no el raro.

LA HUELLA SÓLO CUBRE       §11.2 declara las entradas como «rutas, extensiones y
EL CORPUS                  exclusiones». Faltan: la implementación del validador, sus
                           imports compartidos, el manifiesto y la configuración que lee,
                           los argumentos con que se invocó, y la versión de las
                           herramientas cuando afectan al resultado. Cambiar un helper
                           compartido cambia trece veredictos y ninguna huella.

TRES COSAS SIN SEPARAR     entradas semánticas —si cambian, cambia el veredicto—, entradas
                           del entorno —pueden cambiarlo sin que cambie nada semántico— y el
                           artefacto de salida. Mezcladas, no se puede decir «el veredicto
                           vale, pero se obtuvo con otro intérprete».

CIRCULARIDAD SIN CERRAR    §11.2 dice que `T158` está exento de comprobarse a sí mismo y que
                           un exento no puede declarar vigencia. Correcto, y deja la
                           pregunta sin responder: ENTONCES QUIÉN comprueba la vigencia de
                           la evidencia de `T158`.

ESCENARIOS INCOMPLETOS     §11.4 lista cuatro. Ninguno es el que importa: mismo `HEAD` con
                           fichero modificado.
```

## `H.2` · Lo que se ha corregido

```text
TRES HUELLAS, NO UNA       HUELLA SEMÁNTICA · HUELLA DE ENTORNO · ARTEFACTO DE SALIDA. La
                           evidencia lleva las dos primeras SIN MEZCLARLAS, y por eso puede
                           distinguir «caducada» de «caducada por entorno».

LA CLAVE ES EL CONTENIDO,  `clave = H(huella_semántica ‖ huella_de_entorno)`. El SHA de Git
NUNCA EL SHA DE GIT        se conserva como DATO INFORMATIVO —sirve para localizar el
                           commit— y NO participa en la clave. Con árbol sucio la clave
                           cambia, que es justo lo que la versión anterior no hacía.

LA HUELLA SEMÁNTICA        corpus · implementación del validador · CIERRE TRANSITIVO de sus
CUBRE SEIS COSAS           imports del repositorio, calculado y no escrito a mano ·
                           `validadores.yaml`, `reglas.yaml` y `exclusiones.yaml` ·
                           argumentos de invocación.

LA HUELLA DE ENTORNO       versión mayor.menor del intérprete y versión de cada biblioteca
CUBRE DOS, Y NADA MÁS      de terceros que el validador importa. NI hostname, NI usuario, NI
                           rutas, NI hora: eso rompería el determinismo de `R4`.

LA RAÍZ DE CONFIANZA       la vigencia de la evidencia de `T158` NO la declara `T158`. La
SE DECLARA                 comprueba el RUNNER, que RECALCULA SIEMPRE la de `T158` y nunca
                           la lee de caché. Recalcular es más barato que razonar sobre si
                           vale, y elimina la circularidad de raíz. El runner no es un
                           validador: no publica evidencia sobre sí mismo y su corrección la
                           comprueban las pruebas negativas `N158*`.

EL SUELO QUE QUEDA         si el runner miente, NADA dentro del sistema lo detecta. Cerrar
ABIERTO, DECLARADO         eso exige un verificador externo al repositorio, y NO se resuelve
                           aquí. Se dice en vez de taparlo.

ESCENARIOS NEGATIVOS       los cinco que la crítica exige más la caché servida por clave
                           parcial. Están en §11.5, que hoy tiene ONCE.
                           [errata corregida: decía SEIS]
```

---

# `I` · Trazabilidad: las decisiones y las presiones

## `I.1` · Lo que dice la crítica

```text
NO SE REESCRIBEN      `D16`–`D22` están registradas y son historia. Corregir la arquitectura
`D16`–`D22`           reescribiéndolas borraría que se tomaron y por qué. La vía correcta es
                      una decisión POSTERIOR que diga qué queda revisado, por qué y cómo se
                      revierte — que es exactamente lo que `O7`–`O14` hicieron sin tocar
                      `O1`–`O6`.

EL RECUENTO DE TIPOS  «cuatro tipos nuevos y ni uno más» es una CUOTA fijada ANTES de aplicar
SE CALCULA            la prueba del §3.1, y el manifiesto de transacción quedó fuera de la
                      cuenta sin pasar la prueba. El número final se RECALCULA aplicando la
                      prueba a cada candidato, y sale lo que salga.

LAS PRESIONES SE      cinco presiones escritas sobre una arquitectura que ha cambiado no son
REVISAN               automáticamente las presiones de la arquitectura corregida. Hay que
                      recorrerlas: cuál sigue, cuál se retira, cuál se fusiona y cuál nace.
```

## `I.2` · Lo que se ha corregido

**Once decisiones nuevas, `D23`–`D33`**, en el registro canónico
[`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md). Cada una
declara qué decisión anterior revisa, el motivo y la reversión. **`D16`–`D22` conservan su
texto íntegro.**

```text
D23  el manifiesto de transacción deja de ser artefacto propio      revisa D16
D24  ids de evento direccionados por contenido, no monotónicos      revisa D16 y §2.8
D25  `cobertura` se parte en sujeto · aspecto · responsables ·      revisa D18
     criterio
D26  la certificación sigue siendo cobertura Y exige una            revisa D21
     definición de clase `nivel-certificacion`
D27  `memoria` se generaliza, y se declara                          SUSTITUYE a D20
D28  `adaptador.nivel` desaparece; tres conceptos separados         revisa D18
D29  función total del estado de iniciativa; no se persiste         revisa D22
D30  `estado/` nace en N0, no en N3                                 nueva
D31  clave de caché de `P-08` por contenido, tres huellas           nueva
D32  aplicabilidad de la certificación Integrada por nº de fuentes  nueva
D33  secuencia de migración M5 certifica · M6 retira · M7 verifica  nueva
```

**El recuento de tipos, recalculado y no presupuesto:**

```text
TIPOS CANÓNICOS DE ESTADO NUEVOS · CUATRO
    `iniciativa`   ningún artefacto agrupa items. Un item tiene exactamente un proceso
                   (`b.1`) y un paquete pertenece a un item. Sujeto, autoridad y ciclo
                   propios. SOBREVIVE la prueba.
    `adaptador`    `C2` lo nombra y no existe en ninguna parte. SOBREVIVE, y pierde el
                   campo `nivel`, que era de otro sujeto.
    `cobertura`    nada persiste el nivel de calidad de una parte del producto ni su
                   caducidad. SOBREVIVE, con cuatro campos donde había uno.
    `evento`       `G26` está PENDIENTE en `a.11` porque no existe. SOBREVIVE, y ABSORBE
                   el manifiesto de transacción como una `fase` suya.

LO QUE DEJA DE SER TIPO · UNO
    manifiesto     una transacción es una SECUENCIA DE EVENTOS con `fase` y `tx` común. No
    de transacción tiene ciclo propio porque no tiene fichero que cambie de estado: cada
                   fase es un evento nuevo e inmutable. NO PASA el paso 4 de la prueba.

ESQUEMA DE CLASE NUEVO · UNO, Y NO ES UN TIPO DE ESTADO
    `nivel-        aloja pruebas, propietario, crítico, jerarquía e invalidación de cada
    certificacion` nivel. Es NORMA, no estado, y su precedente exacto ya existe en el
                   corpus: `nivel-novedad.yaml`. Meterlo en `gate` daría a los sesenta y
                   pico gates del sistema dos campos que sólo usa la certificación.

ESQUEMAS AMPLIADOS · DOS
    `memoria`      generalizado, con `plano` nuevo y `capa` condicional (D27)
    `validadores`  bloque `entradas:` (P-08)

TOTAL DE ESQUEMAS   19 vigentes + 4 tipos de estado + 1 de clase = 24
```

**Las presiones normativas, revisadas una a una.** Los identificadores **no se renumeran**:
renumerar rompería la trazabilidad de lo que ya se llevó al Owner.

```text
PN-1  sección (g)              VIGENTE Y AMPLIADA. §2 decide ahora además el escalonado de
                               `fsync`, la regla de commit de Git, la semántica de sellado y
                               el esquema de identidad. Sigue siendo la ÚNICA que bloquea
                               todo el estado durable.
PN-2  O7 tercera vía de        VIGENTE, sin cambio. Ninguna corrección la toca.
      creación de trabajo
PN-3  G03 y ejecución          VIGENTE, y ABSORBE a PN-5.
      desatendida
PN-4  iniciativa frente a b.4  RETIRADA. `D29` cierra la lectura que la motivaba: la función
                               de iniciativa CONSUME el resultado de `b.4` y no redefine su
                               dominio, y no se persiste. F5 puede reinstaurarla si el Owner
                               prefiere una frase aclaratoria en `b.4`; el motivo de la
                               retirada queda escrito para que esa decisión sea suya.
PN-5  Completa frente a G03    FUSIONADA en PN-3 como su consecuencia nombrada. Ya se
                               declaraba «no es una presión independiente».
PN-6  aplicabilidad de la      NUEVA. `D32` declara que la prueba multi-fuente no aplica a
      Integrada frente a O12   productos de 0 y 1 fuente. `O12` es una resolución del Owner
                               y exige Integrada para empezar a programar: reinterpretar su
                               precondición es materia suya, no del autor de F4.

CUATRO PRESIONES VIGENTES: PN-1 · PN-2 · PN-3 · PN-6.  Aquí NO se redacta ninguna enmienda.
```

---

# Lo que sigue abierto tras aplicar la crítica

```text
LA SEGUNDA REVISIÓN         F4c NO está cerrada. Estas correcciones las escribió el autor de
INDEPENDIENTE               F4, y nadie independiente las ha comprobado.

NADA ESTÁ CONSTRUIDO        ni una línea de kernel, runtime, tooling, esquema, adaptador,
                            plantilla, pack, validador o migración. Las correcciones son
                            DISEÑO CORREGIDO, no diseño implementado.

NADA ESTÁ PROBADO           las diecisiete filas de la tabla adversarial, los seis
                            escenarios negativos de `P-08` y los doce escenarios de §14
                            están ESCRITOS. Ninguno se ha ejecutado.

EL PILOTO SIGUE PENDIENTE   `O14` sigue seleccionado y sin ejecutar.

EL SUELO DE `P-08`          si el runner miente, nada dentro del repositorio lo detecta.
                            Declarado, no resuelto.

ORDEN TOTAL ENTRE MÁQUINAS  la cadena de eventos da orden total POR TRANSACCIÓN y orden
                            parcial entre máquinas. Dos ejecutores concurrentes producen una
                            bifurcación detectable, y resolverla es runtime distribuido, que
                            `E2.7` ya dejó abierto.

`X1` Y `P-05`               siguen deferidas. Ninguna corrección cruza esa línea, y `D27`
                            resuelve `capa` precisamente para no cruzarla.

LAS ENMIENDAS DE F5         no se redactan aquí. Cuatro presiones vigentes, y su puerta es
                            el Owner.
```

**Y la frase que no cambia:** ADS sigue siendo un corpus verificado contra sí mismo y **cero
veces contra la realidad**. F4 corregida dice cómo cerrar esa distancia con menos agujeros
que F4 entregada. Sigue sin cerrarla.
