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
| [`CONTRATO-ESTADO-DURABLE.md`](CONTRATO-ESTADO-DURABLE.md) | el contrato derivado que `g.17` nombra: rutas, formato, protocolo, bloqueos y migración |
| `ads_estado.py` | el punto ejecutable. Sin él no habría forma de demostrar una interrupción real: el escenario extremo a extremo **mata procesos**, y para eso hacen falta procesos |
| `estado/` | el paquete: motor, transacción, diario, reconciliación, migración, bloqueo, serialización, rutas, errores, atestación y puntos de fallo |
| `pruebas/` | la batería del motor y el escenario extremo a extremo |

**El censo no se escribe: se deriva.**

```bash
ls -1 kernel/operativo/runtime/estado/*.py | xargs -n1 basename
python3 kernel/operativo/runtime/ads_estado.py --ayuda
```

## Cómo se invoca

```bash
# el motor, sobre un repositorio de control
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> inicializar
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> revision
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> verificar
python3 kernel/operativo/runtime/ads_estado.py --repo <dir> recuperar

# su batería, y su escenario extremo a extremo
python3 kernel/operativo/runtime/pruebas/test_estado_durable.py
python3 kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py
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
NO AFIRMA   que F6 esté completada · que ningún contrato esté CERTIFICADO · que exista
            dispatcher, verificador de admisión, raíz externa productiva ni adaptador ·
            ni que PesquerApp esté desbloqueada

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
