# Circuitos entre equipos

<!-- ads-lint: permitir-vocabulario-prohibido -->

b.16 deriva **diez rutas** a partir del resultado perseguido. Este documento las convierte en
**recorridos concretos**: qué recibe cada equipo, qué comprueba, cómo trabaja, qué deja,
quién puede actuar después, qué ocurre si falla, y cuándo interviene el Owner.

> **No es una cadena obligatoria.** Cada circuito se sigue componiendo por condiciones. Lo
> que aquí se fija es qué ocurre **cuando** una capacidad se activa, no que se active siempre.

## Las seis preguntas que todo paso debe poder responder

Cada tramo de cada circuito responde a las seis. Cuando el detalle es propio de un par de
capacidades, vive en su bloque `ads:handoff`; cuando es propio del circuito, vive aquí.

```text
1  QUÉ RECIBE      artefactos concretos, con su versión
2  QUÉ COMPRUEBA   antes de tomar custodia, no después
3  CÓMO TRABAJA    qué método ejecuta
4  QUÉ DEJA        artefactos, memoria actualizada y capa depositada
5  QUIÉN SIGUE     qué capacidades pueden actuar después, y cuáles en paralelo
6  QUÉ PASA SI FALLA  a quién devuelve, con qué evidencia, y qué freno aplica
```

Y una séptima, transversal: **cuándo interviene el Owner** — sólo donde a.8 lo exige.

---

## FEA · capacidad nueva

```text
ENC ──► PRD ──┬─► [DIS si C-DIS] ──┐
              └─► [ARQ si C-ARQ] ──┤
                                   ├─► [DOM:condiciones] ⊳ CON ──► VER ──► [ENT si C-ENT]
                                   └─► [SEG:condiciones] ⊳        │
                                                                   └─► [USO si C-USO] ──► [APR si C-APR]
propietario global: PRD
```

| tramo | qué comprueba quien recibe | si falla |
|---|---|---|
| ENC → PRD | criterio de éxito escribible; anclaje sin duplicado | devuelve a ENC con el campo que falta |
| PRD → DIS | fuera de alcance escrito; superficie identificada | devuelve a PRD con las dos formas que cumplen igual |
| PRD → ARQ | alcance cerrado; contratos previsibles | devuelve a PRD si el alcance excluye contratos necesarios |
| DIS ∥ ARQ | **pueden ir en paralelo** si sus paquetes cumplen las seis condiciones de a.5 | DSP secuencia si falla alguna |
| DOM/SEG:condiciones ⊳ CON | condiciones comprobables antes de construir | devuelve al plan que las hace incompatibles |
| CON → VER | diferencias declaradas antes de la revisión | infiel: vuelve a CON con la comparación |
| VER → ENT | dosier sin evidencia en rojo | veto de VER: no pasa |
| ENT → USO | señales declaradas y ventana abierta | devuelve a la capa que origina el rojo |

**Owner:** primera dirección de producto (PRD) · primera instancia de patrón visual (DIS) ·
publicación (ENT). En ningún otro punto.

---

## GAP · expectativa ausente respecto a algo existente

Comparte grafo con FEA y **es un proceso distinto**. Las diferencias operativas:

```text
ENCUADRE     el anclaje es sobre LO YA IMPLEMENTADO: qué existe y qué se creía que existía
PRD          ejecuta PRD/Gap, no PRD/Definicion: mide la DISTANCIA, no define alcance nuevo
DIS          si activa, casi siempre en nivel N1: el patrón existe y la superficie se quedó corta
APR          el aprendizaje es OBLIGATORIO en la práctica: por qué apareció el hueco es la
             pregunta más valiosa del sistema, y se pierde si se cierra sin ella
```

**Si al medir la distancia resulta que la expectativa es nueva**, el item ha cambiado de
naturaleza: amplía el alcance, y eso es materia del Owner (b.1).

---

## DEF · defecto

```text
[ARQ:diagnóstico si el diagnóstico no es evidente] ──► CON ──► VER ──► [ENT] ──► [USO] ──► [APR]
                    │
                    └─► [DIS si C-DIS: patrón incumplido, caso no cubierto, o restaurar intención]
propietario global: ARQ si C-ARQ, si no CON
```

```text
UN BUG VISUAL ACTIVA DIS Y NO SE CONVIERTE EN FEA.
El resultado perseguido sigue siendo restaurar un comportamiento esperado.

SI EL DIAGNÓSTICO REVELA C-PRD, el item CAMBIA DE PROCESO (b.1): no se amplía en silencio.
```

**Owner:** ninguno, salvo que el diagnóstico revele materia suya.

---

## INC · incidente en uso real

```text
ENT(contención) ──► ARQ(diagnóstico) ──► CON ──► VER ──► ENT(reentrega) ──► APR OBLIGATORIO
     │                                                                        ▲
     └─► [SEG:condiciones si C-SEG]                                          │
     └─► toda contención que no pueda detenerse ──► ITEM ENLAZADO ACTIVO ────┘
propietario global: ENT
```

| particularidad | por qué |
|---|---|
| ENT actúa **antes** de diagnosticar | contener el daño no espera a entender la causa |
| APR es **obligatorio**, único tipo | un incidente sin aprendizaje registrado se repite |
| la reentrega **satisface** la obligación sólo si restaura el servicio | un rollback que restaura cuenta; decidir no reentregar es RETIRAR la obligación, y son cosas distintas |

**Owner:** inmediato cuando el rollback no cumple los cinco requisitos de a.3.

---

## INV · investigación

```text
INV ──┬─► [CON:experimental cuando la evidencia exige construir]
      └─► [PRD o ARQ según el destino declarado] ──► [APR si C-APR]
propietario global: INV
```

```text
EL ITEM SIGUE SIENDO INV aunque construya: su salida comprometida es CONOCIMIENTO.
UN INV PUEDE CERRAR SIN SEGUNDO ITEM: la evidencia es el resultado.
Sólo nace un item nuevo cuando se decide FABRICAR o INTEGRAR algo con la evidencia.
```

---

## DEU · deuda técnica

```text
ARQ ──► CON ──► VER ──► [ENT si C-ENT] ──► [USO si C-USO] ──► [APR si C-APR]
propietario global: ARQ
```

`C-USO` se activa cuando hay que demostrar ausencia de regresión perceptible, mejora de
rendimiento o accesibilidad, conservación del flujo, o comportamiento correcto en
condiciones reales. **Activar USO no convierte la deuda en feature**: el resultado
perseguido sigue siendo reducir riesgo interno.

---

## DEP · dependencia

```text
SEG:condiciones ⊳ CON ──► VER ──► [ENT si C-ENT]
     ∥ [DOM:condiciones si C-DOM]
     ∥ [ARQ si el cambio de versión altera contratos]
propietario global: PLT
```

> **SEG antes de construir es OBLIGATORIO aquí** (G28). Es el único tipo donde una consulta
> de servicio es condición de entrada y no una activación condicional.

---

## AUD · auditoría de un proyecto existente

```text
El ENCUADRE declara SIETE cosas antes de componer ruta (b.16):
objeto · pregunta · resultado perseguido · consumidor de la conclusión · materia sobre la
que puede actuar · evidencia mínima · criterio de cierre

INV ──┬─► [DOM si C-DOM]
      ├─► [SEG si C-SEG]
      ├─► [DIS/Reconstruccion si C-DIS]
      └─► [PRD sólo si produce una decisión de producto] ──► APR
propietario global: DERIVADO del encargo, nunca asignado a mano
```

**AUD no activa CON** y **puede cerrar en APR sin pasar por PRD**: su resultado legítimo es
conocimiento e items nuevos.

---

## DIR · cambio de dirección

```text
ARQ(radio de impacto)
  ──► capacidades PROPIETARIAS de las decisiones afectadas
  ──► [CON:experimental sólo si hace falta prototipo PARA DECIDIR]
  ──► OWNER en el punto de decisión
  ──► registro de decisiones sustituidas + criterio de éxito
  ──► creación de los ITEMS DERIVADOS
  ──► VER:decision
  ──► cierre
propietario global: la capacidad propietaria de la decisión que se sustituye. NUNCA lo elige DSP.
```

```text
DIR DECIDE, NO IMPLEMENTA.
CON, VER, ENT y USO PRODUCTIVOS NO son obligatorios.
Ninguna construcción productiva puede vivir dentro de un DIR: VER:decision lo comprueba.
La ejecución continúa en ITEMS ENLAZADOS, independientes y paralelizables.
```

**Owner:** obligatorio en el punto de decisión, y en la elección de capacidad líder cuando
las decisiones son inseparables.

---

## SIS · evolución del sistema

```text
SIS ──► CON ──► VER ──► [ENT OBLIGATORIO si modifica el runtime] ──► [APR si C-APR]
propietario global: SIS · sujeto al FRENO DE RACHA de a.7
```

```text
Todo item SIS DEBE enlazar el problema real, la fricción o la capacidad de producto que
justifica su existencia. Sin ese enlace, no se trabaja.
```

---

## Los circuitos que (b) no numera pero el trabajo real produce

### Evolución del sistema de diseño

No es un tipo de proceso: es un **efecto** de DIS/Evolucion cuando el sistema se amplía. El
circuito es el del item que lo provocó; lo que cambia es que `DIS/sistema-de-diseno`
actualiza el sistema y la revisión de consistencia comprueba las superficies vecinas.

### Auditoría de conformidad de la propia organización

Es un item **SIS**, no un AUD: su objeto es la fábrica, no el producto. Lo ejecuta
`SIS/Conformidad`, y sus hallazgos se enrutan como items a las capacidades competentes.

---

## Handoffs declarados

| par | fichero |
|---|---|
| DIS con PRD, ARQ, CON, VER, USO, INV y ENT | [`DIS-handoffs.md`](DIS-handoffs.md) |
| el resto de pares | [`handoffs-generales.md`](handoffs-generales.md) |

Un par de capacidades sin handoff declarado **no está prohibido**: significa que su entrega
se rige por las reglas comunes de [`C5`](../contratos/C5-HANDOFF.md). Los declarados son
aquellos donde la experiencia —o el diseño— ha mostrado que hace falta precisión extra.
