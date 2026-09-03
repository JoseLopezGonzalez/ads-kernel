# `runtime/` — lo que EJECUTA la norma

**Qué hay aquí.** Código. Este directorio es la parte del kernel operativo que **no
describe** el sistema: lo **ejecuta**. Empieza con el motor de **estado durable**, que es el
primer eslabón de `F6` después de la norma.

**Qué NO hay aquí.** Norma. La norma de esta materia es la sección
[`(g)`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md), aprobada por el Owner mediante
`O23`, y **este directorio no la modifica ni la reformula**. Su contrato derivado —el
mecanismo— es [`CONTRATO-ESTADO-DURABLE.md`](CONTRATO-ESTADO-DURABLE.md).

**Y una distinción que conviene no perder.** Los **validadores** de
[`../validadores/`](../validadores/validadores.yaml) comprueban la **consistencia del
corpus**. Esto es otra cosa: administra el **estado de un producto**. Un verde de la batería
del corpus no dice nada sobre si este motor funciona, y por eso el motor trae **su propia
batería**, registrada en el mismo manifiesto canónico y con su propia evidencia.

---

## Qué hay, fichero a fichero

| pieza | qué es |
|---|---|
| [`CONTRATO-ESTADO-DURABLE.md`](CONTRATO-ESTADO-DURABLE.md) | el contrato derivado que `g.17` nombra el primero: rutas, formato, protocolo, bloqueos y migración |
| [`CONTRATO-GOBIERNO-GIT-CONTROL.md`](CONTRATO-GOBIERNO-GIT-CONTROL.md) | el **segundo** de `g.17`: `g.14`, la tabla de propiedad, la concesión de ref y `G-A8` |
| [`CONTRATO-RAIZ-EXTERNA.md`](CONTRATO-RAIZ-EXTERNA.md) | el **tercero** de `g.17`: `g.15`, `O25` y `V6-16`. Firma ASIMÉTRICA, identidad, custodia, rotación e independencia. Su paquete vive FUERA de este directorio |
| [`CONTRATO-RUNTIME-Y-DISPATCHER.md`](CONTRATO-RUNTIME-Y-DISPATCHER.md) | `F6-D`: trabajo elegible, autoridad temporal, despacho, reintentos y vistas derivadas |
| [`CONTRATO-ADMISION.md`](CONTRATO-ADMISION.md) | `F6-A`: los cortes `V2`–`V5` del verificador de admisión, y la deuda `S1-02` |
| [`CONTRATO-ADAPTADOR.md`](CONTRATO-ADAPTADOR.md) | `F6-G` y el corte `V7`: interfaz, adaptador local real, proyección y deriva |
| [`CONTRATO-CICLO-Y-MACROCIRCUITOS.md`](CONTRATO-CICLO-Y-MACROCIRCUITOS.md) | el macrobloque 3: el ciclo de `§7.2`, `Continúa` de `§7.4` y los cuatro macrocircuitos con su `FASE 0` |
| [`CONTRATO-ARBOLES-ADVERSARIALES.md`](CONTRATO-ARBOLES-ADVERSARIALES.md) | `V6-15`: el derivador del conjunto de `§20.5`, su suite de regresión y su matriz |
| [`CONTRATO-CONTENCION.md`](CONTRATO-CONTENCION.md) | `FD-5`: los contenedores de recursos del anfitrión, su detección y su fallo cerrado |
| `ads_estado.py` | el punto ejecutable del motor. Sin él no habría forma de demostrar una interrupción real: el escenario extremo a extremo **mata procesos**, y para eso hacen falta procesos |
| `ads_runtime.py` · `ads_admision.py` · `ads_ciclo.py` · `ads_arboles.py` | los puntos ejecutables del runtime, del verificador de admisión, del ciclo y del derivador de árboles |
| `estado/` | el motor: transacción, diario, reconciliación, migración, bloqueo, serialización, rutas, errores, atestación y puntos de fallo |
| `runtime/` · `gobierno/` · `admision/` · `adaptadores/` · `identidad/` | los cinco paquetes del segundo corte |
| `ciclo/` · `macrocircuitos/` | las ocho etapas del ciclo, `Continúa`, y los cuatro macrocircuitos como composiciones del mismo motor |
| `arboles/` · `contencion/` | `V6-15` —los árboles adversariales derivados, con sus versiones históricas vulnerables— y `FD-5` —la contención del anfitrión, con su detección y sus niveles— |
| `pruebas/` | las once baterías y los tres escenarios extremo a extremo |

**El censo no se escribe: se deriva.**

```bash
ls -1 kernel/operativo/runtime/estado/*.py | xargs -n1 basename
python3 kernel/operativo/runtime/ads_estado.py --ayuda
```

## Cómo se invoca

```bash
# el motor, sobre un repositorio de control
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> inicializar
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> verificar

# el runtime: trabajo, autoridad y despacho por un adaptador real
python3 kernel/operativo/runtime/ads_runtime.py --repo <dir> --instancia runtime-A elegibles
python3 kernel/operativo/runtime/ads_runtime.py --repo <dir> --instancia runtime-A         --adaptador-local <espacio> ciclo

# el verificador de admisión
python3 kernel/operativo/runtime/ads_admision.py --repo <dir> verificar --base <rev>
python3 kernel/operativo/runtime/ads_admision.py --repo <dir> censo-zonas

# las baterías, y los dos escenarios extremo a extremo
python3 kernel/operativo/runtime/pruebas/test_estado_durable.py
python3 kernel/operativo/runtime/pruebas/test_runtime.py
python3 kernel/operativo/runtime/pruebas/test_gobierno_git.py
python3 kernel/operativo/runtime/pruebas/test_admision.py
python3 kernel/operativo/runtime/pruebas/test_adaptadores.py
python3 kernel/operativo/runtime/pruebas/test_identidad.py
python3 kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py
python3 kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py
python3 kernel/operativo/runtime/pruebas/test_ciclo.py
python3 kernel/operativo/runtime/pruebas/test_continua.py
python3 kernel/operativo/runtime/pruebas/test_macrocircuitos.py
python3 kernel/operativo/runtime/pruebas/test_arboles.py
python3 kernel/operativo/runtime/pruebas/test_contencion.py
python3 kernel/operativo/runtime/pruebas/test_raiz_externa.py
python3 kernel/operativo/runtime/pruebas/test_multimaquina.py
python3 kernel/operativo/runtime/pruebas/test_sesion_nueva.py
python3 kernel/operativo/runtime/pruebas/escenario_e2e_f6.py

# el derivador de arboles adversariales de V6-15
python3 kernel/operativo/runtime/ads_arboles.py conjunto --json
python3 kernel/operativo/runtime/ads_arboles.py suite

# la RAIZ EXTERNA vive en un PAQUETE SEPARADO, fuera de runtime/, y se instala FUERA
# del arbol verificado. Se nombra por su ruta y no se enlaza: no viaja con este directorio
#   kernel/operativo/raiz-externa/instalar.py   --destino <fuera-del-arbol>
#   kernel/operativo/raiz-externa/verificador.py capacidades
```

**Los dos entran en el manifiesto canónico de validadores**
—[`validadores.yaml`](../validadores/validadores.yaml)—, los ejecuta el runner y su
evidencia se publica en `../pruebas/evidencia/`. Un validador que no está en el manifiesto
quedaría fuera de la evidencia sin que nada lo dijera, y eso ya pasó una vez.

## Requisito de entorno

La guarda de versión del intérprete vive en
[`../validadores/entorno.py`](../validadores/entorno.py) y se comprueba **antes de correr**.
Un entorno insuficiente termina con código propio —`78`—, distinto del `1` de «una
comprobación no pasó»: un entorno que no llega **no puede confundirse con un producto roto**.

## Lo que este directorio NO afirma

```text
NO AFIRMA   que ningún contrato esté CERTIFICADO · que F6 esté CERRADA · ni que
            PesquerApp esté desbloqueada. Lo que hay construido y probado, y lo que
            NO, se lee en la sede del estado de implementación, y no aquí

IMPLEMENTADO Y PROBADO no es CERTIFICADO: la certificación la emite un juicio
independiente, y no quien construyó
```

El estado de implementación de `F6`, contrato a contrato, tiene una sola sede, y vive en el
repositorio del kernel: **no se enlaza desde aquí a propósito**, porque este directorio VIAJA
a cada proyecto instalado y esa sede no. Se nombra por su ruta, que es lo que un enlace
haría de todas formas:

```text
docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md
```
