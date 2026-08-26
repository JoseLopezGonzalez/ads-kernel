# INVARIANTES — lo que no se modifica en silencio

La regla 12 de la [directiva](ADS-NEXT-OWNER-BRIEF.md) lo ordena: *«no modificar secciones
normativas aprobadas silenciosamente»*. Este documento dice **cuáles son**, **quién puede
cambiar cada una** y **por qué vía**. No las repite: las localiza.

## Cuatro grados de autoridad

```text
APROBADO POR EL OWNER      (a), (b) y sus enmiendas. Se cambian por ENMIENDA numerada,
                           con aprobación explícita y fecha. E1 es el precedente.

CONSTITUCIONAL 1.3.0       kernel/KERNEL.md. Congelado. a.11 declara qué reglas suyas
                           quedan derogadas, sustituidas, ajustadas o pendientes. Nada
                           fuera de a.11 lo deroga.

DERIVADO                   kernel/operativo/ y packs/. Deriva de lo aprobado y lo cita.
                           Se cambia con el proceso normal, sin tocar la fuente.

REGISTRADO                 decisiones tomadas sin consultar (D1–D8) y decisiones que
                           pertenecen al Owner (O1–O6). Reversibles, con su vía escrita.
```

## Lo aprobado por el Owner

| | qué fija | fuente |
|---|---|---|
| (a) | catálogo de capacidades, ficha de doce campos, custodia de paquetes, condición compuesta de paralelismo, contrato de veto, los tres frenos, estado persistido y checkpoint | [`a-CAPACIDADES-APROBADA.md`](../rediseno/a-CAPACIDADES-APROBADA.md) |
| (b) | estados de paquete, estado global como función total, transiciones, ciclo de vida, dependencias, cierre del item, `Continúa`, y la derivación de las diez rutas | [`b-RECORRIDO-APROBADA.md`](../rediseno/b-RECORRIDO-APROBADA.md) |
| E1 | `ENC` como capacidad base, materializada bajo demanda | [`a-ENMIENDA-E1-ENC.md`](../rediseno/a-ENMIENDA-E1-ENC.md) |

**Vía de cambio:** enmienda numerada, aprobada explícitamente por el Owner, conservando el
texto anterior. Ninguna reescritura en sitio.

### Los seis invariantes del estado (a.9)

Son el contrato que **cualquier** runtime debe cumplir, y el punto donde la directiva
presiona más fuerte. Se citan por su identificador —`I1` a `I6`— y viven en `a.9`. La
disposición física concreta **no** está aprobada: `a.9` la delega expresamente. Eso
significa que un runtime puede elegir su forma de almacenamiento sin enmienda, y **no**
puede elegir tener dos autoridades sobre el mismo campo.

### Los tres frenos (a.7), y el que autoriza esta iniciativa

`a.7` sustituyó `K0.9` por dos modos de fallo simétricos, con tres frenos. El tercero
—límite de racha `SIS` = 2— declara su propia excepción:

> **NO APLICA mientras el objetivo explícito del proyecto sea construir o migrar el propio
> kernel/runtime.**

La directiva del Owner hace de eso el objetivo explícito. **Por tanto esta iniciativa no
necesita autorización adicional para ser trabajo `SIS` sostenido**, y la advertencia
registrada al cerrar (b) —«el trabajo vuelve a los proyectos reales»— queda cubierta por la
excepción que la propia especificación escribió. Lo que **sigue vigente** es el modo de
fallo (b), autorreferencia sin producto: la directiva lo enuncia con otras palabras en su
apartado 26 al exigir progresión demostrable en vez de más documentación.

## Lo constitucional que sobrevive intacto

Enumerado en el [mapa del rediseño](../rediseno/00-MAPA.md) bajo *SOBREVIVEN*. Los que esta
evolución toca de cerca:

```text
K-1   las tres capas                    la directiva §4.3 presiona sobre esto — ver X1
K0.8  portabilidad entre proveedores    la directiva §9 la refuerza, no la contradice
K0.10 test de contaminación             cambia si cambia K-1, y sólo entonces
K0.11 el kernel vendorizado no se edita la directiva §15 pide instalador; instalar no es
                                        editar la copia instalada
K0.12 lo aprendido sube upstream        la directiva §12 lo amplía con destinos nuevos
G05   autoridad del Owner
G13   creación no es validación         estructura por defecto desde (a)
G27   seguridad dura
G29   Git: el Owner no es operador Git  la directiva §8 lo desarrolla, no lo deroga
G52   ledgers y regla de retirada
```

## Lo que ya estaba pendiente, y esta evolución hereda

No son invariantes: son **huecos declarados**, y quien los cierre debe saber que ya tenían
dueño asignado.

| | qué falta | delegado a |
|---|---|---|
| `G26` | `JOURNAL`: los tableros no son secuencia de eventos | memoria, eventos y recuperación |
| `G24` · `G34` · `G53` | presupuesto, vía rápida y valor diferencial | secciones (e), (f), (h) del rediseño, nunca iniciadas |
| `K0.2` | «no leer el kernel, compilar menos de 400 líneas» | sustituido por procedimientos por estación; `compile-agents.sh` todavía lo cita |
| `T25` | prueba abierta por diseño | disposición física del estado |
| `O2` | `KERNEL.md` 1.3.0 conviviendo con la línea 2.0 | un item `SIS` que aún no existe |

## La regla operativa de esta iniciativa

```text
1  Ninguna propuesta de arquitectura modifica (a), (b) ni E1. Registra la presión que
   ejerce, y propone la ENMIENDA por separado.

2  Toda contradicción detectada se escribe con las dos posturas enfrentadas, como exige
   el freno 1 de a.7. Ninguna capacidad cede en silencio.

3  Quien propone la arquitectura NO certifica su suficiencia. La directiva lo exige y la
   iteración anterior ya tiene el precedente: auditoría por un lector que no escribió el
   material, con sus hallazgos publicados.

4  Ninguna cifra se escribe a mano. Se deriva, y T151 lo comprueba.

5  Nada sube de estado de prueba por argumento. Sube porque se ejecutó y su salida quedó
   registrada.
```
