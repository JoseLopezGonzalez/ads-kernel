---
kernel:        ^1.0.0
packs:         []                    # p.ej. [web-app] · [wear-os, mobile-app]
project:       <NOMBRE INTERNO>
owner_success: <una línea: qué gana el Owner>
target_env:    <qué es el "entorno real" donde se validan los spikes>
validation:    <quién valida, cada cuánto, bajo qué condiciones>
risk_profile:  <2-4 supuestos que pueden invalidar el proyecto>
compliance:    <marcos aplicables, o "ninguno declarado">
timebox_c0:    <presupuesto del Circuito 0>
---

# PROFILE — <NOMBRE DEL PRODUCTO>

> Hereda `kernel/KERNEL.md` íntegro salvo los overrides declarados en §9.
> Todo lo que aquí no se declare, se resuelve por el KERNEL.

> **Uno por PRODUCTO, nunca uno por repositorio.** Aunque el producto tenga frontend,
> backend, móvil e infraestructura en repositorios distintos, hay un solo PROFILE y vive
> aquí, en el repositorio ADS de control. Fragmentarlo por repositorio crearía varias
> organizaciones que después habría que sincronizar. Si un componente tiene objetivos,
> riesgos o restricciones propios, se declaran **dentro** de este documento, nombrando el
> componente. Qué componentes existen lo dice `SOURCES.toml`, y no se repite aquí.

---

## 1. Definición de éxito del Owner *(obligatorio — K0.13)*

**Sin esto, el sistema optimiza hacia "más completo", que casi nunca es lo que quieres.**

```text
1. <objetivo primario>
   Criterio de fallo: <cuándo diríamos que ha fallado, aunque el código sea bueno>

2. <objetivo secundario>
   Criterio de fallo: ...

3. <opcionalidad que no queremos cerrar>
   Criterio de fallo: ...
```

Consecuencias operativas (mínimo tres, aplicables sin volver a preguntar):

- Ante duda entre `<X>` y `<Y>`, gana `<Y>`.
- `<limitación aceptada conscientemente y sus implicaciones>`.
- `<qué trabajo se diseña ahora pero se ejecuta sólo si ocurre Z>`.

## 2. Propósito y problema

Qué es. Qué problema real resuelve. Qué hacen mal las alternativas existentes.

Una frase que un agente pueda usar para desempatar:

> **<idea central en una línea>**

## 3. Usuarios y contexto de uso

Quién lo usa, dónde, en qué condiciones físicas o de atención, con qué restricciones (sin conexión, con prisa, en móvil, bajo carga, con datos sensibles).

## 4. Principios de producto

De 4 a 7. Cada uno debe servir para **decidir**, no para adornar. Si un principio no permite descartar una opción concreta, sobra.

- **<Principio>.** <Qué implica en la práctica y qué descarta.>

Recomendado incluir siempre uno de degradación:

- **Degradación explícita.** Toda función que dependa de una señal, servicio o permiso potencialmente ausente **DEBE** tener definido su comportamiento degradado antes de implementarse.

## 5. Riesgos técnicos centrales

Los supuestos que, si son falsos, invalidan la propuesta de valor. **No** son bugs ni detalles: son apuestas.

```text
RIESGO-01
Supuesto:       <lo que estamos dando por bueno>
Si es falso:    <qué parte del producto se cae>
Cómo lo medimos: SPIKE-XX
Degradación:    <qué hace el producto si el supuesto falla>
```

## 6. Spikes obligatorios *(G22)*

Ninguno se responde investigando en web. Todos contra el entorno real declarado en `target_env`.

| ID | Pregunta falsable | Criterio de éxito (umbral ANTES de medir) | Bloquea |
|---|---|---|---|
| SPIKE-01 | | | |
| SPIKE-02 | | | |

Primer entregable útil del proyecto: `<el experimento mínimo que responde varios spikes a la vez>`.

## 7. Arquitectura y stack orientativos

→ Al crear `docs/ARCHITECTURE.md` y `docs/STACK.md`, **esta sección se poda** (K0.3).

Capas, límites que no deben cruzarse, y tabla de tecnologías con su función. Marcar qué es decisión fuerte y qué es orientación.

## 8. Decisiones

### 8.1 Fuertes (ya tomadas)

Producto: … · Tecnología: … — revisables sólo ante razones sólidas.

### 8.2 PROVISIONALES *(K0.5)*

Todo lo que la implementación va a forzar. **Nunca dejar esto como "abierto".**

| Decisión | Valor provisional | Condición de revisión |
|---|---|---|
| | | |

### 8.3 ABIERTAS

Sólo lo que la implementación **no** obliga a decidir todavía.

## 9. Overrides declarados del KERNEL *(K0.7)*

Toda excepción, explícita y justificada. Si esta sección está vacía, el KERNEL se hereda íntegro.

```text
OVERRIDE: <sección del kernel>
Motivo:   <por qué este proyecto necesita comportarse distinto>
Alcance:  <hasta dónde llega la excepción>
Revisión: <cuándo se reevalúa>
```

Si un override resulta útil en un segundo proyecto → candidato a KERNEL o PACK (K0.12).

## 10. Cumplimiento y datos sensibles

| Área | Qué implica | Cuándo se ejecuta |
|---|---|---|
| | | |

Si no aplica ninguno, escribir explícitamente **"ninguno declarado"** y por qué. No dejarlo en blanco.

## 11. Especialización organizativa *(G11)*

Qué capacidades del KERNEL se activan en este proyecto y cuáles **no** se activan (decirlo evita departamentos vacíos).

Documentación especializada esperable: …

## 12. Product Baseline *(G23)*

Qué debe demostrar la primera versión coherente, en términos verificables.

- …

## 13. Validación humana *(G36)*

- Quién valida: …
- Bajo qué condiciones: …
- Frecuencia realista: …
- Qué puede capturar la máquina automáticamente para que el validador no tenga que anotarlo: …

## 14. Glosario

Sólo términos del dominio y del producto. Los del KERNEL no se repiten aquí.

## 15. Resumen para nuevos agentes

Un párrafo. Qué construimos, qué es innegociable, qué está en riesgo, qué se mide antes de decidir, y cuál es el criterio de desempate.
