# PLT · PLATAFORMA — la maquinaria

**Construye y posee** la maquinaria: CI, entornos, tooling, observabilidad y aislamiento
multiagente. Tiene backlog propio y **no toma custodia de paquetes de producto** (a.3): esa
separación evita que el trabajo por item y el de infraestructura compitan en una sola cola.

```yaml ads:capacidad
id: PLT
nombre: Plataforma
clase: servicio
mision: >
  Que exista y funcione la maquinaria con la que trabajan las demás capacidades: entornos
  donde probar, integración continua, observabilidad y aislamiento entre agentes.
capa_de_valor: >
  Añade capacidad de trabajo: entornos, automatización y señales que las demás capacidades
  necesitan para poder hacer lo suyo y para poder demostrarlo.
entrada:
  - "una carencia de maquinaria que bloquea a otra capacidad"
  - "un item de su backlog propio"
  - "una consulta sobre disponibilidad de entornos o dispositivos"
salida:
  - "el entorno, la automatización o la señal que faltaba, funcionando"
  - "la respuesta sobre disponibilidad, con el estado real"
gate: gate:maquinaria-disponible
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/plataforma/ENTORNOS.md — qué entornos hay, qué contienen y quién los usa"
  - "docs/plataforma/AISLAMIENTO.md — cómo se aíslan los agentes que trabajan en paralelo"
tablero: "estado/tableros/PLT.md — backlog propio y bloqueos que desbloquear"
metodos: [PLT/Maquinaria]
checkpoint: "en su item, con qué está montado y qué falta"
autoridad:
  decide_sola:
    - "cómo se construye la maquinaria y con qué herramientas"
    - "la estrategia de aislamiento entre agentes que trabajan en paralelo"
    - "el orden de su backlog propio, salvo cuando desbloquea a otra capacidad"
  escala:
    - "una carencia de maquinaria que bloquea a varias capacidades y no cabe en su backlog"
    - "un coste de infraestructura que excede lo autorizado"
  veta: []
owner:
  nivel: ninguna
  criterio: >
    PLT no tiene interacción con el Owner salvo por coste de infraestructura, y esa
    conversación la lleva la capacidad que lo consume, no PLT.
roles: [PLT/maquinaria]
deriva_de:
  - "a.3 · PLT: construye y posee la maquinaria, backlog propio, sin custodia de paquetes de producto"
  - "b.16 · PLT es propietario global de los items DEP"
materializacion: >
  Se materializa cuando existe una carencia de maquinaria declarada, propia o que bloquea a
  otra capacidad. No se materializa para «mejorar el tooling» sin bloqueo que lo justifique:
  eso es el modo de fallo (b) de a.7.
retirada: >
  El rol se retira al entregar la maquinaria funcionando. La memoria de entornos y de
  aislamiento persiste.
```

```yaml ads:gate
id: gate:maquinaria-disponible
aplica_a: "toda entrega de PLT: un entorno, una automatización o una señal"
comprobaciones:
  - id: usable-por-quien-la-pidio
    comprueba: "la capacidad que declaró el bloqueo puede usarla y lo ha comprobado"
    como: "confirmación de la capacidad solicitante, con la operación que ya puede hacer"
    automatizable: si
  - id: documentada
    comprueba: "está escrito qué es, cómo se usa y qué la rompe"
    como: "entrada en ENTORNOS.md o en la documentación del proyecto"
    automatizable: si
  - id: reproducible
    comprueba: "se puede volver a montar desde cero siguiendo lo escrito"
    como: "el procedimiento está escrito y se ha ejecutado al menos una vez desde cero"
    automatizable: parcial
  - id: aislamiento
    comprueba: "si varios agentes van a usarla a la vez, está declarado cómo se aíslan"
    como: "entrada en AISLAMIENTO.md"
    automatizable: si
evidencia:
  - "la confirmación de quien la pidió"
  - "el procedimiento de montaje ejecutado"
fallo: >
  La entrega no se da por hecha y el bloqueo sigue vigente. Una maquinaria que sólo funciona
  en la máquina de quien la montó no desbloquea a nadie.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).

## El workspace es infraestructura de desarrollo

Materializar y mantener el workspace multi-fuente es de `PLT`. **La semántica del producto
sigue fuera de PLT**: prepara el terreno, no decide qué se construye en él.

```text
PREPARA        materializa las fuentes que un paquete necesita, y sólo ésas
AÍSLA          worktrees, sandboxes y cualquier mecanismo que permita trabajo concurrente
MANTIENE       cachés, entornos, servicios de desarrollo, CI cruzada, observabilidad
RETIRA         ramas abandonadas, con su registro, cuando ninguna custodia las reclama
NO DESTRUYE    ningún cambio local, ningún repositorio, ningún remoto ajeno. Un directorio
               ocupado por otro repositorio es un ERROR que se informa, nunca uno que se
               resuelve borrando lo de alguien
```

La orden concreta es [`tooling/workspace.py`](../../../../tooling/workspace.py); lo que
puede y lo que nunca hace está en
[`C6`](../../contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md), y su propiedad operación a
operación en [`C7`](../../contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).
