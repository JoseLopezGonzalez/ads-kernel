# T480–T482 — el estado durable entre dos ramas del mismo control repo

**Qué cierran.** Un hallazgo de la campaña de la Directiva del Owner de La Pesquerapp
(2026-09-15): dos ramas del repositorio de control —`ads/oficina-autonoma` y
`ads/interfaz-como-regla`— publicaban la MISMA revisión del estado durable, y cualquier
transacción en cualquiera de las dos produciría dos diarios con las mismas secuencias y
contenidos distintos, sin que nada lo dijera hasta el conflicto de `git merge`. El motor
detecta bifurcaciones entre dos ALMACENES vivos (`g.6`, `detectar_bifurcacion`); no entre
dos REFERENCIAS Git del mismo repositorio, que es el caso que ocurre.

El mecanismo es [`../runtime/estado/ramas.py`](../runtime/estado/ramas.py), publicado por
`ads_estado.py divergencia`, y su contrato es el §6 bis de
[`../runtime/CONTRATO-ESTADO-DURABLE.md`](../runtime/CONTRATO-ESTADO-DURABLE.md). Se mide
ejecutando: repositorios Git reales con almacenes reales, transacciones aplicadas por el
motor, y una ventana abierta producida matando de verdad al escritor con `ADS_ESTADO_FALLO`.

**Lo que NO afirman.** Que la clasificación sea correcta no significa que la
reconciliación exista: `RIESGO DE CONFLICTO` y `CONFLICTO DIRECTO` dicen qué habría que
hacer y nadie lo hace todavía. Es exactamente lo que la Directiva del Owner pide en su §62
—detectar antes de ejecutar, con vocabulario cerrado— y no lo que pide en §63.

Requisitos de la Directiva del Owner de La Pesquerapp que sostienen: `OWN-ADS-0226`,
`OWN-ADS-0223`, `OWN-ADS-0224`.

```text
T480  cinco clases de colisión de estado entre ramas, una por caso construido
T481  la CLI publica la clase y no resuelve; un diario manipulado y una ventana abierta son BLOQUEO
T482  sin `canonico/` en disco se escribe; con un enlace simbólico debajo, no (defecto reproducido)
```

---

```yaml ads:escenario
id: T480
nombre: El estado durable de dos ramas se clasifica con el vocabulario cerrado de colisiones
cubre: ["CONTRATO-ESTADO-DURABLE §6 bis", "g.6", "OWN-ADS-0226", "OWN-ADS-0224"]
dado:
  - "un control repo Git con un almacén inicializado y confirmado en `main`"
  - "ramas creadas desde ese commit sobre las que el motor aplica transacciones distintas"
cuando:
  - "se compara cada par de ramas con `ramas.comparar` sin abrir ningún almacén"
entonces:
  - "una rama sin transacciones nuevas frente a `main` es SIN INTERFERENCIA"
  - "una rama detrás de otra que avanzó es COMPATIBLE, y la relación dice quién avanza sobre quién"
  - "dos ramas que escribieron objetos DISTINTOS desde el antepasado común son RIESGO DE CONFLICTO"
  - "dos ramas que escribieron el MISMO objeto canónico son CONFLICTO DIRECTO, y el objeto se nombra"
  - "una referencia inexistente, o sin estado durable, es BLOQUEO con su motivo"
  - "ninguna comparación cambia la rama activa ni mueve la revisión de ningún almacén"
falla_si:
  - "una bifurcación con objetos comunes se publica como RIESGO en vez de CONFLICTO DIRECTO"
  - "comparar deja el árbol de trabajo en otra rama o con el estado modificado"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_entre_ramas.py
estado: validador-implementado
```

```yaml ads:escenario
id: T481
nombre: La CLI publica la divergencia y no resuelve; lo injuzgable es BLOQUEO
cubre: ["CONTRATO-ESTADO-DURABLE §6 bis", "§2.4", "g.8", "OWN-ADS-0223"]
dado:
  - "el mismo laboratorio de T480"
  - "una rama cuyo diario fue manipulado en un commit, y otra con una ventana de publicación abierta producida con ADS_ESTADO_FALLO=entre-el-paso-8-y-el-9"
cuando:
  - "se invoca `ads_estado.py --repo <repo> divergencia --ref-a X --ref-b Y`, con y sin --json"
entonces:
  - "la salida lleva la clase, la relación, los objetos comunes y `resolucion: no-se-decide-aqui`"
  - "la salida JSON y la de texto dicen la misma clase"
  - "la rama con el diario manipulado es BLOQUEO y el motivo nombra la secuencia que no encadena"
  - "la rama con ventana abierta es BLOQUEO y el motivo nombra la transacción"
falla_si:
  - "la CLI escribe algo en el estado o cambia de rama"
  - "un diario manipulado se clasifica como si estuviera sano"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_entre_ramas.py
estado: validador-implementado
```

```yaml ads:escenario
id: T482
nombre: Sin canonico/ en disco el motor escribe; con un enlace simbólico debajo, no
cubre: ["CONTRATO-ESTADO-DURABLE §2", "g.13", "rutas.ruta_canonica"]
dado:
  - "un almacén con una escritura confirmada en `main` y una rama creada ANTES de esa escritura"
  - "un checkout a esa rama: Git retira los objetos y con ellos el directorio `canonico/`"
cuando:
  - "el motor aplica una transición que escribe un objeto nuevo"
  - "y, en un almacén sano, se planta un enlace simbólico como dominio bajo `canonico/` y se escribe a través de él"
entonces:
  - "la primera escritura se admite y el objeto entra en `raiz` (antes: RUTA_INVALIDA «hay un enlace simbólico» sin que lo hubiera)"
  - "la escritura a través del enlace sigue siendo RUTA_INVALIDA y no deja ningún byte fuera de `canonico/`"
falla_si:
  - "un almacén sin `canonico/` en disco rechaza escrituras legítimas"
  - "un enlace simbólico bajo `canonico/` deja escribir fuera del árbol"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_entre_ramas.py
estado: validador-implementado
```
