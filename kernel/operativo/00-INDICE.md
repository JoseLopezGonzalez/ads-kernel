# KERNEL OPERATIVO — índice y regla de fuente única

`kernel/operativo/` es la **instanciación ejecutable** de la especificación aprobada en
[`docs/rediseno/a-CAPACIDADES-APROBADA.md`](../../docs/rediseno/a-CAPACIDADES-APROBADA.md)
y [`docs/rediseno/b-RECORRIDO-APROBADA.md`](../../docs/rediseno/b-RECORRIDO-APROBADA.md).

```text
(a) y (b)             ESPECIFICACIÓN NORMATIVA — invariantes, autoridad, estados,
                      recorrido. Aprobadas. No se modifican desde aquí.
kernel/operativo/     CONTENIDO OPERATIVO — roles, métodos, gates, prompts, plantillas,
                      circuitos, rúbricas, validadores y pruebas. Es lo que un equipo
                      ejecuta. Deriva de (a) y (b) y las cita; no las repite.
packs/<clase>/        ESPECIALIZACIÓN POR CLASE DE PROYECTO. Amplía. No sustituye.
PROFILE.md            UN proyecto concreto.
```

## Regla de fuente única

> **Una verdad vive en un fichero.** Los demás la **enlazan**. Repetirla es un defecto de
> conformidad, no una comodidad de lectura.

Cuando un documento necesita una verdad que ya existe:

```text
CORRECTO    «la condición compuesta de paralelismo (a.5)» + enlace
INCORRECTO  copiar las seis condiciones aquí «para que se lea de un tirón»
```

`ads_lint` no detecta toda duplicación semántica. La detecta la revisión adversarial, y
cuando aparece se resuelve **borrando la copia**, nunca sincronizando las dos.

## Mapa de fuente única

| verdad | fuente única |
|---|---|
| catálogo de capacidades, autoridad, veto, frenos, paralelismo, checkpoint | (a) |
| estados, transiciones, cierre, obligaciones, rutas por tipo, `Continúa` | (b) |
| formato canónico de los artefactos operativos | [`esquemas/00-LENGUAJE.md`](esquemas/00-LENGUAJE.md) |
| forma de cada tipo canónico | `esquemas/<tipo>.yaml` |
| ficha operativa de una capacidad | `capacidades/<COD>/CAPACIDAD.md` |
| contrato de un rol | `capacidades/<COD>/roles/<rol>.md` |
| procedimiento de un rol | `capacidades/<COD>/metodos/<Metodo>.md` |
| prompt operativo de un rol | `capacidades/<COD>/prompts/<rol>.md` |
| entrada del Owner y su circuito | `entrada/` |
| excelencia de diseño | `diseno/` |
| entregas entre capacidades | `circuitos/` |
| pruebas de conformidad nuevas | `pruebas/` |
| estado real de cada prueba | [`pruebas/REGISTRO.md`](pruebas/REGISTRO.md) |

## Qué hay aquí

```text
esquemas/       el lenguaje canónico y la forma de cada tipo
contratos/      los contratos transversales: equipo, rol, agente, método, materialización
entrada/        PASO 1 — de la frase del Owner al item
capacidades/    PASOS 4 y 5 — una carpeta por capacidad, con roles, métodos y prompts
diseno/         PASO 3 — el sistema de excelencia de Diseño
circuitos/      PASO 5 — handoffs concretos entre equipos
plantillas/     artefactos rellenables: encuadre, checkpoint, paquete, devolución
validadores/    ads_lint.py y sus reglas
pruebas/        escenarios de conformidad y su registro honesto de estado
```

## Cómo se usa esto sin haber visto ninguna conversación

```text
1  lee esquemas/00-LENGUAJE.md            cómo se leen los bloques canónicos
2  lee contratos/C1-EQUIPO-ROL-AGENTE-METODO.md   qué es un rol y qué debe declarar
3  localiza tu capacidad en capacidades/<COD>/CAPACIDAD.md
4  localiza tu rol y su prompt operativo
5  ejecuta su método paso a paso, escribiendo checkpoint donde el método lo exige
6  cierra por su gate, no por tu criterio
```

Nada de lo anterior requiere leer el kernel entero, ni conocer la historia del proyecto.

## Relación con `kernel/KERNEL.md` 1.3.0

`KERNEL.md` es la constitución en prosa de la versión 1.3.0. La sección a.11 declara qué
reglas suyas quedan derogadas, sustituidas, ajustadas o pendientes. **Mientras el runtime
no exista, `KERNEL.md` sigue siendo el documento de arranque de un proyecto**, y este
directorio es el contenido que ese runtime consumirá. La convivencia y su fecha de
resolución están registradas en
[`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`](../../docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md).
