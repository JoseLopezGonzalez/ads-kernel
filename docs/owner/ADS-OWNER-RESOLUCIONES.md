# RESOLUCIONES DEL OWNER — SEDE CANÓNICA

> **QUÉ ES ESTE DOCUMENTO, Y QUÉ NO ES.**
>
> Contiene **palabras emitidas o ratificadas por el Owner**. **NO es una reconstrucción del
> coordinador.** Cada resolución se registra **íntegramente**, no en resumen.
>
> **Esta sede nace por `O19`**, y nace porque el TERCER GATE DE CERTIFICACIÓN —documento 24—
> demostró que el corpus **había perdido la capacidad de comprobar qué había dicho el Owner**:
> una resolución suya sólo constaba porque el coordinador la transcribía, y ningún revisor
> podía contrastarla contra nada. El adjudicador `X` lo llevó al Owner como una
> **RATIFICACIÓN**, y el Owner ordenó crear esta sede.

## Reglas de esta sede

```text
APPEND-ONLY            las entradas no se editan ni se borran. Una resolución posterior
                       REVISA a la anterior sin borrarla, y la anterior se conserva

AUTORIDAD              esta sede es la AUTORIDAD CANÓNICA. Ninguna paráfrasis en
                       `DECISIONES-Y-CONTRADICCIONES.md` la sustituye: **el registro de
                       decisiones es una PROYECCIÓN DERIVADA**

CADA ENTRADA LLEVA     identificador · fecha · procedencia · texto · alcance ·
                       relaciones de revisión

EL SOBRE DE ANCLA      el sobre externo de cada gate **incluye la huella de esta sede**, y
                       **un gate FALLA CERRADO si la sede no coincide con la huella
                       recibida externamente**

UNA PARÁFRASIS NUNCA   puede ampliar la autoridad del texto canónico
```

## Cómo nace una resolución, desde `O19` en adelante

```text
1  ninguna resolución del Owner nace únicamente en `DECISIONES-Y-CONTRADICCIONES.md`
2  primero se materializa AQUÍ, con su texto completo
3  después se proyecta al registro de decisiones
4  la proyección debe ENLAZAR a la resolución canónica
5  el texto canónico entra en el sobre externo del siguiente gate
6  los revisores reciben su SHA-256 ANTES de leer
7  el adjudicador compara la sede canónica, la proyección y el sobre
8  cualquier diferencia FALLA CERRADO
9  una paráfrasis nunca puede ampliar la autoridad del texto canónico
10 una resolución posterior REVISA, pero no borra, la anterior
```

**El coordinador puede transcribir materialmente la respuesta del Owner porque el Owner lo
está ordenando, pero no puede reinterpretarla ni resumirla como fuente canónica.**

## Qué NO está en esta sede, y por qué

**`O1`–`O16` no se registran aquí.** No se reconstruyen ni se inventan sus textos: se
conservan en su registro histórico actual —`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`,
sección 2— **hasta que exista una ratificación expresa o una fuente primaria verificable**.
Es una orden del Owner en la ratificación de `O19`, y se cumple literalmente.

---

# `O17` · EL NIVEL ESTRUCTURAL Y SU PRODUCTOR

```text
IDENTIFICADOR   O17
FECHA           2026-08-30
PROCEDENCIA     respuesta expresa del Owner a la consulta que el GATE INDEPENDIENTE DE
                CERTIFICACIÓN —documento 22— formuló como su única clase `B`
REVISA          nada. `O1`-`O16` conservan íntegramente su texto
REVISADA POR    nada
PROYECCIÓN      `O17` y `D107` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO autoriza iniciar `F5`, `F6` ni PesquerApp
```

## Texto

**Elijo la opción (b):**

**EL NIVEL ESTRUCTURAL DEBE PRODUCIRSE AL INICIO DE CADA MACROCIRCUITO, COMO PRECONDICIÓN
PROPIA.**

No elijo la alternativa barata de certificarlo sólo durante la instalación. Quiero que
instalación, adopción, migración y actualización comprueben la estructura vigente antes de
continuar.

La prioridad es una base sólida y permanente, aunque suponga más comprobaciones y consumo de
recursos.

### Los cuatro macrocircuitos deben producir el nivel Estructural al arrancar

instalación · adopción · migración · actualización.

### Reglas obligatorias

```text
 1  cada ejecución de un macrocircuito produce exactamente una certificación Estructural
    propia
 2  se produce antes de cualquier mutación canónica del macrocircuito y antes de intentar
    elevarse a Operativa, Integrada o Completa
 3  superar una ejecución anterior no certifica automáticamente la actual
 4  un nivel superior no implica por sí mismo que Estructural siga vigente
 5  si Estructural falla, el macrocircuito se bloquea antes de mutar estado
 6  los cuatro macrocircuitos invocan el mismo contrato y el mismo mecanismo compartido.
    No se crean cuatro implementaciones divergentes
 7  el sujeto de la certificación debe identificar como mínimo:
      · producto o instalación
      · ejecución del macrocircuito
      · revisión del kernel
      · revisión de schemas y contratos aplicables
      · configuración y fuentes relevantes
      · huella de la evidencia
 8  puede reutilizarse evidencia material anterior únicamente si se demuestra que todas sus
    entradas y huellas siguen idénticas
 9  incluso cuando la evidencia pueda reutilizarse, cada ejecución del macrocircuito debe
    producir su propia declaración Estructural, vinculada a esa ejecución
10  la reutilización nunca puede consistir en copiar una certificación anterior ni en
    presumirla vigente
11  la cadena queda: Estructural → Operativa → Integrada → Completa
12  cada nivel conserva productor, evidencia, sujeto, vigencia y condición de invalidación
    propios
```

### Reparto de responsabilidades decidido

```text
· SIS es propietario y productor de la declaración Estructural
· VER produce el dosier o evidencia verificadora, sin apropiarse de la decisión final
· PLT ejecuta la maquinaria técnica cuando el contrato vigente le atribuya esa ejecución
· SEG conserva su capacidad de bloqueo cuando la estructura incumpla seguridad
· El propietario de cada macrocircuito no puede sustituir a SIS en la certificación, pero
  debe exigirla antes de continuar
```

Si alguna atribución técnica más concreta ya está inequívocamente fijada por las fuentes
aprobadas, propágala sin contradecir este reparto. Si una fuente protegida dice algo
incompatible, eso sí constituye una nueva parada real.

## Nota de trazabilidad de `O17`

> **Su procedencia no es verificable contra ninguna fuente primaria del árbol anterior a esta
> sede.** El documento 22 contiene la PREGUNTA, escrita antes de la respuesta, y no puede
> contener el motivo que el Owner dio al responder. **No se afirma que sea falsa: se declara
> INVERIFICABLE**, y por eso existe esta sede.

---

# `O18` · LA RAÍZ DE CONFIANZA DE LA VERIFICACIÓN — TEXTO AMPLIO RATIFICADO

```text
IDENTIFICADOR   O18
FECHA           2026-08-30   ·   RATIFICADA el 2026-08-30 por `O19`
PROCEDENCIA     respuesta expresa del Owner a la consulta que el SEGUNDO GATE DE
                CERTIFICACIÓN —documento 23— formuló como su única clase `B`
REVISA          nada. `O1`-`O17` conservan íntegramente su texto
REVISADA POR    `O19`, que revisa LA PROYECCIÓN INCOMPLETA de `O18`, no su contenido
PROYECCIÓN      `O18` y `D108` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO autoriza iniciar `F5`, `F6` ni PesquerApp
```

## Texto amplio, ratificado

**No elijo ninguna de las tres alternativas en su forma aislada. Elijo una resolución
escalonada:**

```text
1  OPCIÓN (b) PARA CERRAR `F4c`
   ancla documental externa al árbol, recibida por cada revisor antes de leer el repositorio

2  OPCIÓN (c) COMO CONDICIÓN OBLIGATORIA DE `F6`
   verificador externo real antes de la primera adopción permanente de PesquerApp, antes de
   declarar ADS operativo y antes de certificar adaptadores
```

**Rechazo expresamente la opción (a). No acepto retirar la garantía ni asumir como solución
definitiva que una alteración deliberada sea indetectable.**

### Las TRES condiciones obligatorias para el verificador externo real de `F6`

```text
1  debe existir antes de la primera adopción permanente de PesquerApp
2  debe existir antes de declarar ADS operativo
3  debe existir antes de certificar cualquier adaptador
```

### El reparto de responsabilidades

```text
· SIS define el contrato de conformidad
· PLT construye y opera la maquinaria externa
· VER produce el dosier independiente
· SEG gobierna credenciales, bloqueo y fallos de confianza
· el Owner conserva la autoridad de aceptar o rechazar la raíz externa
· el ejecutor externo no puede compartir la identidad de escritura del runtime ADS
```

### Motivo de la decisión

La opción (c) es la garantía final correcta, pero exigir que su infraestructura exista antes
de cerrar `F4c` produciría una dependencia circular:

```text
`F4c` bloquea `F5` · `F5` precede a `F6` · `F6` construiría el verificador
pero `F4c` permanecería abierta hasta que `F6` lo construyera
```

**No acepto ese bloqueo circular.** Por tanto:

```text
· `F4c` puede certificarse mediante el ancla documental externa de (b)
· la limitación residual se declara expresamente
· `F6` debe sustituir esa confianza documental por verificación externa mecánica
· PesquerApp no puede iniciar su adopción permanente mientras esa sustitución no exista y
  esté probada
```

Esto mantiene el avance y conserva la exigencia de una base final sólida.

### El resto de la resolución, ratificado

```text
· opción (b), ancla documental externa, para cerrar `F4c`
· opción (c), verificador externo real, como obligación de `F6`
· rechazo de la opción (a)
· la garantía documental es TRANSITORIA y LIMITADA
· `F4c` NO afirma resistencia completa frente a un actor privilegiado
· el verificador externo NO se implementa durante `F4c`
· esta resolución NO autoriza iniciar `F5`, `F6` ni PesquerApp
```

### Alcance de la garantía documental, dicho por el Owner

```text
LA BATERÍA INTERNA GARANTIZA     coherencia interna · detección de regresiones conocidas ·
                                 derivación de inventarios · contradicciones entre fuentes ·
                                 cambios respecto a referencias recibidas · cumplimiento de
                                 contratos documentales

EL SOBRE EXTERNO AÑADE           una referencia que el árbol no puede redefinir
                                 unilateralmente durante el gate · detección de que el árbol
                                 auditado no coincide con el encargado · detección de que el
                                 manifiesto fue sustituido después del reparto

NO SE AFIRMA QUE PROTEJA         compromiso del canal del Owner · compromiso simultáneo del
FRENTE A                         repositorio y del coordinador · robo de credenciales ·
                                 reescritura autorizada de ramas remotas · manipulación del
                                 ejecutor externo · falsificación de identidad

                                 Esos riesgos pertenecen al verificador externo de `F6`
```

**`M-04` puede cerrarse para el alcance de `F4c` únicamente si el gate independiente
demuestra:** batería interna coherente · sobre externo recibido antes de leer · todas sus
huellas coincidentes · referencias remotas intactas · cobertura completa · **ninguna promesa
de seguridad superior a la realmente entregada**.

---

# `O19` · RATIFICACIÓN DEL TEXTO AMPLIO DE `O18` Y SEDE CANÓNICA

```text
IDENTIFICADOR   O19
FECHA           2026-08-30
PROCEDENCIA     respuesta expresa del Owner a la RATIFICACIÓN que el TERCER GATE DE
                CERTIFICACIÓN —documento 24, §13 de la adjudicación de `X`— le formuló
REVISA          LA PROYECCIÓN INCOMPLETA de `O18`. NO revisa su contenido ni su diseño
REVISADA POR    nada
PROYECCIÓN      `O19` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO autoriza iniciar `F5`
```

## Texto

**Elijo la opción (c), aplicada sobre la opción (a):**

**RATIFICO EL TEXTO AMPLIO DE `O18` Y ORDENO DARLE UNA SEDE CANÓNICA EN `docs/owner/`.**

**La omisión está en la transcripción del coordinador, no en mi resolución original.**

### Lo que `O19` declara

```text
· `O18` fue transcrita de forma INCOMPLETA
· el Owner RATIFICA ahora su contenido amplio
· las dos condiciones omitidas y el reparto PERTENECÍAN a la resolución original
· `O19` revisa la PROYECCIÓN incompleta de `O18`
· la autoridad canónica deja de ser la paráfrasis del coordinador
· la autoridad canónica pasa al documento de resoluciones del Owner
· las sedes derivadas deben citar `O19` y la sede canónica
· la entrada corta de `O18` se conserva como REGISTRO HISTÓRICO de la transcripción
  incompleta
· esta corrección NO cambia el diseño: corrige su PROCEDENCIA y AUTORIDAD
· `O19` tampoco autoriza iniciar `F5`
```

### Sobre las seis sedes que ya contenían el texto amplio

**No se retira ninguna. Su contenido es correcto.**

Sí se corrige **cualquier rótulo que dijera que ese texto era «literal de `O18`»** cuando la
fila corta de `O18` no lo contenía. **A partir de ahora es literal de la SEDE CANÓNICA DEL
OWNER**, y está ratificado mediante `O19`.

### Lo que el Owner ordena sobre el sobre externo

El siguiente sobre debe incluir, además de lo ya establecido:

```text
· ruta de la sede canónica de resoluciones del Owner
· SHA-256 de esa sede OBTENIDO DEL COMMIT AUDITADO
· identificadores `O17`, `O18` y `O19`
· digest del texto canónico de cada resolución
· la relación: `O19` revisa la proyección incompleta de `O18`
· declaración externa de que ésta es la resolución ratificada por el Owner
```

Cada revisor debe recibir externamente: el texto de esta ratificación · el SHA del commit
candidato · el tree SHA · el SHA del manifiesto · el SHA del derivador · **el SHA de la sede
del Owner**. Y **debe comprobar la receta sin ejecutar el emisor.**

**No vuelve a usarse como evidencia primaria:** mensajes de commit · paráfrasis del
coordinador · una fila derivada de `DECISIONES` · afirmaciones internas de que el Owner dijo
algo. **La sede canónica y el sobre recibido externamente son las dos piezas que deben
coincidir.**

### Estado de la ratificación

```text
LA RATIFICACIÓN QUEDA CERRADA
· versión AMPLIA
· tres condiciones obligatorias
· reparto SIS / PLT / VER / SEG / Owner / ejecutor externo
· `O19` revisa la transcripción corta
· `docs/owner/` es la sede canónica
· `O18` NO vuelve a someterse a elección
```

---

# `O20` · LA FRONTERA ENTRE `F4c` Y `F6`, Y EL FIN DE LA RECURSIÓN

```text
IDENTIFICADOR   O20
FECHA           2026-09-01
PROCEDENCIA     decisión expresa del Owner, tomada tras el OCTAVO GATE DE CERTIFICACIÓN
                —documento 29— y a la vista de que dos gates consecutivos, el séptimo y el
                octavo, devolvieron INSUFICIENTE por defectos de IMPLEMENTACIÓN del
                verificador interno y no por arquitectura sin decidir
REVISA          la FRONTERA DE FASE que `O18` y `O19` dejaron implícita. NO revisa su
                contenido, NO revisa su diseño y NO las reescribe: `O17`-`O19` conservan
                íntegramente su texto
REVISADA POR    nada
PROYECCIÓN      `O20` y `D109` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO autoriza iniciar `F5`, `F6` ni PesquerApp. NO declara suficiente a `F4c`:
                eso lo juzga un gate independiente
```

## Texto

**Cierro la recursión entre `F4c` y `F6`, y lo hago cambiando la frontera de certificación
sin rebajar la exigencia final del sistema.**

Ocho gates independientes han encontrado once árboles adversariales. Los cinco primeros
señalaban arquitectura o procedimiento; los tres últimos señalan **la implementación
provisional del verificador interno**, y cada corrección de esa implementación ha abierto la
siguiente. Eso no es un defecto de diligencia: es una **frontera de fase mal puesta**. Estoy
pidiendo a `F4c` que demuestre lo que `F6` tiene que construir.

### 1 · Lo que `F4c` sí debe producir

Una arquitectura **completa, coherente y suficientemente precisa para construir**, que
incluya: invariantes · contratos · propietarios · fases · entradas y salidas · condiciones de
fallo cerrado · matrices adversariales · criterios de aceptación ejecutables · y **asignación
inequívoca de cada obligación a `F5` o a `F6`**.

### 2 · Lo que `F4c` NO tiene que demostrar

`F4c` **no tiene que demostrar que la implementación provisional y mutable del verificador
interno ya satisface todos esos contratos.**

### 3 · Lo que `F6` es responsable de hacer

```text
· implementar el VERIFICADOR DE ADMISIÓN
· implementar la RAÍZ EXTERNA DE CONFIANZA que `O18` y `O19` ya exigen
· cerrar las LECTURAS GIT SEGURAS
· comprobar MUTACIONES de ficheros nuevos y preexistentes
· tratar CODIFICACIONES NO UTF-8
· comprobar ADICIONES, MODIFICACIONES, BORRADOS, RENOMBRADOS y CAMBIOS DE TIPO
· impedir que LA DEFINICIÓN DE LO VERIFICADO Y LA REGLA DE ADMISIÓN puedan excluirse a sí
  mismas
· ejecutar la MATRIZ ADVERSARIAL COMPLETA
· CERTIFICAR la implementación antes de declarar ADS operativo o iniciar la adopción
  permanente de PesquerApp
```

### 4 · Qué es la batería interna, y qué no

La batería interna de `F4c` es **evidencia de consistencia del corpus**, no una raíz
autosuficiente de certificación de su propia implementación.

### 5 · Qué NO demuestra un verde

**Un verde de la batería interna NO demuestra que el verificador de `F6` esté construido ni
certificado.** Nadie puede citarlo para eso.

### 6 · Ningún hallazgo desaparece por este cambio

```text
· los defectos ARQUITECTÓNICOS o DOCUMENTALES siguen bloqueando `F4c`
· los defectos de IMPLEMENTACIÓN del verificador pasan a CONTRATOS OBLIGATORIOS de `F6`
· todos conservan identificador, reproducción, propietario, fase y prueba posterior
· NINGUNO puede marcarse como SUPERADO mientras no se implemente y se ejecute en `F6`
```

### 7 · Qué tiene que confirmar el gate que autorice `F5`

```text
· que NO queda arquitectura por decidir
· que TODOS los contratos de `F6` están completos
· que NINGÚN defecto de implementación se presenta falsamente como corregido
· que las obligaciones pendientes de `F6` NO ocultan una decisión arquitectónica
```

### 8 · PesquerApp

**PesquerApp sigue BLOQUEADA** hasta que `F6` implemente y certifique estos contratos. **No
se autoriza MVP, ni piloto desechable, ni adopción parcial.**

## Nota de trazabilidad de `O20`

> **Qué corrige, dicho sin adorno: una FRONTERA DE FASE CIRCULAR**, detectada tras dos gates
> consecutivos —el séptimo, documento 28, y el octavo, documento 29—. `F4c` bloqueaba a `F5`;
> `F5` precede a `F6`; y `F6` es quien construye el verificador cuya implementación se le
> estaba exigiendo a `F4c`. Es la misma clase de bloqueo circular que `O18` cerró para la
> RAÍZ DE CONFIANZA, un piso más abajo: allí era el mecanismo, aquí es la fase.
>
> **Lo que esta resolución NO hace, y se dice para que nadie lo lea de más:** no rebaja la
> exigencia final —los mismos contratos siguen siendo obligatorios y ahora tienen fase y
> propietario—, no declara suficiente a `F4c`, no cierra ningún hallazgo, no autoriza `F5`,
> `F6` ni PesquerApp, y **no reescribe `O17`, `O18` ni `O19`**, que conservan su texto.
>
> **Su procedencia es la misma que la de `O17`, `O18` y `O19`**: decisión expresa del Owner
> registrada en esta sede, que es append-only. Lo que la distingue es que **no responde a una
> pregunta que un gate le elevara**: los ocho gates declararon expresamente que ninguna
> decisión volvía al Owner. **Esta la toma el Owner por su cuenta**, y consta así.

---

# `O21` · `C-L.5` DEJA DE SER UN ACTO DISCRECIONAL

```text
IDENTIFICADOR   O21
FECHA           2026-09-01
PROCEDENCIA     decisión expresa del Owner, tomada tras el GATE ARQUITECTÓNICO FINAL
                —documento 30— y a la vista de que dos adjudicadores consecutivos trataron
                la certificación de cobertura de forma OPUESTA sin que ninguno incumpliera
                norma alguna: `FF` la certificó MIENTRAS devolvía insuficiencia, y `HH` se
                negó a certificarla POR devolver insuficiencia
REVISA          la SEMÁNTICA de `C-L.5`: qué certifica, cuándo debe declararse y a qué
                queda ligada. NO revisa su contenido normativo —las seis condiciones son
                las que ya estaban escritas— y NO reescribe `O17`, `O18`, `O19` ni `O20`,
                que conservan íntegramente su texto
REVISADA POR    nada
PROYECCIÓN      `O21` y `D110` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO declara suficiente a `F4c`, NO corrige ninguno de los dieciséis
                hallazgos del documento 30, y NO autoriza `F5`, `F6` ni PesquerApp
```

## Texto

**`C-L.5` deja de ser un acto discrecional, y paso a decir exactamente qué certifica, cuándo
hay que declararlo y a qué queda ligado.**

### 1 · Qué certifica, y qué no

`C-L.5` certifica **exclusivamente la COBERTURA de un gate**. **No certifica suficiencia
arquitectónica y no sustituye al veredicto general.**

### 2 · Es independiente del veredicto

Su resultado es **independiente** del veredicto `SUFICIENTE PARA F5` / `INSUFICIENTE PARA
F5`. Son dos preguntas distintas y se responden por separado.

### 3 · No es discrecional

Para un gate **válido**:

- si se cumplen **las seis condiciones normativas** de `C-L.5`, el adjudicador **debe**
  declarar `C-L.5 CERTIFICADA PARA ESTE GATE`;
- si falla cualquiera, **debe** declarar `C-L.5 ABIERTA` **y nombrar exactamente la
  condición incumplida**.

### 4 · Las seis condiciones

```text
1  corpus obligatorio DEFINIDO
2  manifiesto previo de ASIGNACIÓN publicado
3  manifiestos posteriores de LECTURA publicados
4  OBLIGATORIO menos ASIGNADO = vacío
5  ASIGNADO menos LEÍDO = vacío
6  revisores INDEPENDIENTES que declaran CONTRA SU PROPIO INTERÉS qué leyeron
```

### 5 · La certificación queda ligada a una tupla exacta

```text
· tree SHA candidato
· commit candidato
· SHA del manifiesto de asignación
· SHA de los manifiestos de lectura
· identificador del gate
· identidad del adjudicador
```

### 6 · No se transfiere

**No se transfiere automáticamente a otra candidata ni a otro gate.** Cada gate declara la
suya sobre su propia tupla.

### 7 · Las dos declaraciones pueden coexistir

Un gate puede declarar a la vez `C-L.5 CERTIFICADA` e `INSUFICIENTE PARA F5`. **No hay
contradicción**: la primera habla de COBERTURA y la segunda de SUFICIENCIA ARQUITECTÓNICA.

### 8 · Prohibición expresa

**Un adjudicador NO puede negarse a certificar la cobertura porque haya encontrado otros
defectos.**

### 9 · Sobre el gate del documento 30

**No se inventa retrospectivamente un acto que `HH` no emitió.** Se registra exactamente
esto:

```text
· las condiciones de cobertura estaban SATISFECHAS, y el propio adjudicador lo midió
· el ACTO no se emitió, por AUSENCIA DE UNA REGLA entonces vigente que lo hiciera obligatorio
· `O21` elimina esa ambigüedad para los gates POSTERIORES, y no la aplica hacia atrás
```

### 10 · Lo que esta resolución no hace

**No declara suficiente a `F4c`, no corrige ninguno de los dieciséis hallazgos del documento
30, y no autoriza `F5`, `F6` ni PesquerApp.**

## Nota de trazabilidad de `O21`

> **Qué corrige: una AMBIGÜEDAD DE PROCEDIMIENTO, no un defecto de nadie.** Ni `FF` ni `HH`
> incumplieron norma alguna, porque la norma no existía: `C-L.5` describía **cuándo la
> cobertura queda excluida** y no **cuándo queda certificada**, con lo que el acto quedaba a
> criterio del adjudicador y podía oscilar indefinidamente sin que nadie faltara a nada.
> `O21` convierte una decisión en una comprobación.
>
> **Como `O20`, no responde a una pregunta que un gate le elevara**: los nueve gates
> declararon que ninguna decisión volvía al Owner. **La toma el Owner por su cuenta**, y
> consta así.
>
> **Y no toca las seis condiciones**: son exactamente las que `C-L.5` ya exigía —`O-04` fijó
> los dos manifiestos, `P-08` fijó las dos restas, y el documento 19 fijó el corpus
> obligatorio y la independencia—. Lo único nuevo es que **cumplirlas OBLIGA a declararlo**.

---

# `O22` · CERTIFICACIÓN INCREMENTAL DEL DELTA

```text
IDENTIFICADOR   O22
FECHA           2026-09-01
PROCEDENCIA     decisión expresa del Owner, tomada tras el GATE DE VERIFICACIÓN DE LOS DOCE
                `HH2` —documento 32— y a la vista de que ese gate es VÁLIDO, CERTIFICA la
                cobertura, cierra ONCE de sus doce objetos, identifica UN SOLO bloqueo y
                declara EXPRESAMENTE, en su prueba contrafáctica, que cerrado ese bloqueo el
                veredicto sería SUFICIENTE
REVISA          el MÉTODO DE VERIFICACIÓN, y sólo eso: cuándo un gate completo válido puede
                complementarse con una verificación INCREMENTAL en vez de repetirse entero.
                NO revisa el contenido de `O17`, `O18`, `O19`, `O20` ni `O21`, que conservan
                íntegramente su texto, ni las seis condiciones de `C-L.5`, ni el umbral de
                suficiencia
REVISADA POR    nada
PROYECCIÓN      `O22` y `D111` en `DECISIONES-Y-CONTRADICCIONES.md`
ALCANCE         NO declara suficiente a `F4c` —eso lo compone la verificación del delta con
                el gate del documento 32—, NO cierra ningún hallazgo, y NO autoriza ni
                inicia `F5`, `F6` ni PesquerApp
```

## Texto

**Un gate completo y válido no tiene que repetirse entero para juzgar la reparación de su
único bloqueo.** Abro la CERTIFICACIÓN INCREMENTAL DEL DELTA, y la acoto con dureza para que
no sea una puerta de escape.

### 1 · Cuándo se puede usar, y sólo entonces

```text
· el gate anterior es VÁLIDO, y lo declaró su propio adjudicador
· identifica UN SOLO bloqueo
· declara EXPRESAMENTE, y no por inferencia de nadie, que cerrado ese bloqueo el resultado
  sería SUFICIENTE
```

**Si falta cualquiera de las tres, no hay composición: hay gate completo.**

### 2 · Qué puede contener la candidata delta

La nueva candidata **difiere sólo en**: el BLOQUEO, la RESOLUCIÓN que autoriza la composición
—esta misma— y sus PROYECCIONES. **Todos los demás blobs obligatorios permanecen IDÉNTICOS**,
y esa identidad se comprueba blob a blob, no se declara.

### 3 · Qué tiene que hacer el verificador

```text
· leer ÍNTEGRAMENTE todas las fuentes MODIFICADAS
· REPRODUCIR el defecto anterior sobre la candidata que el gate juzgó
· DEMOSTRAR su ausencia sobre la candidata delta
```

### 4 · Qué NO puede hacer el verificador

**No puede corregir nada.** Ni una letra. Quien verifica no repara, y quien repara no
verifica: es la misma frontera que este expediente lleva doce gates sosteniendo.

### 5 · La cobertura se traslada POR DELTA, y sólo así

`C-L.5` certificada por el gate anterior **puede trasladarse por delta** si —y sólo si— **todos
los blobs no modificados coinciden** y **todas las fuentes modificadas se leen íntegras**.

El verificador **debe emitir** `C-L.5 CERTIFICADA POR DELTA`, **o explicar por qué no es
transferible**. No hay tercera salida y no hay silencio.

### 6 · Los hallazgos no bloqueantes NO se ignoran

`O22` **no ignora** los seis hallazgos menores y leves que el documento 32 deja vivos.
**Permanecen REGISTRADOS como NO BLOQUEANTES**, con su identificador, su sede, su remedio, su
propietario y su fase — **porque el adjudicador de ese gate declaró que, cerrando el único
bloqueo, el resultado sería suficiente**, y no porque nadie los rebaje aquí. Ninguno se
declara SUPERADO.

### 7 · Si aparece otro bloqueo

**La composición FALLA, y no habrá otro ciclo.** No se abre una tanda nueva, no se convoca
otro gate y no se vuelve a intentar la composición: se registra el resultado y se para.

### 8 · Lo que esta resolución no hace

**No rebaja el criterio de suficiencia**, que sigue siendo el del documento 32 y el de `O20`
§7. **No inicia `F5`, `F6` ni PesquerApp**, y PesquerApp sigue BLOQUEADA hasta que `F6`
implemente y certifique sus contratos.

## Nota de trazabilidad de `O22`

> **Qué corrige: un COSTE DE MÉTODO, no un defecto de nadie.** El documento 32 devolvió
> INSUFICIENTE por un solo objeto —una precondición de siete palabras ausente de una celda—
> mientras certificaba la cobertura y cerraba once de doce. Repetir un gate completo de tres
> agentes y noventa fuentes para juzgar una frase es desproporcionado, y **la
> desproporción es lo único que esta resolución toca**: el UMBRAL de suficiencia no se mueve,
> y la carga del verificador del delta es MÁS dura por fuente que la de un revisor de gate
> completo —lectura íntegra obligatoria de todo lo modificado, reproducción del defecto
> anterior y demostración de su ausencia—.
>
> **Como `O20` y `O21`, no responde a una pregunta que un gate le elevara**: los doce gates
> declararon que ninguna decisión volvía al Owner. **La toma el Owner por su cuenta**, y
> consta así.
>
> **Y no levanta la OPCIÓN C para el método de corrección iterativa**: lo que abre es una vía
> de VERIFICACIÓN, no una tanda más de corrección general. El alcance de la candidata delta
> lo fija §2, y fuera de él no hay nada que aplicar.

---

# `O23` · DECISIONES NORMATIVAS DE `F5` Y REGLAS PARA COMPLETARLA

**Fecha:** 2026-09-02  
**Autoridad:** Owner  
**Estado:** VIGENTE

## 1 · Objeto

Esta resolución registra conjuntamente las decisiones que requiere `F5` para completar `F5-A`–`F5-G`.

`F4c` permanece CERRADA. `F5` está INICIADA y EN CURSO. `F6` permanece NO INICIADA. PesquerApp permanece BLOQUEADA.

Esta resolución no declara `F5` cerrada, no implementa contratos de `F6` y no autoriza el inicio de PesquerApp.

## 2 · Sección normativa `(g)`

Se adopta una sección `(g)` normativa breve y un contrato derivado que `F6` deberá implementar.

La sección `(g)` fija los componentes obligatorios y las invariantes observables del estado durable: atomicidad, durabilidad, integridad, concurrencia, diario, recuperación, reconciliación, versionado, migración, autoridad de escritura, auditabilidad, gobierno Git del control repo y frontera con la raíz externa de confianza.

Su perímetro incluye íntegramente las materias que las fuentes vigentes reservaron a `(g)` y que `F5` ha reconstruido en `B-01`.

El contrato derivado fija rutas, nombres de fichero, serialización, algoritmos, bloqueos, herramientas y mecanismos concretos. Estos detalles podrán evolucionar sin otra decisión del Owner si preservan las invariantes normativas, mantienen compatibilidad o migración explícita y superan las pruebas del contrato.

## 3 · Raíz externa de confianza

La norma de la raíz externa de confianza forma parte de `(g)` y tendrá un contrato derivado propio para `F6`.

Debe ejecutarse fuera del repositorio verificado, usar una identidad sin permiso de escritura sobre él, recibir desde fuera la política de admisión, fallar de forma cerrada, producir evidencia trazable y bloquear PesquerApp mientras no esté implementada y certificada.

La tecnología, el despliegue, las claves, las rutas y los mecanismos concretos pertenecen al contrato de `F6`.

## 4 · Reconciliación pendiente

Al agotarse los reintentos se escribirá un registro operativo auxiliar durable, separado del estado canónico y del diario canónico.

Ese registro vive en el control repo bajo administración del runtime, sobrevive a reinicios, es append-only o equivalentemente auditable e identifica producto, repositorio, item, intento, causa y momento.

Su existencia permite deducir inequívocamente `reconciliacion-pendiente`. No modifica por sí misma el estado canónico y sólo se retira mediante una transición explícita y auditable de reconciliación.

Su ruta y serialización concretas pertenecen al contrato derivado de `F6`.

## 5 · Gate constitucional y circuito de arranque

Se conserva el gate constitucional de arranque. El circuito nuevo queda subordinado a él. Permanecen vigentes su plazo, sus diez entregables y sus cuatro prohibiciones.

## 6 · Nacimiento del trabajo por política

Se reconoce una tercera vía de nacimiento del trabajo: apertura automática por una política previamente aprobada.

No exige una petición individual del Owner, pero sí política vigente, trazabilidad, límites y posibilidad de suspensión.

## 7 · Participantes

Verificación es participante condicional y productora del dictamen en la ruta de auditoría.

Dominio, Seguridad y Diseño son participantes condicionales en la puesta en marcha de un producto nuevo cuando la materia del descubrimiento requiera sus capacidades.

Cuando una tabla de participación haya colocado un método donde corresponde una capacidad, se sustituirá por la capacidad competente y su condición de participación.

## 8 · Grafía canónica

Para los dos identificadores sometidos a decisión en `D-08`, manda la grafía con tilde de la fuente aprobada.

Los artefactos derivados y la implementación deberán alinearse con ella.

## 9 · Mapa documental

El mapa documental se satisface mediante una derivación mecánica reproducible. No se crea un mapa escrito que dependa de mantenimiento manual.

## 10 · Ratificaciones y correcciones determinadas

Se aprueban:

- las cuatro lecturas y la retirada del borrador `B-05`, incluida la lectura propuesta para el estado durable de la iniciativa;
- la checklist editorial `B-09`;
- la nota de vigencia `B-10`.

No se reabre ninguna de esas lecturas.

## 11 · Aplicación y cierre de `F5`

Las decisiones de esta resolución deberán aplicarse mediante las enmiendas, contratos normativos y proyecciones que corresponda, conservando el material aprobado anterior y su trazabilidad.

`F5` sólo podrá declararse cerrada mediante un acto posterior y expreso del Owner, después de demostrar que:

- `F5-A`–`F5-G` están completos;
- `A1`–`A7` están satisfechos;
- no queda ningún borrador presentado como aprobado sin estarlo;
- la validación final es satisfactoria.

Este texto no inicia `F6`, no declara implementados sus contratos y no desbloquea PesquerApp.

## 12 · Alcance

Esta resolución resuelve conjuntamente `D-01`–`D-10` y `R-01`–`R-05` del paquete de decisiones de `F5`.

La opción elegida para `R-04` es la inscripción directa de este texto por el Owner. La opción elegida para `R-05` es el cierre posterior mediante acto expreso del Owner.

---

# `O24` · CIERRE DE `F5` E INICIO DE `F6`

**Fecha:** 2026-09-02  
**Autoridad:** Owner  
**Estado:** VIGENTE

## 1 · Cierre de `F5`

Declaro `F5` CERRADA.

Las cuatro condiciones establecidas por `O23` §11 están demostradas:

- `F5-A`–`F5-G` están completos;
- `A1`–`A7` están satisfechos;
- no queda ningún borrador presentado como aprobado sin estarlo;
- la validación final es satisfactoria.

## 2 · Inicio de `F6`

Autorizo e inicio `F6`.

`F6` implementará y certificará los contratos técnicos aprobados por `F5`, respetando las invariantes de la sección `(g)`, las enmiendas vigentes y la jerarquía de autoridad del corpus canónico.

Las decisiones sobre rutas, formatos, serialización, algoritmos, bloqueos, herramientas, despliegue y mecanismos internos pertenecen a `F6` cuando la norma las haya dejado expresamente al contrato derivado.

Esas decisiones técnicas no pueden rebajar atomicidad, durabilidad, integridad, recuperación, auditabilidad, independencia de la raíz externa ni compatibilidad o migración explícita.

## 3 · Evidencia de `F6`

La suficiencia de `F6` se demostrará mediante implementación ejecutable y pruebas reproducibles.

La existencia de documentos, contratos o resultados simulados no equivale a implementación ni a certificación.

Cada contrato deberá demostrar, según corresponda:

- escenario positivo;
- escenario negativo;
- recuperación ante interrupción;
- fallo cerrado;
- idempotencia;
- concurrencia;
- trazabilidad;
- integridad;
- compatibilidad o migración.

## 4 · PesquerApp

PesquerApp permanece BLOQUEADA.

El cierre de `F5` y el inicio de `F6` no autorizan:

- MVP;
- piloto desechable;
- adopción parcial;
- integración anticipada;
- ejecución productiva.

PesquerApp sólo podrá comenzar cuando `F6` haya implementado y certificado los contratos que la bloquean.

## 5 · Alcance

Esta resolución no reabre `F4c` ni `F5`, no declara `F6` completada y no declara implementado o certificado ningún contrato antes de su evidencia ejecutable.

---

# `O25` · TITULARIDAD Y CUSTODIA DE LA IDENTIDAD DE FIRMA EXTERNA

**Fecha:** 2026-09-02  
**Autoridad:** Owner  
**Estado:** VIGENTE

## 1 · Titularidad

La identidad criptográfica pertenece a la raíz externa de confianza de cada instalación de ADS.

La autoridad administrativa sobre esa identidad corresponde al Owner.

La identidad no pertenece al repositorio verificado, al control repo, al kernel, al runtime, a un proyecto concreto ni a un agente.

## 2 · Custodia

La clave privada será custodiada por una identidad de servicio dedicada del verificador externo mediante un proveedor de secretos o claves del sistema anfitrión.

La clave privada:

- permanecerá fuera de todos los repositorios;
- no se versionará;
- no aparecerá en estado, diarios, evidencia, configuración exportada, logs o errores;
- no será accesible por el runtime ni por los agentes del repositorio;
- será no exportable cuando el proveedor lo permita;
- será diferente por instalación y entorno.

La ausencia de un proveedor válido provoca fallo cerrado.

## 3 · Autoridad administrativa

El Owner conserva la autoridad para aprovisionar, autorizar, rotar, revocar, recuperar y sustituir la identidad mediante un canal administrativo externo y auditable.

La configuración externa de confianza establece la identidad o huella pública aceptada.

El repositorio verificado no puede cambiar por sí mismo qué identidad acepta la raíz externa.

## 4 · Firmas y evidencia

Las firmas, atestaciones, certificados y huellas públicas pueden incorporarse al repositorio como evidencia.

La clave privada y la autoridad para validar esa evidencia permanecen fuera del árbol verificado.

## 5 · Implementación

`F6` utilizará criptografía estándar y una biblioteca o proveedor mantenido. No implementará primitivas criptográficas propias.

El contrato permitirá:

- rotación;
- periodo de solapamiento explícito;
- claves activas;
- claves retiradas;
- claves revocadas;
- rechazo de claves desconocidas o revocadas;
- trazabilidad sin revelación de secretos.

Las claves efímeras están permitidas únicamente en pruebas y no constituyen custodia productiva.

## 6 · Alcance

Esta resolución cierra `FD-1` como decisión del Owner.

No declara implementada ni certificada la raíz externa, no completa `F6` y no desbloquea PesquerApp.

---

# `O26` · ACEPTACIÓN CONDICIONADA DE LA RAÍZ EXTERNA Y COMPETENCIA DEL GATE FINAL

**Fecha:** 2026-09-04  
**Autoridad:** Owner

## 1 · Aceptación arquitectónica

ACEPTO la raíz externa de confianza de `F6` como mecanismo arquitectónico de
referencia para satisfacer el criterio `B3`, siempre que la implementación
sometida al gate final demuestre conjuntamente:

1. que la raíz y su evidencia viven fuera del árbol verificado;
2. que la firma es asimétrica;
3. que la atestación queda ligada simultáneamente al SHA del commit y a su tree;
4. que el firmante y el verificador son componentes separados;
5. que el verificador no dispone de la clave privada;
6. que el ejecutor de la raíz no comparte capacidad de escritura sobre el
   repositorio de control con el runtime;
7. que existen rotación, solapamiento, retirada y revocación;
8. que clave desconocida, firma inválida, commit incorrecto, tree incorrecto,
   ausencia de proveedor y contaminación del entorno fallan cerrado.

## 2 · Alcance de la aceptación

Esta resolución acepta la ARQUITECTURA y autoriza que una implementación que
cumpla las ocho condiciones sea reconocida como la raíz externa aceptada por el
Owner.

No certifica por sí misma la implementación existente ni ninguna candidata
concreta. La aceptación se vuelve aplicable a una candidata únicamente cuando
un gate independiente VÁLIDO demuestre las ocho condiciones sobre su SHA exacto.

## 3 · Identidad independiente

En el entorno actual acepto como demostración transitoria una identidad distinta
dentro de un contenedor, con el repositorio montado en sólo lectura y controles
positivos que prueben que la identidad puede escribir en su propio espacio.

Para producción, la identidad deberá materializarse mediante una cuenta de
servicio, contenedor o aislamiento equivalente que no tenga permiso de escritura
sobre el repositorio de control.

## 4 · Custodia

La custodia productiva de las claves continúa siendo EXTERNA conforme a `O25`.

Una clave efímera de pruebas, aunque esté fuera de los repositorios y tenga
permisos `0600`, NO constituye custodia productiva.

## 5 · Competencia del gate

Un gate independiente VÁLIDO puede declarar `F6 CERTIFICADA` y `F6 CERRADA` si
demuestra simultáneamente:

1. que no quedan obligaciones internas de `F6` sin implementar;
2. que no quedan propiedades críticas sin una prueba capaz de fallar;
3. que todas las obligaciones tienen trazabilidad hasta evidencia ejecutable;
4. que la implementación satisface las ocho condiciones de esta resolución;
5. que no existen bloqueantes internos vivos.

## 6 · PesquerApp

La certificación y cierre de `F6` NO inician automáticamente PesquerApp.

Si el gate final es suficiente, PesquerApp quedará TÉCNICAMENTE DESBLOQUEADA PARA
UNA ADOPCIÓN CONTROLADA, pero seguirá NO INICIADA hasta una orden expresa del
Owner que defina producto, repositorios, alcance y condiciones de parada.

## 7 · No rebaja

Esta resolución no rebaja los contratos de `F6`, no corrige hallazgos, no
convierte deuda interna en externa y no permite certificar una candidata
incompleta.

## 8 · Condición de fracaso

Si el gate final no es válido o no certifica `F6`, la aceptación arquitectónica
permanece, pero `F6` seguirá ABIERTA y PesquerApp seguirá BLOQUEADA.

---

# `O27` · ACLARACIÓN SOBRE `O26` Y LOS CAMPOS DE LAS RESOLUCIONES HISTÓRICAS

**Fecha:** 2026-09-04  
**Autoridad:** Owner

## 1 · Delimitador de `O26`

La línea:

`FIN LITERAL DE O26.`

era un delimitador externo del encargo dirigido al coordinador y NO formaba parte
del texto resolutivo de `O26`.

Su omisión de la sede canónica fue correcta y no debe repararse añadiéndola ahora.

## 2 · Campos históricos

Los campos de procedencia y relaciones de revisión incorporados por el modelo
documental son exigibles prospectivamente desde la resolución que estableció esa
forma.

No se insertarán retroactivamente dentro de `O23`, `O24`, `O25` ni `O26`, porque
hacerlo rompería:

1. su literalidad;
2. el carácter append-only de la sede;
3. el digest del acto ya emitido.

Su ausencia no invalida esas resoluciones.

## 3 · Protección append-only

La propiedad append-only debe proteger CADA resolución cerrada ya publicada, no
solamente el prefijo correspondiente al nacimiento del fichero.

Una comprobación que permita borrar resoluciones completas posteriores y sustituirlas
por otro texto NO satisface la propiedad.

La implementación deberá derivar las entradas cerradas de la sede, conservar cada
una byte a byte y permitir únicamente añadir una nueva entrada completa al final.

## 4 · Gate y candidato

Los documentos del gate no forman parte de la candidata que el gate certifica.

Toda validación del producto debe ejecutarse sobre un checkout congelado del SHA de
la candidata. El manifiesto, los dictámenes y el documento del gate vivirán en la
rama del gate y no podrán alterar la línea base auditada.

## 5 · Cobertura

Un gate no puede llegar a adjudicación mientras algún revisor tenga una resta:

`ASIGNADO − LEÍDO`

distinta del conjunto vacío.

Si un revisor todavía no ha terminado, debe continuar su lectura. Su lote no puede
darse por cerrado, sustituirse con búsquedas ni compensarse con lo leído por otro
agente.

## 6 · Alcance

Esta resolución:

  · no certifica F6;
  · no corrige por sí misma ningún hallazgo técnico;
  · no declara satisfecho B3;
  · no inicia PesquerApp;
  · no rebaja ninguna obligación;
  · conserva íntegra la aceptación condicionada de O26.

---

# `O28` · CIERRE DE `F6` MEDIANTE VERIFICACIÓN INCREMENTAL SOBRE UN GATE VÁLIDO

**Fecha:** 2026-09-05  
**Autoridad:** Owner

## 1 · Base válida

Reconozco como base de juicio el gate válido publicado en
`review/f6-certificacion-final-insuficiente-20260905`, sobre la candidata
`c2437214c9353185d6b90b8fe86178302d4cf349`.

Su insuficiencia y sus hallazgos permanecen vigentes. Esta resolución no los
revoca ni los corrige.

## 2 · Composición

Autorizo que la certificación final de `F6` se resuelva mediante composición entre:

1. el gate válido anterior;
2. una candidata delta que corrija todos sus bloqueos internos;
3. la identidad byte a byte de todo blob obligatorio no modificado;
4. una regresión completa;
5. un verificador independiente que lea íntegramente todo lo modificado, reproduzca
   los defectos anteriores y pruebe su ausencia;
6. la ejecución expresa de las condiciones de `O26` que el gate anterior no ejerció.

No es necesario repetir la lectura completa de las fuentes que:

1. fueron leídas en el gate válido;
2. no cambian en la candidata delta;
3. conservan exactamente el mismo blob;
4. no dependen semánticamente de una fuente modificada.

## 3 · Significado operativo de `O26` §5.1 y §5.2

Para `O26` §5.1, una obligación interna se considera implementada cuando:

1. pertenece a un universo derivado de las fuentes normativas;
2. tiene trazabilidad inequívoca hasta código productivo;
3. tiene una prueba ejecutable;
4. tiene evidencia ligada al SHA y al tree;
5. su condición de cierre se ejecuta con resultado satisfactorio.

Para `O26` §5.2, una propiedad crítica se considera provista de una prueba capaz de
fallar cuando:

1. la propiedad se deriva de una fuente normativa;
2. existe un sabotaje que alcanza específicamente esa propiedad;
3. el árbol sano queda verde;
4. el sabotaje queda rojo por el motivo esperado;
5. la restauración devuelve el verde;
6. el canal productivo, y no sólo una copia textual, es el ejercido.

Estas reglas hacen comprobables ambos apartados. No afirman imposibilidad matemática
de que exista otro defecto.

## 4 · Hallazgos posteriores

Un hallazgo nuevo bloquea la certificación si permite cualquiera de estos efectos:

  · corrupción o pérdida silenciosa;
  · publicación inválida;
  · doble efecto;
  · evasión de autoridad;
  · falsificación de evidencia;
  · falso verde sobre una obligación crítica;
  · ejecución sin aislamiento exigido;
  · obligación interna de F6 sin implementar.

Los defectos menores que no producen ninguno de esos efectos deben registrarse con
propietario y fase, pero no abren automáticamente otro ciclo.

## 5 · Verificador

La verificación incremental será realizada por un agente independiente que:

  · no haya construido ninguno de los cortes de F6;
  · no modifique la candidata;
  · reciba un sobre de ancla antes de leer;
  · lea íntegramente todos los ficheros modificados;
  · contraste blob a blob los no modificados;
  · ejecute la regresión completa;
  · ataque individualmente los bloqueos;
  · emita un juicio propio.

## 6 · Competencia

Si la composición satisface `O26`, el verificador podrá emitir:

  `F6 CERTIFICADA POR COMPOSICIÓN`
  `F6 CERRADA`

El coordinador sólo podrá registrar literalmente ese acto.

## 7 · PesquerApp

El cierre de `F6` deja PesquerApp técnicamente disponible para una adopción controlada,
pero NO la inicia.

Su inicio requiere una orden posterior y expresa del Owner que identifique producto,
repositorios, alcance, entorno y condiciones de parada.

## 8 · Fin del ciclo

Si la verificación incremental resulta insuficiente:

  · F6 seguirá abierta;
  · PesquerApp seguirá bloqueada;
  · no se abrirá otro ciclo automático;
  · los pendientes se elevarán al Owner como una lista finita.

Esta resolución no rebaja los contratos de F6 ni autoriza ignorar defectos críticos.

---

# `O29` · CRITERIO DE PRUEBA BASADO EN RIESGO PARA EL CIERRE DE `F6`

**Fecha:** 2026-09-06  
**Autoridad:** Owner

## 1 · Corrección de `O28` §3

`O28` §3 se interpretó como si cada cláusula textual `falla_si` tuviera que disponer
de un sabotaje individual y exclusivo.

Esa interpretación NO es la intención del Owner y queda sustituida por esta
resolución.

Una cláusula funcional no se convierte automáticamente en una propiedad crítica
por estar formulada como condición de fallo.

## 2 · Propiedades críticas

Son críticas las propiedades cuya infracción puede producir:

1. pérdida o corrupción silenciosa de estado;
2. publicación parcial o inválida;
3. doble efecto o doble confirmación;
4. evasión de autoridad, permisos o gates;
5. falsificación de evidencia, identidad, commit o tree;
6. ejecución de código no autorizado;
7. degradación silenciosa de un mecanismo de seguridad;
8. incumplimiento de aislamiento;
9. recuperación no idempotente;
10. una declaración de éxito sobre una operación no ejecutada.

Cada propiedad crítica debe tener al menos una prueba adversarial que:

  · alcance el canal productivo;
  · sea verde sobre el árbol sano;
  · quede roja al sabotear la propiedad;
  · falle por el motivo esperado;
  · vuelva a verde tras restaurar.

Varias cláusulas pueden quedar cubiertas por una misma prueba cuando comparten
realmente la misma propiedad y el vínculo se declara.

## 3 · Obligaciones funcionales no críticas

Una obligación funcional no crítica queda probada mediante:

  · caso positivo;
  · caso negativo;
  · caso límite cuando proceda;
  · ejecución del camino productivo;
  · trazabilidad hasta evidencia;
  · vínculo al SHA y tree.

No necesita un mutante artificial por cada frase del contrato.

## 4 · Medición de `O26` §5.1

Una obligación interna se considera implementada cuando:

  · está en el universo normativo;
  · tiene implementación productiva;
  · su condición de cierre se ejecuta;
  · tiene prueba adecuada a su riesgo;
  · tiene evidencia ligada al candidato.

## 5 · Medición de `O26` §5.2

`O26` §5.2 se satisface cuando TODAS las propiedades críticas definidas en §2 tienen
una prueba adversarial capaz de fallar.

No exige un sabotaje para cada cláusula funcional de bajo riesgo.

## 6 · Severidad y certificación

Bloquean la certificación:

  · los defectos críticos descritos en §2;
  · obligaciones internas sin implementar;
  · pruebas que no ejecutan aquello que afirman;
  · falsos verdes materiales;
  · falta de trazabilidad de una obligación interna.

No bloquean por sí solos:

  · cifras documentales caducadas sin efecto operativo;
  · errores menores de redacción;
  · ausencia de un mutante exclusivo para una condición funcional ya ejercida;
  · limitaciones externas correctamente declaradas.

Los defectos no bloqueantes deben registrarse con propietario y fase.

## 7 · Entorno

Una propiedad dependiente del anfitrión puede certificarse para un perfil concreto
si se ejecuta realmente en ese perfil.

La certificación debe declarar su alcance y no universalizarla.

Puede utilizarse:

  · contenedor;
  · namespace;
  · runner separado;
  · identidad de servicio;
  · backend fuerte disponible.

No se exige ejercer un backend que el anfitrión demuestra no ofrecer.

## 8 · Cierre por composición

Autorizo una última verificación incremental sobre el trabajo ya realizado.

Si:

  · las obligaciones internas reales están implementadas;
  · las propiedades críticas tienen pruebas adversariales;
  · las ocho condiciones de O26 se ejercen;
  · M-04 y C-L.7 son adjudicadas favorablemente;
  · no queda ningún bloqueo material;

el verificador independiente podrá declarar:

  `F6 CERTIFICADA POR COMPOSICIÓN`
  `F6 CERRADA`

## 9 · PesquerApp

El cierre de F6 no inicia PesquerApp.

La deja técnicamente disponible para una adopción controlada que requerirá una orden
posterior y expresa del Owner.

## 10 · Fin del método

Después de esta verificación no se abrirá otro ciclo automático.

Si resulta insuficiente, se entregará una lista finita para decisión humana y se
detendrá el método.

---

# `O30` · CIERRE EJECUTIVO DE `F6` POR INVARIANTES ARQUITECTÓNICAS FINITAS

**Fecha:** 2026-09-06  
**Autoridad:** Owner

## 1. Corrección de la unidad de medida

La clasificación automática de cada cláusula `falla_si` mediante las palabras
que contiene NO es una medida competente del riesgo arquitectónico.

Quedan expresamente rechazadas como condiciones de cierre:

1. la obligación de proporcionar un sabotaje distinto para cada cláusula
   `falla_si`;
2. la clasificación de criticidad derivada principalmente de coincidencias
   léxicas;
3. la multiplicación de obligaciones cuando varias cláusulas expresan el mismo
   invariante material;
4. el cierre obtenido rebajando, suprimiendo o renombrando cláusulas para reducir
   un recuento;
5. la exigencia de cientos de mutantes cuando el riesgo material está cubierto
   por una prueba adversarial común y trazable.

Las mediciones anteriores de `O26-SAB` permanecen como evidencia histórica de lo
que aquel instrumento contó, pero NO gobiernan desde esta resolución la
certificación de `F6`.

Esta resolución no declara que aquellas cláusulas sean falsas, prescindibles ni
satisfechas. Corrige la unidad con la que se decide la certificación.

## 2. Catálogo cerrado de invariantes críticos

Para la certificación de `F6`, el universo crítico está formado por los siguientes
VEINTICUATRO invariantes arquitectónicos:

- `K01` · Una transición confirmada sobrevive a caída, reinicio y recuperación.
- `K02` · Una transición no confirmada nunca se publica como estado canónico.
- `K03` · La publicación del estado es atómica y conserva el orden contractual
  entre preparación, publicación y confirmación.
- `K04` · Recuperar o reanudar repetidamente es idempotente y no duplica efectos.
- `K05` · La concurrencia no permite dos confirmaciones para la misma revisión.
- `K06` · Diario, registro y cabezas durables detectan corrupción, truncamiento,
  sustitución y retirada de cola.
- `K07` · Una reconciliación sólo puede cerrarse mediante una transición
  autorizada y auditable.
- `K08` · Versiones y migraciones preservan integridad, usan errores tipados y
  fallan cerradas ante formatos desconocidos o estados imposibles.
- `K09` · Toda evidencia, atestación o certificación queda ligada conjuntamente
  al commit y al tree realmente juzgados.
- `K10` · Firma, verificación, rotación y revocación fallan cerradas y no confunden
  claves de prueba con custodia productiva.
- `K11` · Autoridad, productor, escritor y custodio permanecen separados conforme
  a sus contratos.
- `K12` · El entorno, la procedencia del código y las rutas de importación no
  permiten contaminación silenciosa del ejecutable juzgado.
- `K13` · La sede del Owner es append-only por ENTRADAS COMPLETAS y no puede
  aprobar una sustitución, truncamiento o reescritura de resoluciones.
- `K14` · El verificador de admisión juzga la mutación efectiva y falla cerrado
  ante cambios fuera del universo permitido.
- `K15` · El gobierno Git del control repo serializa correctamente escritores
  locales y entre máquinas, sin último-escritor-gana silencioso.
- `K16` · La contención fuerte alcanza al proceso y a sus descendientes, incluidos
  los que intenten escapar mediante `setsid` u otra nueva sesión.
- `K17` · La ausencia de aislamiento, firma, identidad, backend o capacidad
  requerida nunca se convierte en degradación silenciosa.
- `K18` · Enrutamiento, clasificación y selección se basan en datos estructurados
  y sedes canónicas, no en similitud de prosa.
- `K19` · La política C2/C4 respeta perfil, modelo, cardinalidad, combinaciones,
  integrador y `execution_slots`.
- `K20` · La prevención y observación de inanición no modifica la prioridad
  contractual, ni directamente ni mediante una secuencia de transiciones.
- `K21` · Entregas, acuses, reanudaciones y `Continúa` no pierden ni duplican
  trabajo confirmado.
- `K22` · La evidencia procede de la ejecución declarada, está vinculada al objeto
  juzgado y no admite saltos, omisiones o éxitos fabricados.
- `K23` · La huella del kernel y el sello del producto cubren sus ámbitos
  declarados, se calculan desde el árbol real y no se sustituyen entre sí.
- `K24` · Gates, estados de fase y autoridad impiden declarar éxito,
  certificación o adopción antes del acto competente.

El catálogo `K01`–`K24` es cerrado para este ciclo.

Un verificador sólo podrá proponer `K25` si demuestra un efecto material distinto
que no pueda adscribirse honestamente a ninguno de los veinticuatro. Cambiar la
redacción, la ruta, el nombre de una prueba o la instancia concreta no crea un
invariante nuevo.

## 3. Evidencia suficiente por invariante

Cada `Knn` debe tener:

1. fuente normativa;
2. mecanismo implementado;
3. canal productivo ejercido;
4. al menos un caso sano;
5. al menos una prueba adversarial capaz de poner rojo el mecanismo;
6. resultado esperado del sabotaje;
7. evidencia reproducible;
8. vínculo al commit y al tree juzgados.

Una misma prueba adversarial puede cubrir varios invariantes únicamente cuando:

- ejecuta realmente el mecanismo compartido;
- el vínculo prueba→invariante se declara de forma inequívoca;
- se explica qué observación distinta demuestra para cada invariante;
- al retirar la protección común, la prueba se pone roja por el motivo declarado.

No se exige un mutante exclusivo por cláusula ni por invariante si una prueba
compartida cumple estas condiciones.

## 4. Obligaciones funcionales no críticas

Las obligaciones internas de `F6` que no materialicen un invariante `Knn` no
necesitan un sabotaje exclusivo.

Para considerarlas implementadas deben tener:

1. fuente y propietario;
2. implementación real;
3. caso positivo;
4. caso negativo o de frontera cuando sea aplicable;
5. evidencia ejecutada;
6. trazabilidad hasta su condición exacta de cierre.

La resta de obligaciones internas sin implementar debe quedar vacía.

No se permite vaciarla cambiando una obligación de fase, declarándola externa sin
fuente competente, haciendo pasar documentación por implementación o usando una
batería ajena que no ejerza su condición de cierre.

## 5. Condiciones de `O26`

Las ocho condiciones de `O26` §1 deben ser ejercidas de nuevo sobre la candidata
final mediante sus canales reales.

Una limitación del anfitrión se registrará con exactitud y no se universalizará.
Si existe un backend disponible capaz de ejercer la condición, deberá usarse.

La custodia productiva de claves continúa siendo externa cuando así lo establezca
la resolución competente. Una clave efímera de prueba no la sustituye.

## 6. `M-04` y `C-L.7`

`M-04` y `C-L.7` no se cierran por una etiqueta escrita por quien implementa.

Si sus defectos productivos están corregidos, el verificador independiente final
de este ciclo debe ejercer sus condiciones de cierre y emitir por separado:

- `M-04 SUPERADA` o `M-04 NO SUPERADA`, con causa;
- `C-L.7 CERRADA` o `C-L.7 NO CERRADA`, con causa.

## 7. Certificación y cierre de `F6`

Un único verificador independiente podrá declarar:

- `F6 CERTIFICADA`;
- `F6 CERRADA`;

si, y sólo si, concurren todas estas condiciones:

1. `K01`–`K24` satisfechas;
2. ninguna obligación interna de `F6` sin implementar;
3. las ocho condiciones de `O26` ejercidas y satisfechas;
4. `M-04 SUPERADA`;
5. `C-L.7 CERRADA`;
6. ningún defecto interno BLOQUEANTE o GRAVE que invalide el objeto, la evidencia
   o la certificación;
7. identidad exacta del commit y tree juzgados;
8. sobre de ancla emitido antes de crear al verificador.

Un hallazgo MENOR o de observabilidad no impide el cierre salvo que falsee una de
las ocho condiciones anteriores. Debe permanecer registrado con identificador,
sede, remedio, propietario y fase, sin declararlo superado.

Esta resolución no certifica `F6`. Define quién puede hacerlo y con qué prueba.

## 8. Guía canónica vigente

Antes de la certificación debe existir una única guía operativa vigente que permita
construir, ejecutar, validar y diagnosticar `F6` sin reconstruir su estado leyendo
la sucesión de gates.

La guía:

- referencia las fuentes normativas;
- no copia estados variables que puedan derivarse;
- distingue norma, implementación, evidencia e historia;
- enlaza el catálogo `K01`–`K24`;
- declara comandos reproducibles;
- trata los gates anteriores como evidencia histórica, no como manual operativo.

No se reescriben ni se fusionan los gates, dictámenes, manifiestos o resoluciones
históricas. Su posible contradicción se resuelve en la guía mediante autoridad,
vigencia y remisión, no modificando la historia.

## 9. PesquerApp

Si `F6` queda certificada y cerrada, desaparece exclusivamente el bloqueo técnico
que dependía de completar y certificar `F6`.

PesquerApp queda entonces:

`HABILITADA TÉCNICAMENTE · NO AUTORIZADA · NO INICIADA`

Su adopción, piloto, integración o ejecución necesita una orden posterior y
separada del Owner. Este ciclo no puede iniciarla.

Si `F6` no queda certificada, PesquerApp continúa BLOQUEADA.

## 10. Fin de la recursión

Este es el último ciclo automático de corrección y certificación de `F6`.

Después del dictamen del verificador:

- se registra y publica el resultado;
- no se corrige la candidata en respuesta al dictamen;
- no se abre otro gate;
- no se propone otra tanda automática;
- no se inicia PesquerApp;
- se para cualquiera que sea el resultado.

---

# `O31` · INTERVENCIÓN HUMANA FINAL SOBRE LOS CUATRO CONTROLES PENDIENTES DE `F6`

**Fecha:** 2026-09-07  
**Autoridad:** Owner

## 1. Naturaleza de esta intervención

La parada ordenada por `O30` §10 se cumplió.

Esta resolución no reabre aquella recursión automática. Constituye la decisión humana
posterior que `O30` dejó expresamente fuera de su ciclo.

Se autoriza una única intervención incremental, con alcance cerrado, sobre:

- `V-G1`;
- `V-G2`;
- la condición incumplida de `M-04`;
- la condición incumplida de `C-L.7`.

No se autoriza otra auditoría general de `F6`, otra reclasificación de su universo ni
otra expansión automática de hallazgos.

## 2. Hechos conservados de `O30`

Para esta intervención se conservan como hechos que deben reproducirse, pero no volver
a rediseñarse:

1. `K01`–`K24` satisfechas;
2. las obligaciones internas de `F6` completas;
3. las ocho condiciones de `O26` satisfechas;
4. la candidata de `O30` identificada por commit y tree;
5. PesquerApp no iniciada;
6. los hallazgos menores registrados y no declarados superados.

La verificación incremental debe comprobar que estos hechos no sufren regresión.

No necesita reconstruir la historia completa de gates anteriores.

## 3. Cierre de `V-G1`

El universo de instrumentos y evidencias no puede derivarse únicamente de:

`kernel/operativo/validadores/*.py`

Debe derivarse de todas las filas vivas que declaren un instrumento ejecutable o
`tipo: validador`, cualquiera que sea su directorio.

Para cada fila deben quedar contrastados:

- identificador;
- ejecutable;
- directorio de trabajo;
- argumentos;
- evidencia;
- condición de éxito;
- inclusión en el runner;
- inclusión en el guardián de evidencia.

Añadir, mover u omitir un instrumento debe producir rojo por su ausencia material, no
por una lista manual de rutas.

Todo instrumento que sostenga una condición de certificación debe estar protegido por
`T350` o por un guardián mecánicamente equivalente.

## 4. Cierre de `V-G2`

Toda dispensa reflexiva debe quedar ligada a la invocación declarada completa:

- obligación;
- identificador de fila;
- script;
- directorio de trabajo;
- argumentos normalizados;
- evidencia;
- condición de cierre.

Una dispensa concedida al script suelto es transferible y no es válida.

Deben fallar, como mínimo:

1. cambiar `--obligaciones` por `--help`;
2. conservar el script y cambiar sus argumentos;
3. conservar los argumentos y cambiar el directorio;
4. fabricar una segunda fila que intente reutilizar la dispensa;
5. duplicar la dispensa para otra obligación;
6. invocar una ruta equivalente pero no idéntica a la declarada.

La fila legítima debe seguir funcionando y la dispensa debe ser única.

## 5. Cierre de `M-04`

El universo esperado de instrumentos no puede depender exclusivamente del manifiesto
cuya completitud se está juzgando.

Debe existir una derivación independiente desde las sedes vivas del árbol.

El siguiente ataque debe producir rojo:

1. retirar del manifiesto el instrumento de `K01`–`K24`;
2. retirar también su evidencia;
3. regenerar huella y sello;
4. ejecutar la batería completa.

La ausencia debe ser detectada por el universo independiente.

No se considera cerrado `M-04` mediante una etiqueta. Su condición se acreditará
únicamente si el verificador independiente reproduce este ataque y el árbol falla
cerrado por el motivo correcto.

## 6. Cierre de `C-L.7`

El control debe juzgar la clase:

> copia manual de estado, cardinal o conjunto variable dentro de una sede viva que
> debería derivarlo o remitir a su fuente competente.

No puede depender de una lista cerrada de sustantivos como “hallazgos”, “invariantes”,
“obligaciones” o “sabotajes”.

Debe reconocer, al menos:

- cifras escritas con dígitos;
- cifras escritas con palabras;
- mayúsculas y minúsculas;
- singular y plural;
- puntuación diferente;
- sustantivos desconocidos;
- cardinales introducidos después de escribir el control.

Debe distinguirlos de:

- fechas;
- versiones;
- identificadores normativos;
- SHA y digests;
- citas históricas rotuladas;
- límites contractuales realmente constantes;
- salidas generadas;
- comandos que derivan el valor.

Preferentemente, las sedes vivas no copiarán el cardinal: remitirán a la fuente o
publicarán el comando que lo deriva.

`C-L.7` sólo podrá cerrarse cuando el verificador independiente demuestre la clase con
variantes que el implementador no utilizó para construir el control.

## 7. Verificación por composición

Después de congelar la candidata se creará un único verificador independiente nuevo.

Debe leer íntegramente:

- todos los ficheros modificados desde la candidata de `O30`;
- todos los ficheros modificados por `O30` que sostengan `K01`–`K24`, obligaciones,
  `O26`, `M-04`, `C-L.7`, V-G1 o V-G2;
- O30 y O31;
- los registros finales de O30;
- la guía canónica vigente.

La resta:

`FICHEROS MODIFICADOS O30+O31 − FICHEROS LEÍDOS ÍNTEGRAMENTE`

debe quedar vacía.

La certificación por composición procede si:

1. `V-G1` queda cerrada;
2. `V-G2` queda cerrada;
3. `M-04` queda superada;
4. `C-L.7` queda cerrada;
5. `K01`–`K24` continúan satisfechas;
6. las obligaciones internas continúan completas;
7. las ocho condiciones de `O26` continúan satisfechas;
8. no existe una regresión BLOQUEANTE o GRAVE introducida por el delta;
9. commit, tree, evidencia y sobre corresponden al mismo objeto.

Los hallazgos menores anteriores permanecen registrados. No bloquean salvo que falseen
una de las nueve condiciones anteriores.

## 8. Resultado competente

Si las nueve condiciones de §7 se satisfacen, el verificador independiente queda
autorizado a emitir:

- `V-G1 CERRADA`;
- `V-G2 CERRADA`;
- `M-04 SUPERADA`;
- `C-L.7 CERRADA`;
- `F6 CERTIFICADA POR COMPOSICIÓN`;
- `F6 CERRADA`.

En ese caso, PesquerApp queda:

`HABILITADA TÉCNICAMENTE · NO AUTORIZADA · NO INICIADA`

La creación del repositorio ADS definitivo de PesquerApp necesitará una orden posterior
y separada del Owner.

No habrá repositorio piloto ni copia temporal. Cuando se autorice, se creará
directamente el repositorio global ADS definitivo de PesquerApp como instancia
reproducible del ADS genérico.

Si posteriormente se descubre un defecto estructural del sistema ADS:

1. se corregirá en el repositorio genérico;
2. no se convertirá la instancia de PesquerApp en un fork divergente;
3. el repositorio ADS de PesquerApp podrá eliminarse y recrearse desde el genérico,
   preservando previamente cualquier información propia que no sea regenerable;
4. los repositorios reales de producto seguirán siendo independientes.

## 9. Fallo de la composición

Si cualquiera de las nueve condiciones de §7 falla:

- `F6` continúa no certificada y abierta;
- PesquerApp continúa bloqueada;
- se registra la causa material;
- no se corrige en respuesta al dictamen;
- no se abre otro gate;
- no se inicia otro ciclo automático.

La decisión posterior será estrictamente humana: aceptar el riesgo, intervenir
manualmente o detener el desarrollo del sistema.

## 10. Parada definitiva

Esta intervención permite:

- una implementación;
- una comprobación adversarial previa de alcance cerrado;
- una única pasada de corrección;
- una candidata;
- un sobre;
- un verificador independiente;
- un resultado.

Después del resultado se publica y se para.
