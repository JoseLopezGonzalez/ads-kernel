# El sistema de excelencia de Diseño


> **No buscamos interfaces usables. Buscamos productos con personalidad, actuales,
> expresivos y visualmente excelentes** — interfaces cuya implementación exige verdadero
> trabajo de diseño y de desarrollo, no una plantilla bien rellenada.

Esto no es una preferencia estética del Owner: es un **requisito del kernel**, con la
misma dureza que las reglas de seguridad. Un producto que funciona y no tiene carácter es
un producto rechazado.

## Por qué esto vive en el kernel y no en un pack

En la versión 1.3.0 existía `pack-design-led`, para «productos donde el diseño ES el
diferenciador». Ese pack se ha **promovido al kernel**: la excelencia visual dejó de
depender de la clase de proyecto. Una herramienta interna, un panel de operaciones y un
reloj tienen exigencias distintas de forma —eso lo aportan los packs— pero **ninguno tiene
derecho a ser genérico**.

## Los dos gates, y por qué son dos

```text
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│  USABILIDAD                     │   │  EXCELENCIA VISUAL              │
│                                 │   │                                 │
│  ¿se entiende?                  │   │  ¿tiene personalidad?           │
│  ¿se puede usar?                │   │  ¿es coherente?                 │
│  ¿funciona correctamente?       │   │  ¿es actual?                    │
│  ¿es accesible?                 │   │  ¿hay intención artística?      │
│  ¿aguanta los estados extremos? │   │  ¿tiene calidad de ejecución?   │
└─────────────────────────────────┘   └─────────────────────────────────┘
        gate:usabilidad                      gate:excelencia-visual
        mayoritariamente comprobable          rúbrica + crítica profesional
        por medición y observación            + juicio del Owner donde corresponde
```

**Son independientes y ambos son obligatorios.** Una interfaz puede pasar el primero y ser
rechazada por el segundo. Ésa es exactamente la situación que este sistema existe para
detectar, y la que produjo el escenario de referencia: *«funciona, pero se ve básica, plana
y sin alma»*.

### Los diez motivos de rechazo por excelencia visual

Una interfaz **usable** se rechaza si es:

```text
1  GENÉRICA        podría ser de cualquier producto. No la reconocerías sin el logotipo.
2  BÁSICA          resuelve con los valores por defecto de la herramienta usada.
3  PLANA           sin jerarquía: todo pesa lo mismo y no se sabe dónde mirar.
4  ANTICUADA       recurre a soluciones formales que dejaron de significar algo.
5  INCONSISTENTE   dos zonas del producto resuelven lo mismo de forma distinta sin motivo.
6  VISUALMENTE POBRE  espaciado arbitrario, tipografía sin escala, color sin sistema.
7  SIN JERARQUÍA   ningún elemento domina; la mirada no tiene recorrido.
8  SIN RESPUESTA   no acusa recibo de lo que el usuario hace: sin estados, sin movimiento.
9  SIMPLIFICADA    se construyó por debajo de la intención aprobada, sin devolverla.
10 SIN ALMA        técnicamente correcta y emocionalmente muda. No transmite nada.
```

Cada uno tiene su eje en la rúbrica de [`02-RUBRICAS.md`](02-RUBRICAS.md), con lo que
cuenta como rechazo, como suficiente y como excelente.

### Lo que NO puede pasar

```text
PROHIBIDO   pasar el gate visual porque el de usabilidad está en verde
PROHIBIDO   reducir la excelencia a una puntuación automática
PROHIBIDO   que quien construyó la interfaz emita su dictamen de excelencia
PROHIBIDO   cerrar el gate visual sin dictamen de crítica independiente
PROHIBIDO   aprobar una primera instancia de patrón visual sin el Owner (a.8)
```

## Cómo se conserva el juicio sin abrir una puerta a la arbitrariedad

a.1 dice que un gate **no es un juicio: es una lista**, y que si hace falta juicio, ese
juicio es **otra capacidad activada**. Esto se cumple así:

```text
EL JUICIO       lo emite el rol DIS/critica-visual, independiente, con su método y su
                rúbrica. Produce un DICTAMEN: veredicto, ejes evaluados, evidencia.
EL GATE         comprueba que ese dictamen EXISTE, que su veredicto es conforme, que
                evaluó todos los ejes y que su evidencia está enlazada.
EL OWNER        interviene donde a.8 lo exige: primera instancia de un patrón visual,
                artístico o de interacción, y cambio de dirección.
```

De modo que **el gate sigue siendo una lista comprobable** y el juicio profesional sigue
existiendo, en un rol con nombre y con autoridad declarada. Ni se automatiza el gusto, ni
se aprueba en silencio.

## Las referencias: para investigar, no para copiar

```text
SE HACE       estudiar una obra, EXTRAER SU PRINCIPIO y aplicarlo a un problema distinto
SE HACE       registrar la referencia con autor, enlace y fecha, y qué se extrajo
SE HACE       registrar ANTIRREFERENCIAS: qué no queremos parecer, y por qué

NO SE HACE    reproducir una obra concreta
NO SE HACE    adoptar un estilo completo de una marca existente
NO SE HACE    presentar una referencia sin su principio extraído
NO SE HACE    citar de memoria: la referencia sin enlace comprobable es material inventado
```

Una referencia entregada sin principio extraído **se rechaza en el handoff**: no es
material de trabajo, es un cromo.

## Los tres procedimientos de Diseño

```text
DIS/Fundacion       proyecto nuevo sin dirección visual.  Sin techo de sesiones.
DIS/Reconstruccion  proyecto existente cuya dirección hay que reconstruir del código.
DIS/Evolucion       trabajo diario sobre un sistema ya establecido.
```

Cuál se ejecuta lo decide la [escala de novedad](03-ESCALA-DE-NOVEDAD.md), no el criterio
del agente. Los tres son **métodos de la capacidad `DIS`** y viven, como todos los métodos del
sistema, en `capacidades/DIS/metodos/`. No se describen aquí dos veces.

## El ciclo de calidad

Trece estaciones, con retorno. Está en
[`04-CICLO-DE-CALIDAD.md`](04-CICLO-DE-CALIDAD.md).

## La fidelidad de implementación

Construcción **no puede simplificar en silencio** lo aprobado. Cómo se comprueba, con qué
evidencia y qué ocurre cuando algo no es viable:
[`05-FIDELIDAD.md`](05-FIDELIDAD.md).

## Índice del sistema

| | documento |
|---|---|
| 1 | [`01-MEMORIA-DE-DISENO.md`](01-MEMORIA-DE-DISENO.md) — el corpus persistente y sus tres capas |
| 2 | [`02-RUBRICAS.md`](02-RUBRICAS.md) — usabilidad y excelencia visual, con sus dos gates |
| 3 | [`03-ESCALA-DE-NOVEDAD.md`](03-ESCALA-DE-NOVEDAD.md) — cuánta exploración exige cada trabajo |
| 4 | [`04-CICLO-DE-CALIDAD.md`](04-CICLO-DE-CALIDAD.md) — las trece estaciones y sus retornos |
| 5 | [`05-FIDELIDAD.md`](05-FIDELIDAD.md) — intención aprobada frente a resultado construido |
| — | los tres procedimientos: [`capacidades/DIS/metodos/`](../capacidades/DIS/metodos/) |

El equipo que lo ejecuta, con sus once roles y sus seis métodos:
[`capacidades/DIS/`](../capacidades/DIS/CAPACIDAD.md).
