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
