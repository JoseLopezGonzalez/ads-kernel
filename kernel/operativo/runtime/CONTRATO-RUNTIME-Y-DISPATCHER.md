# CONTRATO · RUNTIME Y DISPATCHER

**Qué es.** El contrato derivado del entregable `F6-D`, cuya norma es
`11-ARQ` §7 —`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que no viaja al proyecto instalado—. Fija cómo el runtime
selecciona trabajo, toma autoridad sobre él, lo ejecuta por un adaptador y escribe el
resultado **en el estado durable que ya existe**.

**Qué NO es.** No es una fuente de verdad. `§7.1` es literal: *«todo lo que decide queda
escrito en el estado canónico ANTES de que valga. Si el runtime muere, el estado sigue
siendo el estado»*. Y no es un segundo sistema de estado: no hay cola propia, ni diario
paralelo, ni recuperación alternativa. Cada decisión durable es una `Transicion` sobre el
`Almacen` de [`CONTRATO-ESTADO-DURABLE.md`](CONTRATO-ESTADO-DURABLE.md).

---

## 1 · Lo que el runtime escribe, y dónde

```text
canonico/items/<id>.json        la unidad de trabajo
canonico/paquetes/<id>.json     la unidad de DESPACHO, con su estado y sus intentos
canonico/leases/<paquete>.json  la autoridad temporal sobre un paquete
canonico/efectos/<efecto>.json  el ACUSE durable de un efecto ya aplicado
operacional/runtime/<inst>.vivo el testigo de vida. NO es durable y está fuera del git
```

**Vocabulario CERRADO del estado de un paquete**, y ninguna otra palabra vale:
`listo` · `despachado` · `ejecutando` · `completado` · `fallido` · `agotado` · `pausado` ·
`cancelado` · `bloqueado` · `esperando-dependencia`. Las transiciones permitidas están
declaradas como dato en `runtime/modelo.py`, y cualquier otra es `EstadoDePaqueteInvalido`.

## 2 · El tiempo lógico es la REVISIÓN, no el reloj

`I-g3` prohíbe reloj de pared, duración e identidad de proceso en cualquier byte durable. Un
lease **no puede** llevar un plazo. En su lugar:

```text
el titular RENUEVA          sube `latido` en cada transición suya sobre el paquete
un aspirante OBSERVA        cada observación es una transición durable que anota el
                            `latido` visto y cuántas observaciones consecutivas lleva
la RECLAMACIÓN es legítima  cuando el aspirante acumula PACIENCIA observaciones sin que
                            `latido` avance. Sube `epoca` y reinicia las observaciones
```

`PACIENCIA` vale **3** por defecto y es **parámetro CALIBRABLE**: `g.6` deja la resolución
entre máquinas al contrato derivado.

**La vía rápida de la misma máquina no sustituye a las observaciones y sólo vale hacia
abajo.** El testigo de vida es un `flock` en el plano operacional, y da **tres** respuestas,
no dos:

```text
el fichero NO existe                → INDECIDIBLE. El titular salió limpiamente, o es de
                                      otra máquina. Manda la regla de observaciones
existe y el `flock` está TOMADO     → VIVO
existe y el `flock` está LIBRE      → MUERTO. Sólo un final abrupto deja esa combinación,
                                      porque una salida limpia RETIRA el fichero
```

> **Y la regla que impide que la vía rápida se coma el lease:** `adquirir` **NUNCA roba**.
> Si hay lease de otro y no está probadamente muerto, es `AutoridadNoDisponible`. Robar lo
> hace sólo `reclamar`, y sólo por una de las dos vías de arriba.

## 3 · Idempotencia del efecto — dos niveles, y no son redundantes

```text
efecto = "ef-" + los doce primeros hexadígitos del digest de (orden, paquete, intento)

NIVEL 1 · el ACUSE      canonico/efectos/<efecto>.json, escrito en la MISMA transición que
  protege el ESTADO     el resultado del paquete: o se ven los dos, o no se ve ninguno
NIVEL 2 · el RECIBO     un fichero del espacio de trabajo del adaptador. El adaptador NO
  protege el EFECTO     escribe en el estado canónico: sería un segundo escritor, y `g.12`
                        declara UNO SOLO
```

**Entre los dos hay una ventana, y se dice en vez de callarla.** Si el proceso muere después
de ejecutar y antes del acuse, el runtime que recupera no ve acuse y **vuelve a invocar** al
adaptador; es el RECIBO el que impide la segunda aplicación y devuelve `repetido: true`. Lo
mide el escenario extremo a extremo: dos invocaciones, **una sola ejecución**.

## 4 · Las cuatro clases de fallo, que no son una

```text
REINTENTABLE          se escribe el fallo, el paquete vuelve a `listo` y suma un intento
DEFINITIVO            no se reintenta: el paquete queda `fallido`
CANCELACIÓN           terminal, y no admite reanudación
PÉRDIDA DE AUTORIDAD  NO se escribe NADA. El lease cambió de titular o de época bajo los
                      pies, y quien perdió la autoridad no toca el estado
```

**Al agotar los intentos**: el paquete pasa a `agotado`, el estado canónico deja de tocarse
y se abre el registro de reconciliación de `g.9` **en la misma pasada**. Un paquete agotado
no vuelve a adquirirse: sólo lo devuelve al trabajo una transición explícita de
reconciliación.

## 5 · Escritura bajo compare-and-swap

El motor aplica cada transición contra la revisión esperada. Con dos instancias reales, la
segunda recibe `RevisionObsoleta` aunque su intención sea legítima. La única puerta de
escritura del runtime es un ayudante que aplica la transición **como función de la revisión
leída**: en cada vuelta relee, **reevalúa la guarda** —¿sigo siendo titular? ¿el paquete
sigue donde esperaba? ¿el acuse ya existe?— y reconstruye. Releer y reaplicar la MISMA
transición convertiría el compare-and-swap en «el último gana», que es lo que `g.6` prohíbe.

## 6 · Vistas derivadas

Se calculan del estado canónico en cada llamada y **no se persisten**. Responden qué se está
construyendo, qué está bloqueado, qué espera decisión del Owner y qué reconciliaciones hay
abiertas. `§7.5` lo dice de una vez: *«una vista que sabe más que el estado es una segunda
verdad»*.

## 7 · Puntos de fallo controlados

Variable `ADS_RUNTIME_FALLO`, `os._exit(70)`, y nueve nombres:
`antes-de-adquirir` · `despues-de-adquirir` · `antes-de-ejecutar` · `durante-la-ejecucion` ·
`despues-del-efecto-antes-del-acuse` · `despues-del-acuse-antes-de-liberar` ·
`antes-de-reintentar` · `antes-de-agotar` · `antes-de-liberar`. El censo se DERIVA con
`fallos.puntos()`, y una prueba comprueba que ningún punto declarado queda sin llamar.

## 8 · Qué demuestra, y dónde

`T182`–`T186` en [`pruebas/test_runtime.py`](pruebas/test_runtime.py), y los veinticinco
pasos de `T193` en
[`pruebas/escenario_e2e_runtime.py`](pruebas/escenario_e2e_runtime.py). Punto ejecutable:
[`ads_runtime.py`](ads_runtime.py).

## 9 · Lo que este contrato NO cubre

El ciclo COMPLETO de `§7.2` —encuadre, composición de rutas por `b.16`, materialización de
equipos por `C4`, gates de capa y handoffs por `C5`— **no está implementado**: lo que existe
es la máquina de despacho sobre la que ese ciclo se apoyará. `Continúa` de `§7.4` tampoco:
su paso 2 exige además regenerar derivados y recompilar proyecciones, y eso es del corte
siguiente. Y **nada de esto está CERTIFICADO**.
