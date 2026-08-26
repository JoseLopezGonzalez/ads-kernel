# Escenarios completos del circuito de entrada


Recorridos íntegros, con lo que el sistema **hace**, lo que **escribe** y lo que **decide
no hacer**. No son ilustraciones: son las pruebas T75 a T84, y su estado real está en
[`../pruebas/REGISTRO-generado.md`](../pruebas/REGISTRO-generado.md).

---

## ESCENARIO A — «Esta pantalla funciona, pero se ve básica, plana y sin alma»

El escenario de referencia. **El sistema no puede traducirlo como «cambiar CSS».**

### Paso 2 · Captura literal

```yaml
expresion_literal:
  - fecha: "2026-08-25T10:12"
    texto: "Esta pantalla funciona, pero se ve básica, plana y sin alma."
    canal: "chat"
```

Los tres adjetivos **son el dato**, no ruido a limpiar. `básica` sugiere ausencia de
intención; `plana`, ausencia de jerarquía o profundidad; `sin alma`, ausencia de carácter.
Tres cosas distintas, y ninguna es una instrucción técnica.

### Paso 3 · Interpretación inicial, con confianza declarada

> *Interpretación provisional:* la superficie cumple su función pero no transmite ninguna
> dirección visual reconocible. Confianza: **baja** — no sé a qué pantalla se refiere, ni
> cuál de los tres adjetivos pesa más, ni si alguna vez se aprobó una dirección para ella.

### Paso 4 · Anclaje — lo que se busca antes de responder nada

```text
BÚSQUEDA 1  ¿cuál es «esta pantalla»?
            → última superficie que el Owner tocó o mencionó, y la que esté abierta
              en el trabajo en curso. Si hay dos candidatas por encima del margen,
              se desambigua por nombre humano.
BÚSQUEDA 2  ¿existe una dirección visual aprobada para esa superficie?
            → memoria de diseño: visión artística, personalidad, principios, patrones
              con alcance que la cubra.
BÚSQUEDA 3  ¿existe un patrón vigente que esa pantalla incumple?
BÚSQUEDA 4  ¿hay items abiertos sobre esa superficie? incluidos aparcados
BÚSQUEDA 5  ¿se dio por hecho un sistema de diseño que no existe?
            ← el hallazgo más probable, y el más incómodo
```

**Resultado del anclaje en el caso típico:**

```yaml
anclaje:
  ya_implementado:
    - "src/paginas/entradas/ListaEntradas.tsx — construida en FEA-009, sin paquete de DIS en su ruta"
  decisiones_que_gobiernan:
    - "ninguna: la ruta de FEA-009 declaró «DIS no activada — sin superficie nueva», y era falso"
  aprendizajes: []
  duplica: []
  no_existe_y_se_creia:
    - "NO existe memoria de diseño del proyecto: no hay visión artística, ni personalidad,
       ni principios visuales escritos. Se ha construido sin dirección aprobada."
```

> Este hallazgo cambia el problema entero. No es que la pantalla esté mal: es que **nunca
> hubo dirección** que cumplir. Sin el anclaje, el sistema habría producido un parche.

### Paso 5 · Incertidumbre

```text
resultado perseguido    ALTA   no puede escribirse: «que tenga alma» no es comprobable
problema observado      MEDIA  hay superficie identificada, no hay caso de uso concreto
alcance                 ALTA   ¿esta pantalla, o todo el producto?
restricciones           MEDIA  se desconoce si el Owner acepta cambiar la base visual
criterio de terminado   ALTA   no puede escribirse evidencia de cierre

GRADO GLOBAL = ALTA   →  PROHIBIDO FORMULAR. Se conversa. Crítica obligatoria después.
```

### Paso 6 · La conversación — enseñar, no interrogar

Se aplica `forma:comentario-subjetivo`. Tres movimientos, en este orden:

**1. Llevarlo a lo concreto.**

> «Cuando dices que se ve plana, ¿qué es lo primero que te chirría al entrar? ¿Y estabas
> mirando algo en concreto o pasando de largo?»

*Respuesta captada literalmente:* «Todo tiene el mismo peso. Entro y no sé dónde mirar
primero. Y parece una tabla de Excel con bordes.»

Esto reclasifica el problema: **jerarquía visual ausente**, no «falta de estilo». Se
escribe en el checkpoint tal como lo dijo.

**2. Enseñarle, con consulta a DIS en modo consulta.**

ENC no interpreta materia de diseño. Pide a DIS **tres referencias con el principio
extraído de cada una**, no tres capturas bonitas:

```text
REFERENCIA A   panel de operaciones de una herramienta de logística
               PRINCIPIO: una sola línea de datos domina la fila; el resto se atenúa
               hasta que se necesita. La jerarquía la crea el CONTRASTE DE PESO, no el color.
REFERENCIA B   aplicación financiera de escritorio
               PRINCIPIO: la densidad alta se hace legible con ritmo vertical constante
               y una única familia tipográfica en tres pesos.
REFERENCIA C   producto editorial
               PRINCIPIO: el carácter viene de una decisión tipográfica arriesgada
               sostenida en todo el producto, no de adornos en cada pantalla.
```

*Reacción captada:* «La A es lo que necesito. La C me gusta pero no pega con esto. La B es
lo que tenemos y por eso me aburre.»

**Eso es información de altísimo valor** y se conserva literal: descarta B (lo actual),
aprueba el principio de A, y sitúa C como aspiración fuera de alcance.

**3. Acotar.**

> «¿Esto lo quieres para esta pantalla o para todo el producto? Te lo pregunto porque
> cambia mucho el trabajo: una pantalla es un ajuste; todo el producto es decidir una
> dirección visual que hoy no existe.»

*Respuesta:* «Para todo. Pero empecemos por ésta, que es la que uso.»

### Paso 7 · Formulación — y aquí se ve por qué no era «cambiar CSS»

La conversación ha destapado **dos cosas distintas**, y se separan en **dos encuadres**:

```yaml ads:encuadre
id: ENC-001
expresion_literal:
  - fecha: "2026-08-25T10:12"
    texto: "Esta pantalla funciona, pero se ve básica, plana y sin alma."
    canal: "chat"
  - fecha: "2026-08-25T10:31"
    texto: "Todo tiene el mismo peso. Entro y no sé dónde mirar primero. Y parece una tabla de Excel con bordes."
    canal: "chat"
  - fecha: "2026-08-25T10:44"
    texto: "Para todo. Pero empecemos por ésta, que es la que uso."
    canal: "chat"
interpretacion: >
  El producto no tiene dirección visual aprobada. Se ha construido resolviendo cada
  pantalla por separado, y el resultado es funcional y sin carácter. El Owner ha
  reconocido el principio de jerarquía por contraste de peso y ha descartado
  expresamente la densidad uniforme actual.
resultado_perseguido: >
  Existe una dirección visual aprobada del producto —personalidad, principios,
  tipografía, color, jerarquía y densidad— aplicada y validada en al menos una superficie
  representativa.
problema_observado: >
  En la lista de entradas todos los elementos tienen el mismo peso visual; el Owner entra
  y no sabe dónde mirar primero. El anclaje confirma que no existe memoria de diseño.
motivo: >
  Es la pantalla que el Owner usa a diario, y la falta de jerarquía le cuesta tiempo en
  cada uso. Además, cada pantalla nueva que se construya sin dirección aumenta la deuda.
situacion_actual: >
  Cero documentos de dirección visual. FEA-009 construyó la lista sin activar DIS,
  declarando en su traza que no había superficie nueva.
expectativas:
  - "una sola línea de datos domina cada fila; el resto se atenúa hasta que se necesita"
  - "la jerarquía se crea por contraste de peso, no por color"
  - "el resultado no se parece a una tabla de hoja de cálculo con bordes"
restricciones:
  - "la densidad de información no puede reducirse: el Owner necesita ver muchas filas"
  - "no se truncan los nombres de lote"
referencias:
  - "referencia A presentada el 2026-08-25, principio: jerarquía por contraste de peso"
  - "referencia C presentada y descartada para esta fase: fuera de alcance"
decisiones_previas:
  - "ninguna vigente: es la primera dirección visual del producto"
suposiciones:
  - "el Owner acepta que la primera superficie tratada sea la lista de entradas"
dudas_abiertas:
  - "si la dirección debe cubrir también las superficies de impresión y exportación"
evidencia_de_cierre:
  - "existe memoria de diseño con visión, personalidad, principios, tipografía, color y densidad"
  - "la lista de entradas aplica la dirección y el Owner la reconoce como suya"
  - "la crítica visual independiente emite dictamen conforme sobre esa superficie"
incertidumbre:
  grado: media
  grado_inicial: media
  ejes: ["resultado perseguido: baja", "problema: baja", "alcance: media", "restricciones: baja", "criterio de terminado: media"]
  motivo: >
    El alcance sigue en media porque «para todo el producto, empezando por ésta» deja
    abierto cuántas superficies entran en esta primera dirección.
nivel_owner: obligatorio
vinculos:
  - "FEA-009 — construyó la superficie sin activar DIS"
  - "ENC-002 — el gap de la superficie concreta, enlazado a este encuadre"
anclaje:
  ya_implementado:
    - "src/paginas/entradas/ListaEntradas.tsx"
  decisiones_que_gobiernan: []
  aprendizajes: []
  duplica: []
  no_existe_y_se_creia:
    - "no existe memoria de diseño del proyecto"
clasificacion:
  naturaleza: entrada:candidato
  tipo_propuesto: FEA
  motivo: >
    El resultado perseguido es que EXISTA una dirección visual del producto, que hoy no
    existe. Es capacidad nueva del sistema de diseño, no reparación de una superficie.
estado: listo-para-dsp
estado_paquete: listo
```

Y el segundo, enlazado:

```text
ENC-002   tipo GAP
resultado perseguido:  la lista de entradas alcanza la dirección visual aprobada
depende de:            ENC-001 — no puede cerrar antes de que exista la dirección
evidencia de cierre:   el Owner entra y sabe dónde mirar primero, sin haber perdido
                       densidad ni truncado nombres de lote
```

### Paso 8 · Crítica independiente

Obligatoria: la incertidumbre fue alta y el nivel de Owner es obligatorio. Un agente
distinto lee **primero la literal** y dictamina.

```text
VEREDICTO: conforme, con dos huecos menores

HUECO 1   «una superficie representativa» no dice cuál.
          QUÉ LO CIERRA: nombrarla en el encuadre — la lista de entradas.
HUECO 2   la restricción «no se truncan los nombres de lote» sale de una conversación
          anterior y no está en la literal de hoy.
          QUÉ LO CIERRA: enlazar la decisión de origen o preguntarlo.
```

Ambos se cierran sin volver a molestar al Owner: el primero por escritura, el segundo
localizando la decisión anterior en la memoria de diseño.

### Paso 9 · Confirmación

**Sí se pide**, y por una razón de la tabla: *primera instancia de un patrón visual* y
*primera dirección de producto*. Se le devuelve el encuadre en prosa, no en YAML:

> «He entendido esto: el producto no tiene todavía una dirección visual decidida, y por eso
> cada pantalla se resuelve sola. Lo que propongo es decidir esa dirección —cómo quieres
> que se vea y se sienta el producto— y aplicarla primero a la lista de entradas, que es la
> que usas. Mantengo tus dos condiciones: no perder densidad y no truncar los nombres de
> lote. ¿Lo he entendido bien?»

### Pasos 10-13 · DSP

```text
ENC-001 → FEA-014 «Dirección visual del producto»
          propietario global: PRD   (el resultado define alcance de producto)
          ruta r1:  PRD → DIS/Fundacion → [ARQ si C-ARQ] → CON → VER → ENT → USO → APR
          no activadas:
            DOM — no toca modelo de dominio ni contratos de datos
            SEG — no toca autenticación, datos personales, red ni dependencias

ENC-002 → GAP-015 «La lista de entradas alcanza la dirección aprobada»
          propietario global: PRD
          dependencia: requiere FEA-014
          estado inicial: esperando-dependencia
```

### Paso 14 · Respuesta al Owner

> «Ya está en marcha. Dos cosas, no una:
>
> **Una dirección visual para el producto** — porque al mirarlo he visto que nunca se
> decidió ninguna, y por eso cada pantalla se ha resuelto por su cuenta. Diseño va a
> trabajar en esto contigo; te van a enseñar direcciones antes de elegir.
>
> **La lista de entradas** — queda enganchada a lo anterior: se rehace cuando la dirección
> esté decidida, con tus dos condiciones intactas.
>
> **No he creado** ninguna tarea de retoque rápido. Cambiar colores y sombras ahora
> tapa el problema y te costaría el doble después.»

### Las CUATRO salidas de esta frase, y por qué ésta produjo dos items

> **«Se ve básica, plana y sin alma» no produce universalmente dos items.** El recorrido de
> arriba terminó en dos porque el **anclaje** encontró que no existía dirección de diseño.
> Con otro anclaje, la misma frase termina en otro sitio, y el sistema no puede tener una
> respuesta memorizada para ella.

```text
EXISTE dirección aprobada y la interfaz la INCUMPLE
   → un GAP. La expectativa está escrita y la superficie no llega a ella.
     No hace falta decidir nada nuevo: hay que cerrar la distancia.
     PRUEBA T154

NO EXISTE dirección de diseño
   → dirección visual (FEA o el proceso que el resultado perseguido determine)
     MÁS un GAP enlazado para la superficie concreta. Son dos porque son dos
     resultados distintos: que exista la dirección, y que esta pantalla la alcance.
     Es el recorrido de arriba. PRUEBA T155

EL OWNER QUIERE SUSTITUIR una dirección vigente
   → posible DIR, y de él nacen los items derivados. DIR decide; no implementa.
     PRUEBA T156

LA INTENCIÓN SIGUE SIENDO AMBIGUA
   → conversación y checkpoint. NINGÚN item todavía, y eso es un resultado
     correcto: crear uno aquí es fabricar trabajo sobre una intención que no se
     ha entendido. PRUEBA T157
```

**Lo que decide cuál de las cuatro es el paso 4**, no el paso 2. Por eso el anclaje va
antes de formular, y por eso `ENC/anclaje` puede ser un agente distinto del interlocutor:
la respuesta a «¿existe dirección aprobada para esta superficie?» no se intuye leyendo la
frase del Owner.

### Lo que este escenario demuestra

```text
[ ] la queja subjetiva NO se tradujo a una tarea técnica
[ ] el anclaje encontró lo que no existía y eso cambió el problema entero
[ ] las referencias se usaron para investigar y conversar, no para copiar
[ ] la reacción del Owner a cada referencia se conserva literal
[ ] una expresión produjo DOS items, uno de ellos dependiente del otro
[ ] se dijo expresamente qué NO se creó y por qué
```

```yaml ads:escenario
id: T75
nombre: El comentario subjetivo no se traduce a tarea técnica
cubre: ["paso 1.6", "forma:comentario-subjetivo", "gate:encuadre-listo", "gate:anclaje-completo"]
dado:
  - "un proyecto con una superficie construida y sin memoria de diseño"
  - "el Owner escribe «Esta pantalla funciona, pero se ve básica, plana y sin alma»"
cuando:
  - "ENC ejecuta ENC/Escucha completo"
entonces:
  - "la literal se conserva con sus tres adjetivos y su fecha"
  - "el anclaje declara que no existe memoria de diseño"
  - "la incertidumbre se declara alta y NO se formula antes de conversar"
  - "se presentan al menos dos referencias con su principio extraído"
  - "la reacción del Owner a cada referencia queda captada literalmente"
  - "se produce un encuadre de dirección visual y otro dependiente para la superficie"
  - "la respuesta al Owner declara qué no se creó"
falla_si:
  - "se crea un item cuyo resultado perseguido sea cambiar estilos, colores o CSS"
  - "se formula el encuadre con incertidumbre alta sin conversar"
  - "el anclaje omite comprobar si existe dirección visual aprobada"
  - "las referencias se presentan sin principio extraído"
  - "la respuesta al Owner no dice qué se decidió no hacer"
ejecucion: requiere-juicio-humano
estado: contrato-definido
```

---

## ESCENARIO B — «eso que te dije de los lotes, ¿cómo va?»

Deíctico sin antecedente. `forma:referencia-anterior`.

```text
1  CAPTURA     literal con fecha
2  RESOLVER    puntuación contra el índice de lo existente:
                 GAP-014 «Trazabilidad de lotes en salidas»   0.85
                   +0.40 resultado coincide · +0.25 materia · +0.10 término del léxico
                   +0.10 último tocado por el Owner en esa materia
                 FEA-008 «Etiquetas de lote en impresión»     0.35
               p(1)=0.85 >= 0.60 · p(1)-p(2)=0.50 >= 0.15 · intención CONSULTAR, reversible
               → SE RESUELVE SIN PREGUNTAR
3  RESPONDER   estado real, en lenguaje natural, sin identificadores:
               «Lo de la trazabilidad de lotes está aparcado desde el 19 de agosto, por
                decisión tuya, para centrar la atención en la pantalla de entradas. Estaba
                en Diseño, en la segunda dirección. Sigue justo donde lo dejaste.»
4  NO HACE     no desaparca · no propone desaparcar · no lo insinúa
```

```yaml ads:escenario
id: T76
nombre: Deíctico resuelto sin preguntar y sin desaparcar
cubre: ["forma:referencia-anterior", "b.13 desambiguación", "a.2 aparcado"]
dado:
  - "existe un item aparcado por el Owner y otro item de materia próxima"
  - "el Owner escribe «eso que te dije de los lotes, ¿cómo va?»"
cuando:
  - "ENC ejecuta la forma de referencia anterior"
entonces:
  - "el antecedente se resuelve por puntuación sin preguntar al Owner"
  - "la respuesta usa el nombre humano del item, nunca su identificador"
  - "la respuesta incluye el motivo de aparcado, con las palabras del Owner"
falla_si:
  - "se pregunta «¿a qué te refieres?» habiendo un candidato por encima del umbral y del margen"
  - "se propone desaparcar, o se sugiere que lleva mucho tiempo parado"
  - "aparece un identificador en la respuesta"
ejecucion: guion-manual
estado: contrato-definido
```

---

## ESCENARIO C — la interrupción y el relevo de agente

`forma:interrupcion`. Es la prueba de que el checkpoint sirve para algo.

```text
DÍA 1   la conversación del escenario A se corta después del paso 6.2 —referencias
        mostradas y reaccionadas— y antes del paso 7.
        El checkpoint escrito contiene:
          resuelto: referencia A aprobada · B descartada como «lo que tenemos» ·
                    C fuera de alcance
          owner_captado: «Todo tiene el mismo peso. Entro y no sé dónde mirar primero.»
          pregunta_pendiente: ¿esto es para esta pantalla o para todo el producto?
          siguiente: formular ENC-001 en cuanto responda al alcance
          based_on: memoria de diseño (inexistente) · índice de lo existente@2026-08-25

DÍA 3   el Owner escribe: «para todo, pero empecemos por ésta»
        Agente NUEVO, que no vio nada de la conversación:
          1 carga el checkpoint del encuadre abierto
          2 comprueba based_on: el índice cambió — se revalida SÓLO la parte afectada
            (¿apareció memoria de diseño en dos días? no)
          3 reconoce que el mensaje responde a pregunta_pendiente
          4 NO vuelve a mostrar las referencias: están con su reacción
          5 continúa en el paso 7, formulando
          6 recuerda en UNA línea lo entendido, sin pedir que se repita nada
```

```yaml ads:escenario
id: T77
nombre: Relevo de agente a mitad de conversación sin pedir resumen al Owner
cubre: ["forma:interrupcion", "a.10 checkpoint", "ENC/Escucha", "T01"]
dado:
  - "un encuadre en curso con checkpoint escrito tras mostrar referencias"
  - "un agente nuevo sin acceso a la conversación anterior"
cuando:
  - "el Owner responde a la pregunta pendiente dos días después"
entonces:
  - "el agente nuevo carga el checkpoint y comprueba based_on"
  - "continúa en el paso exacto sin repetir referencias ya reaccionadas"
  - "no pide al Owner que repita ni resuma nada"
falla_si:
  - "se vuelven a presentar referencias ya mostradas"
  - "se pide al Owner que recuerde de qué se hablaba"
  - "se reinicia el método desde el paso 1"
ejecucion: guion-manual
estado: contrato-definido
```

---

## ESCENARIO D — la orden que llega tarde

Prueba del conflicto de base vigente de a.9, en la puerta de entrada.

```text
1  el Owner escribe «pon lo del stock como urgente»
2  ENC ancla: GAP-021 «Cuadre de stock por almacén», p=0.78, unívoco
3  ENC emite el evento con base = revisión r7 del estado
4  ENTRE la emisión y la aplicación, DSP consume otra orden que cerró GAP-021
5  la base r7 ya no es vigente
   → la orden NO se aplica y NO se borra
   → se marca en conflicto, con las DOS intenciones escritas:
       «pediste marcar urgente el cuadre de stock (r7); entre medias quedó cerrado (r8).
        ¿Lo reabro como item nuevo, o lo dejamos así?»
6  la respuesta del Owner es una expresión nueva y entra por el circuito completo
```

```yaml ads:escenario
id: T78
nombre: Orden emitida sobre base que dejó de ser vigente
cubre: ["ENC/Orden", "gate:orden-emitida", "a.9 protocolo de órdenes", "T24"]
dado:
  - "una orden del Owner emitida sobre una revisión concreta del estado"
  - "el estado cambia entre la emisión y la aplicación"
cuando:
  - "DSP intenta aplicar el evento"
entonces:
  - "la orden no se aplica ni se borra"
  - "queda marcada en conflicto con ambas intenciones escritas"
  - "el Owner recibe las dos y decide"
falla_si:
  - "la orden se aplica sobre una base caducada"
  - "la orden se descarta silenciosamente"
  - "se pierde la atribución de autoridad al Owner"
ejecucion: requiere-runtime
estado: contrato-definido
```

---

## ESCENARIO E — la expresión que NO produce nada

El más importante para el modo de fallo (b): el sistema que fabrica trabajo para parecer útil.

```text
Owner:  «qué manía tienen todos con los dashboards, ¿eh?»

1  CAPTURA     literal con fecha
2  CLASIFICAR  no es petición, no es observación comprobable, no es orden, no es decisión.
               Es comentario sin objetivo en el producto.
3  ANCLAR      no procede: no hay objetivo que anclar
4  RESULTADO   ninguna clase de la taxonomía la reclama como trabajo.
               Se anota en el léxico del Owner que reacciona con reserva ante los
               cuadros de mando, por si en el futuro se propone uno.
5  RESPUESTA   se conversa como se conversa, sin crear nada y sin prometer nada.

NO SE CREA     ni item, ni ficha de vivero, ni tarea de investigación sobre dashboards.
```

```yaml ads:escenario
id: T79
nombre: Un comentario sin objetivo no genera ningún artefacto de trabajo
cubre: ["01-TAXONOMIA", "a.7 modo de fallo (b)", "b.15 regla dura"]
dado:
  - "el Owner hace un comentario que no apunta a nada del producto"
cuando:
  - "ENC ejecuta ENC/Escucha"
entonces:
  - "no se crea item, ni ficha de vivero, ni paquete"
  - "a lo sumo se anota una preferencia en el léxico del Owner"
falla_si:
  - "se crea cualquier unidad de trabajo"
  - "se propone una investigación no pedida"
  - "se abre una ficha de vivero para «no perder la idea»"
ejecucion: guion-manual
estado: contrato-definido
```

---

## ESCENARIO F — el duplicado que el Owner no sabía que existía

```text
Owner:  «necesito poder buscar los pedidos por referencia del proveedor»

4  ANCLAR   búsqueda con tres términos: «referencia proveedor» (Owner),
            «supplier_ref» (código), «referencia externa» (dominio)
            → encuentra GAP-014, APARCADO desde hace tres semanas, persigue exactamente
              ese resultado, con dos capas ya depositadas

DECISIÓN     no se crea item nuevo. Se propone como ORDEN sobre el existente.

RESPUESTA    «Esto ya lo tenemos empezado: lo llamamos "búsqueda por referencia de
              proveedor" y lo aparcaste tú el 4 de agosto para centrarte en las entradas.
              Diseño ya dejó hecha la parte de cómo se muestra. ¿Lo retomamos?»

CLAVE        se pregunta si lo retoma. NO se desaparca solo: aparcar y desaparcar son las
             dos únicas transiciones exclusivas del Owner.
```

```yaml ads:escenario
id: T80
nombre: Duplicado con item aparcado se convierte en propuesta de retomar
cubre: ["ENC/Anclaje", "gate:anclaje-completo", "a.2 aparcado", "T10"]
dado:
  - "existe un item aparcado que persigue el mismo resultado que la nueva expresión"
cuando:
  - "ENC ancla la expresión comparando contra todos los items abiertos"
entonces:
  - "no se crea item nuevo"
  - "se propone al Owner retomar el existente, con su nombre humano y su motivo de aparcado"
  - "el sistema no desaparca por su cuenta"
falla_si:
  - "se crea un item duplicado"
  - "el sistema desaparca sin orden del Owner"
  - "la comparación se limitó a los items activos"
ejecucion: guion-manual
estado: contrato-definido
```

---

## Las cuatro salidas de la expresión subjetiva, como pruebas

```yaml ads:escenario
id: T154
nombre: Con dirección aprobada incumplida, la expresión subjetiva produce un GAP
cubre: ["forma:comentario-subjetivo", "ENC/Anclaje", "b.16 GAP", "9.4"]
dado:
  - "existe memoria de diseño con una dirección aprobada que cubre esta superficie"
  - "la superficie no cumple uno de sus patrones vigentes"
cuando: ["el Owner dice que se ve básica, plana y sin alma"]
entonces:
  - "el anclaje encuentra la dirección aprobada y el patrón incumplido"
  - "nace UN item de tipo GAP, con la distancia medida contra el patrón"
  - "NO se propone una dirección nueva: ya existe y no se discute"
falla_si:
  - "se abre una exploración de dirección teniendo una aprobada y vigente"
  - "nacen dos items donde el resultado perseguido es uno"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T155
nombre: Sin dirección de diseño, la expresión produce dirección más GAP enlazado
cubre: ["forma:comentario-subjetivo", "ENC/Anclaje", "03-ESCALA-DE-NOVEDAD N4 y N3", "9.4"]
dado: ["el anclaje devuelve que NO existe memoria de diseño del producto"]
cuando: ["el Owner dice que se ve básica, plana y sin alma"]
entonces:
  - "nacen DOS items enlazados: que exista la dirección, y que esta superficie la alcance"
  - "el segundo declara depender del primero y no puede cerrar antes"
  - "el nivel de novedad se calcula con las cinco variables, y sale N4 o N3 según haya superficie construida que preservar"
falla_si:
  - "nace un solo item que mezcla fundar la dirección con arreglar la pantalla"
  - "el nivel se elige en vez de calcularse"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T156
nombre: Con dirección vigente que el Owner quiere sustituir, la salida es un DIR
cubre: ["forma:cambio-de-direccion", "b.16 DIR", "G51", "9.4"]
dado: ["existe una dirección visual vigente y aprobada por el Owner"]
cuando: ["el Owner expresa que quiere que el producto se parezca a otra cosa"]
entonces:
  - "el proceso propuesto es DIR, no GAP ni FEA"
  - "el propietario global es la capacidad propietaria de la decisión que se sustituye, y NUNCA lo elige DSP"
  - "DIR decide y registra; la ejecución va en items derivados enlazados"
falla_si:
  - "se trata como un GAP y se pierde el registro de qué decisión queda sustituida"
  - "se implementa la nueva dirección dentro del propio DIR"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T157
nombre: Con la intención todavía ambigua, la expresión NO produce ningún item
cubre: ["forma:comentario-subjetivo", "04-INCERTIDUMBRE", "a.7 modo de fallo (b)", "9.4"]
dado:
  - "el Owner no puede señalar qué le chirría ni en qué superficie"
  - "la incertidumbre en el eje del resultado perseguido sigue alta tras conversar"
cuando: ["se agota ENC/Maduracion sin bajar el grado"]
entonces:
  - "NO nace ningún item"
  - "la expresión queda en el vivero, o se escala al Owner con las dudas abiertas escritas"
  - "el checkpoint conserva lo comprendido, de modo que retomarlo no empieza de cero"
falla_si:
  - "nace un item sobre una intención que nadie ha entendido"
  - "el sistema fabrica una tarea de estilos para tener algo que hacer"
ejecucion: guion-manual
estado: contrato-definido
```
