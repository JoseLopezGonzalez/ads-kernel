# CRÍTICA INDEPENDIENTE DE F3, Y LA PUERTA CORRECTIVA PRE-F4

> **Quién emite esta crítica y quién escribió este fichero no son la misma parte, y conviene
> decirlo con precisión en vez de con una frase que suene mejor.**
>
> ```text
> LOS HALLAZGOS Y EL VEREDICTO   proceden de un REVISOR INDEPENDIENTE, que no participó en
>                                F3 y la revisó después de entregarse.
>
> ESTE FICHERO                   lo creó, transcribió e integró el AUTOR DE F3. Es trabajo
>                                material suyo: transcribir no es emitir.
>
> LO QUE EL AUTOR DE F3 NO HIZO  no reescribió los hallazgos para cambiar su veredicto, no
>                                los suavizó, y NO certifica su propia suficiencia. La
>                                certificación de F3 no está en este fichero ni la da él.
> ```
>
> El plan de investigación exige que **quien propone no certifique su propia suficiencia**, y
> la iteración anterior dejó el precedente: una auditoría independiente encontró treinta y
> tres hallazgos, dos de ellos en pruebas que figuraban como superadas sin comprobar lo que
> su nombre afirmaba. Esa exigencia recae sobre **el juicio**, no sobre quién teclea el
> fichero. Confundir las dos cosas convertiría la independencia en una cuestión de autoría
> material, que es justo lo que no es.

## Cómo se lee

```text
LO QUE DICE LA CRÍTICA     procede del REVISOR INDEPENDIENTE. Lo transcribe el autor de
                           F3, y no lo reescribe para que suene mejor ni para que encaje con
                           lo que la síntesis ya había concluido.

LO QUE SE HA CORREGIDO     es trabajo del autor de F3 sobre este repositorio, y va marcado
                           como tal. Ninguna corrección borra la conclusión anterior: la
                           síntesis conserva su texto y gana un addendum.

QUÉ NO ACREDITA ESTO       que F3 esté certificada. Aplicar una crítica no es superarla:
                           quien la aplicó es quien la recibió.

LO QUE SIGUE ABIERTO       se dice. La puerta pre-F4 se cierra con lo corregido, no con lo
                           prometido.
```

**El veredicto de partida del revisor:** F3 es válida como base. Lo que sigue son seis
correcciones sobre ella, no su sustitución. **Ese veredicto es suyo, no del autor de F3**, y
se transcribe sin matizarlo.

---

# Los seis hallazgos

## `CI-1` · `H4` reduce incorrectamente el universo auditable

**Lo que dice la crítica.** `H4` concluye que la matriz de cobertura es
`componente × capacidad`. `C6` define el componente como una **unidad lógica** del tipo
`web`, `api`, `mobile` o `infra`, referenciada por `source` + `path`. El documento del Owner
exige auditar además módulos, áreas funcionales, pantallas, flujos, formularios, patrones
visuales, APIs, integraciones, entidades, reglas, migraciones, entornos, pipelines,
despliegues, documentos, agentes, skills y adaptadores. Ninguno de ésos es un componente de
`C6`, y forzarlos a serlo deformaría el manifiesto del producto.

**Qué se corrige.** El componente pasa a ser **raíz o ámbito principal**, no el sujeto único.
F4 necesita un **contrato de sujeto auditable** que admita referencias subordinadas y
transversales. La matriz es `sujeto auditable × dimensión`.

**Qué NO autoriza esta corrección.** Crear un tipo canónico nuevo por reflejo. `D11` ya
rechazó `source` y `component` como tipos porque duplicarían `SOURCES.toml`, y la regla del
§26.5 obliga a intentar primero expresarlo con lo existente: referencias entre artefactos,
alcance tipado y los artefactos que ya declaran superficie. F4 decide, y decide después de
contrastarlo.

**Estado:** `H4` **revisado**. Ver el addendum de [`09-SINTESIS.md`](09-SINTESIS.md).

## `CI-2` · `H5` afirma prematuramente que el contrato documental es `memoria` con dos campos

**Lo que dice la crítica.** `memoria.yaml` describe *«una sección del corpus persistente de un
equipo»*, y su campo `capa` está acotado a `kernel`, `pack` y `profile`. Por sí solo no cubre
lo que exigen el §5.19 y el §5.23: procedencia, fuentes y **revisiones examinadas**,
relaciones entre documentos, decisiones, items y dosieres, aplicabilidad por familia, gaps,
contradicciones conocidas y evidencia. Decir «es `memoria` con dos campos» cierra por
aritmética una pregunta de diseño.

**Qué se corrige.** `H5` se reclasifica de conclusión a **reutilización candidata**. F4 elige
entre tres vías, y ninguna está decidida aquí:

```text
1  GENERALIZAR memoria        ampliar su alcance y su enum de capa
2  METADATA ESPECIALIZADA     un bloque documental propio, distinto de memoria
3  COMPOSICIÓN                un contrato común sobre primitivas que ya existen
```

**La condición que sí se conserva de `H5`**, porque no depende de cuál se elija: **no se
duplican fuentes de verdad**. Siete de los campos que el §5.23 pide ya existen con ese
significado en `memoria.yaml`, y la vía que se escoja tiene que explicar qué hace con ellos.

**Estado:** `H5` **degradado a candidato**, con su pregunta abierta.

## `CI-3` · `X8` y las preguntas 3 y 4 no estaban abiertas

**Lo que dice la crítica.** `C4` ya fija las tres cosas que `X8` planteaba como
contradicción: existe un catálogo completo disponible, se materializan permanentemente
**`DSP` y `SIS`**, y `ENC` se materializa **bajo demanda** por `E1`. No hay contradicción que
resolver: hay una lectura que la síntesis no hizo.

**Qué se corrige.** `X8` se resuelve **por lectura**: la distribución trae catálogo y
estructura preconfigurada; `C4` gobierna la materialización. Las preguntas 3 y 4 salen del
conjunto que necesita al Owner. Volverían a abrirse sólo con una enmienda formal a `C4` o a
`E1`, y **aquí no se propone ninguna**.

**Estado:** `X8` **cerrada**. Preguntas 3 y 4 **retiradas**.

## `CI-4` · `X7` estaba mal planteada en las dos direcciones

**Lo que dice la crítica.** El mínimo documental no son doce ficheros obligatorios —que es lo
que el §5.18 sugiere leído literalmente—, y tampoco es «lo necesario para reanudar o pasar un
gate» —que es lo que la síntesis propuso a cambio—. Las doce áreas del §5.18 son un **mínimo
semántico profesional evaluable**: materia que un producto gobernado tiene que tener resuelta,
no ficheros que tenga que tener creados.

**Qué se corrige.** El mínimo documental queda así:

```text
DOCE ÁREAS SEMÁNTICAS      obligatorias como MATERIA, no como ficheros
COMPACTACIÓN FÍSICA        varias áreas pueden vivir en un documento; en un producto pequeño,
                           en muy pocos
PROFUNDIDAD PROPORCIONAL   a tamaño, naturaleza y riesgo del producto
ÁREAS CONDICIONALES        se activan por aplicabilidad
«NO APLICABLE»             es una evaluación registrada CON MOTIVO, nunca una ausencia
REANUDACIÓN Y GATES        son COMPROBACIONES del mínimo, no su única razón de existir
```

La última línea es la corrección al texto de la síntesis: `T171` y la reanudación siguen
siendo la forma de comprobar que el mínimo se sostiene, y dejan de presentarse como la
definición de qué es el mínimo.

**Estado:** `X7` **cerrada** por la resolución `O8` del Owner.

## `CI-5` · `H1` es correcto, y no autoriza a aplanar las rutas

**Lo que dice la crítica.** Compartir un motor de composición no convierte cuatro recorridos
en uno. Instalación nueva, adopción, migración de un ADS anterior y actualización de un ADS
instalado conservan cada uno sus **disparadores, precondiciones, fases, evidencias, gates,
rollback y certificación propios**.

**Qué se corrige.** `H1` se conserva entero y gana esa condición explícita. La conclusión
—no hacen falta tipos de proceso nuevos— no cambia; lo que se prohíbe es leerla como que los
cuatro recorridos son intercambiables.

**Estado:** `H1` **conservado, con condición añadida**.

## `CI-6` · `H3` es correcto, y necesita cuatro piezas separadas

**Lo que dice la crítica.** «El adaptador es una proyección compilada» describe bien el
modelo y esconde que son cuatro cosas con dueños y ciclos distintos.

```text
1  DEFINICIÓN CANÓNICA NEUTRAL   en el repositorio de control. Es la fuente.
2  PROYECCIONES GENERADAS        en las ubicaciones que cada proveedor DESCUBRE por su
                                 cuenta. No las elige ADS: las impone el entorno.
3  HUELLA Y VALIDADOR DE DERIVA   lo que hace comprobable que 2 sigue derivando de 1.
4  PRUEBA DE HUMO EN SESIÓN NUEVA lo que demuestra que 2 funciona donde tiene que funcionar.
```

**Qué se corrige.** `H3` se conserva y se desglosa en esas cuatro piezas, que F4 diseña por
separado aunque compartan contrato.

**Estado:** `H3` **conservado, desglosado**.

---

# Las ocho resoluciones del Owner

Se registran por su vía: son decisiones que pertenecen al Owner, y su registro canónico es la
sección 2 de
[`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md), donde
entran como **`O7`–`O14`**. Aquí se enumeran con su efecto sobre F3; el registro manda.

| | resolución | efecto sobre F3 |
|---|---|---|
| `O7` | política revocable de auditoría recurrente | **cierra `X6`**. Detectar e inventariar es automático y no crea trabajo; abrir auditorías se autoriza por evento, riesgo, recurrencia y caducidad dentro de la política; las correcciones mecánicas y locales viven en campañas preautorizadas con pruebas y `VER` independiente; producto, UX, arquitectura, seguridad, datos y comportamiento crítico conservan sus gates. Una única decisión declara alcance, prioridad, presupuesto, umbrales y revocación |
| `O8` | mínimo documental de doce áreas semánticas | **cierra `X7`**, en los términos de `CI-4` |
| `O9` | distribución con catálogo completo y estructura preconfigurada | **cierra `X8`**, en los términos de `CI-3`. `DSP` y `SIS` permanentes; `ENC` y las demás bajo demanda según `C4` |
| `O10` | `docs/owner/` como destino canónico del material en voz del Owner | **cierra `P-07` en su ubicación**, que era la parte que la síntesis dejó al Owner |
| `O11` | la unidad amplia se llama **`iniciativa`** | **cierra la pregunta 6**. Tipo o artefacto canónico de coordinación, con identidad, estado durable, alcance, gates y dosier vivo derivado. **No es un proceso nuevo**: compone rutas, items y paquetes existentes |
| `O12` | gate «ahora puedes empezar a programar» | **cierra la pregunta 7**. Certificación **Integrada** + baseline aprobado + ningún desconocido crítico sin clasificar. La certificación **Completa** es lo que permite declarar terminada y plenamente certificada una instalación o adopción |
| `O13` | primera matriz de entornos agentic | **cierra la pregunta 8**. Claude Code y Codex son el primer **OBJETIVO** de soporte y certificación — **hoy ninguno lo está**, y sólo lo estarán tras una prueba de humo real. Cursor y Gemini figuran desde el diseño en nivel compatible o genérico hasta superar la suya. Fallback genérico obligatorio. **Ningún soporte se declara sin ejecución real**, y fijar el objetivo no es alcanzarlo |
| `O14` | piloto principal: **PesquerApp** | **cierra la pregunta 9**. En clones y workspace aislados, sin tocar ramas productivas. Debe probar adopción multi-repo de un producto existente, `T169`, `T170`, `CA-10`, `CA-11`, el §100 y los límites de fan-out. **No se ejecuta todavía**: queda seleccionado y con sus condiciones escritas |

## Qué queda de las nueve preguntas del Owner

```text
CERRADAS POR RESOLUCIÓN   1 (O7) · 2 (O8) · 5 (O10) · 6 (O11) · 7 (O12) · 8 (O13) · 9 (O14)
RETIRADAS POR LECTURA     3 y 4 — C4 y E1 ya las respondían (CI-3)

QUEDAN CERO PREGUNTAS ABIERTAS del conjunto que la síntesis elevó al Owner.
```

Lo que **no** desaparece con ellas son los trabajos que esas resoluciones ordenan, y que
siguen sin construirse. Están abajo.

---

# El defecto de `T158`

Es el hallazgo que obliga a esta puerta correctiva, y no procede de una lectura: procede de
una ejecución.

## Qué ocurrió

```text
1  F3 añade dos documentos al corpus.
2  Bajo un intérprete sin `tomllib`, el validador `fuentes` falla y el runner —correctamente—
   NO sobrescribe su evidencia. Esa negativa protege la evidencia buena de ser pisada por una
   mala, y es un comportamiento que se conserva.
3  Efecto secundario: `fuentes-salida.txt` sigue declarando la cobertura de T161 sobre un
   corpus anterior. La cifra describe un corpus que ya no existe.
4  T158 pasa con éxito. Cabecera de procedencia válida, código 0, firma de éxito presente,
   `debe_contener` satisfecho. Ninguna de sus ocho comprobaciones mira la vigencia.
```

## Por qué `T158` no lo veía

`T158` comprobaba **procedencia y forma** de la evidencia: de quién es, qué orden la produjo,
con qué código terminó, si afirma un éxito que su salida respalda, si contiene marcas de
fallo. Ninguna de esas preguntas se responde distinto cuando la evidencia envejece: una
cobertura desactualizada satisface `ficheros recorridos` exactamente igual de bien que la
correcta.

**Es la misma familia del defecto que creó `T158`**, por otra vía. Allí la evidencia estaba
corrupta y el informe afirmaba éxito. Aquí la evidencia está intacta y **caducada**.

## Qué se ha corregido

Un contrato de **vigencia** declarativo en `validadores.yaml`: un validador puede declarar
qué valor de su evidencia es derivable del corpus, y `T158` lo **recalcula** y lo compara.

```text
COBERTURA COMPLETA       T161. La cifra de ficheros recorridos se recalcula sobre el corpus
                         vigente, con la MISMA definición de recorrido que usa T161 — una
                         sola implementación, importada, nunca copiada.

FALLA CERRADO            una `vigencia` que declara un recuento sin implementación registrada
                         es un fallo, no un silencio.

SIN CIRCULARIDAD         un componente exento de su propia comprobación no puede declarar
                         vigencia. T158 no se acepta a sí mismo.

ALCANCE RESTANTE         los otros doce validadores. Su evidencia sigue sin comprobación de
                         vigencia, y eso se declara — ver `P-08` abajo.
```

Y una regresión que reproduce el caso real, en `comprobar_negativos.py`:

```text
N158g   la cobertura publicada describe un corpus con dos ficheros menos que el vigente,
        con cabecera, código y firma válidos. Deriva la cifra del propio fichero: NO
        hay ningún 280 ni 282 escrito en la prueba.
N158h   una `vigencia` declara un recuento que nadie implementa. El mecanismo tiene que
        fallar en vez de dar por buena la evidencia que no sabe comprobar.
```

## `P-08` · La vigencia de la evidencia está garantizada para `T161`, no para el resto

```text
QUÉ QUEDA CUBIERTO   la cobertura de T161, por recálculo determinista del corpus recorrido.

QUÉ NO               los otros doce validadores. Su evidencia puede envejecer igual, y hoy
                     nada lo detectaría. Ejemplos con cifra publicada: «documentos
                     analizados» de T147, «unidades de instrucción revisadas» de T153,
                     «Ran N tests» de las pruebas de workspace.

POR QUÉ NO SE CIERRA AQUÍ   la solución general es una decisión arquitectónica: vincular
                     cada evidencia con una huella de las ENTRADAS que su validador leyó
                     exige declarar esas entradas por validador, y eso toca el manifiesto,
                     los trece validadores y el runner. Es materia de F4, no de una puerta
                     correctiva.

QUÉ NO PUEDE AFIRMARSE MIENTRAS TANTO   que toda la evidencia del repositorio tenga vigencia
                     garantizada. No la tiene, y decirlo es la mitad de la corrección.
```

---

# Estado de la puerta correctiva pre-F4

| | qué exigía la crítica | estado |
|---|---|---|
| `CI-1` | corregir `H4`: sujeto auditable, no sólo componente | **corregido** en el addendum de la síntesis |
| `CI-2` | reclasificar `H5` como candidato | **corregido** en el addendum |
| `CI-3` | resolver `X8` por lectura y retirar las preguntas 3 y 4 | **corregido** en el addendum · `O9` |
| `CI-4` | corregir `X7`: doce áreas semánticas | **corregido** en el addendum · `O8` |
| `CI-5` | `H1` conservado, sin aplanar rutas | **corregido** en el addendum |
| `CI-6` | `H3` conservado, desglosado en cuatro piezas | **corregido** en el addendum |
| `R1`–`R8` | registrar las resoluciones por su vía | **registradas** como `O7`–`O14` |
| `T158` | regresión que falla contra el código anterior, y corrección | **corregido**, con `P-08` declarado abierto |

## Lo que sigue abierto, y no lo cierra esta puerta

```text
F4                       no iniciada. Nada de esta puerta la adelanta.
P-08                     vigencia de la evidencia más allá de T161.
X1 · P-05                deferidas. Ninguna corrección de aquí las toca, y ninguna cruza
                         la línea del blueprint hacia una cuarta capa.
EL PILOTO                seleccionado por O14 y NO ejecutado. Mientras no se ejecute,
                         T169, T170, CA-10, CA-11 y el §100 como descubrimiento siguen
                         sin demostrarse, y la columna de uso real sigue vacía.
LOS SOPORTES AGENTIC     O13 fija la matriz objetivo. Ninguno está certificado: certificar
                         exige la prueba de humo, y la prueba de humo exige adaptador.
LA MIGRACIÓN DE P-07     hecha para los dos documentos de la raíz. Los tres que viven en
                         docs/evolucion/ conservan su exención individual, y su migración
                         queda pendiente.
```

**(a), (b), `E1`, `E2` y `K-1` no se han tocado.** Ninguna corrección de esta puerta las
modifica, y ninguna propone enmienda.
