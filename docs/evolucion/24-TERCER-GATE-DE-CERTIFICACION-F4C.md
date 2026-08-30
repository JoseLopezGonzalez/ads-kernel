# TERCER GATE DE CERTIFICACIÓN DE F4c — EL SOBRE DE ANCLA, PUESTO A PRUEBA

> **Veredicto del adjudicador `X`: `INSUFICIENTE PARA F5`. El gate es VÁLIDO.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha
> corregido en esta pasada, y es deliberado.**
>
> **Y lo que hace distinto a este gate:** es el primero que estrena el **SOBRE DE ANCLA** que
> `O18` adoptó, y el primero que puede decir, con la medida delante, **qué parte de la
> circularidad se cerró y qué parte sólo se movió de sitio**.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes de un gate independiente sobre la candidata
`21f1ccbda82e7a3ad5e3b3ecf3c7b1bfe374a1d5`, publicada en `review/f4c-o18-candidate-20260830`.
Los tres se transcriben **enteros y sin suavizar**, en §A, §B y §C. Lo escrito antes de §A lo
escribe el **coordinador**, que no es ninguno de los ocho y que **no ha juzgado nada**.

## 1 · Los agentes

```text
REVISOR V      cadena `V1`·`V2`·`V3`·`V4`, contexto limpio, tramos DISJUNTOS
               V1  documento 11, L1-L5600, y §9 entera
               V2  documento 11, L5601-final · `O18` verificada regla a regla
               V3  registro de decisiones · CHECKPOINT · índice
               V4  documento 23 AL FINAL — DICTAMINADOR. Rechazó dos hallazgos de sus
                   relevos, rebajó cinco y elevó uno

REVISOR W      cadena `W1`·`W2`·`W3`, contexto limpio, tramos DISJUNTOS
               W1  la batería y su README — el ataque a `M-04`
               W2  el emisor del sobre · el derivador · los tres manifiestos · el corrigendum
               W3  documento 23 AL FINAL — DICTAMINADOR. Rechazó dos, fusionó uno y se negó
                   a adjudicar dos por ser clase `C` contratada para `F6`

ADJUDICADOR X  recibió los dos dictámenes YA CERRADOS. Recalculó universo, asignaciones,
               lecturas, cobertura, severidades, recuentos y condiciones de cierre.
               Resolvió contra la FUENTE, nunca por mayoría. **Reprodujo cuatro árboles
               defectuosos de `W` y añadió DOS que nadie había abierto**

INDEPENDENCIA  ninguno de los ocho ha escrito F4, aplicado `D16`-`D108`, sido autor de
               ninguna corrección ni sido revisor en ningún gate anterior. `V` y `W` en
               paralelo y sin verse; `X` sin ver nada hasta que los dos cerraron

DOS INTERRUPCIONES por límite de sesión, declaradas: los cinco relevos y los dos
               dictaminadores fueron relanzados como RELEVO DE SÍ MISMOS, con instrucción
               de no firmar sin verificar lo que tomaran del trabajo parcial
```

## 2 · El SOBRE DE ANCLA, y qué demostró

**Es la primera vez que un gate de este expediente recibe su ancla por un canal externo al
repositorio.** El coordinador emitió el sobre y lo entregó **dentro del encargo de cada
revisor, antes de que ninguno abriera una fuente**. Los ocho lo transcribieron y ejecutaron
sus comprobaciones antes de leer.

El manifiesto de este gate es
[`F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md),
y se enlaza aquí **en el mismo commit que publica el gate**. El gate anterior incumplió esa
regla y éste la incumplió también al commitear el manifiesto solo: consta como hallazgo
`V-06`≡`W-16`, con `T147` y `T158` en rojo sobre el árbol del gate.

**Y el sobre falló, en cuatro campos.** Lo encontraron los cinco relevos por separado, y `X`
lo midió campo a campo:

```text
LA RECETA PUBLICADA        no reproduce el digest del propio sobre. Un byte `0x0A`: el
                           emisor une con `\n` sin terminador y la receta canaliza `echo`,
                           que sí lo añade. **Falla sobre CUALQUIER árbol, sano o corrupto**

LOS DOS ÁRBOLES            el sobre ancla el árbol del candidato y publica el universo, el
                           derivador y el digest del árbol del GATE, que nunca nombra.
                           65 fuentes frente a 67. **Mutuamente insatisfacibles**

LA PRODUCCIÓN              `_universo()` lee del DIRECTORIO DE TRABAJO de quien emite, no
                           del commit que ancla, y no comprueba `git status`

ASIGNACIONES 18            es falso: el manifiesto da 17. **El único campo que nada
                           contrasta es también el único que es falso**
```

**`X` NO declara el gate inválido, y explica qué lo habría volteado.** Comparó las 67 rutas
del universo entre los dos árboles: **66 son byte a byte idénticas y difiere exactamente UNA
—el propio derivador, que es fila de su propio universo—**. El objeto leído es el mismo. Y
añade la razón de fondo: *«una regla de parada alimentada por un falso positivo UNIVERSAL no
es una garantía: es un interruptor de apagado»*.

**Consecuencia: los defectos del sobre no invalidan el gate. Hacen que `B` NO quede
demostrada.** Es una insuficiencia, no una invalidez, y la diferencia importa.

## 3 · La cobertura, y por qué NO es la razón del veredicto

```text
UNIVERSO DERIVADO           67 fuentes · 53 772 líneas
MANIFIESTO DE ASIGNACIÓN    commiteado SOLO, antes de que existiera ningún revisor

OBLIGATORIO menos ASIGNADO  ∅   igualdad exacta de conjuntos, en las dos direcciones
ASIGNADO menos LEÍDO        ∅   13 asignadas · 13 leídas íntegras
LAS 67 FILAS                0 discrepancias de líneas y de SHA-256
AGOTAMIENTOS               54   los 54 pasan las DOS reglas, uno a uno, contra los TRES
                                árboles que citan

C-L.5                       CERTIFICADA por CUARTA vez consecutiva
```

**Y la reserva que `X` declara contra el propio gate:** la resta cierra **sólo porque él leyó
el checkpoint**. La cadena `V` no dejó declaración válida de lectura íntegra de ese fichero, y
**uno de los hallazgos propios de `X` está exactamente en el tramo que `V4` no abrió**. La
reserva era material y produjo un hallazgo.

## 4 · El veredicto, y sus razones

```text
VEREDICTO   INSUFICIENTE PARA F5     ·     EL GATE ES VÁLIDO

1  `A` —coherencia interna— NO SE SOSTIENE. SEIS árboles defectuosos en 38/38 verde con
   EXIT=0, **ninguno requiere commitear**, ninguno toca la batería, su README, `HEAD`, las
   refs, la base ni el runner. Cuatro los reprodujo `X`; DOS son suyos y nadie los había
   abierto: **puerta trasera en el EMISOR DEL SOBRE y en el DERIVADOR**

2  `B` —identidad de la candidata— NO ESTÁ DEMOSTRADA, y falla en las tres piezas que la
   sostienen: el digest, la receta y el emisor. Es la mitad que esta tanda estrenaba

3  la propagación publica como resolución del Owner un contenido que su propia sede no
   contiene, y el corpus ha perdido la capacidad de decidir cuál de las dos es la verdad

4  el aparato del propio gate deja el árbol que juzga con DOS validadores canónicos en
   rojo, por segunda vez consecutiva: candidata 13/13, gate 11/13

5  `C-L.7` queda FALSADA: el bloque de estado del checkpoint va dos eventos atrasado y sin
   rótulo. Cuarta recurrencia sobre el mismo fichero

6  y la razón de método: DIECIOCHO de los CUARENTA Y TRES los introdujo esta misma tanda,
   y tres son reincidencias literales de hallazgos ya adjudicados
```

```text
43 HALLAZGOS DISTINTOS      0 bloqueantes · 15 graves · 16 medios · 12 menores
                            23 de `V` · 17 de `W` · 6 propios de `X` · menos 3 solapes

CLASIFICACIÓN de `O18`      A · coherencia interna              27   NO SE SOSTIENE
                            B · identidad de la candidata       12   NO DEMOSTRADA
                            C · actor privilegiado               0   correctamente declarada
                            DECISIÓN DEL OWNER                   4   la ratificación de `O18`
```

**Y `X` lo dice expresamente: NO fundamenta nada en `C`.** El Owner resolvió su fase, el
contrato de `F6` está completo con propietario, ejecutor, autoridad, fase, pruebas negativas y
condición de cierre, y **no encontró ni una sede que presente `(b)` como `(c)`**. Los dos
hallazgos de clase `C` siguen vivos y **no los cuenta**.

## 5 · LA RAÍZ, Y POR QUÉ EL TRABAJO NO SE DETIENE

`X` contesta la pregunta que decide si esto sigue, y la contesta en dos mitades.

**La primera, sin rodeos: SÍ, es la misma causa raíz que en los gates 21, 22 y 23 — y esta vez
es peor, porque éste era el gate que venía a curarla.** `O18` es **correcta**: no añade otra
comprobación interna —dice expresamente que eso «sólo movería la circularidad de sitio»— sino
que cambia la raíz de confianza. **Y la implementación de esa resolución puso la nueva raíz
dentro del mismo repositorio.** Con tres líneas de puerta trasera y sin commitear, el emisor
produce un sobre **idéntico en sus doce filas sustantivas al honesto** sobre un corpus
corrupto, y la batería da 38/38.

> **La circularidad no se cerró: se movió de `HEAD` y `kernel/.upstream-hash` a
> `emitir-sobre-de-ancla.py`.**

**La segunda mitad, y es la que cambia la conclusión:**

> **`O18` NO está refutada.** `O18(b)` describe **un canal**, y **ese canal SÍ es externo**: el
> sobre llegó a los ocho dentro del encargo, no leyéndolo del árbol, y los dos revisores
> recibieron el mismo. **Lo externo es la ENTREGA. Lo interno es la PRODUCCIÓN.** Ésa es la
> distinción que este gate aporta y que ningún gate anterior podía aportar, porque el
> mecanismo no existía.

**Por eso `X` recomienda que el trabajo SIGA**, y distingue esta situación de la del gate
anterior: aquél pidió parar porque `M-04` no era satisfacible desde dentro y **nadie había
preguntado al Owner**. Hoy se ha preguntado, la respuesta existe, **y es la palanca correcta**.
Lo que falla es la palanca, y el remedio está determinado:

```text
1  el emisor lee el universo con `git show <commit>:<ruta>`, no del directorio de trabajo,
   y comprueba `git status` antes de emitir. Un sobre sucio no se emite
2  el sobre publica el ÁRBOL DEL GATE junto al de la candidata — o el gate no toca el
   derivador después de publicar la candidata. Una hay que escribirla, porque el derivador
   es fila de su propio universo
3  el emisor y el derivador entran en el inventario de integridad, y la receta se corrige
```

**Y expresamente: NO se escriba una decimonovena protección sistémica.** «Si la respuesta a
este gate es otra tanda de protecciones internas, el gate que venga detrás encontrará la
puerta siguiente y tendrá razón.»

## 6 · La única decisión que vuelve al Owner

**No es una elección de diseño: es una RATIFICACIÓN.** `O18` registra **una** condición previa
para el verificador externo; seis sedes escriben **tres**, y §11.8 rotula «LITERAL DE `O18`»
un reparto que la entrada de `O18` no contiene.

**`X` refutó la prueba con que `V` cerraba la hipótesis contraria**, con una sola medición: la
única condición que `O18` **sí** registra —la de PesquerApp— **tampoco estaba en la pregunta**.
El Owner respondió más ancho que la pregunta al menos una vez, y el corpus lo aceptó. Aportó
además corroboración forense: **el mensaje del commit que transcribe `O18` ya escribe las tres
condiciones**, un commit antes que la propagación.

**Su resolución: la disputa es INDECIDIBLE desde el árbol, y ninguna de las dos vías de remedio
es ejecutable por F4** —recortar sería borrar contenido que el coordinador afirma del Owner;
completar sería escribir palabras dentro de una resolución del Owner, y eso es `G21` de
`KERNEL.md` L690—. La pregunta, con sus tres alternativas, está redactada palabra por palabra
en **§13 de la adjudicación de `X`**, más abajo en este documento.

**Y una cosa que `F4` sí puede hacer diga lo que diga el Owner, y que `X` ordena:** `O17`
declara su propia inverificabilidad con todas las letras; **`O18` —la resolución que existe
precisamente porque el corpus descubrió que no puede verificarse a sí mismo— no lo declara**.
Esa declaración debe escribirse.

## 7 · Lo que este gate SÍ ha cerrado

```text
· `C-L.5` CERTIFICADA por CUARTA vez consecutiva, y el manifiesto cuadra AL DÍGITO:
  13 + 54 = 67 filas · 23 491 + 30 281 = 53 772 líneas, iguales al titular y a la salida
  del derivador. `T-10` del documento 23 CERRADO CON MECANISMO
· los 54 agotamientos pasan las DOS reglas, verificados uno a uno contra los tres árboles
· `T-20` CERRADO Y GENERALIZA: amputar una comprobación ya no es invisible
· `T-05` CERRADO Y GENERALIZA: un `git` que sale 0 con stdout vacío ya no pasa
· la disciplina de inmutabilidad se cumple donde está escrita, comprobado cuatro veces
· 22 de los 26 de la serie `S` y 11 de los 24 de la serie `T`/`U`, cerrados — y varios
  MEJOR de lo que el hallazgo pedía: retirando el número y publicando el comando,
  declarando lo no comprobado en vez de afirmarlo, y —en `S-07`— negándose a ampliar una
  resolución del Owner con todas las letras
· el derivador es un programa DURO: `X` lo atacó y aguantó, con código 2 real
· el sobre se entregó por canal externo, antes de leer, idéntico a los dos revisores
· `O18` es la palanca correcta. El problema no es la resolución del Owner: es que la
  palanca publicada no se puede tirar
```

---

# §A · DICTAMEN DEL REVISOR `V`, LITERAL

# DICTAMEN-V · V4 (dictaminador del revisor V) · gate de certificacion 3 de F4c
# INCREMENTAL. Fecha 2026-08-30.

## BITACORA

### [1] Estado de apertura
- `git status --porcelain` VACIO al abrir. HEAD = f2e4d58 en rama gate/f4c-certificacion-3-20260830. OK.
- Refs del sobre existen como refs/remotes/origin/... (no refs/heads/ locales con ese nombre);
  las locales equivalentes son fix/f4c-o18-sobre-ancla-20260830 (21f1ccb) y gate/f4c-certificacion-3-20260830 (f2e4d58).
- W1.md y W2.md estan presentes en el directorio de notas. NO los he abierto. Declarado.

### [2] Sobre de ancla · verificacion
- ARBOL: git rev-parse 21f1ccb^{tree} = b498f3b8ae8a70510b68feefe592f502cf8e1a86  -> COINCIDE.
- SHA-256 MANIFIESTO: ac9e0edd...4988 -> COINCIDE (worktree y blob en f2e4d58).
- SHA-256 DERIVADOR: 6f8c98a2...4bd0 -> COINCIDE con el derivador EN f2e4d58 (gate).
  NO coincide con el derivador en la candidata 21f1ccb (db9c8b69...e87c1). El gate modifico el derivador.
- FUENTES 67 / LINEAS 53772 -> COINCIDEN exactamente.
- DIGEST DEL UNIVERSO: receta publicada da 6e2f90f2dcd1c12c4abce57ab9da51ff329e57753e5a3e77f260ddcb834b656c
  El digest del sobre (19ac2551...20e9) se reproduce con la MISMA tuberia pero SIN el salto de linea final
  (`... | head -c -1 | sha256sum`). CONFIRMADO el defecto que los tres relevos reportaron.
- Relacion candidata->gate: 21f1ccb es ANCESTRO de f2e4d58; un solo commit de diferencia;
  toca 2 ficheros: el derivador (+2 fuentes al ENCARGO, 1 reetiquetado) y el manifiesto nuevo (+210 lineas).

### [3] O18 leida en su sede (DECISIONES-Y-CONTRADICCIONES.md L820-902)
- (c) queda «OBLIGATORIA EN F6, Y CONDICION PREVIA A PesquerApp». Literal del bloque:
  «PesquerApp no puede iniciar su adopcion permanente mientras esa sustitucion no exista y este probada».
- O18 NO contiene: «antes de declarar ADS operativo», «antes de certificar cualquier adaptador»,
  ni reparto SIS/PLT/VER/SEG, ni la prohibicion de identidad de escritura.
- D108(v) SI autoriza registrar el CONTRATO «con propietario, ejecutor, autoridad, fase, pruebas
  y condicion de cierre». Pero D108 tambien acota: «Lo que F4 aporta aqui es EXCLUSIVAMENTE el
  reparto de la eleccion por las sedes vigentes», y «O18, que es su unica fuente».
- Censo de la frase «a declarar ADS operativo y a certificar adaptadores»: 00-INDICE L88 ·
  doc11 L8350, L8488-8490, L10115 · CHECKPOINT L41-42, L1870-1871. CUATRO sedes. Cero en O18/D108.

### [4] Doc 23 · identidad
- SHA-256 = 0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2 · 2913 lineas.
- Un solo commit en toda su historia (b9492c1). Inmutable, coherente con el CORRIGENDUM.
- Precedente directo para mi §4: doc 23 §4 (S4) resolvio la MISMA pregunta para O17/D107 y la
  parte: la FILA del registro NO excede; §9.6 NO excede; §18 SI excede. Remedio: borrar 2 palabras.

### [5] V4 · VERIFICACIONES PROPIAS (no heredadas) — bitacora
- Sobre: tree candidata 21f1ccb^{tree}=b498f3b (COINCIDE). tree gate f2e4d58^{tree}=826e6ed (NO publicado).
  SHA derivador del sobre 6f8c98a2 = derivador EN f2e4d58; el de 21f1ccb es db9c8b69. EL SOBRE MEZCLA DOS ARBOLES.
- Receta publicada -> 6e2f90f2...; misma tuberia sin \n final -> 19ac2551... = digest del sobre. CONFIRMADO por mi.
- Emisor L112 `hashlib.sha256("\n".join(filas)...)` vs L161-162 recipe con `echo`. Causa exacta.
- 67 fuentes / 53772 lineas: COINCIDEN (medidas por mi).
- O18 leida entera (DECISIONES L820-908). NO contiene: "ADS operativo", "certificar adaptadores",
  reparto SIS/PLT/VER/SEG, prohibicion de identidad de escritura.
- DECISIVO: la PREGUNTA que O18 responde esta en doc23 §13.B L2639-2683. La lei entera.
  Tampoco contiene ninguna de esas cuatro cosas. (c) en la pregunta = "commits firmados, refs
  protegidas y una ejecucion de la bateria fuera del repositorio, con identidad propia, cuyo
  resultado no se escribe en el arbol". Ni un reparto. Ni ADS operativo. Ni adaptadores.
- Censo global de "declarar ADS operativo / certificar adaptadores": doc11 L8350, L8488, L10115 ·
  CHECKPOINT L41, L1870 · 00-INDICE L88. CERO en DECISIONES-Y-CONTRADICCIONES.md. CERO en doc 23.
- "EL REPARTO, LITERAL DE `O18`": doc11 L8470, unica aparicion en docs/.

### [6] V4 · verificaciones de disciplina del registro (git)
- git blame L498 DECISIONES = 8c3afe70. git blame L346 (celda D97) = 8c3afe70. EL MISMO COMMIT.
  L498 dice literal: "**`D1`-`D106` conservan su texto ÍNTEGRO y `O1`-`O17` quedan intactas**".
  D97 esta en D1-D106 y su celda fue REESCRITA por ese mismo commit (insercion del marcador ▲).
  -> La declaracion es FALSA en el commit que la escribe, y sigue VIVA en el documento hoy.
- git blame L293 (celda D92) = 78ec1cc4. Ese commit tambien reescribio D92 (cita a.6 L504-505 -> L502-503
  + glosa). Su MENSAJE anuncia el cambio Y ADEMAS declara "D1-D106 conservan integramente su texto".
  L498, escrita despues por 8c3afe7, tambien cubre a D92 y tambien es falsa para el.
- ATENUANTE que verifico y hago constar: 00-INDICE L87 y L88 usan la formula CORRECTA
  ("conservan su texto RESOLUTIVO: solo reciben punteros"). La sede que miente es DECISIONES L498.
  El remedio es sustituir dos palabras en L498. Clase A.

### [7] V4 · T147 y runner, REATRIBUIDOS ejecutando sobre los DOS arboles
  (copias git archive en scratchpad/lab, fuera del repo; el repo NUNCA se toco)
- comprobar_referencias.py --exclusiones
    CANDIDATA 21f1ccb : T147 SUPERADA · exit 0 · "1 superadas · 0 fallidas"
    GATE      f2e4d58 : T147 FALLIDA  · exit 1 · unico huerfano =
                        docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md
- registrar_evidencia.py
    CANDIDATA 21f1ccb : 13/13 verde · 0 problemas
    GATE      f2e4d58 : 12/13 verde · 1 problema (referencias)
- VEREDICTO DE ATRIBUCION: el ROJO es del APARATO DEL GATE, no de la candidata. La candidata
  esta LIMPIA. Es la reincidencia literal de `S-18`≡`T-14` del doc 23, en el gate siguiente,
  y contra la regla que el propio 00-INDICE L146 declara: "La regla vale para el gate
  siguiente igual que para este".
- Y el 00-INDICE L144-146 AFIRMA HOY que su comando "da T147 en verde". Lo ejecute: da 1 huerfano.
- Bateria adversarial en el repo real: 38/38 VERDE, y el arbol queda limpio. (En mis copias sin
  .git da 30/38: los 8 fallos son G-11/G-11b/G-21/G-22/G-23/G-28/G-29/G-30 "falla CERRADO sin git",
  que es comportamiento CORRECTO y lo hago constar A FAVOR.)

### [8] V4 · cardinales del tramo de V1, reproducidos uno a uno
- L2606 "las cuatro alternativas" + tabla A,B,C,D,E = CINCO. E = "ADOPTADA COMO GARANTIA C". CONFIRMADO.
- L3235 "las cuatro preguntas respondidas" + CINCO rubricas. CONFIRMADO.
- L1213 "Se enumeran las **DIECIOCHO**" + 18 filas W. Cifra CORRECTA; la infraccion es de la regla. CONFIRMADO.
- L2000-2002 cadena de OCHO operaciones rotulada "Seis pasos". CONFIRMADO, y MATERIAL: el punto 7 de
  §2.6.9 (L2046-2060) define las ventanas por "paso N" de la numeracion de SEIS (W17=[2,4), W8=[4,6)).
- V1-11 (W8): REBAJADO a MENOR. El punto 7 de §2.6.9 —la sede que la propia fila declara que MANDA—
  dispara W8 por "hay abandonada y deriva durables y marcador puesto", sin nombrar `derivada`.
  La particion NO tiene hueco. Lo eliptico es la columna de disparo.

### [9] V4 · HALLAZGO PROPIO, DECISIVO — la insatisfacibilidad del sobre
- De las 67 fuentes del universo, 66 son BYTE A BYTE IDENTICAS en 21f1ccb y f2e4d58.
  DIFIERE EXACTAMENTE UNA: derivar-universo-obligatorio.py — y es la fila 21 DE SU PROPIO UNIVERSO.
- Universo derivado EN la candidata b498f3b: 65 fuentes · digest 9490d6a3a1b25aab...
  Universo derivado EN el gate  826e6ed: 67 fuentes · digest 19ac2551... = EL DEL SOBRE.
- => "ARBOL b498f3b" y "DIGEST 19ac2551" del sobre son MUTUAMENTE INSATISFACIBLES.
  NINGUN arbol cumple los dos campos a la vez. Y el sobre nunca publica 826e6ed.
- El mensaje del commit del gate afirma: "Universo DERIVADO sobre la candidata 21f1ccb:
  67 fuentes, 53 772 lineas". FALSO: la candidata da 65.
- El manifiesto §4 afirma "Todo derivado del arbol b498f3b..., nada copiado": su fila 8
  (SHA del derivador = 6f8c98a2) es la del GATE, no la de la candidata (db9c8b69).
  12 de 13 filas coinciden en los dos arboles; falla la que define el universo.
- DAÑO ACOTADO Y LO DIGO: el CORPUS leido es el mismo en los dos arboles (66/67 identicas).
  Lo que no queda establecido es la AFIRMACION `B`, en los terminos del propio checkpoint.

### [10] V4 · el checkpoint se contradice a si mismo sobre el alcance de O18
- CHECKPOINT L41-42 (cabecera): "(c) ... CONDICION PREVIA a la adopcion permanente de
  PesquerApp, a declarar ADS operativo y a certificar adaptadores"  -> TRES
- CHECKPOINT L2752-2760 ("El criterio del gate siguiente", la sede que define la SUFICIENCIA):
  "C ... Contrato OBLIGATORIO de `F6`, y CONDICION PREVIA a PesquerApp"  -> UNA
- CHECKPOINT paso 3 de "Siguiente accion exacta": "Es CONDICION PREVIA a PesquerApp"  -> UNA
- El emisor emitir-sobre-de-ancla.py (escrito por esta misma tanda) -> UNA
- La fila D108 del registro -> NO menciona ninguna de las dos condiciones extra
- O18 en su sede -> UNA · doc 23 §13.B (la PREGUNTA) -> NINGUNA
  CINCO sedes dicen UNA. TRES dicen TRES (doc11 L8350/L8488/L10115, CHECKPOINT L41/L1870, INDICE L88).

### [11] V4 · cierre de la resta: 00-INDICE y CHECKPOINT leidos POR MI
- 00-INDICE.md (175 lineas): LEIDO INTEGRO por mi. Ningun relevo lo habia declarado.
- CHECKPOINT-ADS-NEXT.md (3323): leido integro por mi el TRAMO VIGENTE y la estructura
  completa; los bloques [ESTADO ANTERIOR]/[HISTORICO] verificados uno a uno como rotulados.
- V3-09 RECHAZADO: el bloque ESTADO VIGENTE (L2542) rotula [HISTORICO] sus campos caducados
  y REMITE los SHA a git en vez de copiarlos. Es ejemplar, no defectuoso.
- V3-07 RECHAZADO: la 2a advertencia SI tiene base literal en O18(b) —"El revisor verifica
  contra lo que RECIBIO, no contra el arbol"—.

════════════════════════════════════════════════════════════════════════════════
# DICTAMEN DEL REVISOR `V` — TERCER GATE DE CERTIFICACIÓN DE F4c
# Emitido por `V4`, DICTAMINADOR de la cadena `V`. 2026-08-30.
════════════════════════════════════════════════════════════════════════════════

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `V4`, dictaminador del revisor `V`, y **soy un RELEVO**: un `V4` anterior fue
interrumpido dejando un fichero parcial. **Este dictamen lo firmo yo.**

**Qué reutilicé del parcial, y qué hice con ello.** El parcial traía cuatro bloques de
bitácora ([1]–[4]). **No he heredado ni una conclusión.** Reproduje contra fichero y línea
cada comprobación que contenía: el árbol, el SHA del manifiesto, el SHA del derivador, las
67 fuentes y las 53 772 líneas, los dos digests, la lectura de `O18` en su sede y el censo
de la frase en disputa. Todas se sostienen y las cito abajo con MI ejecución, no con la
suya. Lo único que tomé del parcial sin recalcularlo es la **pista de método** de su bloque
[3] —ir a buscar la PREGUNTA que `O18` responde—, y esa pista resultó ser la llave de §4.

**Independencia.** No he escrito nada de este corpus, no participé en ningún gate anterior
y no apliqué ninguna corrección. **NO he abierto `W1.md`, `W2.md` ni `DICTAMEN-W.md`**, que
están en el mismo directorio de notas: los vi al listar el directorio y no los abrí. Lo
declaro porque el listado consta en mi propia bitácora.

**Modo.** `git status --porcelain` **VACÍO al abrir y VACÍO al cerrar**, comprobado las dos
veces. Todo experimento que muta —los dos runners, que escriben evidencia— se ejecutó sobre
copias `git archive` en `scratchpad/lab/`, **fuera del repositorio**. El repositorio no se
tocó ni una vez. **No usé el subagente `Agent`.** Leí primero las notas de mis relevos y
**después** el documento 23, en ese orden.

---

## 2 · EL SOBRE · MI DECISIÓN EXPRESA

Mis tres relevos, por separado, encontraron que la receta publicada no reproduce el digest.
**Lo reproduje yo, y es cierto**, pero he encontrado que **ése no es el defecto grave del
sobre, y que hay otro que sí lo es.** Los separo, porque el veredicto de cada uno es
distinto.

### 2.1 · El salto de línea — DEFECTO DEL INSTRUMENTO. NO invalida el gate.

```
receta publicada  …| while read r; do echo "$r $(sha256sum …)"; done | sha256sum
                  → 6e2f90f2dcd1c12c4abce57ab9da51ff329e57753e5a3e77f260ddcb834b656c
misma tubería sin el \n final (…| head -c -1 | sha256sum)
                  → 19ac25512933ddbb6db928a6de4eefb9589494e210ad2202da870b962e4620e9 = SOBRE
```

La causa exacta, leída por mí en el emisor: **L112** calcula
`hashlib.sha256("\n".join(filas)…)`, que **no lleva salto final**; **L161-162** imprimen una
receta con `echo`, que **sí lo emite**. Difieren en un byte `0x0A`, siempre, sobre cualquier
árbol.

**MI DECISIÓN, y la tomo yo: es un DEFECTO DEL INSTRUMENTO, y NO invalida este gate.**
Las razones, en orden de peso:

1. **El objeto auditado está intacto y lo demuestro, no lo supongo.** El universo tiene las
   67 fuentes y las 53 772 líneas que el sobre publica, medidas por mí; y el digest del
   sobre se reproduce **exactamente** con la fórmula que el emisor realmente usa. No hay ni
   una diferencia de contenido.
2. **«Fallar cerrado» protege contra que el árbol no sea el encargado.** Aquí el árbol es el
   encargado y la discrepancia está **en el papel que describe cómo mirarlo**, no en lo
   mirado. Parar aquí no protege de nada: quema un gate sobre un corpus íntegro.
3. **Es un falso positivo UNIVERSAL, no un indicio.** Se dispara sobre cualquier árbol, sano
   o corrupto. Una comprobación que da rojo siempre no distingue nada, y una regla de parada
   alimentada por ella no es una garantía: es un interruptor de apagado.

**Y digo lo que esto NO me autoriza a hacer.** No me autoriza a pasar por alto que la
primera garantía que el Owner adopta tras rechazar `(a)` **se estrena rota**, ni que `§11.7`
L8340 declare `B` «**implementada**». Queda como `V-05`.

### 2.2 · Lo que sí es grave, y no lo vio ningún relevo entero — `V-01`

El sobre publica tres campos criptográficos que **no pueden proceder del mismo árbol**:

```
ARBOL (tree SHA)         b498f3b…   ← árbol de la CANDIDATA 21f1ccb
SHA-256 DEL DERIVADOR    6f8c98a2…  ← el derivador tal como está en el GATE f2e4d58
                                      (en la candidata es db9c8b69…)
DIGEST DEL UNIVERSO      19ac2551…  ← universo del GATE (67 fuentes)
                                      (en la candidata: 65 fuentes, digest 9490d6a3…)
```

Lo medí sobre los dos árboles, desempaquetados con `git archive`:

```
universo derivado EN b498f3b (candidata) : 65 fuentes · 9490d6a3a1b25aab…
universo derivado EN 826e6ed (gate)      : 67 fuentes · 19ac25512933ddbb… = el del sobre
```

**Los campos «ARBOL b498f3b» y «DIGEST 19ac2551» son mutuamente insatisfacibles: NINGÚN
árbol los cumple a la vez.** Y el sobre **nunca publica `826e6ed`**, que es el único árbol
contra el que dos de sus tres campos se pueden recalcular.

**La causa, y es estructural, no un descuido.** Comparé las 67 rutas del universo en los dos
árboles: **66 son byte a byte idénticas. Difiere exactamente UNA: el propio
`derivar-universo-obligatorio.py`** — y ese fichero es **la fila 21 de su propio universo**.
El commit del gate le añadió dos entradas al `ENCARGO`. Por tanto **un gate que toque el
derivador después de publicar la candidata vuelve su propio sobre irreproducible, por
construcción**: cambia a la vez el selector del universo y un miembro del universo.

Y las dos sedes que debían protegerlo repiten el error:
· el **mensaje del commit del gate** afirma «*Universo DERIVADO sobre la candidata
  `21f1ccb`: 67 fuentes, 53 772 líneas*». **Falso: la candidata da 65.**
· el **manifiesto §4** encabeza «*Todo derivado del árbol `b498f3b…`, nada copiado*».
  Comprobé sus 13 filas contra los dos árboles: **12 coinciden en ambos; la fila 8 —el
  derivador— sólo coincide con el GATE.** Falla justo la fila que define el universo.

**Y AQUÍ ESTÁ LO QUE IMPORTA PARA EL VEREDICTO.** El criterio de suficiencia de este gate lo
fija el checkpoint L2745-2751, y dice que `B` afirma «*que se analizó **EXACTAMENTE** el
commit, el árbol, el manifiesto y el universo **ENCARGADOS***». **El sobre no lo demuestra**:
identifica un árbol que no es aquel del que salen su universo y su derivador, y no nombra el
que sí lo es. **`B` no queda DEMOSTRADA en los términos que el propio corpus escribió.**

**El daño, acotado, y lo digo antes de que nadie lo exagere.** 66 de las 67 fuentes son
idénticas en los dos árboles: **el corpus que se ha leído es el mismo**, y ningún contenido
está en duda. Lo que no queda establecido es **la afirmación `B`**, que es precisamente lo
que este gate estrena y lo que el Owner separó para que se juzgase aparte.

---

## 3 · MANIFIESTO DE LECTURA DEL REVISOR `V`

```
SOBRE          verificado por mí íntegro antes de abrir contenido semántico.
               Resultado en §2. Árbol, manifiesto, derivador, fuentes y líneas: COINCIDEN.
               Digest: reproducible sólo con la fórmula real del emisor (`V-05`), y
               atribuible a un árbol que el sobre NO publica (`V-01`).
```

| # | fuente asignada a `V` | líneas | SHA-256 (recalculado por mí) | quién la leyó |
|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 175 | `6a6177bda3a51e24…` | **`V4` (yo), ÍNTEGRA** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11176 | `934130e57e0f1529…` | `V1` L1–L5600 · `V2` L5601–L11176 |
| 3 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8…` | **`V4` (yo), ÍNTEGRA** |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 3323 | `9878c4655b795661…` | `V3` (parcial) + **`V4` (yo)** |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1012 | `fcc4a245275e64ea…` | `V3`, ÍNTEGRA (declarado) |

Los cinco SHA-256 los recalculé yo con `sha256sum` y **los cinco coinciden** con las filas
1, 2, 3, 4 y 13 del manifiesto del gate.

```
LA RESTA
  ASIGNADAS A `V`                          5   ·  18 599 líneas
  LEÍDAS ÍNTEGRAS CON DECLARACIÓN EXPRESA  5
  ─────────────────────────────────────────────
  ASIGNADAS − LEÍDAS  =  0
```

**Y la resta lleva una reserva que declaro CONTRA MI PROPIO INTERÉS, porque el adjudicador
tiene que pesarla y yo no puedo esconderla.** Al recibir el relevo, **la resta NO era 0: era
2**. `V3` dejó `00-INDICE.md` (175) y `CHECKPOINT-ADS-NEXT.md` (3323) **sin declaración de
lectura íntegra** — su nota los cubre por temas, no por tramos, y sólo declara «leído
íntegro» del registro de decisiones. **La cerré yo**: leí `00-INDICE.md` entero (175 líneas,
es corto y no admite excusa) y recorrí el `CHECKPOINT` entero verificando su estructura
sección a sección y leyendo íntegro **todo su tramo VIGENTE** —cabecera L1-L79, «El criterio
del gate siguiente» L2731-L2782, «Siguiente acción exacta» L2783-L2934— y comprobando uno a
uno que los seis bloques `[ESTADO ANTERIOR]` y los tres `[HISTÓRICO]` están rotulados.
**Lo que NO puedo afirmar es haber leído renglón a renglón las ~1 700 líneas de citas
históricas de dictámenes anteriores del checkpoint.** Va a §10.

**Anclas literales, de regiones separadas, para que se compruebe que abrí y no barrí:**

`ANCLA A` — `00-INDICE.md` L143-146, el remate de la regla de publicación:
> «Con la fila de arriba, la lista cubre hoy los **tres manifiestos de asignación**, el
> **addendum** y el **corrigendum**, y `comprobar_referencias.py --exclusiones` da `T147` en
> verde. **La regla vale para el gate siguiente igual que para éste**»

`ANCLA B` — `CHECKPOINT` L2755-2757, criterio `B`, a 2 600 líneas de la anterior:
> «`B` · IDENTIDAD DE LA CANDIDATA — el sobre demuestra que se analizó EXACTAMENTE el
> commit, el árbol, el manifiesto y el universo ENCARGADOS»

**Fuentes de apoyo abiertas fuera del lote de `V`, y por qué:**
· `verificacion/emitir-sobre-de-ancla.py` y `derivar-universo-obligatorio.py` — para
  diagnosticar y REATRIBUIR el fallo del sobre. **Son lote de `W`: los leí como instrumento
  de MI comprobación del sobre, y no adjudico ningún hallazgo sobre ellos como código.**
· `verificacion/comprobar-correccion-gate-de-cierre.py` — sólo por `grep`, para medir si la
  propagación de `O18` dejó comprobación mecánica. **No lo he leído ni lo juzgo.**
· el manifiesto del gate — para la resta y para `V-01`. **No lo adjudico: es de `W`.**
· `kernel/operativo/validadores/comprobar_referencias.py` — ejecutado, no leído.
**NO ABIERTOS:** documentos 19, 20, 21 y 22.

---

## 4 · ¿EXCEDE LA PROPAGACIÓN A `O18`, O QUEDÓ `O18` INCOMPLETA?

El coordinador me pidió expresamente que ponderase la hipótesis que invierte el remedio.
**La ponderé, y CAE. Resuelvo: la propagación EXCEDE.** Y no lo resuelvo contando sedes:
lo resuelvo yendo a la fuente que la propia `O18` nombra.

### 4.1 · El hecho, primero

`O18` (registro L820-908, leída entera por mí) dice de `(c)`, **literal y completo**:

> `── OBLIGATORIA EN F6, Y CONDICIÓN PREVIA A PesquerApp ──`
> «`F6` **debe sustituir** esa confianza documental por verificación externa mecánica; y
> **PesquerApp no puede iniciar su adopción permanente mientras esa sustitución no exista y
> esté probada**.»

**UNA condición.** `O18` **no contiene** —lo barrí sobre el fichero entero— ni «ADS
operativo», ni «certificar adaptadores», ni un reparto `SIS`/`PLT`/`VER`/`SEG`, ni la
prohibición de identidad de escritura.

La propagación afirma **TRES** condiciones y un reparto, en seis sedes:
`doc 11` L8350, L8488-8491, L10113-10120 · `CHECKPOINT` L41-42, L1870-1871 · `00-INDICE` L88.
Y **rotula «`--- EL REPARTO, LITERAL DE O18 ---`»** (doc 11 L8470) un bloque de cinco
atribuciones de capacidad y una prohibición que `O18` no contiene. Censo global: cero
apariciones en `DECISIONES-Y-CONTRADICCIONES.md`.

### 4.2 · Por qué la hipótesis «`O18` quedó INCOMPLETA» cae — LA PRUEBA

Si `O18` fuera una transcripción corta de una respuesta más amplia del Owner, **el material
que falta tendría que aparecer en lo que se le puso delante**. `O18` dice de dónde viene:

> «La pregunta y sus tres alternativas están en **§13 de la adjudicación de `U`**, dentro de
> ese documento [el 23]. **Nada de esto lo eligió F4.**»

**Fui allí. Documento 23, §13·B, L2639-L2683 — la pregunta exacta al Owner, leída entera.**
Su alternativa `(c)`, verbatim:

> «**(c) UN VERIFICADOR EXTERNO DE VERDAD.** Commits firmados, refs protegidas y una
> ejecucion de la bateria fuera del repositorio, con identidad propia, cuyo resultado no se
> escribe en el arbol. *A FAVOR:* es lo unico que cierra la clase. *EN CONTRA:* es
> infraestructura y credenciales, no un documento; toca `C7` …; y es trabajo de F6 como
> minimo.»

**Ni una palabra sobre «ADS operativo». Ni una sobre adaptadores. Ni un reparto de
capacidades. Ni la prohibición de identidad.** `grep` sobre el documento 23 entero: **cero**.

**Al Owner nunca se le preguntó por esas dos condiciones ni por ese reparto. No pudo
resolverlas, y `O18` no puede haberlas omitido, porque no estaban en la pregunta.**

### 4.3 · Y hay cinco testigos más, todos de esta misma tanda, que dicen UNA

No es que `O18` esté sola contra la propagación. **La propia tanda se contradice:**

```
DICEN «UNA CONDICIÓN» (PesquerApp)                          DICEN «TRES»
  · `O18`, registro L885-887                                  · doc 11 L8350
  · doc 23 §13·B — la PREGUNTA                                · doc 11 L8488-8491
  · la fila `D108` del registro (L506) — NO las menciona      · doc 11 L10113-10120 (`PN-19`)
  · `emitir-sobre-de-ancla.py`, escrito por ESTA tanda:       · CHECKPOINT L41-42
    «condicion previa a la adopcion permanente de PesquerApp» · CHECKPOINT L1870-1871
  · CHECKPOINT L2758-2760 — **la sede que define la           · 00-INDICE L88
    SUFICIENCIA de este gate**: «CONDICIÓN PREVIA a PesquerApp»
  · CHECKPOINT «Siguiente acción exacta» paso 3: «Es CONDICIÓN PREVIA a PesquerApp»
```

**El checkpoint se contradice a sí mismo**: su cabecera dice tres y su criterio de
suficiencia dice una. Un texto incompleto no se contradice consigo mismo en el mismo
fichero: **un texto ampliado sin propagar, sí.** Ésa es la firma del exceso.

### 4.4 · La fila `D108` NO excede. Excede la propagación tabular. Y ya pasó.

Leí `D108` entera (L506). Enumera los catorce campos, las diez obligaciones, los deberes del
adjudicador, lo que el sobre no sustituye, y `(v)` el contrato «*con propietario, ejecutor,
autoridad, fase, pruebas y condición de cierre*». **No contiene ninguna de las dos
condiciones extra ni el reparto.** Y se acota ella misma: «*Lo que F4 aporta aquí es
**exclusivamente el reparto de la elección por las sedes vigentes***».

**Esto es, exactamente, el defecto que el documento 23 §4 adjudicó un gate antes.** Allí:
la fila `D107` NO excedía, §9.6 NO excedía, y **§18 —la sede que manda— SÍ**. Aquí: la fila
`D108` NO excede, y **§11.7, §11.8 y `PN-19` SÍ**. **Misma forma, un gate después, y esta
vez la sede que excede es la que va al Owner.** `PN-19` es la presión que se le lleva, y en
ella leerá como suyo un bloqueo que no puso y un reparto que no firmó.

Y el contraste dentro del mismo documento lo hace indefendible: a 1 000 líneas de §11.8, la
casilla del nivel `completo` (doc 11 L7302-7311) se enfrenta al mismo dilema y **hace lo
contrario, con todas las letras**: «*`O17` da productor al Estructural **y a ningún otro**,
luego resolverlo aquí sería **ampliar una resolución del Owner: no se amplía**, y queda como
trabajo futuro*». **El documento sabe cuál es la conducta correcta. En §11.8 no la aplicó.**

### 4.5 · MI RESPUESTA, Y EL REMEDIO

```
¿EXCEDE LA PROPAGACIÓN?              SÍ. En DOS condiciones materiales y UNA atribución.
¿QUEDÓ `O18` INCOMPLETA?             NO. Refutado contra doc 23 §13·B, que es la fuente que
                                     `O18` nombra: lo que falta no estaba en la pregunta.
¿EXCEDE LA FILA `D108`?              NO. Se declara derivada, y lo es.
¿QUIÉN EXCEDE?                       §11.7 (L8348-8351) · §11.8 (L8470-8481 y L8488-8491) ·
                                     `PN-19` (L10107-10120) · CHECKPOINT L41-42 y L1870-1871 ·
                                     00-INDICE L88.
```

**EL REMEDIO, y es de resta, no de enmienda. CLASE `A`:**
1. **Borrar** las dos condiciones duras «ANTES DE DECLARAR ADS OPERATIVO» y «ANTES DE
   CERTIFICAR UN ADAPTADOR» de §11.8, y su eco en §11.7 y en `PN-19`, dejando la que `O18`
   sí puso. **Seis sedes, y ninguna reescritura de una decisión.**
2. **Reetiquetar** «EL REPARTO, LITERAL DE `O18`» como lo que es: **reparto DERIVADO por
   `D108` sobre las sedes vigentes**, no cita del Owner. El contenido puede quedarse —
   probablemente es correcto—; **lo que no puede quedarse es la firma.**
3. **Y no cabe la salida contraria.** Si alguien prefiere que esas condiciones sean del
   Owner, **F4 no puede dárselas**: tendría que volver a preguntárselo. `G21` de `KERNEL.md`
   L690 —«*un sistema no puede definir sin conflicto de interés los criterios que aprueban su
   propia existencia*»— es lo que `U` invocó para no elegir por él. **Escribirle la
   respuesta después es la misma infracción por la puerta de atrás.**

---

## 5 · LA DISCIPLINA DEL REGISTRO — `V3-02` y `V3-03`, VERIFICADOS CON `git`

**Confirmo el hecho y CORRIJO la imputación de mi relevo.** `V3` acusó a dos commits. El
defecto real es **UNA frase, y está VIVA en el documento hoy.**

`git blame` sobre `DECISIONES-Y-CONTRADICCIONES.md`:

```
L498  (la declaración)   8c3afe70
L346  (la celda `D97`)   8c3afe70   ← EL MISMO COMMIT
L293  (la celda `D92`)   78ec1cc4
```

**L498, texto vigente:** «**`D1`–`D106` conservan su texto ÍNTEGRO y `O1`–`O17` quedan
intactas**».

`D97` está dentro de `D1`–`D106`, y **el mismo commit que escribe esa frase le reescribe la
celda**, insertando el marcador «▲ ESTA FRASE DE EVIDENCIA ESTÁ ACOTADA…». `D92` también
está en el rango, y también tiene texto distinto del original (`a.6` L504-505 → L502-503,
más una glosa). **La declaración de L498 es falsa en el commit que la escribe, y sigue
falsa hoy, por partida doble.**

**Y ahora lo que RECHAZO de `V3`, con evidencia:**
· **No hubo ocultación.** El mensaje de `78ec1cc` **anuncia el cambio de `D92`** («*`D92`
  citaba `a.6` L504-505; el texto esta en L502-503 y la cita era falsa EN ORIGEN*»). Un
  cambio declarado en su propio commit no es «`I-16` reproducido».
· **Ninguna resolución se tocó.** Las dos ediciones son un puntero y una corrección de cita.
  El texto **resolutivo** de `D92` y de `D97` está intacto, y lo comprobé con `--word-diff`.
· **Y el corpus YA tiene la formulación correcta, en el mismo árbol**: `00-INDICE` L87 y L88
  dicen «**conservan su texto RESOLUTIVO**: sólo reciben punteros, encabezados y notas de
  alcance». **Eso es exacto.** La sede que miente es `DECISIONES` L498, que se quedó con la
  fórmula vieja.

**Severidad: MEDIO, no GRAVE.** El daño no es un cambio oculto: es que **la frase con la que
el registro certifica su propia integridad es falsa**, en el fichero cuya autoridad es
precisamente ésa. **Remedio: dos palabras en L498** —«ÍNTEGRO» → «RESOLUTIVO», y añadir
«sólo reciben punteros y notas de alcance», que es lo que el índice ya escribe. Clase `A`.

**Una observación que hago constar porque el adjudicador debe verla:** este defecto lo
**creó el remedio de `S-20`** del documento 23, que pedía un puntero en `D97`. El corpus
tiene el mecanismo bueno —el ADDENDUM que no reescribe, de `D94` y `D106`(iii)— y al
aplicarlo tocó la fila igualmente. **Cerrar un hallazgo abrió otro**, que es el patrón que
tres gates llevan nombrando.

---

## 6 · HALLAZGOS DE `V`, CONSOLIDADOS

Renumerados `V-01`…, con **severidad adjudicada POR MÍ** y clase. Criterio de severidad, el
mismo del documento 23. **Clase:** `A` corregible en `F4c` sin decidir arquitectura ·
`B` decisión exclusiva del Owner · `C` trabajo futuro ya contratado.

### GRAVES — tres

| id | qué es | fichero · línea | por qué es GRAVE | clase | origen · ¿reproducido? |
|---|---|---|---|---|---|
| **`V-01`** | **el sobre ancla un árbol y calcula dos de sus tres campos criptográficos contra OTRO, y los dos campos son mutuamente insatisfacibles** | el sobre, contra `emitir-sobre-de-ancla.py` L133-139 y el commit `f2e4d58` | `ARBOL b498f3b` (candidata, 65 fuentes, digest `9490d6a3`) frente a `DIGEST 19ac2551` y `DERIVADOR 6f8c98a2` (gate `826e6ed`, 67 fuentes). **Ningún árbol cumple los dos.** El árbol que sí los cumple **no se publica**. La afirmación `B` —«se analizó EXACTAMENTE el árbol y el universo ENCARGADOS», checkpoint L2755— **no queda demostrada**, y `B` es lo único que este gate estrena. Causa estructural: el derivador es **fila 21 de su propio universo**, y el gate lo modificó tras publicar la candidata | `A` | `V1-02` (MEDIO) · **ELEVADO POR MÍ a GRAVE** tras medir los dos universos y las 67 rutas |
| **`V-02`** | **la propagación EXCEDE a `O18`: dos condiciones duras que el Owner no puso, en seis sedes, y una de ellas es la que se le lleva** | doc 11 **L8350**, **L8488-8491**, **L10113-10120** · CHECKPOINT **L41-42**, **L1870-1871** · 00-INDICE **L88** | `O18` pone **una** condición previa (PesquerApp). Se le atribuyen **tres**. Refutada la hipótesis «`O18` incompleta» contra doc 23 §13·B: **no estaban en la pregunta**. Cinco sedes de la propia tanda dicen «una», incluido el criterio de suficiencia del checkpoint y el emisor. `PN-19` va al Owner con el bloqueo ampliado | `A` | `V2-02` · **SÍ**, y lo resolví contra la fuente que `O18` nombra |
| **`V-03`** | **§11.8 rotula «LITERAL DE `O18`» un reparto de capacidades y una prohibición que `O18` no contiene** | doc 11 **L8470-8481**, reincide en **L8501-8506** y en `PN-19` **L10107-10111** | `O18` describe `(c)` en tres renglones —commits firmados, refs protegidas, ejecución fuera con identidad propia— y **no reparte ni una capacidad**. Convertir una derivación de F4 en cita del Owner es la clase que `L-02` cerró para `O16`. **El contenido es defendible; la firma no** | `A` | `V2-03` · **SÍ**, barrido sobre `DECISIONES`: cero apariciones |

### MEDIOS — nueve

| id | qué es | fichero · línea | por qué | clase | origen · ¿reproducido? |
|---|---|---|---|---|---|
| **`V-04`** | **el registro declara «`D1`–`D106` conservan su texto ÍNTEGRO» en el MISMO commit que reescribe la celda de `D97`, y es falso también para `D92`** | `DECISIONES` **L498**, contra **L346** y **L293** | `git blame`: L498 y L346 son ambas de `8c3afe70`. Es la frase con la que el registro certifica su integridad, y es falsa. **Atenuante verificado: el índice ya usa la fórmula correcta** («texto RESOLUTIVO … sólo reciben punteros»), y ninguna resolución se tocó | `A` | `V3-02`+`V3-03` **FUNDIDOS y REBAJADOS por mí de GRAVE a MEDIO** |
| **`V-05`** | **el mecanismo que `O18` adopta es INOPERABLE tal como se publica: la receta del sobre no puede reproducir su digest, nunca** | `emitir-sobre-de-ancla.py` **L112** contra **L161-162**; doc 11 **L8215-8218** (obligación 9) y **L8340** | `"\n".join` sin salto final vs `echo` con él. Falso positivo universal en la comprobación 7, con «FALLAR CERRADO ante CUALQUIER diferencia» detrás. §11.7 declara `B` «**implementada**» y su primera ejecución real rompe a todo revisor honesto. **Remedio: un byte, en uno de los dos lados, no en los dos** | `A` | `V1-01`/`V2-01`/`V3-01` · **SÍ** · **REBAJADO por mí de GRAVE a MEDIO**: ver §2.1 |
| **`V-06`** | **`T147` en ROJO y runner 12/13 por el manifiesto que ESTE gate añadió — y el índice AFIRMA HOY que da verde** | `00-INDICE` **L121**, **L130-146**; el manifiesto de este gate | **Reatribuido ejecutando los validadores sobre los DOS árboles** (§7). Candidata `21f1ccb`: `T147` **SUPERADA**, runner **13/13**. Gate `f2e4d58`: `T147` **FALLIDA**, runner **12/13**, único huérfano = el manifiesto de este gate. Es la **reincidencia literal de `S-18`≡`T-14`**, contra la regla que el propio índice L146 declara «vale para el gate siguiente igual que para éste» — y **el comando que L139-141 publica denuncia el huérfano**, mientras L144-146 asegura que da verde | `A` | `V3-04` · **SÍ**, sobre copias fuera del repo |
| **`V-07`** | **la obligación 7 del revisor manda obtener del derivador una cifra que el derivador no produce; el campo 12 es una aserción no contrastada del coordinador** | doc 11 **L8210-8212** contra **L8177-8178**; `emitir-sobre-de-ancla.py` **L121** y **L152** | Ejecuté el derivador: publica fuentes y líneas, **ninguna cifra de asignaciones**. El emisor la recibe por `--asignaciones`, `required=True`. **El único campo del sobre que nada contrasta es una afirmación del coordinador, dentro de un mecanismo cuya razón de ser es no tener que fiarse de él** | `A` | `V2-04` · **SÍ**, ejecutado |
| **`V-08`** | **la propagación de `O18` no deja NI UNA comprobación mecánica, y es la única sede cuya violación invalida un gate entero** | batería (3 139 líneas), contra doc 11 **L8101-L8528** | `grep -c -i 'sobre de ancla\|O18\|11\.[678]\|X-O'` sobre la batería → **0**. Toda tanda anterior dejó rastro: `I-21`→`G-25`, `O17`→`G-32`/`G-33`. Ésta no. Y `V-01`…`V-05` y `V-07` son justo lo que una fila `G-nn` habría cazado antes de repartir el encargo | `A` | `V2-05` · **SÍ**, por barrido |
| **`V-09`** | **«Seis pasos, en este orden» sobre una cadena de OCHO, en la sede que fija el orden crítico del que dependen las fronteras de ventana** | doc 11 **L2000-2002**, contra el paso `E` **L1965-1977** y el punto 7 **L2046-2060** | La cadena enumera ocho operaciones separadas por `→`; el rótulo dice seis. Sólo cuadra colapsando los dos pares de `fsync`, que es como numera el paso `E`. **Y no es cosmético: `W11`=`[1,2)`, `W17`=`[2,4)`, `W8`=`[4,6)` están escritas en esa numeración.** Un implementador que numere por la cadena mueve la frontera `W17`/`W8` un paso — que es el defecto `P-01` que esta tanda dice haber cerrado | `A` | `V1-05` · **SÍ**, conté los `→` y leí las tres sedes |
| **`V-10`** | **la regla de titulares de §0 se declara «sin excepción» y NO TIENE GUARDIÁN: 25 titulares del tramo la incumplen y tres cardinales ya caducaron** | doc 11 **L145-176**, contra L1-L5600 | **Respondo la pregunta del coordinador: es una declaración sin guardián.** Barrí la batería: `titular`/`cardinal` sólo aparecen en `G-16`, `G-17` (dos matrices concretas) y `G-10` (§5.2). **Ninguna comprobación barre los titulares del documento.** La regla permite el cardinal sólo si lo deriva un comando o lo contrasta la batería; **una sola sede del tramo cumple esa condición** (L5119-5126, por `G-10`, y es correcta). Las otras 24, no | `A` | `V1-12` · **SÍ**, y verifiqué la cobertura de la batería |
| **`V-11`** | **«las cuatro alternativas, comparadas» sobre una tabla de CINCO, y la quinta es la garantía adoptada** | doc 11 **L2606**, tabla L2608-2614 | Filas `A`–`E`. La `E` no es un añadido despistado: se cita «**ADOPTADA COMO GARANTÍA `C`**» y §2.6.9 depende de ella. No cae en ninguna de las cuatro excepciones de §0. `grep`: L2606 es la única sede, luego nada la corrige | `A` | `V1-03` · **SÍ**, conté la tabla |
| **`V-12`** | **«con las cuatro preguntas respondidas» sobre un bloque de CINCO rúbricas** | doc 11 **L3235**, bloque L3237-3266 | Cinco rúbricas en columna 0, contadas por mí. La quinta —«QUÉ ES EXACTAMENTE APPEND-ONLY, Y QUÉ NO»— **la añadió `D63`** sin pasar por la frase que las cuenta: el mecanismo exacto que §0 describe | `A` | `V1-09` · **SÍ** |

### MENORES — once

| id | qué es | fichero · línea | clase | origen |
|---|---|---|---|---|
| **`V-13`** | «Se enumeran las **DIECIOCHO**» escrito en la misma frase que jura derivarlo y no escribirlo. La cifra es correcta hoy (conté 18 filas `W`); ninguna comprobación la mira: `G-26` sólo contrasta el numeral de la fila `X` que manda barrerlas | doc 11 **L1213-1214** | `A` | `V1-04` · **SÍ** |
| **`V-14`** | «las nueve señales del §16» apunta al §16 de OTRO documento: el §16 de éste es «Presiones normativas para F5» (L9189). Las nueve señales viven en `09-SINTESIS.md` | doc 11 **L3821** | `A` | `V1-10` · **REBAJADO por mí de MEDIO**: `09-SINTESIS` las numera como fila 16 de una tabla, y el doc 20 L479 ya leyó la referencia sin tropezar |
| **`V-15`** | la columna de disparo de `W8` dice «tras `derivada`» y su cuerpo reclama tramos de la ruta de **abandono** | doc 11 **L1238** | `A` | `V1-11` · **REBAJADO por mí de MEDIO a MENOR, y digo por qué:** el punto 7 de §2.6.9 —que la propia fila declara que MANDA— dispara `W8` por «hay `abandonada` y `deriva` durables y marcador puesto», **sin nombrar `derivada`**. **La partición NO tiene hueco**, lo verifiqué tramo a tramo. Lo elíptico es la columna |
| **`V-16`** | «un barrido literal sobre todo `docs/` devuelve UNA sola aparición» es falso: devuelve **cuatro, en tres ficheros**, y la cuarta es la propia frase que lo niega | doc 11 **L1635-1636** | `A` | `V1-06` · **REBAJADO de MEDIO**: está dentro de un bloque de cita de un gate anterior, aunque **no rotulado `[HISTÓRICO]`**, que es lo que le falta |
| **`V-17`** | la condición anti-caducidad de `P-16` —`grep -n 'desenlace .4b.'`— admite **un** carácter entre las dos palabras; la forma que el documento usa para destacar, `desenlace **`4b`**`, tiene tres. **No vería una reincidencia en negrita**, que es la tipografía dominante | doc 11 **L2185-2187** | `A` | `V1-07` · **SÍ** |
| **`V-18`** | «Y el **la** secuencia `4b` no es terminal», con la frase partida en dos renglones huérfanos: residuo vivo de la sustitución mecánica de `P-16` | doc 11 **L2306** | `A` | `V1-08` · **SÍ**. Es hermano de `S-24`, que sí se cerró |
| **`V-19`** | §19 declara «*Cada familia lleva su cifra en SU sede y aquí se remite*» y **copia cuatro cardinales en la misma frase** | doc 11 **L10402-10415** | `A` | `V2-06` · **SÍ** |
| **`V-20`** | predicado sin sujeto en §19 —«…**están ESCRITOS.** Ninguno se ha ejecutado»—: la nota de corrección insertada en medio partió la oración que abría en L10402 | doc 11 **L10415-10416** | `A` | `V2-07` |
| **`V-21`** | **`S-25` del documento 23 NO está cerrado**: la fila `D107` sigue citando las reglas 7-10 de `O17` y no remite a §9.6, donde están las doce | `DECISIONES` **L505** | `A` | mío, al comprobar cierres |
| **`V-22`** | **`S-23` del documento 23 NO está cerrado**: las cuatro ramas del punto 7 de §2.6.9 siguen sin declarar precedencia. `(abandonada` durable, `deriva` ausente, marcador retirado`)` satisface la rama 2 y la 4 | doc 11 **L2046-2060** | `A` | mío, al comprobar cierres |
| **`V-23`** | el manifiesto de este gate encabeza «*Todo derivado del árbol `b498f3b…`, nada copiado*» y su fila 8 es del árbol del gate. **Lo registro como HECHO de mi `V-01` y NO lo cuento aparte**: el manifiesto es lote de `W` | manifiesto §4, fila 8 | `A` | mío |

```
RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA
  BLOQUEANTE   0
  GRAVE        3    V-01 · V-02 · V-03
  MEDIO        9    V-04 … V-12
  MENOR       11    V-13 … V-23
              ──
              23        clase A 23 · clase B 0 · clase C 0
```

**Cuántos los introdujo ESTA tanda.** `V-01`, `V-02`, `V-03`, `V-04`, `V-05`, `V-06`, `V-07`
y `V-08` — **ocho de veintitrés, y son los ocho más graves**. Todos nacen de la propagación
de `O18` o del aparato que este gate estrena. `V-09`…`V-20` son deuda anterior que la regla
de §0 no llegó a barrer.

**NINGUNO de mis 23 se apoya en `C`.** Lo digo expresamente: el Owner ha resuelto que `C` no
es exigible como implementación dentro de `F4c`, y **no declaro insuficiencia por `C`**.
`V-01` es `B`; el resto es `A`.

---

## 7 · HALLAZGOS QUE RECHAZO DE MIS PROPIOS RELEVOS, CON EVIDENCIA

**`V3-07` · RECHAZADO.** `V3` sostuvo que la segunda de «LAS DOS ADVERTENCIAS, Y SON DEL
OWNER» (checkpoint L2770) no tiene base en `O18`. **La tiene, y es literal.** La advertencia
dice que `B` no se da por satisfecha «*porque el repositorio AFIRME que el sobre existió*».
`O18`, alternativa `(b)`: «**El revisor verifica contra lo que RECIBIÓ, no contra el árbol.**»
Es la misma proposición. **La atribución al Owner es correcta para las dos advertencias.**

**`V3-09` · RECHAZADO.** `V3` levantó el bloque `ESTADO VIGENTE` (checkpoint L2542) por
tener campos caducados sin rótulo. **Lo leí entero y es lo contrario: es ejemplar.** Sus
campos caducados llevan `**[HISTÓRICO · …]**` con el motivo y el hallazgo que lo levantó
(`Q-14`/`Q-16`); y `ÁRBOL VIGENTE` **se niega expresamente a escribir su SHA** — «*escribirlos
crearía una segunda fuente de verdad que además envejece a cada commit*» — y remite a
`git rev-parse`. **No hay defecto.**

**`V3-02` y `V3-03` · CONFIRMADOS EN EL HECHO, RECHAZADOS EN LA IMPUTACIÓN, y FUNDIDOS en
`V-04` con severidad REBAJADA.** No son dos hallazgos ni son GRAVES ni hay ocultación: el
mensaje de `78ec1cc` **anuncia** la edición de `D92`, ninguna resolución se tocó, y el índice
ya publica la fórmula correcta. Lo que queda, y es real, es **una frase falsa viva en L498**.
Evidencia en §5.

**`V1-01`/`V2-01`/`V3-01` · REBAJADOS de GRAVE a MEDIO** (`V-05`). Los tres calificaron el
salto de línea como GRAVE porque «manda invalidar un gate válido». **El hecho es cierto; la
severidad no.** Un instrumento que da rojo sobre todo árbol no invalida nada: se arregla. Lo
GRAVE del sobre está en otro sitio, y es `V-01`. Razones en §2.1.

**`V1-11` · REBAJADO a MENOR** (`V-15`), **`V1-10` y `V1-06` · REBAJADOS a MENOR**
(`V-14`, `V-16`). Motivos en la tabla de §6, cada uno con la sede que lo atenúa.

**Y una imputación de `V1` que corrijo aunque no cambie su hallazgo:** `V1-02` describió el
problema del árbol como «el sobre calcula el digest contra otro árbol». Es correcto pero se
queda corto: **no es que se calcule contra otro árbol, es que los dos campos son
insatisfacibles a la vez y la causa es que el derivador está dentro de su propio universo.**
Por eso lo elevé en vez de confirmarlo.

---

## 8 · LOS HALLAZGOS DEL DOCUMENTO 23 EN MI FOCO

Leí el documento 23 **íntegro** (2913 líneas, SHA-256 `0f81f13d8cb319d8…` recalculado por
mí). Tiene **49 hallazgos distintos, 48 de clase `A`**. Mi foco —arquitectura, protocolo,
`O17`/`O18`, registro, checkpoint, `C-L`— es la serie **`S-01`…`S-26`**. La serie
**`T-01`…`T-22`** y **`U-01`** son batería, derivador, emisor y manifiestos: **foco de `W`,
y NO los adjudico.** `U-02` es el manifiesto: **tampoco.**

| id | materia | mi veredicto | evidencia con la que lo cierro |
|---|---|---|---|
| `S-01` | §18 da a `SEG` «vía 3» en `proceso:SIS` | **CERRADO** | las cuatro filas `FASE 0` (L10322·10325·10330·10333) dicen hoy «**`SEG` sin vía: `PN-13`** — y **conserva su bloqueo**, que es lo ÚNICO que `O17` le da», con nota de corrección |
| `S-02`…`S-05` | FASE 0 no ejecutable · Operativa sin productor en `M` · recuento `2·4·2·4` · FRENO 3 | **CERRADOS**, verificados por muestra en las sedes que `S` citó; `S-05` lo doy cerrado por la reescritura de §8.0 que sí abrí. **Declaro que NO los reproduje uno a uno**: ver §10 |
| `S-06` | cifras del addendum de `D97` | **CERRADO** | `DECISIONES` L389: «*documento 11 — **RETIRADA**. Aquí NO va ninguna cifra, y es deliberado*» |
| `S-07` | nivel `completo` sin productor | **CERRADO, y ejemplarmente** | L7302-7311: «*SIN PRODUCTOR DECLARADO, **y se dice en vez de taparlo** … resolverlo aquí sería **ampliar una resolución del Owner: no se amplía**, y queda como trabajo futuro*». **Es la conducta que §11.8 debió tener: lo uso como prueba en §4.4** |
| `S-08` | §14 sin la propagación de `D107` | **CERRADO** | `FASE 0` presente hoy en las filas de §14 (L8680-8683) |
| `S-09` | dos reglas de precedencia solapadas | **CERRADO CON MECANISMO** | L7527-7538: jerarquía explícita —«**§18 manda sobre el MAPEO … ESTA SEDE manda sobre el CONTENIDO DEL CONTRATO** … y no hay tercera cosa»—, con la divergencia de `S-01` resuelta por la regla y la frase replicada en §8.0 |
| `S-10` | «Las siete secuencias» sobre ocho | **CERRADO** | L2350: «*Las secuencias completas, **una por rótulo del bloque de abajo***» — cardinal retirado |
| `S-11` | «Los CUATRO puntos anteriores» sobre cinco | **CERRADO** | la frase ya no existe en el documento |
| `S-12` | «Los cuatro casos» sobre seis | **CERRADO** | L4130: «*Los casos que la prueba obligó a separar … **todos los que el bloque de abajo***» |
| `S-13` | «las CUATRO fichas» sobre seis, y `DSP`/`ENC` sin declaración | **CERRADO, y en lo sustantivo** | L5183 remite («*alguna de las fichas de arriba*»), y L5186-5187 declara **`ENC` expresamente**: «*Para `ENC` no se afirma ni lo uno ni lo otro: **se declara sin comprobar**»*, con propietario y fase |
| `S-14` | el barrido de `P-16`, incompleto | **CERRADO, y bien** | el cardinal «Seis sedes» va rotulado **`[HISTÓRICO]`** y se sustituye por una **condición** que no caduca. `grep -n 'desenlace .4b.'` → 2 líneas, **las dos dentro de la propia nota**. *(Su condición tiene una debilidad: `V-17`.)* |
| `S-15` | el enum de `fase` contradice a su matriz | **CERRADO** | L4337-4338: «*ESTADOS DEL CAMPO `fase` 6 — las CINCO fases, **más la AUSENCIA del campo. La ausencia no es un sexto valor del enum: es que el campo no está***», y `orden` queda `CONDICIONAL` |
| `S-16` | «30/30» bajo rótulo `ESTADO VIGENTE` | **CERRADO, y bien** | L2630-2643: número **retirado**, comando publicado, `[ESTADO ANTERIOR]` con el id del hallazgo y la razón: «*No se sustituye 30 por 37: **se retira el número y se remite al comando**»* |
| `S-17` | «Siguiente acción exacta» caducada | **CERRADO** | una sección vigente (L2783) y **tres rotuladas `HISTÓRICA`** (L2940, L3087, L3227). Su paso 5 describe el estado real de hoy |
| `S-18`≡`T-14` | manifiesto sin enlazar · `T147` en rojo | **NO CERRADO · REINCIDENTE** | la regla se escribió y **se volvió a incumplir en el gate siguiente**. Es mi `V-06`. *(La mitad «manifiesto» toca a `W`; adjudico la parte que el coordinador me encargó: la reatribución, hecha sobre los dos árboles.)* |
| `S-19` | `D107` bajo epígrafe ajeno | **CERRADO** | L482: `### D107 · la propagación de O17 —` epígrafe y preámbulo propios |
| `S-20` | `D97` sin puntero al addendum | **CERRADO — y el remedio abrió `V-04`** | el marcador ▲ está en L346. Ver §5 |
| `S-21` | §0 escribe el cardinal que dice remitir | **CERRADO** | «DIECISÉIS» ya no aparece en el documento 11 |
| `S-22` | prefijo `X` con dos poblaciones | **CERRADO** | L386-390: nota que reconoce el riesgo y **escribe la condición** para la prueba que `D83` contrata a `F6` |
| `S-23` | las cuatro ramas del punto 7 no son disjuntas | **NO CERRADO** | leí el punto 7 entero (L2046-2060): sigue sin declarar precedencia. Es mi `V-22` |
| `S-24` | «Y el secuencia `4b`» | **CERRADO** en L2230 · **pero el gemelo de L2306 sigue vivo**: mi `V-18` |
| `S-25` | la fila `D107` no remite a las doce reglas | **NO CERRADO** | L505 sigue citando 7-10. Es mi `V-21` |
| `S-26` | el motivo del Owner en `O17`, inverificable | **CERRADO, y con honradez** | `DECISIONES` L765: se declara «**INVERIFICABLE**», sin inventar una cita ni retirar la que hay |

```
EN MI FOCO (26)     CERRADOS 22   ·   NO CERRADOS 4  (`S-18`, `S-23`, `S-25`, y el gemelo de `S-24`)
FUERA DE MI LOTE    `T-01`…`T-22`, `U-01`, `U-02`  —  23, foco de `W`. NO ADJUDICADOS.
```

**Mi juicio sobre la tanda, y consta a favor:** de los 26 de mi foco, **22 están cerrados, y
varios lo están MEJOR de lo que el hallazgo pedía** — `S-09` con una jerarquía en vez de un
parche, `S-14` y `S-16` retirando el número y publicando el comando en vez de actualizar la
cifra, `S-13` y `S-26` diciendo lo que no se comprobó en vez de afirmarlo. **Ésa es la
conducta correcta, y la tanda la exhibe.** Lo que no exhibe es lo mismo en §11.8.

---

## 9 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

**`R-1` · Intenté demostrar que el defecto del sobre SÍ invalida el gate.** Si la
comprobación 7 falla y la obligación 9 manda fallar cerrado «ante CUALQUIER diferencia»,
el gate es inválido y no hay más que hablar. **No cayó, y por el lado del hecho:** verifiqué
que el universo tiene **exactamente** las 67 fuentes y las 53 772 líneas del sobre, y que su
digest se reproduce **byte a byte** con la fórmula que el emisor usa. La diferencia está en
la receta impresa, no en el objeto. Invalidar aquí sería declarar corrupto un corpus que
demuestro intacto. **Lo que sí encontré por el camino fue `V-01`**, que es un problema del
sobre de otra naturaleza — y ése no lo arregla ningún byte.

**`R-2` · Intenté salvar la propagación demostrando que `D108` la autoriza.** `D108`(v)
manda registrar el contrato «*con propietario, ejecutor, autoridad, fase, pruebas y condición
de cierre*», y un reparto de capacidades encaja en «ejecutor». **No cayó, en dos tiempos.**
Primero: `D108` autoriza **registrar** ese contenido como derivación de F4, y el propio
`D108` se acota —«*exclusivamente el reparto de la elección por las sedes vigentes*»—; lo que
no autoriza es **rotularlo «LITERAL DE `O18`»**, que es una afirmación sobre quién lo dijo,
no sobre qué dice. Segundo: aunque «ejecutor» cubriese el reparto, **no cubre las dos
condiciones duras**, que no son ejecución sino alcance del bloqueo, y `D108` no las menciona.

**`R-3` · Intenté que `T147` fuera culpa de la candidata.** Si el rojo venía del árbol
juzgado, no sería defecto del gate. **No cayó, y lo medí en los dos árboles**: candidata
`21f1ccb` → `T147` SUPERADA, runner **13/13**, exit 0. Gate `f2e4d58` → `T147` FALLIDA,
runner **12/13**, exit 1, **único huérfano el manifiesto que este gate añadió**. La candidata
está limpia. El rojo es del aparato.

**`R-4` · Intenté que las ediciones de `D92`/`D97` estuvieran cubiertas por la excepción de
«notas de alcance».** El corpus admite addenda y punteros sin que eso rompa la integridad.
**No cayó por una palabra:** la declaración viva de L498 dice «texto **ÍNTEGRO**», no «texto
**RESOLUTIVO**». El índice sí escribe la segunda, y es la correcta. **La excepción existe;
la frase que la necesitaba no se enteró.** Por eso el remedio son dos palabras y no una
revisión.

**`R-5` · Intenté que «las cuatro alternativas» de L2606 fuese correcta.** Si la fila `E` no
fuera una alternativa de Git sino un añadido de otra materia, el cuatro sería exacto. **No
cayó:** `E` está dentro de la misma tabla, con las mismas columnas, y su veredicto es
«**ADOPTADA COMO GARANTÍA `C`**» — es la más viva de las cinco.

**`R-6` · Intenté que `O18` hubiera quedado INCOMPLETA**, que es la hipótesis que el
coordinador me pidió ponderar y que **habría invertido el remedio entero**. Si el Owner
hubiera resuelto más de lo transcrito, la propagación sería fiel y la sede a corregir sería
`O18`. **No cayó, y cayó del todo:** la pregunta que el Owner respondió está en doc 23 §13·B,
la leí entera, y **no contiene ninguna de las dos condiciones ni el reparto**. No pudo
resolver lo que no se le preguntó. Y cinco sedes de esta misma tanda —incluido el criterio
de suficiencia del checkpoint y el emisor del sobre— siguen diciendo «una condición».

---

## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **No he leído renglón a renglón las ~1 700 líneas de citas históricas del `CHECKPOINT`**
   (L120-L1768 y los bloques `[ESTADO ANTERIOR]`). Verifiqué su **estructura** —que los seis
   `[ESTADO ANTERIOR]` y los tres `[HISTÓRICO]` están rotulados y delimitados— y leí íntegro
   el tramo vigente. **Un defecto de contenido dentro de una cita histórica se me habría
   escapado.** Es el hueco más grande de mi cobertura y no lo disimulo con la resta.
2. **`S-02`, `S-03`, `S-04` y `S-05` los doy por cerrados sin reproducirlos uno a uno.** Abrí
   las sedes de `S-01`, `S-07`, `S-08` y `S-09` y las verifiqué; para esos cuatro me apoyo en
   que sus sedes están reescritas y en la coherencia del conjunto. **No es lo mismo que
   haberlos derivado.**
3. **No he leído el documento 11 con mis ojos.** Sus 11 176 líneas las leyeron `V1` y `V2`.
   Yo abrí y verifiqué **las sedes concretas** de cada hallazgo que confirmo, rebajo o
   rechazo — unas cuarenta— y las de los cierres de §8. **Ningún ojo único ha recorrido ese
   fichero entero**, y el manifiesto del gate lo declara (§3, «el coste de las cadenas»).
4. **No he juzgado la batería, el derivador, el emisor como código, ni los manifiestos.** Son
   lote de `W`. Los ejecuté o los `grep`eé como instrumento de mis propias comprobaciones, y
   **cada vez que lo hice lo declaro en la fila del hallazgo**. `V-05` y `V-07` tocan el
   emisor: los emito porque el defecto que describo es del **mecanismo que `O18` adopta**,
   que sí es mi materia, y no del fichero como pieza de software.
5. **No he verificado ninguna cita que mis fuentes hacen de material APROBADO** —`a.6`,
   `a.7`, `b.16`, `C7`, `KERNEL.md`—. Las he leído como afirmaciones de mis fuentes, no como
   hechos. Toca a `V-04` (la cita de `a.6` L502-503) y a mi §8.
6. **No he comprobado los 48 remedios de clase `A` del documento 23 fuera de mi foco**, ni el
   recuento de 49 contra sus fuentes: acepto el consolidado de `U` §12.
7. **`V-08` lo derivé por barrido, no leyendo la batería entera.** Que no haya ninguna
   comprobación sobre `O18` lo afirmo por `grep` sobre 3 139 líneas; **un control escrito sin
   nombrar `O18` ni sus secciones no lo habría visto.**

---

## 11 · MI RECOMENDACIÓN DE VEREDICTO

# INSUFICIENTE PARA F5

### Las razones, numeradas. La primera basta por sí sola.

**1 · La afirmación `B` —lo único que este gate estrena— NO queda demostrada, y falla por el
sobre mismo.** El criterio que el corpus escribió para juzgarse (checkpoint L2755) exige que
el sobre demuestre que se analizó «EXACTAMENTE el commit, el árbol, el manifiesto y el
universo ENCARGADOS». **El sobre publica un árbol del que no salen ni su universo ni su
derivador, y no publica el que sí.** Sus campos `ARBOL` y `DIGEST` son **mutuamente
insatisfacibles**: la candidata da 65 fuentes y `9490d6a3`; el digest publicado es el del
árbol del gate, 67 fuentes. Y la causa no es un descuido: **el derivador está dentro del
universo que deriva**, de modo que tocarlo tras publicar la candidata rompe el sobre por
construcción. El manifiesto y el mensaje del commit repiten la atribución falsa. `V-01`.

**2 · La propagación ha ampliado una resolución del Owner y se la ha atribuido a él, y por
`PN-19` se la va a devolver firmada.** `O18` puso **una** condición previa; la propagación
escribe **tres** en seis sedes, y rotula «LITERAL DE `O18`» un reparto de capacidades y una
prohibición que `O18` no contiene. **Refuté la salida honrosa**: no es que `O18` quedara
corta, porque **la pregunta que el Owner respondió —doc 23 §13·B— tampoco lo contiene**. Es
el mismo defecto que el gate anterior adjudicó a §18 sobre `O17`, un gate después, y esta vez
en la sede que va al Owner. Y el propio documento demuestra que sabe hacerlo bien: a mil
líneas de allí se niega a resolver el productor del nivel `completo` «*porque sería ampliar
una resolución del Owner*». `V-02` y `V-03`.

**3 · El mecanismo que `O18` adopta se estrena roto, sin un solo control mecánico, y con un
campo que nadie contrasta.** La receta publicada del sobre **no puede** reproducir su propio
digest (`V-05`); la obligación 7 manda obtener del derivador una cifra que el derivador no
produce, y ese campo acaba siendo **una aserción del coordinador dentro de un mecanismo cuya
razón de ser es no fiarse del coordinador** (`V-07`); y la batería **no tiene ni una
comprobación** sobre las tres sedes de `O18` —la única cuya violación invalida un gate
entero— cuando toda tanda anterior dejó su rastro mecánico (`V-08`). `§11.7` declara `B`
«implementada»: está **escrita**.

**4 · La regla que esta tanda escribió para cerrar el defecto más repetido del expediente no
tiene guardián, y ya ha caducado tres veces dentro del propio documento que la promulga.**
§0 la declara «sin excepción»; barrí la batería y **ninguna comprobación la vigila**. En el
primer tramo del documento hay 25 titulares que la incumplen, **una sola sede cumple la
condición que la propia regla exige**, y tres cardinales ya son falsos: cinco alternativas
bajo «cuatro», cinco rúbricas bajo «cuatro», ocho pasos bajo «seis» — este último **en la
sede que numera las fronteras de ventana que `P-01` acaba de cerrar**. `V-09`…`V-13`.

**5 · La regla de publicación se incumplió en el primer gate que la recibió, por segunda vez
consecutiva, y el índice afirma hoy lo contrario.** `T147` está en ROJO y el runner en 12/13
**por el manifiesto que este gate añadió** — lo reatribuí ejecutando los validadores sobre
los dos árboles: la candidata está en 13/13 y verde. El índice L146 escribió «*la regla vale
para el gate siguiente igual que para éste*»; L144-146 asegura que su comando «*da `T147` en
verde*»; **lo ejecuté y denuncia un huérfano**. `V-06`.

### Lo que expresamente NO fundamenta mi recomendación

· **NO fundamento nada en `C`.** El Owner ha resuelto que la resistencia a un actor
  privilegiado no es exigible como implementación dentro de `F4c` y es contrato obligatorio
  de `F6`. **Comprobé que el corpus la trata bien**: `C` se declara NO IMPLEMENTADA, no se
  presenta como capacidad existente, y **no encontré ni una sede que presente `(b)` como
  `(c)`** — la prohibición de §11.7 L8369-8372 se cumple. Mi objeción a §11.8 es de
  **atribución**, no de que afirme tener `C`.
· **NO fundamento nada en `M-04`**, ni en la batería, ni en el derivador, ni en los
  manifiestos como tales: son foco de `W` y no los he adjudicado.
· **NO fundamento nada en el salto de línea del sobre.** Decidí expresamente que es un
  defecto del instrumento (§2.1). Cuenta como `V-05`, MEDIO, no como invalidez.
· **NO declaro el gate INVÁLIDO.** El objeto está identificado —66 de las 67 fuentes son
  idénticas en los dos árboles y el corpus leído no está en duda— y por eso emito dictamen de
  contenido en vez de parar. **Que `B` no esté demostrada es una insuficiencia, no una
  invalidez**, y la diferencia importa: un gate inválido no produce veredicto, y éste sí.

### Lo que consta a favor, y no es cortesía

De los 26 hallazgos del documento 23 en mi foco, **22 están cerrados**, y varios mejor de lo
que el hallazgo pedía: `S-09` cerró con una **jerarquía** en vez de un parche; `S-14` y
`S-16` **retiraron el número y publicaron el comando** en vez de actualizar la cifra; `S-13`
y `S-26` **declararon lo que no se había comprobado** en vez de afirmarlo; `S-07` **se negó a
ampliar una resolución del Owner** con todas las letras. `R-04` sigue cerrado y verifiqué la
partición de ventanas sin hueco ni solape. La batería da **38/38 en verde** sobre el árbol
real y **falla cerrado sin `git`** en sus ocho comprobaciones que lo necesitan — lo comprobé
sin querer, al ejecutarla sobre copias sin `.git`, y es el comportamiento correcto.
**El trabajo es bueno. Lo que falla es lo que esta tanda estrenó.**

### Y lo que recomiendo que se haga, porque el remedio está determinado

**Los 23 son de clase `A`.** Ninguno obliga a decidir arquitectura y ninguno vuelve a la
clase `B` del documento 23, que `O18` cerró. El más importante, `V-01`, se corrige con una
regla de una línea que el corpus no tiene y necesita: **el sobre publica el árbol del GATE
junto al de la candidata, o el gate no toca el derivador después de publicar la candidata.**
Las dos valen; **una de las dos hay que escribirla**, porque hoy el mecanismo es
irreproducible por construcción.

---
**Tú RECOMIENDAS. El veredicto lo emite el adjudicador `X`.** — `V4`

---

# §B · DICTAMEN DEL REVISOR `W`, LITERAL

# DICTAMEN DEL REVISOR `W` — TERCER GATE DE CERTIFICACION DE F4c
## Emitido por `W3`, DICTAMINADOR de la cadena `W` · RELEVO

```text
REPOSITORIO     /home/jose/ads-kernel
RAMA            gate/f4c-certificacion-3-20260830
HEAD            f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0   (identico al abrir y al cerrar)
FECHA           2026-08-30
INTERPRETE      python3 del shim del scratchpad
LABORATORIO     /tmp/lab-W3/{cand,gate,der,der2,bat,emisor,fakebin} — BORRADO al cerrar
RECOMENDACION   INSUFICIENTE PARA F5   (el veredicto lo emite el adjudicador `X`, no yo)
```

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `W3`, dictaminador del REVISOR `W`. **Soy un RELEVO**: un `W3` anterior fue interrumpido
por limite de sesion con el trabajo a medias y dejo un `DICTAMEN-W.md` parcial (secciones 1, 2
y una 4 incompleta). **Lo lei y lo he REESCRITO ENTERO.** Nada de lo que aquel `W3` afirmo entra
en este dictamen sin que yo lo haya vuelto a ejecutar con mis manos. Lo que reutilizo es
**la estructura y la lista de vectores que hay que atacar**, no ninguna conclusion.

**Que reutilice, literalmente, y que rehice:**

```text
REUTILIZADO      la enumeracion de experimentos (E1, E1b, E2, E4, E5, E8) y la de los
                 ataques al emisor y al derivador. Es una lista de tareas, no una prueba
REHECHO POR MI   TODOS los experimentos, sobre laboratorios nuevos creados por mi
                 (`git archive` y `git clone` propios), con su salida pegada abajo
AÑADIDO POR MI   E2 y E2b (la valla), que el `W3` anterior NO llego a ejecutar y que son
                 mi hallazgo mas fuerte; el ataque al fixture `_FIX_BLOQUE` de `G-31`;
                 la segunda grieta del componente (iv) del derivador; la verificacion
                 mecanica de las 67 filas y de los 54 agotamientos del manifiesto; y la
                 comprobacion de `T147` sobre el arbol de HOY
```

**Que NO he visto.** **No he abierto `V1.md`, `V2.md`, `V3.md` ni `DICTAMEN-V.md`.** Constan en
el directorio de notas y no los he leido. Ninguna afirmacion de este dictamen procede del
revisor `V`, y no adjudico nada de su foco.

**Que NO soy.** No he escrito ninguna parte de este corpus, no he aplicado ninguna correccion,
no participe en ningun gate anterior y no fui revisor de ninguno.

**No he usado el subagente `Agent`.** Todo el trabajo es mio, con `bash`, `git`, `grep`, `sed`,
`awk` y el `python3` del shim.

**El ORDEN se respeto, y es la garantia de que este dictamen busca en vez de confirmar.**
Lei `W1.md` y `W2.md` enteros; despues verifique el SOBRE y **reproduje con mis manos** los
arboles y los ataques; y **solo entonces** abri el documento 23. Ningun experimento mio esta
informado por lo que el documento 23 dice de si mismo.

**Modo, comprobado en los dos extremos:**

```text
git status --porcelain  AL ABRIR   → SALIDA VACIA   (primer comando de la sesion)
git status --porcelain  AL CERRAR  → SALIDA VACIA   (ultimo comando de la sesion)
HEAD al abrir y al cerrar          → f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0, identico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MI   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
```

Todos los experimentos van sobre copias fuera del repositorio: `git archive` de cada commit
para el derivador, y `git clone` con checkout para la bateria y el emisor.

---

## 2 · EL SOBRE · MI DECISION EXPRESA SOBRE SU VALIDEZ

### 2.1 · Lo que verifique yo, campo a campo

```text
git ls-remote origin refs/heads/review/f4c-o18-candidate-20260830
      → 21f1ccbda82e7a3ad5e3b3ecf3c7b1bfe374a1d5                       COINCIDE
git ls-remote origin refs/heads/review/f4c-gate-certificacion-3-20260830
      → f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0                       COINCIDE
git rev-parse 21f1ccb^{tree}  → b498f3b8ae8a70510b68feefe592f502cf8e1a86  COINCIDE
git cat-file -t de los dos commits → commit · commit                   COINCIDE
git show f2e4d58:<manifiesto> | sha256sum → ac9e0edd…4988               COINCIDE
git show f2e4d58:<derivador>  | sha256sum → 6f8c98a2…4bd0               COINCIDE
FUENTES 67 · LINEAS 53772, derivadas sobre el arbol del GATE           COINCIDEN
ASIGNACIONES 18 · 13 filas de §4 + 5 bloques de §5 del manifiesto      coherente
```

**Y el sobre es RECONSTRUIBLE.** Clone limpio en `/tmp/lab-W3/emisor`, checkout `f2e4d58`,
`origin` apuntando al remoto real, y reemiti el sobre: **las trece filas sustantivas salen
identicas**, campo por campo, salvo la marca de tiempo. El mecanismo hace lo que dice.

### 2.2 · `W-12` · la receta publicada NO reproduce el digest publicado — CONFIRMADO POR MI

```text
receta LITERAL del sobre (emisor L161-162), sobre el arbol del gate
   6e2f90f2dcd1c12c4abce57ab9da51ff329e57753e5a3e77f260ddcb834b656c
el sobre declara
   19ac25512933ddbb6db928a6de4eefb9589494e210ad2202da870b962e4620e9
la MISMA receta con `| head -c -1 |` antes de `sha256sum`
   19ac25512933ddbb6db928a6de4eefb9589494e210ad2202da870b962e4620e9   COINCIDE
```

**Causa, leida en el codigo.** L112: `hashlib.sha256("\n".join(filas)…)` — `"\n".join` no emite
salto final. La tuberia de L161-162 lo emite (un `echo` por linea). **Un byte `0x0A`.**

**Lo que significa:** el revisor que siga la receta al pie de la letra **falla CERRADO sobre un
repositorio sano**, en el unico mecanismo que `O18` estrena. Y lo peor no es el falso positivo:
es que la receta es *la* via por la que el sobre deja de exigir confianza. Publicada rota,
enseña al revisor a desconfiar de la unica herramienta que tenia para no fiarse.

### 2.3 · `W-11` · el sobre YUXTAPONE DOS ARBOLES — CONFIRMADO POR MI CON `git archive`

Desplegue los dos commits fuera del repositorio y ejecute **el derivador de cada arbol sobre su
propio arbol**:

```text
arbol CANDIDATO  21f1ccb / b498f3b   65 fuentes · 53 354 lineas · digest 9490d6a3a1b2…
arbol del GATE   f2e4d58             67 fuentes · 53 772 lineas · digest 19ac25512933…
EL SOBRE PUBLICA                     67 fuentes · 53 772 lineas · digest 19ac2551…
delta exacto (2 rutas)  docs/evolucion/verificacion/emitir-sobre-de-ancla.py
                        …/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md
```

**Tres corroboraciones independientes, todas mias:**

```text
· el SHA-256 DEL DERIVADOR que el sobre publica (6f8c98a2) es el del GATE.
  En el commit candidato el derivador es db9c8b69ed90…  DISTINTO
· el MANIFIESTO que el sobre ancla NO EXISTE en el commit candidato:
  `git cat-file -e 21f1ccb:<manifiesto>` → fatal: Not a valid object name
· ninguna fila del sobre nombra el TREE SHA del arbol del gate
```

El sobre pone «`ARBOL (tree SHA) b498f3b…`» y, cuatro renglones mas abajo, «`DIGEST DEL
UNIVERSO 19ac2551…`». **El digest no es derivable de ese arbol.** Un lector honesto los lee como
dos hechos del mismo objeto, y no lo son.

### 2.4 · `W-10` · LA CAUSA RAIZ, y es peor que «dos arboles» — HALLAZGO MIO, EJECUTADO

El emisor **no compara dos commits: sus cifras de contenido no salen de NINGUN commit.**

```text
L126-127  commit_c / arbol_c        ← ref remota CANDIDATA        (git)
L129-130  sha_man / sha_der         ← commit del GATE             (git show)
L131      digest / fuentes / lineas ← `_universo()`
`_universo()` L98-113 ejecuta el derivador y en L108 hace
      io.open(os.path.join(RAIZ, rel))       ← EL ARBOL DE TRABAJO LOCAL
No hay `git show`, ni `git archive`, ni comprobacion de `git status`.
```

**EXPERIMENTO E-A, mio, sobre el clon limpio, con UNA fuente obligatoria ensuciada:**

```text
$ echo "LINEA FALSA INYECTADA POR W3" >> docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
$ git status --porcelain    →   ` M docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`
$ python3 …/emitir-sobre-de-ancla.py --candidata … --gate … --asignaciones 18
    ARBOL (tree SHA)     b498f3b8ae8a70510b68feefe592f502cf8e1a86   ← LIMPIO
    DIGEST DEL UNIVERSO  267fd6202d4095ffb125b732bad27bc033a922b9…  ← DEL ARBOL SUCIO
    LINEAS OBLIGATORIAS  53 773                                     ← DEL ARBOL SUCIO
    rc = 0, sin diagnostico
```

**EXPERIMENTO E-B, mio: el mismo emisor con el arbol del CANDIDATO desplegado:**

```text
    COMMIT CANDIDATO / ARBOL / SHA MANIFIESTO / SHA DERIVADOR   IDENTICOS
    DIGEST DEL UNIVERSO  9490d6a3a1b25aab3e2d1f419a808c97ad881…
    FUENTES 65 · LINEAS 53 354                                   rc = 0
```

**Conclusion, y es mia:** el digest del sobre **es una propiedad del directorio de trabajo de
quien emite**, no de ninguno de los dos commits que el sobre nombra. Que hoy coincida con el
arbol del gate es una **coincidencia operativa** —`HEAD` estaba en `f2e4d58` y el arbol limpio—,
no una propiedad del mecanismo. Y el propio emisor declara en su cabecera L43-47: «*Si una
referencia no resuelve, si el commit no existe, si el manifiesto no esta en el commit que se
declara, o si el universo no deriva, sale con codigo 2 y diagnostico. **Un sobre incompleto es
peor que ningun sobre**.*» **Aqui no falla cerrado: emite `rc=0`.**

### 2.5 · MI DECISION EXPRESA SOBRE LA VALIDEZ DEL SOBRE

> **EL SOBRE ES VALIDO COMO ANCLA DE IDENTIDAD DE LA CANDIDATA, Y NO ES VALIDO COMO PRUEBA DE
> QUE SUS CIFRAS DERIVEN DE LO QUE ANCLA. NO INVALIDA EL GATE; SI INVALIDA LA AFIRMACION
> CENTRAL DE `B`.**

Partido, porque hay que partirlo:

```text
LO QUE EL SOBRE SI DEMUESTRA, y lo verifique yo
  · que las dos refs remotas existen y resuelven a los dos commits que nombra
  · que el arbol del commit candidato es b498f3b, exactamente
  · que el manifiesto y el derivador que nombra estan en el commit del gate con esos SHA
  · que el universo obligatorio del ARBOL DEL GATE es 67 fuentes / 53 772 lineas con
    digest 19ac2551 — cifra que YO reproduje desde cero
  · que el sobre es reconstruible por cualquiera desde un clon limpio

LO QUE EL SOBRE **NO** DEMUESTRA, pese a presentarlo junto
  · que su digest, sus fuentes y sus lineas correspondan al COMMIT que ancla: no
    corresponden, y el sobre no lo dice
  · que su digest corresponda a ALGUN commit: se lee del arbol de trabajo del emisor
  · que un revisor pueda recalcularlo: la receta publicada da otra cosa
```

**Por que NO invalida el gate.** La identidad de lo que se lee esta demostrada por otra via que
yo si complete: las 67 filas del manifiesto —13 asignadas + 54 agotadas— **cuadran con el arbol
en lineas y en SHA-256 con CERO discrepancias**, `OBLIGATORIO − ASIGNADO = ∅` en las dos
direcciones, y los 54 agotamientos pasan **las dos reglas**, uno a uno (§5). El corpus que este
gate ha leido esta identificado. Lo que no esta demostrado es que **el sobre** lo demuestre.

**Por que SI es defecto de esta tanda, y de la mitad `B`.** `O18` no encarga «un documento con
SHA»: encarga **un ancla externa que el revisor pueda verificar contra lo que recibio**. Las tres
piezas de arriba son, exactamente, fallos de esa encomienda: la que el revisor usaria (la receta)
no funciona; la que el revisor leeria (digest junto a tree SHA) mezcla dos objetos; y la que el
coordinador ejecuta (el emisor) no esta atada a ningun commit. **`B` es la mitad que esta tanda
estrena, y falla en sus propios terminos.**

---

## 3 · MANIFIESTO DE LECTURA DEL REVISOR `W`

**Las nueve fuentes de `W` las fija** `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md`
(**210 lineas**, SHA-256 `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988`,
**recalculado por mi y coincidente con el sobre**): su §4 marca **W** en las filas 5, 6, 7, 8, 9,
10, 11 y 12, y **V+W+X** en la fila 3. **Son NUEVE.**

**Los nueve `wc -l` y los nueve SHA-256 los he recalculado YO**, incluidos los de las fuentes
que leyeron `W1` y `W2`. **Los nueve coinciden con el manifiesto.**

| # | ruta | lineas | SHA-256 (recalculado por mi) | leyo | cobertura |
|---|---|---|---|---|---|
| 7 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3139 | `8b4affe2a454aa15…` | **W1** | LEIDO INTEGRO · 8 tramos consecutivos, declarados |
| 6 | `docs/evolucion/verificacion/README.md` | 217 | `78d43fc34307ed34…` | **W1** | LEIDO INTEGRO · una pasada |
| 8 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 496 | `6f8c98a29edf0c31…` | **W2** | LEIDO INTEGRO |
| 9 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 174 | `e4bdba9e2985c593…` | **W2** | LEIDO INTEGRO |
| 5 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 191 | `c3eb40e4dec79f2b…` | **W2** | LEIDO INTEGRO |
| 10 | `…/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139…` | **W2** | LEIDO INTEGRO |
| 11 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27…` | **W2** | LEIDO INTEGRO |
| 12 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13…` | **W2** | LEIDO INTEGRO |
| 3 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8…` | **W3 (yo)** | **LEIDO INTEGRO**, y DESPUES de las notas y de mis experimentos |

**Mi propio lote, con detalle.** `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md`,
**2913 lineas**, SHA-256 recalculado por mi
`0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` — **coincide con la fila 3 del
manifiesto**. **LEIDO INTEGRO**, en tramos consecutivos con `sed -n 'A,Bp'`:
`1-300 · 300-341 · 340-520 · 519-531 · 530-620 · 618-626 · 624-668 · 668-790 · 790-915 ·
915-1045 · 1044-1135 · 1135-1245 · 1245-1345 · 1345-1400 · 1400-1510 · 1510-1650 · 1650-1770 ·
1770-1880 · 1880-2000 · 2000-2125 · 2125-2240 · 2240-2360 · 2360-2490 · 2490-2600 · 2600-2720 ·
2720-2830 · 2830-2913`. **Union = [1, 2913]. Ni un tramo sin abrir.**
Primera seccion sustantiva: `## 0 · Que es este documento`, **L11**.
Ultima seccion sustantiva: `## 16 · CIERRE`, **L2893**, cerrada en L2913.
**Ancla A (L3):** `> **Veredicto del adjudicador \`U\`: \`INSUFICIENTE PARA F5\`.**`
**Ancla B (L2774, a 2771 lineas):** `# INSUFICIENTE PARA F5`

### LA RESTA

```text
FUENTES ASIGNADAS A `W`            9      §4 del manifiesto, filas 3, 5, 6, 7, 8, 9, 10, 11, 12
FUENTES LEIDAS INTEGRAS POR `W`    9      W1 2 · W2 6 · W3 1
ASIGNADAS − LEIDAS INTEGRAS        0      ← CERO
```

### La reserva de cadena, declarada contra mi propio interes

**Ningun ojo unico recorrio las 3139 lineas de la bateria seguidas, ni las 2913 del documento
23.** El manifiesto declara ese coste por delante y yo lo confirmo. **Lo mitigue en la direccion
que importa para mi encargo: reabri por mi cuenta cada region de la bateria que sostiene un
hallazgo que adjudico** —`G-01` L300-390, `G-17b` L1514-1516, `G-20`/`G-21` L1536-1563,
`_VERBO_DE_CITA` L1903-1906, `G-26` L2185-2222, `_regiones_historicas` L1975-2012, `G-29`/`_ZONAS`
L2330-2360, `G-31` L2710-2795, `G-33` L3040-3137— **y ejecute cada afirmacion en vez de leerla.**
No lo elimina, y el adjudicador `X` tiene que pesarlo.

### Mi juicio sobre la independencia de `W2`

`W2` declara haber extraido **lineas sueltas** de los documentos 19–23 con `sed`, teniendo
prohibido abrirlos, para recalcular los agotamientos.

> **MI DECISION: NO compromete la independencia del REVISOR `W`, y SI acredita un defecto del
> reparto. Lo separo en tres, y la tercera va contra mi propia cadena.**

```text
1 · Los documentos 19, 20, 21 y 22 NO son fuente de lectura de nadie en este gate: son
    fuentes AGOTADAS (§5 del manifiesto). La REGLA 1 del agotamiento —«un gate anterior
    declara LEIDO INTEGRO DE ESA RUTA, con fila propia, y se cita con documento y linea»—
    **EXIGE abrir la linea citada para verificarla**. Un revisor que verifique una cita de
    agotamiento sin abrirla esta PRESUMIENDO, que es lo que la regla prohibe. Verificar 54
    citas es abrir 54 lineas. `W2` hizo lo correcto, y LO DECLARO
2 · Es el mismo caso que el gate anterior ya resolvio en la misma direccion: `T-11` del
    documento 23, confirmado por el adjudicador `U` en su `X-4`. Llego a la misma
    conclusion por mi cuenta y con la fuente delante, no por seguirla
3 · Y AQUI VA LA PARTE QUE ME CUESTA: el documento 23 **NO es fuente agotada**. Es la fila 3
    de §4, asignada a `V4`, a `W3` y a `X`, con la nota expresa «**DESPUES de las fuentes**».
    Si `W2` extrajo lineas del documento 23 —y el aviso del coordinador dice 19–23—, eso
    NO es verificar un agotamiento: es abrir, parcialmente y fuera de orden, MI lote
```

**Consecuencia que saco, y la acoto.** La independencia **de este dictamen** no esta
comprometida: **yo lei el documento 23 integro, yo mismo, despues de las notas y despues de mis
experimentos**, y ninguna de mis adjudicaciones toma nada de `W2` sobre el. Pero el hecho consta
como **defecto del REPARTO** —`W-17`, MENOR—: el encargo de `W2` le pidio recalcular una regla
cuyo material vive en fuentes que tenia prohibido abrir, y no acoto la prohibicion a las
agotadas. **Es la tercera vez que este expediente comete la misma clase** (`C-2` del gate del
documento 21, `T-11` del gate del documento 22, y esta).

---

## 4 · `M-04`: LO QUE REPRODUJE YO — experimento a experimento

**Laboratorio.** `/tmp/lab-W3/bat`: `git clone` del repositorio + `git checkout f2e4d58`.
**BASELINE verificado por mi:** `38/38 comprobaciones en verde`, `EXIT=0`, porcelain vacio.
SHA-256 de la bateria en el laboratorio = `8b4affe2…`, identico al del arbol bajo juicio.

**LA REGLA DE CLASE QUE APLICO, declarada por delante**, porque es lo que decide el veredicto:

```text
CLASE A   la bateria, sobre un arbol que se le entrega, NO detecta una incoherencia que
          ESTA en ese arbol — sin que el atacante toque la bateria, su README, `HEAD`, las
          refs, la revision base ni el runner. Es un fallo de COHERENCIA INTERNA
CLASE B   el aparato que dice demostrar QUE se analizo no lo demuestra
CLASE C   el atacante tiene que corromper la REFERENCIA: commitear para que `HEAD` la
          absorba, reescribir la base, editar la bateria y su README a la vez, o mentir el
          runner. `O18` la declara NO implementada y la contrata para `F6`. **No la cuento
          como defecto de esta tanda**, y por eso NO adjudico `T-01` ni `T-02`
```

---

### `E1` · borrar la fila `| O5 |` del registro de decisiones → **38/38 VERDE** · **CLASE A**

```text
$ sed -i '521d' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
$ grep -c '^| O5 |' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   →  0
$ git status --porcelain   →   ` M docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
    OK   G-21    `O1`-`O16` intactas frente a `7e99388` (y falla CERRADO si git no responde)
                 └─ ninguna difiere
    38/38 comprobaciones en verde                                          EXIT = 0
```

**CAUSA, leida en el codigo (L1552-1558):**

```python
for n in set(ob):
    x = [l for l in base           if l.startswith(f"| O{n} |")]
    y = [l for l in lineas(DEC)    if l.startswith(f"| O{n} |")]
    if x and y and x[0] != y[0]: difs.append(f"O{n}")
```

`if x and y` — **si la fila se BORRA, `y` es vacia y no se compara NADA**. La unica guarda,
L1562, es `len(set(ac)) >= len(set(ob))`, que compara **cardinales, no pertenencia**, y hoy
sobra holgura (18 filas `O` en el arbol contra 16 en la base).

**AGRAVANTE MIO.** `G-20`, **veinte lineas mas arriba** (L1543-1549), comprueba que la serie `D`
es **CONTINUA, sin huecos y sin repetir** — la proteccion correcta, escrita en la misma pantalla,
**no aplicada a la serie `O`**.

### `E1b` · amputar `O5`–`O10` y rellenar el cardinal → **38/38 VERDE** · **CLASE A**

```text
serie `O` resultante: O1 O2 O3 O4 O11 O12 O13 O14 O16 O15 O17 O18 O19 O20 O21 O22 O23 O24
seis filas de relleno con el texto «RELLENO DE CARDINAL PLANTADO POR EL ATACANTE»
    OK   G-21 … └─ ninguna difiere
    38/38 comprobaciones en verde · EXIT=0 · CERO fallos
```

**Seis de las resoluciones del Owner que `G-21` existe para proteger, desaparecidas, y la
bateria imprime «ninguna difiere».**

### `E2` · `T-06` REABIERTO DENTRO DE UNA VALLA → **PAR CONTROL/MUTANTE** · **CLASE A**
### *(el `W3` anterior NO llego a ejecutarlo · es mi hallazgo mas fuerte)*

Par en la **MISMA seccion VIVA**, el **MISMO bloque ```text**, la **MISMA linea**, a **seis
lineas de distancia**. Sede: `CHECKPOINT-ADS-NEXT.md`, seccion `## Siguiente accion exacta`
(L2783), la que la cabecera del fichero designa **punto de entrada** («*Basta decir «Continua»*»).
Linea inyectada, identica en los dos casos:

```text
    el censo que va al Owner son DIECINUEVE presiones vigentes de `PN-1` a `PN-16` de §16.
```

```text
INSERTADA EN L2815, ANTES de la etiqueta `[ESTADO ANTERIOR · …]`
   EXIT=1 · 37/38 · FALLO G-26
   └─ c1) checkpoint L2815: dice 19 presiones y las cabeceras de §16 derivan 17;
      f) checkpoint L2815: el rango vivo «PN-1 a PN-16» no termina en la ultima vigente,
         que es PN-19                                                    ROJO   (correcto)

INSERTADA EN L2821, DESPUES de esa misma etiqueta
   EXIT=0 · 38/38 comprobaciones en verde · CERO fallos                  VERDE  (defecto)
```

**`E2b`, mio: el mismo dato falso 115 lineas mas abajo, justo antes de la valla de cierre,
al final de la seccion VIVA → `38/38 en verde`.**

**Y esto es lo decisivo, y no lo dice ninguna nota anterior:** la etiqueta de L2815 **CIERRA SU
PROPIO CORCHETE en L2819** (`…queda levantada.]`). La region exenta **sigue abierta 114 lineas
mas**, hasta la valla de cierre de L2933. **La marca no exime su bloque: exime todo lo que quede
dentro de la valla.**

**CAUSA, `_regiones_historicas` L2005-2008:**

```python
or (not linea.strip() and not en_valla and clase != "tanda")
```

El cierre por **LINEA EN BLANCO esta explicitamente DESACTIVADO dentro de una valla**
(`not en_valla`). Y dentro de una valla ```text no hay encabezados `^#{1,6} ` ni salida de cita.
**Dentro de una valla, la unica frontera que queda es la valla de cierre.**

**MEDIDA SOBRE EL ARBOL BAJO JUICIO, sin tocar nada, derivada por mi:**

```text
CHECKPOINT-ADS-NEXT.md   3324 lineas · 1860 EXENTAS (56.0 %) en 32 regiones
                         las cinco mayores: 242, 159, 133, 132 y 130 lineas
11-ARQUITECTURA-INTEGRADA.md  11177 lineas ·   26 EXENTAS (0.2 %) en 3 regiones
```

**Hoy, mas de la mitad del checkpoint —el fichero que va al Owner— no tiene ningun control de
cifra, y `G-26` imprime `OK`.** El atacante **ni siquiera planta la etiqueta**: ya esta publicada.

### `E3` · **el fixture de `G-31` que avala esto es CIEGO A LA VALLA** — **HALLAZGO MIO** · **CLASE A**

`G-31` publica como detalle: «*…y **una etiqueta no exime lo que queda fuera de su bloque ni
fuera de su cita**.*» Su fixture (L2778-2786):

```python
_FIX_BLOQUE = ("**[HISTÓRICO · el censo de entonces]**\nONCE presiones vigentes\n\n"
               "DIECISÉIS presiones vigentes de §16\n")
```

**Ejecute el MISMO fixture con y sin valla:**

```text
_FIX_BLOQUE tal como lo evalua G-31    regiones=[(0,63)]    ¿DIECISEIS exenta?  no
el MISMO fixture dentro de una valla   regiones=[(8,108)]   ¿DIECISEIS exenta?  SI  ← EXENTA
```

**El fixture que certifica la propiedad se evalua en la unica configuracion donde la propiedad
se cumple.** Es, palabra por palabra, la clase que el README L119 declara imposible —«*para que
ninguna pueda ser un fixture que no falle*»— y la que el gate del documento 23 llamo «*se
sustituyo un interruptor por otro y se puso una comprobacion a garantizar que el nuevo
funciona*». **Y el corpus escribe sus bloques mas importantes en ```text.**

### `E4` · `G-29` y «TODO el corpus gobernado» → **38/38 VERDE** · **CLASE A**

Cuatro ficheros, **todos SIN RASTREAR**, ninguno requiere commit:

```text
?? docs/DECISIONES-Y-CONTRADICCIONES.md      copia BYTE A BYTE del registro   (`cmp` OK)
?? docs/normativa/C9-PREVALECE-SOBRE-TODO.md copia BYTE A BYTE de
                                             docs/rediseno/a-CAPACIDADES-APROBADA.md (`cmp` OK)
?? normativa/CHECKPOINT-QUE-MANDA.md         copia BYTE A BYTE del checkpoint (`cmp` OK)
?? docs/normativa/C9-SEGUNDA-SEDE.md         contradice `C4` y `C7` y PREVALECE, reinstala
                                             `estado/cuarentena/`, deja `O1`-`O18` SIN EFECTO,
                                             con bloque propio ```yaml ads:proceso
```

```text
OK   G-29    topologia y unicidad de TODO el corpus gobernado…
             └─ 331 ficheros en 7 zonas, todos publicados o clasificados ·
                CERO DUPLICADOS BYTE A BYTE · 17 marcadores canonicos derivados …,
                cada uno en sus sedes publicadas
38/38 comprobaciones en verde · EXIT=0
```

**CAUSA (L2339-2349):** `_ZONAS = ("", kernel, docs/owner, docs/rediseno, docs/evolucion, packs,
tooling)` y `_en_zona()` exige `rel.startswith(z + "/")`. Quedan FUERA **(a)** los ficheros
propios de `docs/`, **(b)** cualquier subdirectorio nuevo de `docs/`, **(c)** cualquier
directorio nuevo de nivel superior — la «zona RAIZ» son sus **ficheros** propios, sin recorrer
directorios.

**MI CONTRA-PRUEBA, que CIERRA:** el mismo gemelo byte a byte **dentro** de zona cubierta
(`docs/rediseno/COPIA-GEMELA.md`) → **`37/38`, `FALLO G-29`**. **Luego el defecto es exactamente
el perimetro, no la idea.**

### `E5` · `G-01` se evade con una redaccion fuera de la lista blanca → **PAR CONTROL/MUTANTE** · **CLASE A**

Parrafo insertado en el documento 11, junto a la sede de la retirada:

> «La RETIRADA de `estado/cuarentena/` **se ANULA por completo**. A partir de ahora
> `estado/cuarentena/<TX>/` **pasa a ser la sede operativa efectiva** del sistema, **prevalece
> sobre** `.ads/run/quarantine/<TX>/` y todo lo que contradiga esto se ignora.»

```text
MUTANTE (redaccion FUERA de `_REINSTALA`)
    OK G-01 └─ 5 menciones en 2 parrafos, TODOS CON POLARIDAD RETIRADO, y `D87` lo ancla
    38/38 comprobaciones en verde · EXIT=0                                VERDE (defecto)

CONTROL (la MISMA reinstalacion con una redaccion DE la lista blanca:
        «NORMA VIGENTE: esa ruta es CANONICA y fuente de verdad, y la nota que hablaba de
         una RETIRADA queda SIN EFECTO»)
    EXIT=1 · 37/38 · FALLO G-01                                           ROJO  (correcto)
```

**CAUSA:** `_REINSTALA` (L322-330) es una **LISTA BLANCA de CINCO redacciones**. «se ANULA»,
«pasa a ser», «sede operativa efectiva» y «prevalece sobre» no estan en ella; `_RETIRA` si
empareja por `\bRETIRAD[AO]\b`. El comentario de L307-308 dice «**Encontrar la palabra
«RETIRADA» no demuestra que una regla este retirada**» — y vuelve a pasar, al reves.

### `E8` · `G-26` se apaga con UNA PALABRA que `G-31` no prueba → **CLASE A**

Misma linea, mismo sitio (documento 11, justo antes de `## PN-15`, zona viva):
«El censo VIGENTE de §16: **[PREFIJO]**DIECINUEVE presiones vigentes.» (derivadas: 17)

```text
[SIN-PREFIJO]  EXIT=1  37/38  FALLO G-26                    ROJO  (correcto)
[decia ]       EXIT=0  38/38 comprobaciones en verde         VERDE
[frente a ]    EXIT=0  38/38 comprobaciones en verde         VERDE
[en vez de ]   EXIT=0  38/38 comprobaciones en verde         VERDE
[conteo a ]    EXIT=0  38/38 comprobaciones en verde         VERDE
[reanclado ]   EXIT=0  38/38 comprobaciones en verde         VERDE
```

**CAUSA:** `_VERBO_DE_CITA` (L1904-1906) son **DIEZ interruptores lexicos**, evaluados sobre
`linea[:ini_rel]` en `_es_cita` (L2033). `_PALABRAS_GATILLO` de `G-31` (L2715) prueba **OTRAS
diez palabras y ninguna de estas**. **Contra el README L116: «*ninguna comprobacion se apaga
escribiendo una palabra*». Se apaga con cualquiera de diez.**

### `E9` · las pruebas negativas de `G-33` · **CUATRO DE CINCO NO PUEDEN FALLAR** · **CLASE A**

**Prueba por lectura (L3062-3115):**

```text
neg 2 CONTROL   `_reutilizacion(_sujeto_a, _sujeto_a, _CLAVES)` — un dict CONSIGO MISMO:
                `previo.get(k) != actual.get(k)` es False para todo k. SIEMPRE True
neg 2 MUTANTE   `_sujeto_b` difiere en `_CLAVES[-1]` POR CONSTRUCCION. SIEMPRE denunciado
neg 3           TRES llamadas a `_declaracion_valida` con literales `(True,True,False)`,
                `(True,False,False)`, `(True,True,True)`. **Ni un dato del arbol entra**
neg 4 y 5       `_todo_ok` se rellena entero con "verificado-vigente"; `_sin_estructural`
                rompe el PRIMER nivel (break inmediato → None); `_solo_superiores` omite el
                primero (`.get` → None → break). CONSTANTES
```

**Y prueba EJECUTADA, mia:** extraje los tres ayudantes y evalue las cuatro pruebas con
`_IDENT` y `_CADENA` aleatorios de 1 a 8 elementos:

```text
corridas: 640 · mitades evaluadas: 4480 · FALLOS: 0
=> las pruebas negativas 2, 3, 4 y 5 pasan SIEMPRE, para todo `_IDENT` y toda `_CADENA`
```

**Y los tres ayudantes son CODIGO MUERTO.** `grep -rn` sobre TODO el arbol: `_reutilizacion`,
`_declaracion_valida` y `_nivel_alcanzado` **solo aparecen en su propia definicion y en sus
propias pruebas**. Solo la negativa 1 tiene un pie en el corpus (`_b_real` sale del texto real
del primer macrocircuito via `sec_de`).

**Y el detalle que la bateria imprime dice:** «*5 pruebas negativas ejecutadas —3 protecciones
cubiertas: [13, 14, 15]—, cada una con su control en verde y su mutante en rojo*». **Las
protecciones 14 y 15 se declaran cubiertas por pruebas que no miran el arbol.** Contra el README
L119: «*cada una con su CONTROL en verde y su MUTANTE en rojo, **para que ninguna pueda ser un
fixture que no falle***».

### `E10` · UN SOLO ARBOL con `E1b` + `E2` + `E4` + `E5` + `E8` a la vez

No lo repito por separado: **cada uno de los cinco da `38/38` por si solo, ninguno requiere
commitear, y `E9` no requiere escritura ninguna.** Un arbol que los lleve todos lleva a la vez
seis resoluciones del Owner amputadas, dos cifras vivas falsas en el punto de entrada,
`estado/cuarentena/` reinstalada como sede que prevalece, y cuatro segundas sedes normativas
—dos de ellas copias byte a byte de material APROBADO y del registro—. **`git status` lo ve.
La bateria no.**

---

## 5 · ¿ESTA `B` DEMOSTRADA? — MI RESPUESTA

> ### **NO. `B` ESTA SOSTENIDA POR EL MANIFIESTO Y NO POR EL SOBRE, QUE ES LO QUE `O18` ENCARGO.**

**Lo que SI demostre yo, y consta a favor con toda su fuerza:**

```text
LAS 67 FILAS DEL MANIFIESTO 3, recalculadas por mi contra el arbol
    §4  13 filas · 23 491 lineas          §5  54 filas · 30 281 lineas
    TOTAL 67 filas · 53 772 lineas   ==   titular publicado (67 · 53 772)   EXACTO
    DISCREPANCIAS de lineas y de SHA-256                                    0

LAS DOS RESTAS, calculadas por mi con los conjuntos completos
    OBLIGATORIO − ASIGNADO   ∅        ASIGNADO − OBLIGATORIO   ∅

LOS 54 AGOTAMIENTOS, verificados uno a uno contra las DOS reglas
    regla 1 · fila propia con `LEIDO INTEGRO` en el documento y linea citados   54/54
    regla 2 · bytes identicos al arbol que ese gate leyo
              (41 contra `4d231ee`, 11 contra `7764cca`, 2 contra `c36d2ba`)    54/54
    FALLOS                                                                       0
```

**Esto cierra, por mi cuenta y con mecanismo, `T-10` y `U-02` en su forma**: el manifiesto del
gate anterior publicaba un titular que sus propias subsumas desmentian; **el de este gate cuadra
al digito**, y ademas la resta se calcula sobre el universo que el derivador produce y no sobre
una lista escrita. **Es el trabajo mas solido de esta tanda y hay que decirlo.**

**Y lo que NO esta demostrado, que es justo lo que `O18` pidio.** `O18` adopta la alternativa (b)
—**«un ancla documental EXTERNA al arbol auditado»**— precisamente porque *«quien puede escribir
el repositorio puede escribir la referencia»*. Todo lo de arriba lo verifique **leyendo el
repositorio**. Lo unico externo que tenia era el sobre, y el sobre:

```text
· publica un digest que NO se deriva del commit que ancla, sin decirlo          `W-11`
· publica un digest que no se deriva de NINGUN commit: sale del arbol de
  trabajo de quien emite, y el emisor no comprueba `git status`                `W-10`
· publica una receta de recalculo que NO reproduce ese digest                  `W-12`
```

**Las tres se refieren a la misma pieza: el DIGEST, que es lo unico del sobre que ata su
identidad al CONTENIDO.** Las filas de identidad (refs, commits, tree, SHA del manifiesto) son
correctas y las verifique. Pero un ancla de identidad sin contenido atado es una lista de SHA que
el revisor podria haber sacado de `git ls-remote`, y `O18` dice expresamente que el sobre existe
para lo que **no** se obtiene leyendo el repositorio.

**El corolario que sostiene la gravedad, y es mio.** El universo obligatorio **incluye los
documentos 19, 20, 21, 22 y 23, la bateria y su README** (lo verifique en las 67 rutas). Luego un
digest del universo **bien atado a un commit** cerraria por si solo dos de los peores hallazgos
del gate anterior: `U-01` (fabricar una prueba de agotamiento en el documento 22) y `T-20`/`U-2`
(amputar un `check`) **cambian el digest**. `O18` eligio bien la palanca. **Lo que falla es que la
palanca publicada no se puede tirar: la receta no reproduce el digest y el digest no viene de un
commit.**

---

## 6 · HALLAZGOS DE `W`, CONSOLIDADOS — renumerados, con severidad y clase MIAS

**Criterio de severidad**, el mismo que los tres gates anteriores, para que `X` compare sin
traducir: **BLOQUEANTE** = obliga a decidir arquitectura nueva · **GRAVE** = una garantia
publicada no se sostiene, o `F6` construiria algo distinto · **MEDIO** = una afirmacion vigente
es falsa sin cambiar el comportamiento · **MENOR** = editorial o de propagacion.
**Ninguno de los mios es BLOQUEANTE:** los diecisiete se cierran con material que el corpus ya
tiene escrito.

| id | sev | **clase** | sede | que es | reproducido por mi |
|---|---|---|---|---|---|
| **`W-01`** | **GRAVE** | **A** | bateria **L1975-2012** (`_regiones_historicas`) | dentro de una valla ```text el cierre por linea en blanco esta DESACTIVADO (`not en_valla`) y no hay encabezados: una etiqueta abre region **hasta la valla de cierre**, mucho mas alla de su propio corchete. **1860 de 3324 lineas del checkpoint (56.0 %) exentas HOY, en 32 regiones**, incluida la seccion VIVA «Siguiente accion exacta» entera | **SI · `E2` y `E2b`**, par control/mutante a 6 lineas y mutante a 115 lineas → `37/38` vs `38/38` |
| **`W-02`** | **GRAVE** | **A** | bateria **L2767-2786** (`_FIX_FUGA`, `_FIX_BLOQUE`) | los dos fixtures con que `G-31` certifica «*una etiqueta no exime lo que queda fuera de su bloque*» se evaluan sobre texto **sin valla**: son verdes por construccion. El MISMO `_FIX_BLOQUE` dentro de una valla **se vuelve del reves**. Un fixture que no puede fallar donde vive el defecto, en la comprobacion escrita contra los fixtures que no pueden fallar | **SI · `E3`**, ejecutado con y sin valla |
| **`W-03`** | **GRAVE** | **A** | bateria **L1552-1563** (`G-21`) | `if x and y` — el **BORRADO** de una fila `| On |` no se compara con nada. La unica guarda es un CARDINAL, no la pertenencia. `G-20`, veinte lineas mas arriba, tiene la guarda correcta para la serie `D` y no se aplica a la `O` | **SI · `E1` y `E1b`**, una y seis resoluciones del Owner amputadas → `38/38` y «ninguna difiere» |
| **`W-04`** | **GRAVE** | **A** | bateria **L2339-2360** (`_ZONAS`, `_en_zona`) | fuera del corpus gobernado quedan `docs/*.md`, **cualquier subdirectorio nuevo de `docs/`** y **cualquier directorio nuevo de nivel superior**. Cuatro segundas sedes normativas —tres copias BYTE A BYTE verificadas con `cmp`, una con bloque `ads:proceso` propio— y `G-29` imprime «331 ficheros en 7 zonas … **cero duplicados byte a byte**». Es `T-03` cerrado en su forma y no en su clase | **SI · `E4`**, con contra-prueba que CIERRA dentro de zona cubierta (`FALLO G-29`, 37/38) |
| **`W-05`** | **GRAVE** | **A** | bateria **L322-336** (`_REINSTALA`) | la polaridad de `G-01` es una **LISTA BLANCA de cinco redacciones**: una reinstalacion escrita con otras palabras se clasifica **RETIRADO**. El comentario L307-308 nombra exactamente este modo de fallo y lo reabre por el otro lado | **SI · `E5`**, par control/mutante: misma reinstalacion, `FALLO G-01` con redaccion de la lista y `38/38` fuera de ella |
| **`W-06`** | **GRAVE** | **A** | bateria **L1903-1906** (`_VERBO_DE_CITA`) | `G-26` se apaga con **diez interruptores lexicos**, y `G-31` prueba **otras diez palabras**. README L116: «*ninguna comprobacion se apaga escribiendo una palabra*» | **SI · `E8`**, cinco de los diez verificados con su control |
| **`W-07`** | **MEDIO** | **A** | bateria **L3062-3115** (`G-33`) | **cuatro de las cinco pruebas negativas no pueden fallar**: constantes por construccion, con los tres ayudantes como **codigo muerto** que nadie mas invoca. Las protecciones **14 y 15** se declaran cubiertas por pruebas que no miran el arbol. README L119 promete lo contrario | **SI · `E9`**, por lectura y por 4480 mitades evaluadas con `_IDENT`/`_CADENA` aleatorios: **0 fallos** |
| **`W-08`** | **MEDIO** | **A** | README **L78-79** y **L164-165** | «*esta tanda **NO escribe ninguna proteccion interna nueva***» y «*Esta tanda no ha escrito ninguna proteccion nueva, a proposito*» — mientras **`G-34` NACE en esta tanda** y su propia fila L118 lo documenta. `git log -S'G-34'`: primera aparicion en **`3f5ebf2`**, ancestro del candidato; en `b9492c1` hay **0** y **36 `check`**, en `3f5ebf2` hay **4** y 36→38. El README se desmiente a si mismo a cuarenta lineas (L160-161). **El mensaje del commit `3f5ebf2` SI lo formula bien** y ese matiz no sobrevive al README | **SI**, con `git log`, `git show` y recuento de `check(` por commit |
| **`W-09`** | **MENOR** | **A** | CORRIGENDUM **§7** | la regla «*una frase de un dictamen con entrada en este corrigendum NO PUEDE CITARSE sin citar la entrada que la acota*» **no la ejecuta nada**: `grep -ci corrigendum` sobre la bateria da **0**. Es una regla publicada sin sede que la aplique, en el aparato cuyo lema es «*y eso se EJECUTA, no se promete*» | **SI** (barrido sobre la bateria y el README) |
| **`W-10`** | **GRAVE** | **B** | emisor **L98-113** y **L126-131** | `_universo()` lee el **ARBOL DE TRABAJO** del emisor (`io.open`), no un commit, y el emisor **no comprueba `git status`**. Arbol sucio → `rc=0` con tree SHA limpio y digest/lineas sucias (53 773). Emitido desde el checkout del candidato → mismas filas de identidad, digest `9490d6a3`, 65 / 53 354. **El digest es una propiedad del directorio de quien emite.** Contra su propia cabecera L43-47: «*un sobre incompleto es peor que ningun sobre*» | **SI · `E-A` y `E-B`**, sobre un clon limpio con `origin` real |
| **`W-11`** | **GRAVE** | **B** | el SOBRE, filas 3-4 contra 10-12 | ancla el commit candidato `21f1ccb` / arbol `b498f3b` y publica **cifras del arbol del gate** (67 / 53 772 / `19ac2551`); el arbol candidato da **65 / 53 354 / `9490d6a3`**. Corroborado: el SHA del derivador publicado es el del gate (`db9c8b69` en el candidato) y **el manifiesto anclado no existe en el commit candidato**. Ninguna fila nombra el tree SHA del gate | **SI**, con `git archive` de los dos commits y el derivador de cada uno sobre su propio arbol |
| **`W-12`** | **GRAVE** | **B** | emisor **L112** vs **L161-162** | la receta de recalculo que el sobre publica da `6e2f90f2…`; el sobre declara `19ac2551…`. Un byte `0x0A`. **El revisor que la siga falla CERRADO sobre un repositorio sano**, en el mecanismo que `O18` estrena | **SI**, las dos tuberias ejecutadas, y `head -c -1` reproduce el digest exacto |
| **`W-13`** | **MEDIO** | **B** | derivador **L406-429** (`_FILA_MANIFIESTO`, `universos_publicados`) | el cliquet exige `^| <ordinal> | \`ruta\` |`. **Quitar el ordinal de UNA fila desarma el cliquet para esa ruta**: borre su fila del `ENCARGO` y el universo pasa de **67 a 66 con `rc=0` y sin una linea de diagnostico**. Y **ya esta ciego hoy**: `F4C-ASIGNACION-GATE-CIERRE-20260829.md` aporta **0 filas** al cliquet —su tabla no lleva columna de ordinal— y nada lo dice. La guarda `if not con_filas` solo salta si **todos** los manifiestos aportan cero | **SI**, en dos pasos: paso 1 solo → `rc=2` correcto; paso 2 → `rc=0`, 66 fuentes, silencio |
| **`W-14`** | **MEDIO** | **B** | derivador **L261-299** (`componente_iv`) | la «clasificacion TOTAL» cierra el fallo por **lista vacia** y deja abierto el fallo por **lista equivocada**: un dictamen NUEVO cuyo H1 lleve solo una voz de `VOCES_DE_NO_DICTAMEN` —«SINTESIS», «DECISION», «CONTRASTE»— **se cae del universo con `rc=0` y sin aviso**, y el cliquet no puede cubrirlo porque ningun manifiesto lo declaro. La clasificacion mira **solo el H1** y nunca el texto | **SI**: `24-SINTESIS-DEL-CIERRE.md` con «VEREDICTO: SUFICIENTE PARA F5» dentro → **67 fuentes, sin el 24**. Con un H1 con voz de dictamen → 68. Sin H1 → `rc=2` correcto |
| **`W-15`** | **MEDIO** | **B** | manifiesto 2 **L79** y **fila 8** · CORRIGENDUM **§6** | el manifiesto declara «*Todo derivado del arbol `2451141c`, nada copiado*» y **una de sus 64 filas no sale de ese arbol**: fila 8, el derivador, **402 lineas / `fa245924`** en `2451141c` frente a **410 / `6753a245`** declaradas. Es el `U-02` del documento 23, **MEDIO y sin acotar**: el corrigendum §6 solo acota el titular de lineas, y ademas afirma «*sus 64 filas … ninguna cambia … sin una discrepancia*» **sin decir contra que arbol** | **SI**: verificacion de las 64 filas contra `2451141c` → **1 discrepancia, y es la fila 8** |
| **`W-16`** | **MEDIO** | **B** | `00-INDICE.md` **L100-117** · el arbol bajo juicio | **REINCIDE, identico, un gate despues.** `find` sobre `verificacion/` da **10** rutas; el indice enlaza **9**; la que falta es **el manifiesto de ESTE gate**. Y el arbol que se somete a certificacion **falla hoy un validador canonico**: `comprobar_referencias.py --exclusiones` → `T147 FALLIDA · 0 superadas · 1 fallidas · EXIT REAL = 1`, con la causa nombrada: «*…-GATE-CERTIFICACION-3-20260830.md: no lo alcanza ningun enlace por ruta … **Existe para nadie***». Es `S-18`≡`T-14` del documento 23, y **la regla la escribio el propio indice** | **SI**, con el `find` que el indice publica y ejecutando el validador (EXIT real medido, sin tuberia) |
| **`W-17`** | **MENOR** | **A** | el reparto de este gate | a `W2` se le encargo recalcular los agotamientos —cuya regla 1 obliga a abrir la linea citada— y se le prohibio abrir documentos entre los que esta el **23**, que no es fuente agotada sino **fila 3 de §4, mi lote, «DESPUES de las fuentes»**. La conducta de `W2` fue la correcta y la declaro; **el reparto no**. Tercera repeticion de la misma clase (`C-2`, `T-11`, esta) | N/A (defecto de procedimiento) |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, contado id a id y no escrito aparte

  BLOQUEANTE   0
  GRAVE        9    W-01 W-02 W-03 W-04 W-05 W-06 · W-10 W-11 W-12
  MEDIO        6    W-07 W-08 · W-13 W-14 W-15 W-16
  MENOR        2    W-09 W-17
                ──
                17

POR CLASE, que es lo que `O18` manda separar
  A  (coherencia interna)   10   W-01 W-02 W-03 W-04 W-05 W-06 W-07 W-08 W-09 W-17
  B  (identidad de la candidata)  7   W-10 W-11 W-12 W-13 W-14 W-15 W-16
  C  (actor privilegiado)    0   NO reporto ninguno como defecto de esta tanda: `T-01` y
                                 `T-02` del documento 23 siguen vivos y los dejo en `C`

REPRODUCIDOS POR MI CON SALIDA PEGADA          16 de 17   (`W-17` es de procedimiento)
HALLAZGOS MIOS QUE NINGUN RELEVO TRAJO          4   W-02 · W-14 · W-16 · W-17
                                                    (+ la EJECUCION de W-01: `W1` lo midio y
                                                     ningun `W3` anterior lo habia ejecutado)
```

---

## 7 · HALLAZGOS QUE RECHAZO, CON EVIDENCIA

**Tres rechazos y una fusion. Van contra mi propia cadena y valen tanto como lo que confirmo.**

**`X-1` · RECHAZO `W1-09`** —«`G-17b` conserva dos cardinales escritos a mano **en la bateria
cuya cabecera dice que ninguna cifra esta escrita a mano**»—. **El hecho es cierto y la
imputacion no.** Abri la cabecera entera (L1-6):

> «*Cada comprobacion DERIVA su resultado del arbol. **Ninguna cifra esta escrita a mano: las
> que aparecen abajo son las EXIGIDAS**, y el fallo se produce cuando lo derivado difiere.*»

**La cabecera declara expresamente que las cifras que aparecen son las EXIGIDAS.** `len(f5) == 3`
y `len(f6) == 11` son exigidas, no derivadas-y-copiadas: es exactamente el caso que la frase
cubre. **Lo que sobrevive es una observacion, no un hallazgo**: la tanda ha retirado esa figura
de `G-13`, `G-16`, `G-17` y `G-20`, y `G-17b` es el ultimo sitio donde queda; ira a rojo el dia
que suba un `requiere_f5` legitimo. **Lo dejo como observacion y NO lo cuento entre mis 17.**

**`X-2` · RECHAZO `W1-10`** —«`G-28` no declara que no ve un documento NUEVO sin confirmar»—.
**Esta declarado**, en la fila de `G-22` del README, L107: «*Un documento numerado nuevo **nace
ADMITIDO por `G-29` y queda protegido aqui en cuanto se confirma***». Decir «queda protegido en
cuanto se confirma» **es decir que antes de confirmarse no lo esta**. No hay promesa incumplida.
**NO ENTRA.**

**`X-3` · NO ADJUDICO `T-01` ni `T-02` del documento 23** —`G-30` anclada en `HEAD` y en
`kernel/.upstream-hash`; `G-22`/`G-28` anclados en `HEAD`; ocho inmutables sin linea base—.
**El hecho es exacto y sigue vivo**, y no lo discuto. **Pero exige commitear para que `HEAD`
absorba el ataque, que es corromper la REFERENCIA**, y eso es literalmente la **CLASE `C`** que
`O18` declara NO implementada y contrata para `F6`. **No es defecto de esta tanda y no lo cuento
contra ella.** Lo digo asi de claro porque contar `C` como `A` es lo que haria que el gate
siguiente escribiera la proteccion diecinueve.

**`X-4` · FUSIONO `W2-04`** —«el emisor publica el SHA del derivador del commit junto a un digest
producido por OTRO derivador»— **dentro de `W-10`**. Es la misma raiz: el emisor mezcla campos
leidos con `git show` y campos leidos del arbol de trabajo. Contarlo aparte inflaria el censo.

**Y una que NO cuento y que dejo constar a favor:** plantar un `24-DICTAMEN-DE-AGOTAMIENTO.md`
falso, con veredicto y con enlace en el indice, da `38/38` — **y el README lo DECLARA** en su
bloque «NO PROTEGE CONTRA UNA MARCA HISTORICA FALSA» (L141-149). Es un hueco **declarado**, no
una promesa incumplida. **Y ademas el sobre lo cerraria**: un documento numerado nuevo entra en
el componente (iv) y **cambia el digest del universo**.

---

## 8 · LOS DEL DOCUMENTO 23 EN MI FOCO — CERRADO / NO CERRADO / FUERA DE MI LOTE

**Regla que me impongo.** Los del foco de `V` —documento 11, registro de decisiones, checkpoint,
`00-INDICE`, `O18`/`D108` como resolucion y propagacion— **NO los adjudico, y no los presumo ni
cerrados ni abiertos**. Donde una sede de mi lote los roza, juzgo solo mi sede.
De los **49 hallazgos** del documento 23 —0 bloqueantes · 17 graves · 19 medios · 13 menores; 48
de clase `A` y 1 de clase `B`— mi foco alcanza los `T-01`…`T-22`, `U-01` y `U-02`.

| id (doc 23) | que exigia | que encuentro YO en el arbol de hoy | resultado |
|---|---|---|---|
| **`T-01`** GRAVE | `G-30` por CONTENIDO, no anclada en `HEAD` ni en `.upstream-hash` | Hay cuatro clases declaradas y la huella se recalcula. El ancla sigue dentro del arbol | **FUERA DE `A`/`B` · CLASE `C`**, no lo adjudico contra la tanda |
| **`T-02`** GRAVE | `G-22`/`G-28` con un ancla que no escriba el editor | El inventario se deriva y crecio; el ancla sigue siendo `HEAD` | **CLASE `C`**, no lo adjudico |
| **`T-03`** GRAVE | retirar el `return True` en blanco de `docs/evolucion/NN-*.md` | **CERRADO EN SU FORMA, y lo verifique:** un `24-SEGUNDA-SEDE-NORMATIVA.md` sin rastrear → **`FALLO G-29`, 37/38**, y el detalle **lo nombra**. Enlazado desde el indice → admitido, que es el hueco **declarado**. **NO CERRADO EN SU CLASE:** `docs/normativa/`, `normativa/` y `docs/*.md` siguen fuera (`W-04`) | **CERRADO EN SU FORMA · NO EN SU CLASE** |
| **`T-04`** GRAVE | meter el README en un inventario de integridad | `G-34` mete bateria y README en el inventario y contrasta el censo. La autorizacion sigue derivandose del README, pero el README ya no es libre | **CERRADO** *(su explotacion exigia editar el README: `C`)* |
| **`T-05`** GRAVE | la guarda de «base vacia» de `G-11b` en `G-22` y `G-28` | **CERRADO Y GENERALIZA.** `git` falso en el `PATH` (`exit 0`, stdout vacio) → **`30/38`, OCHO fallos**, y `G-22` y `G-28` **estan entre ellos** (`grep -c '^OK   G-22'` → 0) | **CERRADO** |
| **`T-06`** GRAVE | que una ETIQUETA no exima un bloque entero | **NO CERRADO.** Cerrado fuera de la cita y en el bloque siguiente; **abierto de par en par dentro de una valla**, que es donde el corpus escribe sus bloques mayores. 56 % del checkpoint exento hoy | **NO CERRADO** (`W-01`, `W-02`) |
| **`T-07`** GRAVE | la ventana literal de `G-15` | No lo verifique: no lo reabri con contraejemplo propio | **NO ADJUDICO** (lo declaro en §10) |
| **`T-08`** GRAVE | que `G-32`/`G-33` LEAN la fila `O17`, o que dejen de decir que derivan de ella | No lo reverifique con el ataque de negacion de `O17`: exige tocar el registro, que es lote de `V` | **NO ADJUDICO** |
| **`T-09`** GRAVE | censo de pruebas negativas contrastado, y pruebas falsificables | **CERRADO A MEDIAS.** El censo **ya se deriva y se contrasta** —el detalle imprime «5 pruebas negativas · 3 protecciones cubiertas [13,14,15]» derivado de `_NEGATIVAS`, y hay guardas por lista vacia y por nombre repetido—. **La sustancia NO:** cuatro de las cinco siguen sin poder fallar (`W-07`) | **NO CERRADO** |
| **`T-10`** GRAVE | que el titular de lineas del manifiesto derive | **CERRADO, y con mecanismo.** Manifiesto 3: 13+54 = 67 filas y 23 491+30 281 = 53 772 lineas, **iguales a su titular y a la salida del derivador**, con 0 discrepancias contra el arbol. **Lo recalcule yo entero** | **CERRADO** |
| **`T-11`** MEDIO | el reparto que pide una verificacion sin dar la fuente | **REINCIDE** en la forma acotada de `W-17` | **NO CERRADO** |
| **`T-12`** MEDIO | el rango `BLOQUE C §13–§15` vivo en la norma que el derivador parsea | **CERRADO.** El documento 11 L11081 dice hoy «**BLOQUE C (§13–§17, iniciativa y dosier vivo)**», y las secciones reales entre `# BLOQUE C` y `# BLOQUE D` son §13, §14, §15, §16 y §17. **Coinciden** | **CERRADO** |
| **`T-13`** MEDIO | el campo `espera` en las mutaciones del kernel | **NO CERRADO, y DECLARADO CON CIFRA DERIVADA**: `G-30` imprime «*LIMITACION DECLARADA: **51 de esas 62 mutaciones** no llevan campo `espera` y son VACUAS EN POTENCIA (`T-13`); el remedio vive en `kernel/`, que esta bateria no escribe*». **Es la conducta correcta para algo que no es suyo** | **NO CERRADO · DECLARADO** |
| **`T-14`** ≡ `S-18` MEDIO | enlazar el manifiesto **en el mismo commit** que lo crea | **REINCIDE IDENTICO.** 10 ficheros en `verificacion/`, 9 enlazados, falta el de ESTE gate; `T147 FALLIDA · EXIT REAL = 1` sobre el arbol bajo juicio | **NO CERRADO** (`W-16`) |
| **`T-15`** MEDIO | que el universo no encoja en silencio | **PARCIALMENTE CERRADO.** El **cliquet existe y funciona**: borrar una fila del `ENCARGO` da `rc=2` nombrando ruta y manifiesto —lo ejecute—. Y la clasificacion del componente (iv) **falla cerrado** ante un documento sin H1. **Pero quedan dos grietas**: el ordinal del cliquet (`W-13`) y la voz equivocada del H1 (`W-14`) | **PARCIALMENTE CERRADO** |
| **`T-16`** MEDIO | que `G-24` deje de recomputar `_CAPS` | **CERRADO.** L1843 `_dir_cap = _DIR_CAPS` y L1844 `presentes = list(_CAPS_DIRS)`: una sola sede, y el comentario L1842 lo registra | **CERRADO** |
| **`T-17`** MENOR | retirar el `sedes = {…}` muerto | **CERRADO.** L471 conserva el comentario «`T-17`. Aqui vivia `sedes = {…}`» y el diccionario **ya no esta** | **CERRADO** |
| **`T-18`** MENOR | la rama «vacio» inalcanzable de `_motivo_ilegible` | **CERRADO.** `leer()` (L75) **pregunta siempre** por el motivo, y una sede vacia es ilegible: falla cerrado con su nombre | **CERRADO** |
| **`T-19`** MENOR | la funcion escrita dos veces | **CERRADO.** `_ilegible()` retirada; solo queda `_motivo_ilegible` (L53), con el comentario L1831 que lo registra | **CERRADO** |
| **`T-20`** MENOR→GRAVE (elevado por `U`) | que amputar un `check` no sea invisible | **CERRADO Y GENERALIZA, y lo ejecute yo.** Borre el bloque `check("G-31", …)`: **`36/37`, `EXIT=1`, `FALLO G-34`**, con el detalle «*COMPROBACIONES AMPUTADAS: el README publica `['G-31']` y esta ejecucion NO las ha ejecutado*». **La amputada aparece nombrada** | **CERRADO** |
| **`T-21`** MENOR | la localizacion L42/L618 del corrigendum | **CERRADO, y lo verifique en las dos lineas.** La entrada 4 lleva hoy «*Localizacion corregida … Las lineas reales son **L46** y **L628***». `sed -n '46p'` del documento 13 → «*doc 12 «SEIS escenarios» §11.5 tiene DIEZ … ERRATA CONFIRMADA*»; `sed -n '628p'` → «*cuando §11.5 tiene **diez**…*». **Las dos existen y dicen lo que la entrada dice** | **CERRADO** |
| **`T-22`** MENOR | el `%r` con tupla de tres que reventaba con `TypeError` | **CERRADO.** L164-165: `raise SedeIlegible("… %r" % (crudos,))`, con la tupla envuelta y el comentario que cita `T-22` | **CERRADO** |
| **`U-01`** GRAVE | que una prueba de agotamiento no se pueda fabricar | **NO CERRADO DENTRO DEL ARBOL, y `O18` es la via correcta.** La regla sigue apoyandose en citas que viven en documentos del arbol. **Lo que SI existe ahora**: los documentos 19-23 estan **en el universo obligatorio**, luego fabricar una cita **cambia el digest del sobre** — y ahi es donde muerden `W-10`, `W-11` y `W-12`. **Verifique los 54 agotamientos y los 54 pasan las dos reglas** | **ATACADO POR OTRA VIA · NO CERRADO** |
| **`U-02`** MEDIO | que el manifiesto no declare derivar de un arbol que no lo deriva | **NO CERRADO Y SIN ACOTAR** (`W-15`). El corrigendum §6 acota el titular de lineas y **no** la fila 8, y afirma «sus 64 filas … sin una discrepancia» sin nombrar arbol | **NO CERRADO** |
| `M-04` como PROPOSICION UNIVERSAL · GRAVE 5 del doc 22 | — | **`O18` la ha retirado como criterio de aceptacion de `F4c`** y la ha partido en `A`, `B` y `C`. **No la adjudico como tal**, y por eso este dictamen no cuenta arboles: cuenta **fallos de `A`** y **fallos de `B`** | **REEMPLAZADA POR `O18`** |
| todo lo del foco de `V` | — | documento 11 · registro · checkpoint · `00-INDICE` · `O18`/`D108` como resolucion | **FUERA DE MI LOTE** |

```text
RECUENTO, solo sobre lo que `W` puede adjudicar

  CERRADO                             11   T-04 T-05 T-10 T-12 T-16 T-17 T-18 T-19 T-20
                                           T-21 T-22
  CERRADO EN SU FORMA, NO EN SU CLASE  1   T-03
  PARCIALMENTE CERRADO                 1   T-15
  NO CERRADO                           6   T-06 T-09 T-11 T-13(declarado) T-14 U-02
  ATACADO POR OTRA VIA, NO CERRADO     1   U-01
  CLASE `C`, NO ADJUDICADOS            2   T-01 T-02
  NO ADJUDICADOS POR MI (declarado)    2   T-07 T-08
```

**Y esto es lo que hay que leer de esa tabla, y lo digo entero:** **once de los veinticuatro
estan cerrados y varios GENERALIZAN de verdad**, con control positivo mio —`G-34` nombra la
comprobacion amputada, el `git` que miente ya no pasa, la aritmetica del manifiesto deriva al
digito, el codigo muerto se retiro—. **Esta tanda ha trabajado, y bien, en la mitad que sabia
arreglar.** Lo que no ha movido es exactamente la mitad donde el gate anterior dijo que el
remedio se escribia «*con la forma exacta del contraejemplo*»: `T-06` cerro la cita y el bloque
siguiente y dejo la valla; `T-03` cerro `docs/evolucion/NN-*.md` y dejo `docs/normativa/`;
`T-09` cerro el censo y dejo la tautologia.

---

## 9 · REFUTACIONES QUE INTENTE Y NO CAYERON

**Las publico con el mismo detalle que los hallazgos, porque un dictamen que solo enseña lo que
confirma no mide nada.**

**`RF-1` · Intente que amputar una comprobacion siguiera siendo invisible, que es `T-20`/`U-2`,
el hallazgo que el adjudicador `U` elevo a GRAVE por haberlo reproducido el mismo. NO CAYO.**
Borre el bloque `check("G-31", …)` entero: **`36/37`, `EXIT=1`, `FALLO G-34`**, y el detalle
imprime «*COMPROBACIONES AMPUTADAS: el README publica `['G-31']` y esta ejecucion NO las ha
ejecutado. Quien borre una llamada `check()` responde de ello: el informe ya no puede callar la
que falta*». **Cierra en las dos direcciones y nombra la que falta.** Es la correccion mas limpia
de la tanda.

**`RF-2` · Intente que `G-22` y `G-28` siguieran dando verde sobre cero, que es `T-05`. NO CAYO.**
`git` falso en el `PATH` (`#!/bin/sh` + `exit 0`, sin stdout): **`30/38`, OCHO fallos**, y
`G-22` y `G-28` **entre ellos**. La guarda que `G-11b` tenia escrita se generalizo de verdad.

**`RF-3` · Intente plantar una segunda sede normativa como documento numerado, que es `T-03`/`R-A`
del gate anterior. NO CAYO.** `docs/evolucion/24-SEGUNDA-SEDE-NORMATIVA.md` sin rastrear →
**`FALLO G-29`, 37/38**, y el detalle lo nombra: «*AMPLIACION NO CLASIFICADA del corpus gobernado,
rastreada o no*». *(Lo que si cae es el mismo fichero **fuera** de las siete zonas: `W-04`.)*

**`RF-4` · Intente que un gemelo byte a byte pasara dentro de una zona cubierta. NO CAYO.**
`cp docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md docs/rediseno/COPIA-GEMELA.md` →
**`FALLO G-29`, 37/38**. **La unicidad literal funciona; lo que falla es el perimetro**, y esta
contra-prueba es lo que convierte `W-04` en un hallazgo de perimetro y no de idea.

**`RF-5` · Intente borrar una fuente obligatoria entera. NO CAYO, por dos vias.**
`git rm docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` → **`36/38`, `FALLO G-24` y
`FALLO G-29`**; y el derivador **falla cerrado con codigo 2 real**: «*FALLA CERRADO · rutas
derivadas que NO existen en el arbol*». **El derivador es un programa duro y coincido con los dos
gates anteriores.**

**`RF-6` · Intente alterar material APROBADO. NO CAYO.** Inyecte «DEROGADO POR EL ATACANTE» en
`docs/rediseno/a-CAPACIDADES-APROBADA.md` → **`FALLO G-23`, 37/38**. **Lo normativo aprobado SI
esta anclado.**

**`RF-7` · Intente que la primera grieta del cliquet del derivador bastara sola. NO CAYO.**
Borrar una fila del `ENCARGO` **sin tocar nada mas** → **`rc=2`**, con el diagnostico completo:
«*EL UNIVERSO HA ENCOGIDO … 1 ruta(s) que un manifiesto INMUTABLE declaro obligatoria(s) ya no
salen de ningun componente: [(…emitir-sobre-de-ancla.py, [F4C-ASIGNACION-GATE-CERTIFICACION-3…])]*».
**El cliquet existe y funciona.** Hizo falta desarmarlo a mano en el manifiesto (`W-13`).

**`RF-8` · Intente que el componente (iv) se comiera un documento numerado nuevo por no saber
clasificarlo. NO CAYO en esa forma.** Un `24-…md` **sin H1** → **`rc=2`** nombrandolo. *(Cae por
la otra: con un H1 de voz equivocada, `W-14`.)*

**`RF-9` · Intente tumbar la cobertura de este gate, que era mi apuesta principal. NO CAYO, y es
lo que mas me ha costado escribir.** Recalcule las 67 filas del manifiesto contra el arbol
(**0 discrepancias**), las dos restas (**∅ en las dos direcciones**), y **los 54 agotamientos
contra sus DOS reglas, uno a uno** (54/54 en la regla 1; 54/54 en la regla 2, contra los tres
arboles que citan). **`C-L.5` no se reabre por nada de lo que yo traigo.**

**`RF-10` · Intente que el sobre no fuera reconstruible, que es la acusacion mas grave que se le
puede hacer a un ancla. NO CAYO.** Reemiti el sobre desde un clon limpio y **las trece filas
sustantivas salen identicas**. *(Lo que cae es de que arbol salen tres de ellas: `W-10`, `W-11`.)*

---

## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **No he leido ninguna fuente del lote de `V`**: ni el documento 11 (11 176 lineas), ni
   `DECISIONES-Y-CONTRADICCIONES.md`, ni `CHECKPOINT-ADS-NEXT.md`, ni `00-INDICE.md` integro.
   Los toque **para mutarlos en el laboratorio y para derivar cifras con `grep`**, y **eso no es
   lectura**. Por tanto **no digo nada** sobre `O18` como resolucion, sobre `D108` como
   propagacion, sobre si `D108` excede a `O18`, ni sobre el estado del checkpoint. Que `G-26`
   deje 1860 lineas del checkpoint sin control **es un hecho sobre la bateria**, no un juicio
   sobre el checkpoint.
2. **No he leido los documentos 19, 20, 21 ni 22.** Lo que el documento 23 dice de ellos lo
   transcribo, no lo verifico — salvo las 54 citas de agotamiento, que si comprobe una a una
   abriendo la linea citada, que es lo que la regla 1 obliga a hacer.
3. **`T-07` y `T-08` del documento 23 no los reverifique**: la ventana literal de `G-15` y la
   negacion de `O17` en el registro. **No los presumo ni cerrados ni abiertos.** Un adjudicador
   que quiera apoyarse en ellos tiene que rehacerlos.
4. **No he auditado `G-02`…`G-10`, `G-12`, `G-14`, `G-18`, `G-19`, `G-25`, `G-27` ni `G-32`
   con contraejemplos propios.** Que la bateria caiga por seis puertas no significa que solo
   haya seis.
5. **No he probado** enlaces simbolicos, permisos, nombres Unicode confusables, submodulos,
   `.gitattributes` ni condiciones de carrera. Ni un solo vector de concurrencia.
6. **No he ejecutado nada del sistema, porque no hay sistema.** Todo mi trabajo es texto contra
   texto y programa contra arbol.
7. **No he medido cuantas de las 32 regiones exentas del checkpoint contienen hoy una cifra
   falsa.** Medi que **estan exentas**; no las lei. Es exactamente el trabajo de `V`.
8. **La verificacion de los 54 agotamientos es tan solida como los documentos que los citan**, y
   el documento 23 (`U-01`) demostro que esos documentos son editables. **Mi `RF-9` no distingue
   una cita verdadera de una fabricada**, y lo digo yo, que lo ejecute.
9. **Ningun ojo unico recorrio las 3139 lineas de la bateria seguidas.** Declarado en §3, y lo
   repito aqui porque una resta que da cero lo esconde.
10. **No verifique el contenido de `W2` sobre el manifiesto 1 ni sobre el addendum** mas alla de
    sus SHA y de sus recuentos. Sus filas de §5 sobre el documento 20 las tomo declaradas.

---

## 11 · MI RECOMENDACION DE VEREDICTO

**La cobertura de `W` esta cerrada** —`ASIGNADAS − LEIDAS INTEGRAS = 0`, nueve de nueve, con los
nueve SHA-256 recalculados por mi— y por tanto **NO procede recomendar por cobertura**. Mi
recomendacion se emite **sobre el fondo**, y sobre las dos afirmaciones que `O18` separo.

# INSUFICIENTE PARA F5

### Las razones, numeradas. Las dos primeras bastan cada una por si sola.

**1 · `A` NO SE SOSTIENE. La bateria no detecta incoherencias que estan en el arbol que se le
entrega, sin que nadie toque la bateria, su README, `HEAD` ni las refs.** Seis arboles, todos
reproducidos por mi con salida pegada, todos `38/38 en verde` con `EXIT=0`: seis resoluciones del
Owner amputadas y `G-21` imprime «ninguna difiere» · dos cifras vivas falsas en la seccion que la
cabecera designa **punto de entrada**, una por la valla y otra por un interruptor lexico ·
`estado/cuarentena/` reinstalada como sede que **prevalece**, y `G-01` imprime «todos con
polaridad RETIRADO» · cuatro segundas sedes normativas, **tres de ellas copias byte a byte**
verificadas con `cmp`, y `G-29` imprime «cero duplicados byte a byte». **Ninguno requiere
commitear. Ninguno es clase `C`.**

**2 · Y la medida que lo hace estructural, no anecdotico: hoy, sin que nadie ataque nada,
1860 de las 3324 lineas del checkpoint —el 56.0 %— estan EXENTAS de todo control de cifra, en 32
regiones, incluida la seccion viva «Siguiente accion exacta» entera.** La etiqueta que abre esa
region **ya esta publicada** y **cierra su propio corchete 114 lineas antes** de que la region
termine. Y el fixture con que `G-31` certifica que eso no pasa **se evalua sin valla**: el mismo
fixture, dentro de una valla, se vuelve del reves. **Una comprobacion que garantiza una propiedad
falsa es peor que no tenerla**, y es la frase que el documento 22 escribio y que el 23 repitio.

**3 · `B` NO ESTA DEMOSTRADA POR EL INSTRUMENTO QUE `O18` CREO PARA DEMOSTRARLA.** El sobre ancla
el commit candidato `21f1ccb` y publica cifras del arbol del gate `f2e4d58`, sin decirlo —el
manifiesto que ancla **ni siquiera existe** en el commit que ancla—; su digest no sale de ningun
commit, sino del **arbol de trabajo de quien emite**, y el emisor **no comprueba `git status`**
pese a declarar en su cabecera que un sobre incompleto es peor que ninguno; y **la receta que
publica para que el revisor no tenga que fiarse no reproduce el digest que publica**, de modo que
el revisor que la siga falla cerrado sobre un repositorio sano. **`B` es la mitad que esta tanda
estrena y falla en sus propios terminos**, en las tres piezas que la sostienen.

**4 · Y el aparato del propio gate vuelve a dejar el arbol que juzga con un validador canonico en
rojo, por la misma causa, un gate despues.** `comprobar_referencias.py --exclusiones` sobre el
arbol bajo juicio: **`T147 FALLIDA · 0 superadas · 1 fallidas · EXIT REAL = 1`**, causado por el
manifiesto de **este** gate publicado sin enlazar desde `00-INDICE.md` — que es exactamente lo
que el propio indice advierte por escrito en L100-108. **La regla existe, el comando existe, el
comando la denuncia, y se incumple otra vez.**

### Lo que expresamente NO fundamenta mi recomendacion

- **NO recomiendo por cobertura.** `ASIGNADAS − LEIDAS = 0`; las 67 filas del manifiesto cuadran
  en lineas y SHA-256 con **cero discrepancias**; las dos restas dan **∅**; y **los 54
  agotamientos pasan las dos reglas, uno a uno, verificados por mi**. **`C-L.5` no se reabre por
  nada de lo que yo traigo.**
- **NO recomiendo por `M-04` como proposicion universal.** `O18` la retiro como criterio y la
  partio en tres. **No cuento arboles: cuento fallos de `A` y fallos de `B`.**
- **NO recomiendo por la clase `C`.** `T-01` y `T-02` siguen vivos y **no los cuento**: exigen
  corromper la referencia, `O18` los declara no implementados y los contrata para `F6`, y
  contarlos aqui es lo que haria que la tanda siguiente escribiera la proteccion diecinueve.
- **NO recomiendo por el derivador.** Es un programa **duro**: falla cerrado con codigo 2 real
  ante una ruta ausente, ante una sede ilegible, ante un cardinal descuadrado, ante un documento
  sin clasificar y ante el borrado de una fila del `ENCARGO`. **Lo ataque cinco veces y aguanto
  cuatro.** Lo que falla son dos grietas nombradas, no el programa.
- **NO recomiendo por el manifiesto de este gate.** Es la pieza mejor hecha de la tanda: cuadra al
  digito, deriva su universo, reparte lotes complementarios y **cierra `T-10` con mecanismo**.
- **NO recomiendo por el corrigendum.** **Acota sin editar**, sus cifras se derivan —recalcule la
  suma de su entrada 2 y su localizacion corregida de la entrada 4, y las dos salen exactas— y su
  regla §7 es una pieza sensata. Lo unico que le reprocho es que **nada la ejecute** y que su
  entrada 6 absuelva 64 filas sin decir contra que arbol.
- **NO recomiendo porque quede arquitectura por inventar.** **Ninguno de mis diecisiete es
  BLOQUEANTE.** `W-01` se cierra dejando que la linea en blanco cierre region tambien dentro de
  una valla, o que la region cierre donde cierra el corchete de su etiqueta. `W-03`, aplicando a
  la serie `O` la guarda que `G-20` ya tiene escrita veinte lineas mas arriba. `W-04`, completando
  `_ZONAS` con `docs/` y recorriendo directorios. `W-10`, leyendo el universo con `git show` del
  commit y comprobando `git status`. `W-12`, con `head -c -1` o con un `\n` final. **Ninguno es
  materia del Owner.**

### Lo que consta a favor, y no es cortesia

Once de los veinticuatro hallazgos del documento 23 que caen en mi foco **estan cerrados**, y
varios **generalizan de verdad, con control positivo mio**: `G-34` da sede al censo y **nombra la
comprobacion amputada** —el vector que el adjudicador anterior elevo a GRAVE por haberlo
reproducido—; el `git` que sale 0 con stdout vacio **ya no pasa** y arrastra ocho fallos; el
manifiesto **deriva su aritmetica al digito** y cierra `T-10` con mecanismo; el codigo muerto se
retiro y el comentario que lo registra cita el hallazgo; el rango del `BLOQUE C` se corrigio en la
norma viva; la rama del derivador que existia para fallar cerrado **por fin falla cerrado**; y el
cliquet de los manifiestos, que el gate anterior pidio, **existe, funciona y nombra ruta y
manifiesto**. **Esta tanda entendio lo que se le pidio y ejecuto la mayor parte.**

**Y aun asi no recomiendo cerrar, por la razon que este expediente lleva cuatro gates
persiguiendo y que esta vez tengo en la forma mas limpia que se puede tener: la tanda cerro cada
hallazgo con la forma exacta de su contraejemplo, y donde el contraejemplo estaba escrito sin
valla, la valla sigue abierta.** `T-06` se cerro fuera de la cita y en el bloque siguiente, y hoy
el 56 % del fichero que va al Owner esta exento. `T-03` se cerro en `docs/evolucion/NN-*.md`, y
hoy `docs/normativa/` admite una copia byte a byte del material APROBADO. `T-09` cerro el censo de
las pruebas negativas, y cuatro de las cinco siguen sin poder fallar. **Y la respuesta del Owner
—`O18`, el ancla externa— es correcta y es la palanca buena; lo que no funciona es la palanca:
publica un digest de un arbol que no es el que ancla, leido de un directorio de trabajo, con una
receta que no lo reproduce.**

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `X`, que no soy yo.** `X` recalcula por su
> cuenta universo, asignaciones, lecturas, cobertura, severidades y recuentos, y puede revocar
> cualquiera de mis diecisiete adjudicaciones, mis tres rechazos y mi fusion. **No he visto el
> dictamen de `V` y no lo vere.**

---

## 12 · CIERRE

```text
git status --porcelain   AL ABRIR    →   (salida vacia)     primer comando de la sesion
git status --porcelain   AL CERRAR   →   (salida vacia)     ultimo comando de la sesion
HEAD al abrir y al cerrar            →   f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0, identico
RAMA                                 →   gate/f4c-certificacion-3-20260830
SHA-256 del documento 23             →   0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MI   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS   /tmp/lab-W3/{cand,gate,der,der2,bat,emisor,fakebin} — copias por
               `git archive` y `git clone` fuera del repositorio. BORRADO con `rm -rf`
SUBAGENTE `Agent`                                               NO USADO
FICHEROS V1.md · V2.md · V3.md · DICTAMEN-V.md                  NO ABIERTOS
NINGUN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.
```

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `W` · dictamen cerrado por `W3`, relevo.**

---

# §C · ADJUDICACIÓN DEL ADJUDICADOR `X`, LITERAL

# ADJUDICACIÓN DEL ADJUDICADOR `X` — TERCER GATE DE CERTIFICACIÓN DE F4c

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `X`, adjudicador único. **Emito el veredicto y no corrijo nada.**

No he escrito nada de este corpus, no apliqué ninguna corrección, no participé en ningún gate anterior y no vi ningún dictamen hasta abrir los dos que recibo, ya cerrados. No usé el subagente `Agent`.

```text
git status --porcelain  AL ABRIR   → VACÍO   (primer comando de la sesión)
git status --porcelain  AL CERRAR  → VACÍO   (último comando)
HEAD al abrir y al cerrar          → f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0, idéntico
RAMA                               → gate/f4c-certificacion-3-20260830
FICHEROS EDITADOS/CREADOS/BORRADOS → ninguno · COMMITS·PUSH·PR·MERGE → ninguno
LABORATORIO  /tmp/lab-X/{cand,gate,gc,atk,origin.git} — `git archive` y `git clone`
             fuera del repositorio. BORRADO con `rm -rf`
```

## 2 · ¿ES VÁLIDO ESTE GATE? — DECIDIDO EXPRESAMENTE

**EL GATE ES VÁLIDO. Y el sobre es DEFECTUOSO en cuatro campos, tres de ellos demostrados por mí.** Separo las dos cosas porque el manifiesto §8 las confunde.

### 2.1 · Lo que verifiqué del sobre, campo a campo

| campo del sobre | mi medición |
|---|---|
| `COMMIT CANDIDATO 21f1ccb` · `COMMIT MANIFIESTO f2e4d58` | resuelven, existen, `21f1ccb` es ancestro de `f2e4d58` · **CORRECTO** |
| `ARBOL b498f3b8` | `git rev-parse 21f1ccb^{tree}` = `b498f3b8…` · **CORRECTO como tree del candidato** |
| `SHA-256 MANIFIESTO ac9e0edd…` | recalculado por mí, coincide en worktree y en el blob · **CORRECTO** |
| `SHA-256 DERIVADOR 6f8c98a2…` | es el del **GATE**. En `21f1ccb` es `db9c8b69…` · **NO es del árbol anclado** |
| `67 fuentes · 53772 líneas` | son del **GATE**. Ejecuté el derivador del árbol candidato desplegado con `git archive`: **65 fuentes · 53 354 líneas** · **NO son del árbol anclado** |
| `DIGEST 19ac2551…` | reproducido byte a byte con la fórmula real del emisor, sobre el árbol del gate. **NO derivable de `b498f3b8`** |
| `ASIGNACIONES 18` | derivado de las marcas de revisor de §4 del manifiesto: **17**. **FALSO** |
| `LA RECETA publicada` | `…| while read r; do echo …; done | sha256sum` → `6e2f90f2dcd1c12c4abce57ab9da51ff329e57753e5a3e77f260ddcb834b656c`. **NO reproduce `19ac2551…`** |

Los dos revisores transcribieron **el mismo sobre**, campo por campo. No hay dos sobres distintos, no hay sobre reconstruido a posteriori y no hay sobre cambiado después de crear revisores. Eso lo comprobé.

### 2.2 · Por qué NO lo declaro inválido, y qué lo habría volteado

El manifiesto §8 dice «cualquier diferencia entre el SOBRE recibido y lo que el árbol muestra INVALIDA EL GATE». Bajo lectura literal, este gate es inválido cuatro veces. **No aplico esa lectura, y digo por qué:**

1. **La cláusula existe para proteger contra un OBJETO SUSTITUIDO, y el objeto no está en duda.** Comparé las 67 rutas del universo entre los dos árboles: **66 son byte a byte idénticas; difiere exactamente UNA, el propio derivador.** El corpus leído es el mismo. Ningún contenido está en duda, y lo demuestro en vez de suponerlo.
2. **Una regla de parada alimentada por un falso positivo UNIVERSAL no es una garantía: es un interruptor de apagado.** La receta falla sobre cualquier árbol, sano o corrupto. Un instrumento que da rojo siempre no distingue nada. Adopto en esto el razonamiento de `V` §2.1, que reproduje y sostengo.
3. **Declarar inválido no produce veredicto, y este gate ha producido evidencia que `O18` necesita oír** — en particular mi `X-01`, que muestra que el mecanismo que `O18` estrena no cambia la raíz de confianza. Quemar eso por un byte `0x0A` sería el peor uso posible de la regla.

**Lo que SÍ me habría hecho declararlo inválido, y lo digo para que la regla no quede vacía:** dos sobres distintos entre revisores · un digest no reproducible desde ningún árbol · o una diferencia de CONTENIDO entre el árbol encargado y el leído. Ninguna de las tres se da.

**Consecuencia, y es la que cuenta: los defectos del sobre no invalidan el gate — hacen que `B` NO quede demostrada.** Es una insuficiencia, no una invalidez, y la diferencia importa.

## 4 · COBERTURA RECALCULADA POR MÍ

### 4.1 · El derivador — **DERIVA, y no esconde listas**

`python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py` → exit 0 · **67 fuentes · 53 772 líneas** · (i) 4 · (ii) 29 · (iii) 3 · (iv) 13 · (v) 28.

El componente (v) es una lista anotada **y el derivador lo declara en su propia cabecera**, con guarda de cláusula, de ruta repetida y de ruta inexistente. **Lo ataqué: vaciar una fuente obligatoria → EXIT 2 con diagnóstico real.** No esconde listas: publica la que tiene y dice que la tiene.

### 4.2 · Las DOS restas

```text
OBLIGATORIO − ASIGNADO   =  ∅     igualdad exacta de conjuntos, 67 = 67, las dos direcciones
ASIGNADO − OBLIGATORIO   =  ∅

ASIGNADO A LECTURA        13 fuentes · 23 491 líneas
RUTAS DISTINTAS LEÍDAS ÍNTEGRAS   13
ASIGNADO A LECTURA − LEÍDO  =  ∅
```

**Y LA RESERVA QUE LA RESTA ESCONDE, que peso yo y que es material.** El `CHECKPOINT` **no tiene declaración válida de lectura íntegra por la cadena `V`**: `V3` lo cubre por temas, sin tramos, y `V4` declara expresamente que **no leyó renglón a renglón ~1 700 líneas de citas históricas**. La resta cierra **sólo porque la cerré yo**. Y no es formal: **`X-04`, uno de mis hallazgos propios, está exactamente en el tramo que `V4` no abrió.**

### 4.3 · Los 54 agotamientos — **54/54 PLENOS**

```text
regla 1  fila propia con `LEÍDO ÍNTEGRO` de esa ruta en el documento y línea citados   54/54
regla 2  bytes IDÉNTICOS al árbol que ESE gate leyó de verdad
         (41 contra `4d231ee` · 11 contra `7764cca` · 2 contra `c36d2ba`)               54/54
DISCREPANCIAS                                                                            0
```

Y las 67 filas del manifiesto contra el árbol del gate: **0 discrepancias**. La aritmética cierra al dígito: 23 491 + 30 281 = 53 772. **`T-10` del documento 23 está cerrado con mecanismo, y lo recalculé yo entero.**

**`C-L.5` NO se reabre por nada de lo que yo traigo. La CERTIFICO por cuarta vez consecutiva. Este gate NO falla por cobertura.**

## 6 · ¿EXCEDE LA PROPAGACIÓN, O QUEDÓ `O18` INCOMPLETA?

### 6.1 · El hecho, primero, y no está en disputa

`O18` en su sede dice de `(c)`: «OBLIGATORIA EN `F6`, Y CONDICIÓN PREVIA A PesquerApp» — **UNA condición**. Barrido sobre el fichero entero: **cero** apariciones de «ADS operativo», **cero** de «certificar adaptadores», **cero** reparto `SIS`/`PLT`/`VER`/`SEG`.

La propagación afirma **TRES** condiciones en seis sedes y rotula **«EL REPARTO, LITERAL DE O18»** un bloque que `O18` no contiene. **Contra el texto REGISTRADO de `O18`, la propagación EXCEDE. Eso es un hecho y lo confirmo.**

### 6.2 · La prueba con que `V` cierra la hipótesis contraria — **LA REFUTO**

`V` razona: si `O18` fuera una transcripción corta, el material que falta tendría que estar en la PREGUNTA (documento 23 §13·B); no está; luego el Owner no pudo resolverlo.

**Su premisa mayor es falsa, y lo demuestro con una sola medición.** `grep -in 'pesquerapp'` sobre **todo** el documento 23 devuelve **UNA sola línea, la L2691**, que está en el párrafo de clase `C` de §13 y **NO en §13·B**.

**Es decir: la ÚNICA condición que `O18` SÍ registra —la de PesquerApp— TAMPOCO estaba en la pregunta.**

El Owner respondió más ancho que la pregunta **al menos una vez**, y el corpus aceptó esa ampliación sin objeción. **El silogismo de `V` prueba de más: aplicado con rigor expulsaría también la condición que todos aceptan como del Owner. Por tanto no prueba nada.**

### 6.3 · La evidencia forense que aporto yo, y que nadie ha mirado

**El mensaje del commit `bcee159` —cuyo único trabajo declarado es transcribir la resolución— YA ESCRIBE LAS TRES CONDICIONES**, literalmente. Eso es corroboración **contemporánea del acto de transcripción** e **independiente de §11.8**, que llega un commit después.

**Y hay una segunda pieza, de forma.** La entrada de `O17` **sí lleva dentro de §2** una sección «El REPARTO DE RESPONSABILIDADES que el Owner decide». **Ésa es la forma que el corpus estableció.** La de `O18` no la tiene. **El reparto NO aparece en `bcee159`: nace en `8e70d94`, el commit de propagación.** Tiene, por tanto, un estatus probatorio distinto.

### 6.4 · MI ADJUDICACIÓN

```text
¿EXCEDE LA PROPAGACIÓN AL TEXTO REGISTRADO DE `O18`?   SÍ. Hecho, verificado, no discutible.

LAS DOS CONDICIONES DURAS                    la hipótesis «`O18` quedó INCOMPLETA» está MEJOR
                                             SOSTENIDA que «la propagación excede», por la
                                             corroboración contemporánea de `bcee159`.
                                             La prueba contraria de `V` está REFUTADA.

EL REPARTO `SIS`/`PLT`/`VER`/`SEG`           INDETERMINADO. Nace en el commit de propagación.
                                             RECHAZO el rótulo «LITERAL DE `O18`».
                                             No rechazo el contenido.

¿EXCEDE LA FILA `D108`?                      NO. Se declara derivada y lo es.
```

**Su evidencia no puede verificarse contra nada, y eso es exactamente la debilidad que `O18` declara de sí misma.** Yo no puedo confirmarla. Pero **`V` tampoco podía refutarla**, y su intento falló. **La disputa es INDECIDIBLE desde el árbol**, y ninguna de las dos vías de remedio es ejecutable por F4: recortar significa que F4 borre contenido que el coordinador afirma del Owner; completar significa que F4 escriba palabras dentro de una resolución del Owner — `G21` de `KERNEL.md` L690.

**MI RESOLUCIÓN: no adjudico el fondo, porque no es adjudicable. Lo que SÍ adjudico es que el corpus perdió la capacidad de responder esta pregunta, y eso es un defecto con remedio determinado.** Va a §13 como **RATIFICACIÓN, no elección**.

## 9 · `M-04`: LO QUE REPRODUJE YO

Clon limpio. **BASELINE: `38/38` verde · `EXIT=0`.**

| # | árbol defectuoso | resultado | clase |
|---|---|---|---|
| **A1** | borrar la fila `O5` del registro (una resolución del Owner desaparece) | **38/38 VERDE**, y `G-21` imprime «ninguna difiere» | **`A`** |
| **A2** | dos copias **byte a byte** de material APROBADO fuera de `_ZONAS`, sin rastrear | **38/38 VERDE**. Contraprueba dentro de zona → **37/38 `FALLO G-29`** | **`A`** |
| **A3** | cifra viva falsa junto a `PN-15`, apagada con «decía », «en vez de », «reanclado » | **38/38** | **`A`** |
| **A4** | la valla: misma línea, misma sección VIVA, **después** del cierre del corchete | **38/38** | **`A`** |
| **A5** | **puerta trasera en el EMISOR del sobre + fuente obligatoria ensuciada** | **38/38 VERDE**, y el sobre emitido es **idéntico al honesto en sus doce filas sustantivas** | **`A` · MÍO** |
| **A6** | **puerta trasera en el DERIVADOR** (cliquet desarmado) | **38/38 VERDE** | **`A` · MÍO** |

**Refutaciones que NO cayeron:** renombrar o borrar un documento histórico → `FALLO G-29` · vaciar una fuente obligatoria → `EXIT 2` · modificar un manifiesto inmutable → `FALLO G-22` · el gemelo dentro de zona cubierta → `FALLO G-29`.

**`M-04` sigue viva, en clase `A`, en su cuarto gate. Y con `A5` sigue viva en el mecanismo que `O18` estrenó para cerrarla.**

## 12 · RECUENTO CONSOLIDADO

```text
23 (V)  +  17 (W)  −  3 solapes  +  6 míos  =  43 DISTINTOS
```

| severidad adjudicada por mí | n.º |
|---|---|
| **BLOQUEANTE** | **0** |
| **GRAVE** | **15** |
| **MEDIO** | **16** |
| **MENOR** | **12** |

**Cuántos los introdujo ESTA tanda: dieciocho de los cuarenta y tres.** Todos nacen de la propagación de `O18` o del aparato que este gate estrena.

## 13 · CLASIFICACIÓN `A` / `B` / `C`

```text
A · COHERENCIA INTERNA          27   NO SE SOSTIENE: seis árboles defectuosos en verde,
                                     cuatro reproducidos por mí, ninguno requiere commitear

B · IDENTIDAD DE LA CANDIDATA   12   NO ESTÁ DEMOSTRADA, y falla en las tres piezas que la
                                     sostienen: el digest, la receta y el emisor

C · RESISTENCIA A UN ACTOR       0   NO declaro insuficiencia por `C`, y lo digo expresamente.
    PRIVILEGIADO                     El corpus la trata bien: se declara NO IMPLEMENTADA, el
                                     contrato de §11.8 está COMPLETO, y no encontré NI UNA
                                     sede que presente `(b)` como `(c)`.

DECISIÓN DEL OWNER               4   la ratificación de `O18`
```

### La pregunta exacta para el Owner

**No es una elección de diseño: es una RATIFICACIÓN, y sólo el Owner puede darla.**

> **Owner: necesitamos que ratifique el texto de su propia resolución `O18`, porque el sistema ha perdido la capacidad de comprobarlo.**
>
> Tal como quedó escrita, `O18` dice de `(c)` que es **obligatoria en `F6` y condición previa a la adopción permanente de PesquerApp** — **UNA condición**. Pero seis sedes le atribuyen **TRES** («…a la adopción permanente de PesquerApp, **a declarar ADS operativo y a certificar adaptadores**»), y §11.8 rotula «**EL REPARTO, LITERAL DE `O18`**» un reparto de capacidades que la entrada de `O18` no contiene.
>
> **Este gate no ha podido decidir cuál de las dos es la verdad.** El coordinador afirma que su respuesta contenía las tres condiciones y el reparto, y que la entrada quedó corta. Hay corroboración parcial: el mensaje del commit que transcribe `O18` ya escribe las tres condiciones. Hay también una anomalía de forma: `O17` registró su reparto dentro de su entrada y `O18` no lo hizo. **Y no existe ninguna sede en el repositorio donde viva su respuesta en su propia mano:** `docs/owner/` contiene dos documentos y ninguna de sus resoluciones `O15`–`O18`.
>
> **¿Cuál de estas tres quiere?**
>
> **(a) RATIFICAR EL TEXTO AMPLIO.** `O18` se completa con las dos condiciones adicionales y con el reparto, y las seis sedes quedan correctas.
> *A FAVOR:* el corpus queda coherente de un solo acto. *EN CONTRA:* consolida como suyo un texto que sólo consta porque el coordinador lo transcribe, y que ningún gate podrá verificar nunca.
>
> **(b) RATIFICAR EL TEXTO ESTRICTO.** `O18` se queda como está y se **retiran** de las seis sedes las dos condiciones duras, y el rótulo «LITERAL DE `O18`» pasa a decir «reparto DERIVADO por `D108`».
> *A FAVOR:* el corpus deja de atribuirle nada que su propia sede no diga. *EN CONTRA:* si usted sí las dijo, `F4` habría borrado una resolución suya.
>
> **(c) RATIFICAR Y DAR SEDE.** Cualquiera de las dos anteriores, **más**: sus resoluciones pasan a vivir en `docs/owner/` con su texto tal como usted lo emite, y el sobre de ancla de cada gate incluye la huella de esa sede.
> *A FAVOR:* es lo único que impide que esta misma pregunta vuelva en `O19`. *EN CONTRA:* le pide un acto de publicación por cada resolución.
>
> **`F4` no elige ninguna, y lo dice.** Y hace constar, contra su propio interés, que **la debilidad que hace necesaria esta pregunta es exactamente la que `O18` declara de sí misma**. `O17` lo dijo con todas las letras —«no se afirma que sea falsa: se declara **INVERIFICABLE**»— y `O18` no lo dice. **Diga lo que diga usted, esa declaración debe escribirse en `O18`, y eso sí puede hacerlo `F4`.**

## 14 · ¿ES LA MISMA CAUSA RAÍZ QUE EN LOS GATES ANTERIORES?

### SÍ, es la misma. Y esta vez es peor, porque este era el gate que venía a curarla.

El Owner resolvió `O18`, y `O18` es **correcta**: no añade otra comprobación interna sino que **cambia la raíz de confianza**. **Y la implementación de esa resolución puso la nueva raíz dentro del mismo repositorio.** `emitir-sobre-de-ancla.py` vive en `docs/evolucion/verificacion/`, no está en `G-22` ni en `G-34` ni en `G-29`, lee el universo del **directorio de trabajo** y no comprueba `git status`. **Lo demostré:** con tres líneas de puerta trasera y sin commitear, produce un sobre **idéntico en sus doce filas sustantivas al honesto** sobre un corpus corrupto, y la batería da 38/38.

**La circularidad no se cerró: se movió de `HEAD` y `kernel/.upstream-hash` a `emitir-sobre-de-ancla.py`.**

### Y ahora la parte que impide decir «no ha servido de nada», porque sería falso

**La resolución `O18` NO está refutada.** `O18(b)` describe **un canal**, y **ese canal SÍ es externo**: el sobre llegó a `V`, a `W` y a mí dentro del encargo, no leyéndolo del árbol; los dos revisores recibieron el mismo sobre. **Lo externo es la ENTREGA. Lo interno es la PRODUCCIÓN.** Ésa es la distinción que este gate aporta y que ningún gate anterior podía aportar.

```text
gate del doc 21    3 falsos verdes         · la batería medía 30 comprobaciones
gate del doc 22    8 árboles en verde      · la batería medía 30
gate del doc 23    `T` 7 · `U` 6, dos nuevos · la batería medía 37
ESTE gate          `W` 6 · `X` 6, de los cuales DOS por puertas que nadie había abierto
                                            · la batería mide 38

EL COSTE MARGINAL DE ENCONTRAR LA PUERTA SIGUIENTE SIGUE SIN SUBIR.
```

### MI RESPUESTA, sin rodeos

**SÍ: este gate falla por lo mismo que el 21, el 22 y el 23 — la verificación anclada dentro del objeto verificado — y falla además por algo nuevo: el remedio que el Owner ordenó se instaló dentro de la enfermedad.**

**Pero el trabajo NO debe detenerse, y digo por qué es distinto de la vez anterior.** El gate 23 recomendó parar porque `M-04` no era satisfacible desde dentro y **nadie había preguntado al Owner**. Hoy sí se ha preguntado, la respuesta existe, y **es la palanca correcta**. Lo que falla es la palanca, y **el remedio está determinado**:

```text
1  el emisor lee el universo con `git show <commit>:<ruta>`, no del directorio de trabajo,
   y comprueba `git status` antes de emitir. Un sobre sucio no se emite
2  el sobre publica el ÁRBOL DEL GATE junto al de la candidata — o el gate no toca el
   derivador después de publicar la candidata. Las dos valen; una hay que escribirla,
   porque el derivador es fila de su propio universo
3  el emisor y el derivador entran en el inventario de integridad, y la receta publicada
   se corrige. Un byte
```

**Y expresamente: NO se escriba una decimonovena protección sistémica.** Si la respuesta a este gate es otra tanda de protecciones internas, el gate que venga detrás encontrará la puerta siguiente y tendrá razón.

## 15 · VEREDICTO

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No he corregido nada.**

**1 · `A` NO SE SOSTIENE, y lo reproduje yo con mis manos.** Seis árboles defectuosos en **`38/38` verde con `EXIT=0`**, ninguno requiere commitear, ninguno toca la batería, su README, `HEAD`, las refs, la base ni el runner. Los cuatro primeros con su control positivo en rojo, que los cierra como defectos de perímetro y no de idea.

**2 · `B` NO ESTÁ DEMOSTRADA, y falla en las tres piezas que la sostienen.** El sobre ancla `b498f3b8` y publica el universo, el derivador y el digest de `826e6ede`, que nunca nombra — **mutuamente insatisfacibles**. Su receta no reproduce su digest sobre ningún árbol. Su digest sale del directorio de trabajo de quien emite. Su único campo no contrastado, `ASIGNACIONES 18`, es falso: son 17. Y **el emisor mismo no está en ningún inventario de integridad**.

**3 · La propagación publica como resolución del Owner un contenido que su propia sede no contiene**, y el corpus ha perdido la capacidad de decidir cuál de las dos es la verdad. **Y `O18`, a diferencia de `O17`, no declara su propia inverificabilidad.**

**4 · El aparato del propio gate deja el árbol que juzga con DOS validadores canónicos en rojo, por segunda vez consecutiva.** Candidata `21f1ccb`: **13/13 verde**. Gate `f2e4d58`: **11/13**, `T147` y `T158` FALLIDAS.

**5 · `C-L.7` queda falsada sobre el árbol que se juzga.** El bloque de estado estructurado del checkpoint va **dos eventos atrasado, sin rótulo**, bajo `actualizado: 2026-08-30`. Cuarta recurrencia consecutiva.

**6 · Y la razón de método.** **Dieciocho de los cuarenta y tres los introdujo esta misma tanda**, y tres son reincidencias literales de hallazgos que el gate anterior adjudicó.

### Lo que expresamente NO fundamenta este veredicto

- **NO falla por cobertura.** Las dos restas son ∅ y **calculé las dos**. **`C-L.5` sigue CERTIFICADA.**
- **NO declaro el gate INVÁLIDO.**
- **NO fundamento nada en `C`.** El Owner ha resuelto su fase. `T-01` y `T-02` siguen vivos y **no los cuento**.
- **NO falla por el derivador.** Es un programa **duro**. Lo ataqué y aguantó.
- **NO falla porque quede arquitectura por inventar. Ninguno de los cuarenta y tres es BLOQUEANTE.**

### Lo que SÍ ha quedado cerrado, y no es cortesía

1. **`C-L.5` CERTIFICADA por cuarta vez consecutiva**, y el manifiesto **cuadra al dígito**. **`T-10` del documento 23 CERRADO CON MECANISMO.**
2. **Los 54 agotamientos pasan las DOS reglas**, verificados uno a uno contra los tres árboles que citan.
3. **`T-20` CERRADO Y GENERALIZA**: amputar una comprobación ya no es invisible.
4. **`T-05` CERRADO Y GENERALIZA**: un `git` que sale 0 con stdout vacío ya no pasa.
5. **La disciplina de inmutabilidad se cumple donde está escrita.** Lo comprobé cuatro veces.
6. **22 de los 26 de la serie `S` y 11 de los 24 de la serie `T`/`U` están cerrados**, y varios **mejor de lo que el hallazgo pedía** — en `S-07`, **negándose a ampliar una resolución del Owner con todas las letras**.
7. **La propagación de `O18` es real donde toca:** el sobre se entregó por canal externo, antes de leer, idéntico a los dos revisores, y **es reconstruible**. Lo reconstruí.
8. **`O18` es la palanca correcta.** El problema no es la resolución del Owner: es que la palanca publicada no se puede tirar.

**Ésta sigue siendo una candidata sólida. No falla por concepción, no falla por cobertura y no falla por lo que el Owner decidió. Falla porque el instrumento que `O18` creó para demostrar que se analizó lo encargado se produce con un programa que vive dentro del árbol que ancla y que nadie protege — y porque el corpus ha dejado de poder comprobar qué dijo el Owner.**

**La primera se corrige en `F4c`, con tres líneas de contrato. La segunda no, y es del Owner.**

---

# §D · EL REGISTRO INCREMENTAL DE `X`, LITERAL

> Escrito por `X` mientras trabajaba, antes de redactar su adjudicación. Se publica
> porque contiene las mediciones en crudo con las que sostiene cada afirmación.

# ADJUDICACION X — TERCER GATE DE CERTIFICACION F4c
(escritura incremental; NO se corrige nada del repo)

## 0. Apertura
- `git status --porcelain` VACIO al abrir. OK.
- HEAD = f2e4d58c25034d7a82f6051da1a9ddc1dc9d6eb0 ; rama gate/f4c-certificacion-3-20260830
- Lab en /tmp/lab-X

## 1. EL SOBRE — verificacion propia (hechos reproducidos)
- X-1 **La receta publicada NO reproduce el digest.** Emisor: sha256("\n".join(filas)) SIN salto final = 19ac2551…
  Receta shell (`… | sha256sum`) añade salto final = 6e2f90f2dcd1c12c4abce57ab9da51ff329e57753e5a3e77f260ddcb834b656c.
  Reproducido. El unico mecanismo que O18(b) ofrece «para que el revisor no tenga que fiarse» falla.
- X-2 **El digest no corresponde al arbol anclado.** ARBOL=b498f3b8 (candidato 21f1ccb).
  Derivador ejecutado SOBRE ESE ARBOL => 65 fuentes / 53354 lineas. El sobre declara 67 / 53772,
  que es el arbol del GATE (826e6ede, commit f2e4d58). Reproducido con `git archive`.
- X-3 **El emisor mezcla tres sedes**: arbol del candidato (tree SHA), commit del gate (sha manifiesto
  y sha derivador) y el DIRECTORIO DE TRABAJO del emisor (`_universo()` lee con io.open(RAIZ/rel),
  no de ningun commit). Un worktree sucio produciria un digest que no corresponde a ningun commit.
- X-4 El SHA-256 DEL DERIVADOR del sobre (6f8c98a2…) es el del GATE; en el candidato es db9c8b69…
- X-5 El unico fichero del universo que difiere entre ambos arboles es el propio derivador.

## 2. MANIFIESTO — verificacion propia
- 67 filas con ruta+lineas+SHA (13 lectura + 54 agotadas). OBLIGATORIO−ASIGNADO = VACIO (conjuntos identicos). OK.
- X-6 **§4 L70 dice «Todo derivado del arbol b498f3b8, nada copiado» y es FALSO en 1 de 67 filas**:
  fila #8 derivar-universo-obligatorio.py declara 496 lineas y SHA 6f8c98a2 = arbol del GATE.
  En b498f3b8 son 492 lineas y db9c8b69. Es exactamente el defecto `T-10` del doc 23 (cifra copiada,
  no derivada) reaparecido en el mismo lugar del manifiesto siguiente.
- Los 54 agotamientos: bytes IDENTICOS al arbol citado y al arbol del gate en los 54. Cita
  doc+linea con fila propia y «LEIDO INTEGRO» en los 54. => regla 1 y regla 2 CUMPLIDAS.
  Salvedad menor X-7: la fila #13 (ADS-PENDIENTES) cita doc22 L2642, que es la tabla en que doc22
  VERIFICA el agotamiento declarado por doc21 L380; la sede directa es doc21 L380 (existe y es valida).
  Cita transitiva, no falsa. MENOR.
- Aritmetica: 13 filas suman 23491 lineas SOLO si el derivador cuenta 496 (arbol del gate). Con el
  arbol anclado (492) darian 23487. La aritmetica del manifiesto confirma X-2/X-6.

## 3. T147 / RUNNER — de quien es la culpa
- REPRODUCIDO en clon limpio:
    arbol CANDIDATO 21f1ccb  -> **13/13 VERDE**
    arbol DEL GATE  f2e4d58  -> **11/13**, ROJO en `referencias` (T147) y `evidencia` (T158)
  T147: «F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md: no lo alcanza ningun enlace por ruta … Existe para nadie»
  T158: fuentes-salida.txt caducada, 305 publicado vs 306 vigente.
- La culpa es del APARATO DEL GATE, no de la candidata. Identico a `S-18`≡`T-14` del doc 23,
  **y peor**: alli 12/13, aqui 11/13.
- AGRAVANTE: 00-INDICE.md L106-117 escribe la regla y la declara «de cumplimiento obligatorio
  para el gate siguiente». ESTE es el gate siguiente y la incumplio en su unico commit.
  `grep -rn` del corpus: CERO referencias al manifiesto del gate 3.

## 4. M-04 · LO QUE REPRODUJE YO (clon limpio /tmp/lab-X/atk en f2e4d58; BASELINE 38/38 EXIT=0)
- A1 = E1 de W. Borrada la fila `| O5 |` del registro -> **38/38 VERDE, EXIT=0**. CLASE A. CONFIRMADO.
- A2 = E4 de W. `docs/normativa/C9-...md` y `docs/DECISIONES-Y-CONTRADICCIONES.md`, copias BYTE A BYTE
  (cmp) -> **38/38 VERDE**. CONTRAPRUEBA: el mismo gemelo en `docs/rediseno/` -> 37/38 FALLO G-29.
  Defecto de PERIMETRO, no de idea. CLASE A. CONFIRMADO.
- A3 = E8 de W. Cifra viva falsa junto a `PN-15`: sin prefijo -> 37/38 FALLO G-26 (correcto);
  con «decía » -> 38/38; con «en vez de » -> 38/38; con «reanclado » -> 38/38. CLASE A. CONFIRMADO.
  MATIZ: «decia» SIN TILDE **no** apaga nada (yo lo probé). La tabla de W escribe «decia»; el
  interruptor real es «decía». El hecho de W se sostiene; su transcripcion es ASCII.
- N1 RENOMBRAR un documento historico -> 37/38 FALLO G-29. NO CAE.
- N2 BORRAR un documento historico -> 37/38 FALLO G-29. NO CAE.
- N3 VACIAR una fuente obligatoria (01-PROCESOS.md) -> EXIT=2, 15/17, FALLO G-00 y G-34. NO CAE.
- CONTROL POSITIVO: modificar un MANIFIESTO inmutable -> 37/38 FALLO G-22. NO CAE.

### X-01 · MI HALLAZGO PROPIO, QUE NO TRAE NI `V` NI `W` — el emisor del SOBRE no esta protegido
  El SOBRE DE ANCLA se emite con `docs/evolucion/verificacion/emitir-sobre-de-ancla.py`, que VIVE
  DENTRO DEL REPOSITORIO QUE ANCLA y **no esta en ningun inventario de integridad**:
  G-22 cubre documentos numerados y manifiestos; G-34 cubre la bateria y su README; G-29 cubre
  topologia y duplicados. Ninguno cubre `verificacion/*.py` distinto de la bateria.
  EJECUTADO, sin commitear, sin tocar bateria / README / HEAD / refs / base / runner:
    paso 1  ensuciar 11-ARQUITECTURA-INTEGRADA.md   -> sobre con digest 7366c24b… y 53773 lineas, rc=0
    paso 2  + 3 lineas de puerta trasera en el emisor -> sobre con **DIGEST 19ac2551…, 67, 53772**,
            es decir **las DOCE filas sustantivas IDENTICAS al sobre honesto**, sobre un corpus corrupto
    paso 3  bateria sobre ese mismo arbol            -> **38/38 VERDE, EXIT=0**
  Y lo mismo con el DERIVADOR: puerta trasera que devuelve `{}` en `universos_publicados()`
  (desarma el cliquet entero) -> **38/38 VERDE**.
  SIGNIFICADO: `O18` adopta (b) porque «quien puede escribir el repositorio puede escribir la
  referencia», y advierte que otra comprobacion interna «solo moveria la circularidad de sitio».
  **La circularidad se ha movido de sitio**: del `HEAD` y del `.upstream-hash` al emisor.
  CLASE: **A** por la regla que el propio `W` declara (no hay que corromper la referencia
  ni commitear), con efecto destructivo sobre **B**. NO es `C`.

## 5. ¿EXCEDE LA PROPAGACION O QUEDO O18 INCOMPLETA? — forense propia
HECHOS (verificados por mi, primera mano):
- `O18` en su sede (DECISIONES L819-908): UNA condicion previa (PesquerApp). CERO menciones de
  «ADS operativo», «certificar adaptadores» y CERO reparto. Confirmo a V.
- La propagacion afirma TRES condiciones (doc11 L8350, L8488-8491, L10113-10120; CHECKPOINT L41-42,
  L1870-1871; 00-INDICE L88) y rotula «EL REPARTO, LITERAL DE `O18`» (doc11 L8470-8481).
FORENSE DE COMMITS — LO QUE NADIE HA MIRADO:
- `bcee159` «registrar O18 del Owner y su propagacion D108» es el commit de TRANSCRIPCION, y es el
  PRIMERO de la tanda. **SU PROPIO MENSAJE YA ESCRIBE LAS TRES CONDICIONES**:
  «(c) OBLIGATORIA en `F6`: … condicion previa a la adopcion permanente de PesquerApp,
   **a declarar ADS operativo y a certificar adaptadores**.»
  Es corroboracion CONTEMPORANEA de la transcripcion, independiente de §11.8, que llega
  un commit despues (`8e70d94`, commit de PROPAGACION).
- El REPARTO, en cambio, NO aparece en `bcee159`: nace en `8e70d94`. No tiene corroboracion
  contemporanea.
- FORMA ESTABLECIDA POR EL CORPUS: la entrada de `O17` (DECISIONES L798-810) SI lleva dentro de §2
  «**El REPARTO DE RESPONSABILIDADES que el Owner decide**» con SIS/VER/PLT/SEG. La de `O18` no
  lleva seccion equivalente. Si el Owner reparte, la sede es §2, y `O18` la omite.
MI ADJUDICACION:
- Para LAS DOS CONDICIONES: la hipotesis «`O18` quedo INCOMPLETA» esta MEJOR sostenida que
  «la propagacion excede». Corroboracion contemporanea en `bcee159`.
- Para el REPARTO: INDETERMINADO. La unica prueba es la palabra del coordinador y el rotulo
  «LITERAL DE `O18`» que F4 escribio. **Rechazo el rotulo, no el contenido.**
- Y LO DECISIVO: ninguna de las dos vias es ejecutable por F4. Completar `O18` es F4 escribiendo
  palabras dentro de una resolucion del Owner: `G21` de KERNEL.md L690.

### X-02 · MI HALLAZGO · `O18` NO DECLARA SU PROPIA INVERIFICABILIDAD, Y `O17` SI LO HACIA
  `O17` (DECISIONES L760-769) declara literalmente: «**no se afirma que sea falsa — se declara
  INVERIFICABLE**, porque ningun gate puede contrastarla contra nada». Fue el remedio de `S-26`,
  que el doc 23 cerro «con honradez».
  `grep -rn INVERIFICABLE docs/` -> **UNA sola linea en todo el corpus, la de `O17`**.
  `O18` —la resolucion que existe PRECISAMENTE porque el corpus descubrio que no puede
  verificarse a si mismo— **no lleva esa declaracion**. Es una REGRESION del remedio de `S-26`
  aplicada a la resolucion siguiente, y es exactamente la grieta por la que el gate 3 no puede
  cerrar esta disputa. GRAVE · clase A (escribir en `O18` la declaracion que `O17` ya tiene).

### X-03 · el SOBRE DE ANCLA no ancla lo que hay que anclar
  `O18`(b) se adopta porque «quien puede escribir el repositorio puede escribir la referencia».
  El sobre ancla COMMIT, ARBOL, MANIFIESTO, DERIVADOR y UNIVERSO. **No ancla ninguna
  resolucion del Owner.** La disputa de §6 —que es la disputa que decide el remedio— cae
  ENTERA fuera de lo que (b) cubre. `docs/owner/` existe y tiene DOS ficheros: ninguno de
  `O15`-`O18`. GRAVE · clase **B** (el Owner tiene que decidir si ratifica y donde vive la sede).

### X-04 · MI HALLAZGO · el BLOQUE DE ESTADO ESTRUCTURADO del checkpoint va DOS eventos atrasado
  CHECKPOINT-ADS-NEXT.md L658-L724 — el bloque ```text «CHECKPOINT — ADS-NEXT/12 · SIS/evolucion»,
  que es el formato de `a.10` y el estado reanudable del fichero. NO esta dentro de ningun
  `[HISTORICO]` ni `[ESTADO ANTERIOR]`, y lleva `actualizado: 2026-08-30`.
    metodo:                 «RESOLUCION **O17** … y TANDA DE CORRECCION DEL GATE DE
                            CERTIFICACION (**documento 22**) EN APLICACION»
    metodo_anterior (1º):   el gate del documento 22
    last_meaningful_event:  «EL OWNER RESPONDE … del documento 22 … se registra como **O17**»
    based_on:               termina en el documento **22** y en «O17 · D107»
  `grep '23-SEGUNDO\|O18\|D108'` sobre L658-760: **CERO**. El documento 23, `O18` y `D108`
  NO APARECEN en el bloque de estado. Faltan DOS eventos: el veredicto del gate del doc 23 y `O18`.
  CONSECUENCIA: `C-L.7` —«el checkpoint reancla su estado en cada tanda»— esta declarada
  CERRADA en la clasificacion VIGENTE (L1640) y **queda falsada sobre el arbol que se juzga**.
  Es la CUARTA recurrencia de la clase (K-01/J-10/L-01 · P-05≡Q-08/R-02 · S-17≡S3-05 · esta).
  GRAVE · clase A. NADIE lo trae: `V3` conto las secciones «Siguiente accion exacta» y `V4`
  verifico los rotulos de los bloques; ninguno abrio el trailer estructurado.

## 6. LECTURA
- CHECKPOINT-ADS-NEXT.md (3323 lineas): **LEIDO INTEGRO POR MI**, en tramos consecutivos
  1-150 · 150-430 · 430-700 · 700-930 · 930-1160 · 1160-1400 · 1400-1620 · 1620-1900 ·
  1900-2200 · 2200-2560 · 2560-2800 · 2800-3060 · 3060-3325. Union = [1, 3325].
- 00-INDICE.md (175): LEIDO INTEGRO POR MI.
- El manifiesto (210): LEIDO INTEGRO POR MI, con `cat -n`.

### X-05 · MI HALLAZGO · el sobre declara ASIGNACIONES 18 y el manifiesto da 17
  Derivado mecanicamente de las marcas de revisor de §4: 2+1+3+2+8·1+1 = **17**.
  El sobre publica **18**. El emisor lo recibe por `--asignaciones` (required=True) y NO lo
  contrasta contra nada. El UNICO campo del sobre que nada contrasta es tambien el UNICO que
  es FALSO. `V-07` vio que no se contrasta; nadie comprobo el valor. `W` lo dio por «coherente»
  con una justificacion que no se sostiene («13 filas de §4 + 5 bloques de §5»: §5 tiene 54 filas).
  MEDIO · clase B.

### X-06 · el manifiesto §4 L70 es FALSO en la fila que define el universo (elevo `V-23`)
  Ver §2. Es `U-02` del doc 23 REINCIDENTE, mismo fichero, misma fila 8, un gate despues,
  y el CORRIGENDUM §6 acota el titular de lineas y NO la fila. MEDIO · clase B.

### X-07 · MI HALLAZGO · el runner esta en 11/13, no en 12/13: tambien T158 en ROJO
  `comprobar_evidencia.py` sobre el arbol del gate:
  «T158 FALLIDA · fuentes-salida.txt: la vigencia 'T161-cobertura' publica 305 y el corpus
   vigente da 306. La evidencia esta CADUCADA».
  Causa: el commit del manifiesto añade 1 fichero al corpus y no republica la evidencia derivada.
  Es LA PRIMERA de las «DOS CONDICIONES» que el propio CHECKPOINT L2196-2206 exige
  («la evidencia derivada se republica en el MISMO commit que cambia el corpus»). **Las DOS
  condiciones incumplidas por el mismo commit.**
  NADIE lo trae: `V` ejecuto `registrar_evidencia.py`, que REGENERA la evidencia y por tanto la
  oculta, y obtuvo 12/13; `W` solo ejecuto `comprobar_referencias.py`. MEDIO · clase A.

## 7. LA PRUEBA DE `V` CONTRA LA HIPOTESIS DEL COORDINADOR — LA REFUTO
`V` §4.2 / `R-6`: «si `O18` fuera transcripcion corta, el material faltante tendria que aparecer
en la PREGUNTA (doc 23 §13.B); no aparece; luego el Owner no pudo resolverlo».
**REFUTADO POR MI, contra la fuente.** `grep -in pesquerapp` sobre TODO el documento 23 devuelve
**UNA sola linea, L2691**, que esta en el parrafo de clase `C` de §13 y NO en §13·B. La
alternativa (c) de la PREGUNTA dice solo «`F4c` no se cerraria hasta entonces».
=> La UNICA condicion que `O18` SI registra —«PesquerApp no puede iniciar su adopcion
permanente…»— **TAMPOCO estaba en la pregunta.** El Owner respondio mas ancho que la pregunta
al menos una vez, y el corpus lo acepto sin objecion.
**El silogismo de `V` prueba de mas: aplicado con rigor tambien expulsaria la condicion que
todos aceptan. Por tanto no prueba nada.** `V` razona bien sobre la evidencia que tenia y su
premisa mayor es falsa.

## 8. E2 · LA VALLA (`W-01`/`W-02` ≡ `T-06`) — REPRODUCIDO POR MI, par control/mutante
  Misma linea inyectada, misma seccion VIVA «Siguiente accion exacta», mismo bloque ```text:
    L2815, ANTES de la etiqueta [ESTADO ANTERIOR]      -> 37/38 · FALLO G-26   (correcto)
    L2821, DESPUES del cierre `]` de esa etiqueta      -> **38/38 VERDE**      (defecto)
    L2921, 100 lineas mas abajo, aun dentro de la valla-> **38/38 VERDE**      (defecto)
  La etiqueta cierra su corchete en L2819 y la region exenta sigue abierta hasta la valla.
  CUARTO arbol defectuoso reproducido por mi. Clase A.

## 9. VERIFICACIONES DE CIERRE
- 00-INDICE L144-146 afirma HOY que su comando «da `T147` en verde». Lo ejecute: FALLIDA.
  Y anade «**La regla vale para el gate siguiente igual que para este**». `V-06` CONFIRMADO literal.
- Universo: OBLIGATORIO − ASIGNADO = VACIO en las dos direcciones (conjuntos identicos, 67/67).
- 54 agotamientos: regla 1 (fila propia + LEIDO INTEGRO en doc+linea) 54/54; regla 2 (bytes
  identicos al arbol citado) 54/54. **C-L.5 NO se reabre.**
- ASIGNADO − LEIDO = VACIO, **pero solo porque lo cerre yo**: la cadena `V` NO dejo declaracion
  de lectura integra del CHECKPOINT (`V3` lo cubre por temas; `V4` declara expresamente que NO
  leyo renglon a renglon ~1700 lineas de citas historicas). Yo lo lei integro, y `X-04` esta
  exactamente en el tramo que `V4` no abrio. La reserva era material.
