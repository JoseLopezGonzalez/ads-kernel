# BASELINE — qué es ADS hoy, comprobado

Trabajo **23.1** de la [directiva](ADS-NEXT-OWNER-BRIEF.md). Reconstruye el estado real del
sistema antes de que nadie proponga arquitectura nueva.

**Regla de este documento:** ninguna afirmación de funcionamiento sin ejecución. Lo que no
se ha ejecutado se declara como contrato, y punto.

## Cómo se ha construido

```text
LECTURA        el corpus completo: (a), (b), E1, kernel/operativo/, packs/, tooling/,
               README, START_HERE, y los registros de decisiones y auditoría
EJECUCIÓN      los validadores del manifiesto canónico, uno a uno, capturando su código
               de salida — no su prosa
CONTRASTE      git: qué contiene cada referencia, y qué no
FECHA          2026-08-26
```

## Dónde vive ADS realmente

La directiva pide el estado «en `main`». La respuesta comprobada:

| referencia | versión de release | contiene el corpus 2.0 |
|---|---|---|
| `origin/main` | 2.0.0-alpha.2 | **sí** — entró por el PR #2, con la auditoría y sus correcciones |
| `redesign/kernel-2.0` *(HEAD)* | 2.0.0-alpha.2 | sí — es `origin/main` más el commit que incorpora esta directiva |
| `main` local | 1.3.0 | no — es una referencia local desactualizada, no un estado del repositorio |

**No hay divergencia de contenido entre la rama de trabajo y el remoto.** El único commit
de diferencia añade los dos documentos del Owner y corrige la matriz de hallazgos.

El baseline se tomó sobre **2.0.0-alpha.2**. Esta iniciativa publica **2.0.0-alpha.3**, y
por un solo motivo, escrito en el [changelog](../../kernel/KERNEL_CHANGELOG.md): alojar un
documento en voz del Owner. Ningún contrato, esquema, rol, método ni gate cambia.

## La escala de realidad, aplicada

Los seis niveles son los del apartado 21 de la directiva, y coinciden con los cuatro
estados de [`REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md) más el uso real.

| subsistema | contrato | implementación | prueba ejecutada | superada | uso en proyecto real |
|---|---|---|---|---|---|
| lenguaje canónico y esquemas | sí | `ads_lint` | sí | sí | **no** |
| contratos transversales C1–C5 | sí | validadores estructurales | sí | sí | **no** |
| capacidades, roles, métodos, prompts | sí | texto ejecutable por un agente | parcial: sólo su forma | sólo su forma | **no** |
| gates | sí | listas comprobables escritas | sólo su forma | sólo su forma | **no** |
| recorrido, estados, transiciones, procesos | sí | — | **no** | no | **no** |
| estado persistido y tableros (a.9) | seis invariantes | **no existe ningún fichero de estado** | no | no | **no** |
| checkpoint (a.10) | sí | plantilla + uso a mano en `docs/` | no como mecanismo | no | **no** |
| packs `web-app` · `mobile-app` · `wear-os` | sí | contenido escrito, composición computable | sí, la composición | sí | **no** |
| validadores | sí | once ejecutables | sí | sí | **no** |
| instalación `new-project.sh` | sí | script | sí, por T148 | sí | **no** |
| runtime y dispatcher | parcial | **no existen** | no | no | no |
| adaptadores de proveedor | **no existe contrato** | no | no | no | no |
| gobierno Git del proyecto real | sólo `G29` en prosa 1.3.0 | no | no | no | no |
| adopción de proyecto existente | «Ruta B» de `START_HERE` | copia manual + un prompt | no | no | no |
| aprendizaje proyecto → ADS | `APR/Promocion` + `docs/UPSTREAM.md` | plantilla vacía | no | no | no |
| actualización ADS → proyecto instalado | **no existe contrato** | sólo detección de divergencia | — | — | no |

La columna que importa es la última. **Está vacía entera.** Ninguna pieza de ADS ha pasado
por un proyecto real.

## Lo que se ejecuta hoy, y con qué resultado

Reproducible con una sola orden, desde la raíz:

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # vacío: los generados son deterministas
```

Ejecutado el 2026-08-26 sobre este árbol: **los once validadores del manifiesto terminan en
verde**, y su salida es la publicada en
[`pruebas/evidencia/`](../../kernel/operativo/pruebas/evidencia/). El desglose por prueba,
derivado y no escrito a mano, está en
[`REGISTRO-generado.md`](../../kernel/operativo/pruebas/REGISTRO-generado.md).

**Al entrar esta iniciativa, dos de ellos fallaban**, y el motivo es un hallazgo del propio
baseline:

```text
ads_lint                 8 errores de vocabulario, todos en los dos documentos del Owner
comprobar_referencias    T147 FALLIDA: los dos documentos del Owner «existen para nadie»
```

Los dos documentos entraron al repositorio sin quedar integrados en el corpus. No es un
defecto de la directiva: es que **ADS no tenía forma declarada de alojar un documento en voz
del Owner**. Resuelto por la vía que el propio kernel prevé —exención acotada con motivo en
[`exclusiones.yaml`](../../kernel/operativo/validadores/exclusiones.yaml), y alcanzabilidad
por el [índice](00-INDICE.md)— y registrado como candidato de contrato en
[`02-MAPA-DIRECTIVA.md`](02-MAPA-DIRECTIVA.md).

## Lo que hoy es manual

Nada de esto tiene ejecutor automático. Lo hace un agente leyendo un método, o el Owner.

```text
ENRUTAR un item a su ruta            DSP está escrito; no hay quien lo ejecute
MANTENER el estado de un paquete     no hay fichero de estado que mantener
ESCRIBIR y leer checkpoints          formato definido; el portador es la disciplina
APLICAR los tres frenos de a.7       DSP/supervision está escrito; nadie cuenta
COMPONER una ruta                    b.16 la deriva; la derivación la hace una persona
INSTALAR en un proyecto existente    copiar directorios a mano (START_HERE, ruta B)
CONSTRUIR el PROFILE                 rellenar una plantilla, o conversar
COMPILAR AGENTS.md                   tooling/compile-agents.sh NO compila: imprime un
                                     encargo, y lo hace contra packs/*.md, la forma
                                     PLANA de la línea 1.3.0 que ya no existe
ACTUALIZAR un proyecto instalado     no hay procedimiento; sólo detección de divergencia
```

## Lo que está ausente por completo

Ausente significa: **no hay contrato, no hay implementación y no hay prueba**.

```text
runtime · dispatcher · colas · event log · recuperación tras fallo
adaptadores de proveedor agentic — el kernel es neutral por AUSENCIA, no por diseño
gobierno Git del proyecto real más allá de una regla en prosa de 1.3.0
trazabilidad item/paquete ↔ commit ↔ release ↔ despliegue
circuito de adopción de un proyecto con historia
circuito de construcción asistida del PROFILE
migración de un proyecto de una versión de ADS a otra, y su rollback
capa de conocimiento tecnológico reutilizable entre NUESTROS proyectos
documentación consultable de lo aprendido, separada del changelog
vista ejecutiva para el Owner sobre estado persistido
```

## Deudas y contradicciones conocidas, ya registradas

No se reabren aquí. Se enumeran porque cualquier arquitectura nueva las hereda.

| | qué | dónde vive |
|---|---|---|
| A-30 | asimetría de profundidad: `DIS` tiene once roles frente a uno o tres de las demás | [matriz de correcciones](../rediseno/CORRECCIONES-POST-AUDITORIA.md) · aceptada como deuda |
| G26 | `JOURNAL` no está derogado: los tableros no son secuencia de eventos | `a.11` · se decide con memoria y eventos |
| T25 | abierta por diseño hasta que exista disposición física del estado | [`REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md) |
| C1 | `ENC` como capacidad frente a la letra de `a.3` | [decisiones](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) · resuelta por E1, la frase de `a.3` sigue sin enmendar |
| O2 | `KERNEL.md` 1.3.0 conviviendo con la línea 2.0 | ídem · con su condición de resolución escrita |
| O3–O6 | umbral de anclaje, presupuesto de exploración, veto visual, idioma | ídem · con valor por defecto implementado |
| — | `compile-agents.sh` apunta a la forma plana de packs, retirada por D3 | este baseline; no estaba registrado |
| — | el checkpoint de la iniciativa anterior nombra una rama que ya no existe en local | este baseline; es historia de una iniciativa cerrada, no un defecto activo |

## La conclusión que condiciona todo lo que sigue

```text
ADS es hoy un CORPUS NORMATIVO Y OPERATIVO COMPLETO, verificado contra sí mismo
por once validadores, y CERO VECES CONTRA LA REALIDAD.

La directiva pide una plataforma instalable, portable, acumulativa y multiagente.
La distancia entre ambas cosas NO es documentación: es ejecución.
```
