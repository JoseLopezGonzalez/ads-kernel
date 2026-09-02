# 02 · MODELO OPERATIVO

Cómo circula el trabajo en ADS: de la frase del Owner al cierre del item, y de la
instalación del sistema a su actualización. **Este documento explica el recorrido; las
normas viven en sus contratos y se enlazan.**

Antes: [`01-MODELO-DEL-SISTEMA.md`](01-MODELO-DEL-SISTEMA.md).

---

## 1 · Paso 1 · de la expresión del Owner al item

**Ninguna expresión del Owner se convierte en trabajo por sí sola.** Terminar sin item es un
resultado correcto siempre que la intención no esté comprendida ni sea accionable.

```text
LA EXPRESIÓN LITERAL   se conserva SIEMPRE. La interpretación se añade al lado, nunca
                       encima.
LA CLASIFICACIÓN       por clase de expresión: la mayoría no produce trabajo.
EL CIRCUITO            estaciones con caminos de vuelta y dueño por tramo.
LAS FORMAS             de conversación, cada una con lo que resuelve sola y lo que
                       pregunta.
LOS TRES CRITERIOS     incertidumbre · confirmación · anclaje. Comprobables, con umbral
                       declarado y calibrable por uso real.
```

La capacidad que lo ejecuta es `ENC`. **Sede del paso 1, con sus cinco documentos en orden
de lectura:** [`kernel/operativo/entrada/00-INDICE.md`](../../kernel/operativo/entrada/00-INDICE.md).
Los recorridos completos de entrada, incluido el de referencia, están en
[`entrada/05-ESCENARIOS.md`](../../kernel/operativo/entrada/05-ESCENARIOS.md).

## 2 · El proceso lo determina el RESULTADO PERSEGUIDO

**Ésta es la regla de la que dependen las demás**: el proceso de un item **no** se elige por
las capacidades que se van a usar, sino por el resultado que persigue.

```text
FEA  capacidad nueva          GAP  expectativa o calidad ausente
DEF  defecto                  INC  incidente en uso real
INV  investigación            DEU  deuda técnica
DEP  dependencia              AUD  auditoría de un proyecto existente
DIR  cambio de dirección      SIS  evolución del sistema
```

**Cada proceso declara** su intención, su condición de entrada, su propietario global, sus
obligaciones —con capa exigida, capacidad productora, criterio de satisfacción y autoridad
de retirada— y sus capacidades condicionales con la condición exacta que las activa.

**Sede única, en forma canónica:**
[`recorrido/01-PROCESOS.md`](../../kernel/operativo/recorrido/01-PROCESOS.md). El recuento se
deriva:

```bash
grep -c '^id: proceso:' kernel/operativo/recorrido/01-PROCESOS.md
```

## 3 · Item, paquete, ruta, capa y obligación

```text
ITEM         la unidad de trabajo. Tiene proceso, ruta, estado global y propietario global.
RUTA         la composición de obligaciones y capacidades que el proceso deriva.
PAQUETE      la unidad de ejecución que una capacidad toma en custodia.
CAPA         lo que una capacidad DEPOSITA. Tiene vigencia: vigente, sustituida, invalidada.
OBLIGACIÓN   un resultado que DEBE existir para que la intención del proceso esté cumplida.
```

**Y hay una distinción de la que depende la honestidad del sistema entero:**

```text
SATISFECHA   existe capa vigente que produce el resultado exigido. EL RESULTADO EXISTE.
RETIRADA     una recomposición APROBADA declaró que la obligación dejó de ser necesaria,
             con quién tuvo autoridad y cómo afecta al resultado. EL RESULTADO NO EXISTE.
HUÉRFANA     ni satisfecha ni retirada. BLOQUEA EL CIERRE.
```

**Un informe que sume satisfechas y retiradas y lo presente como entregado es un defecto de
conformidad, no un redondeo.** Sede de los seis conceptos, de la tabla de autoridad por
materia y de las tres reglas duras —cancelar un paquete no retira su obligación · `DSP` no
retira · una retirada que cambia el resultado perseguido activa cambio de proceso—:
[`recorrido/00-OBLIGACIONES-Y-CIERRE.md`](../../kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md).

## 4 · Entregas entre capacidades: el handoff

**Un handoff no es «pasar el trabajo».** Tiene cinco obligaciones: quién entrega qué · qué
comprueba quien recibe · qué lo hace rechazable · qué evidencia acompaña una devolución ·
qué checkpoint sobrevive para que el receptor reanude sin hablar con el emisor.

**La regla que evita el rebote infinito:**

```text
QUIEN RECIBE COMPRUEBA ANTES DE TOMAR CUSTODIA.
  rechaza antes de aceptar  →  el paquete NO cambia de custodia. NO es devolución.
  acepta y luego descubre   →  ES devolución, y cuenta para el freno.
```

Forma del handoff: [`C5-HANDOFF.md`](../../kernel/operativo/contratos/C5-HANDOFF.md).
**Instancias concretas entre capacidades:**
[`circuitos/00-CIRCUITOS.md`](../../kernel/operativo/circuitos/00-CIRCUITOS.md) y
[`circuitos/handoffs-generales.md`](../../kernel/operativo/circuitos/handoffs-generales.md);
las de diseño, en
[`circuitos/DIS-handoffs.md`](../../kernel/operativo/circuitos/DIS-handoffs.md).
**`C5` define la forma; los circuitos, las instancias.**

## 5 · Los circuitos, y las seis preguntas que todo paso responde

```text
1  QUÉ RECIBE          artefactos concretos, con su versión
2  QUÉ COMPRUEBA       antes de tomar custodia, no después
3  CÓMO TRABAJA        qué método ejecuta
4  QUÉ DEJA            artefactos, memoria actualizada y capa depositada
5  QUIÉN SIGUE         qué capacidades pueden actuar después, y cuáles en paralelo
6  QUÉ PASA SI FALLA   a quién devuelve, con qué evidencia, y qué freno aplica
7  (transversal)       cuándo interviene el Owner — sólo donde la especificación lo exige
```

**Un circuito no es una cadena obligatoria**: se compone por condiciones. Lo que se fija es
qué ocurre **cuando** una capacidad se activa, no que se active siempre. Sede:
[`circuitos/00-CIRCUITOS.md`](../../kernel/operativo/circuitos/00-CIRCUITOS.md).

## 6 · Cierre del item

**`DSP` verifica; no declara.** La integración semántica la declara el propietario global, y
la retirada pertenece a la recomposición aprobada.

El gate `gate:cierre-de-item` comprueba, con evidencia y de forma automatizable:
terminación de la ruta vigente · cero obligaciones huérfanas · toda retirada con autoridad
identificada · vigencia de las capas · integración declarada por el propietario global ·
`learning_candidate` resuelto · y que el informe separe satisfechas de retiradas.

```text
SI FALLA   el item NO cierra. Sus salidas legítimas son `cancelado`, `bloqueado` o
           `en espera` — jamás `cerrado`.
```

Sede del gate, con sus comprobaciones y su fallo:
[`recorrido/00-OBLIGACIONES-Y-CIERRE.md`](../../kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md).
Plantilla del informe: [`plantillas/CIERRE.md`](../../kernel/operativo/plantillas/CIERRE.md).

## 7 · Trabajo autónomo, interrupción, reanudación y escalado

### Reanudación — la orden `Continúa`

**`Continúa` no significa «haz todo lo pendiente».** Es un procedimiento determinista de
siete pasos cuyo paso de verificación pregunta, entre otras cosas: si existen los artefactos
que los paquetes dicen haber producido · si hay transacciones abiertas · si hay deriva no
transaccional respecto a `HEAD` · si hay derivados divergentes de su revisión de origen · si
hay proyecciones con la huella rota · si siguen viables las dependencias en espera.

```text
TRANSACCIÓN ABIERTA   dos ramas, y no hay una tercera:
  COMPLETAR   todo casa con su base o su resultado → se aplica lo que falte en el orden
              declarado, y se regeneran los derivados
  MARCAR      algo no casa NI con la base NI con el resultado → `conflicto`, con copia
              íntegra de lo divergente. La salida la decide LA AUTORIDAD
NINGUNA DE LAS DOS cierra dejando una mezcla parcial publicable.
LO PUBLICADO NO SE RESTAURA NUNCA de forma automática; la reversión está acotada a lo
ESPECULATIVO LOCAL, y se verifica byte a byte antes de emitirse.
```

Sede: [`11-ARQUITECTURA-INTEGRADA.md` §7.4](../evolucion/11-ARQUITECTURA-INTEGRADA.md).
**Está DISEÑADO y NO CONSTRUIDO**, como el runtime que lo ejecuta —ver
[`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md)—.

### Escalado al Owner

```text
TRES NIVELES DE ATENCIÓN   obligatoria · opcional acumulada · ninguna
EL LOTE                    lo que espera al Owner se presenta AGRUPADO y ordenado por
                           coste de puesta en contexto
LA VISTA EJECUTIVA         es DERIVADA del estado canónico, no un informe redactado. Una
                           vista que sabe más que el estado es una segunda verdad
NO RESPONDE                nada que no esté en el estado
EL OWNER NO ES OPERADOR    ni de Git ni del runtime
```

## 8 · Los cuatro macrocircuitos del sistema

**Además del trabajo sobre el producto, ADS tiene cuatro circuitos sobre sí mismo:**

```text
N  INSTALACIÓN     en un proyecto nuevo
A  ADOPCIÓN        profunda, de un producto existente con historia
M  MIGRACIÓN       desde una versión anterior de ADS
U  ACTUALIZACIÓN   de ADS en un proyecto ya instalado
```

**Los cuatro arrancan con una `FASE 0` propia**: producen su propia certificación
Estructural **antes de cualquier mutación canónica**, mediante el **mismo** contrato
compartido —`gate:sistema-conforme`—. Si Estructural falla, el macrocircuito **se bloquea
antes de mutar estado**. Superar una ejecución anterior no certifica la actual, y un nivel
superior no implica que Estructural siga vigente.

> **Esto no es una convención de este corpus: es una resolución del Owner**, con su reparto
> de responsabilidades y sus reglas obligatorias. Sede canónica y precedencia en
> [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md); desarrollo arquitectónico y
> mapeo de cada macrocircuito a su proceso, en
> [`11-ARQUITECTURA-INTEGRADA.md` §8 y §18](../evolucion/11-ARQUITECTURA-INTEGRADA.md).
> **Ninguno de los cuatro está construido.**

## 9 · Git, y la convergencia multi-fuente

```text
POR FUENTE, SE CONSERVA   rama principal protegida · unidad de trabajo aislada · commits
                          como checkpoints trazables · push autónomo dentro de lo
                          autorizado · PR como punto de convergencia · CI como autoridad
                          automática · niveles de autoridad de merge graduados por riesgo ·
                          commit != push != merge != release != publicación · tags y
                          reversión · el Owner NO es operador Git

SE DEROGA                 la relación universal implícita que ataba cada item a UNA rama y
                          a UN pull request. Su formulación literal, y la enmienda que la
                          retiró, viven en `C7`; aquí no se reproduce, porque el corpus
                          tiene un verificador que persigue esa formulación por su FORMA

LA RELACIÓN CORRECTA      item o paquete → 0..N SOURCE CHANGES, uno por fuente
LA INTEGRACIÓN            es LÓGICA y evidenciada: un INTEGRATION SET declara la
                          combinación exacta de revisiones que se probó junta. NO existe
                          un commit multi-repositorio, y no se finge
```

Quién pide, quién ejecuta, quién bloquea y quién verifica cada operación:
[`C7-GOBIERNO-GIT-MULTI-SOURCE.md`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).
Plantilla del conjunto de integración:
[`plantillas/INTEGRATION-SET.md`](../../kernel/operativo/plantillas/INTEGRATION-SET.md).

## 10 · Adaptadores previstos, y una ausencia que se declara

```text
LO QUE HAY      una definición canónica NEUTRAL del comportamiento, PROYECCIONES generadas
                por entorno agentic, una HUELLA con validador de deriva y una prueba de
                humo en sesión nueva. Ningún adaptador está CERTIFICADO.

LO QUE NO HAY   **el corpus vigente NO contempla ningún adaptador de gestión de trabajo
                externa —Linear, Jira o equivalente—.** No está diseñado, no está
                contratado y no está prohibido: sencillamente **no existe en ninguna
                sede**, y quien lo necesite tiene que llevarlo al Owner como decisión
                nueva. Este corpus no la toma.
```

Arquitectura de adaptadores:
[`11-ARQUITECTURA-INTEGRADA.md` §6](../evolucion/11-ARQUITECTURA-INTEGRADA.md).

## 11 · Qué puede y qué NO puede hacer cada participante

| participante | puede | NO puede |
|---|---|---|
| **Owner** | decidir alcance, aprobar baselines, retirar obligaciones en materia suya, levantar vetos que le pertenecen, aceptar o rechazar la raíz externa de confianza | operar Git; sustituir a una capacidad en su materia; ser sustituido en las decisiones que la especificación le reserva |
| **`ENC`** | transcribir la expresión literal, encuadrar, medir incertidumbre, confirmación y anclaje | convertir una expresión en trabajo sin que los criterios se satisfagan |
| **`DSP`** | componer la ruta, materializar equipos, despachar paquetes, verificar el gate de cierre | **RETIRAR una obligación** —es autoridad semántica y no la tiene—; declarar la integración |
| **capacidad con custodia** | depositar su capa, declarar su vigencia, aceptar o rechazar un handoff antes de la custodia | declarar la capa de otra capacidad; cerrar el item |
| **propietario global** | declarar la integración semántica completa | sustituir el gate de cierre por su criterio |
| **`VER`** | producir el dosier de evidencia independiente | apropiarse de la decisión que pertenece a otra capacidad |
| **`SEG`** | bloquear por incumplimiento de seguridad, gobernar credenciales | ser retirada de un tramo donde la especificación la hace irretirable |
| **`PLT`** | ejecutar la maquinaria técnica y materializar | decidir lo que el contrato atribuye a otra capacidad |
| **`SIS`** | ser propietario y productor de la declaración Estructural | ser sustituido por el propietario del macrocircuito |
| **un verificador independiente** | leer, reproducir un defecto, demostrar su ausencia y dictaminar | **corregir nada.** Quien verifica no repara, y quien repara no verifica |

**La sede de la autoridad no es esta tabla**: es la especificación aprobada —(a) y (b) con
sus enmiendas— y los contratos que la instancian. La jerarquía completa y su precedencia
están en [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md).

## 12 · Escenarios completos, de principio a fin

**No se reescriben aquí: existen, están escritos y son ejecutables como prueba.**

| escenario | dónde |
|---|---|
| seis recorridos de entrada, incluido el de referencia | [`entrada/05-ESCENARIOS.md`](../../kernel/operativo/entrada/05-ESCENARIOS.md) |
| un circuito completo por cada uno de los diez procesos | [`circuitos/00-CIRCUITOS.md`](../../kernel/operativo/circuitos/00-CIRCUITOS.md) |
| escenarios extremo a extremo del sistema integrado | [`11-ARQUITECTURA-INTEGRADA.md` §14](../evolucion/11-ARQUITECTURA-INTEGRADA.md) |
| los cuatro macrocircuitos, paso a paso | [`11-ARQUITECTURA-INTEGRADA.md` §8](../evolucion/11-ARQUITECTURA-INTEGRADA.md) |
