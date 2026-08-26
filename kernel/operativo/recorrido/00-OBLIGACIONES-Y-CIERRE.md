# Obligaciones del proceso y cierre del item

> **Terminar la ejecución no es producir el resultado.** Ésa es la distinción sobre la que
> descansa toda la sección (b), y hasta la auditoría independiente no tenía **dónde
> escribirse**: no había campo, ni esquema, ni gate, ni plantilla. Las palabras
> `obligación_satisfecha`, `obligación_retirada` y `obligación_huérfana` no aparecían una
> sola vez en el corpus operativo (hallazgo **A-09**). Este documento las materializa.

## Los seis conceptos, y qué se rompe al confundirlos

```text
OBLIGACIÓN            un resultado que DEBE existir para que la intención del proceso esté
                      cumplida. Cada capacidad OBLIGATORIA de la ruta genera una (b.16).

SATISFECHA            existe una CAPA VIGENTE que produce el resultado exigido, o existe
                      otra capa vigente ENLAZADA que lo cubre explícitamente.
                      → EL RESULTADO EXISTE.

RETIRADA              una recomposición APROBADA declara que la obligación dejó de ser
                      necesaria, identifica QUIÉN tuvo autoridad y explica CÓMO AFECTA al
                      resultado perseguido.
                      → EL RESULTADO NO EXISTE, y consta que se decidió eliminarlo.

RESUELTA              satisfecha O retirada. Es lo que el cierre exige.

HUÉRFANA              ni satisfecha ni retirada. La ejecución terminó y el resultado no
                      existe NI consta que se decidiera eliminarlo. Bloquea el cierre.

CAPA VIGENTE          `vigente` · `sustituida` · `invalidada` (b.3). Sólo una capa
                      `vigente` satisface; una `sustituida` satisface a través de la que
                      la reemplaza; una `invalidada` no satisface nada.
```

> **Producir lo que una obligación exigía y decidir que ya no forma parte del alcance son
> resultados DISTINTOS.** Si se llaman igual, el sistema puede informar de que entregó algo
> que en realidad se eliminó. Por eso son dos predicados y sólo uno significa que el
> resultado existe.

## Dónde vive cada cosa, quién la muta y quién tiene la autoridad

Los cinco conceptos de a.9 —propietario del campo, autoridad, ordenante, escritor del
comando y ejecutor de mutación— aplican aquí sin excepción:

| qué | se persiste en | autoridad semántica | ejecutor de mutación | proyección |
|---|---|---|---|---|
| la obligación y su enunciado | `estado/items/<ID>/01-ruta.md`, al componer la ruta | DSP compone la ruta; **el enunciado deriva del proceso**, no lo inventa DSP | DSP / runtime | `vista.md` del item, y la columna `necesita para avanzar` del tablero |
| **satisfacción** | el paquete que depositó la capa | la capacidad con custodia de esa capa | esa capacidad | el informe de cierre, columna SATISFECHAS |
| **retirada** | `estado/items/<ID>/01-ruta.md`, en la recomposición aprobada | la que fije el proceso: capacidad propietaria de la materia, propietario global u **Owner** si es materia suya. **NUNCA DSP** | DSP / runtime, con la orden ya autorizada | el informe de cierre, columna RETIRADAS |
| **vigencia de la capa** | el paquete propietario de la capa | la capacidad propietaria de esa capa, o el Owner en materia suya (b.5) | esa capacidad | `03-integracion.md` |
| **integración semántica** | `estado/items/<ID>/03-integracion.md` | **el propietario global**, y sólo él | propietario global | estado global del item |
| **resolución de aprendizaje** | el cierre del item: `learning_candidate: none \| <enlace>` | la capacidad que cierra, con APR si hay señal | DSP registra el valor | el informe de cierre |

**Tres reglas duras, y las tres existen porque su ausencia produjo el hallazgo:**

```text
1  CANCELAR UN PAQUETE NO RETIRA SU OBLIGACIÓN. Detiene la ejecución y deja la obligación
   HUÉRFANA mientras nadie con autoridad la retire. Cerrar todos los paquetes no resuelve
   nada por sí mismo.

2  DSP NO RETIRA. Retirar es autoridad semántica, y DSP no la tiene (b.5, b.9). DSP
   SOLICITA la retirada a quien la posee y la registra cuando llega autorizada.

3  UNA RETIRADA QUE CAMBIA MATERIALMENTE EL RESULTADO PERSEGUIDO no es una recomposición
   rutinaria: activa la regla de b.1 —cambio de proceso o item nuevo—. Recomponer no puede
   ser la vía silenciosa para reducir el alcance.
```

## El gate de cierre

Las cinco condiciones de b.10, como lista comprobable. **DSP verifica; no declara**: la
integración la declara el propietario global, y la retirada pertenece a la recomposición
aprobada.

```yaml ads:gate
id: gate:cierre-de-item
aplica_a: "todo item que se propone cerrar, sea cual sea su tipo de proceso"
comprobaciones:
  - id: terminacion
    comprueba: "ningún paquete de la RUTA VIGENTE continúa abierto: todos están cerrado o cancelado"
    como: "recuento de estados de paquete sobre la ruta vigente, no sobre rutas anteriores"
    automatizable: si
  - id: obligaciones-resueltas
    comprueba: "cero obligaciones huérfanas: toda obligación vigente del proceso está SATISFECHA o RETIRADA"
    como: "por cada obligación de la ruta, existe capa vigente que la satisface, o retirada aprobada con autoridad identificada"
    automatizable: si
  - id: retirada-con-autoridad
    comprueba: "toda obligación retirada identifica quién tuvo autoridad y explica cómo afecta al resultado perseguido"
    como: "lectura del registro de recomposición que la retiró"
    automatizable: si
  - id: vigencia
    comprueba: "ninguna obligación se apoya en una capa invalidada, y ninguna capa sustituida satisface salvo a través de la que la reemplaza"
    como: "recorrido de la vigencia de cada capa enlazada por una obligación satisfecha"
    automatizable: si
  - id: integracion
    comprueba: "el PROPIETARIO GLOBAL ha declarado la integración semántica completa"
    como: "declaración firmada en 03-integracion.md, con su identificador de rol"
    automatizable: si
  - id: aprendizaje
    comprueba: "learning_candidate está resuelto: none, o un enlace a la señal"
    como: "campo presente en el cierre; APR recibe paquete sólo si es distinto de none"
    automatizable: si
  - id: informe-separa
    comprueba: "el informe de cierre reporta POR SEPARADO obligaciones satisfechas y retiradas, y no suma ambas como entregado"
    como: "comparación del informe contra la plantilla de CIERRE"
    automatizable: si
evidencia:
  - "el recuento de estados de la ruta vigente"
  - "la tabla de obligaciones con su estado y la capa o la retirada que las resuelve"
  - "la declaración de integración semántica del propietario global"
  - "el informe de cierre con sus dos cifras separadas"
fallo: >
  El item NO cierra. Con obligación huérfana, su estado global es `bloqueado` si el trabajo
  de reemplazo es identificable, o `en espera` si lo que falta es decidir si se retira
  (b.4 P10). Un item con todos sus paquetes cancelados y ninguna retirada aprobada no puede
  cerrar nunca: su salida legítima es `cancelado`, `bloqueado` o `en espera`, jamás
  `cerrado`.
```

> **Una obligación RETIRADA nunca se reporta como funcionalidad, evidencia ni resultado
> entregado.** Un informe que sume satisfechas y retiradas y lo presente como entregado es
> un defecto de conformidad, no un redondeo. La plantilla que lo impide está en
> [`../plantillas/CIERRE.md`](../plantillas/CIERRE.md).

## Los diez procesos y sus obligaciones

Las obligaciones no se inventan por item: **se derivan del proceso**. Cada capacidad
marcada obligatoria en b.16 genera una, y aquí quedan en forma canónica para que el
runtime las cree y el gate las compruebe.

Los procesos están en [`01-PROCESOS.md`](01-PROCESOS.md).
