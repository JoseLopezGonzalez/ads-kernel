# El lenguaje canónico del kernel operativo

<!-- ads-lint: permitir-vocabulario-prohibido -->

Este fichero explica **cómo se escribe** todo lo demás. Es la única fuente sobre el
formato; ningún otro documento redefine estas reglas.

## Regla de doble lectura

Todo artefacto operativo del kernel es un `.md` que un humano lee de principio a fin,
y que contiene **uno o varios bloques canónicos** que una máquina interpreta sin
ambigüedad.

````text
```yaml ads:<tipo>
id: DIS/direccion-artistica
...
```
````

- El *info string* empieza por `yaml`, de modo que GitHub y los editores resaltan el
  bloque. La segunda palabra, `ads:<tipo>`, declara qué esquema lo valida.
- **La prosa que rodea al bloque explica; el bloque manda.** Si la prosa y el bloque se
  contradicen, es un defecto de conformidad que `ads_lint` no siempre detecta y que la
  revisión humana **DEBE** corregir: nunca se resuelve dando prioridad a la prosa.
- Un fichero **PUEDE** tener varios bloques sólo cuando es un catálogo declarado como
  tal en su cabecera (por ejemplo, el catálogo de formas de conversación).

## Tipos canónicos

| tipo | qué declara | esquema |
|---|---|---|
| `esquema` | la forma de un tipo canónico | `esquemas/esquema.yaml` |
| `capacidad` | los doce campos de a.1 para una capacidad | `esquemas/capacidad.yaml` |
| `rol` | el contrato común de rol | `esquemas/rol.yaml` |
| `metodo` | un procedimiento ejecutable | `esquemas/metodo.yaml` |
| `gate` | una lista comprobable de salida | `esquemas/gate.yaml` |
| `veto` | el contrato de veto de a.5 | `esquemas/veto.yaml` |
| `perfil-agente` | exigencia de capacidades de modelo, sin marca | `esquemas/perfil-agente.yaml` |
| `composicion` | qué roles se materializan para una clase de trabajo | `esquemas/composicion.yaml` |
| `entrada` | una clase de expresión del Owner antes de ser item | `esquemas/entrada.yaml` |
| `forma-conversacion` | cómo se atiende una clase de expresión | `esquemas/forma-conversacion.yaml` |
| `encuadre` | el dosier que consume DSP para crear un item | `esquemas/encuadre.yaml` |
| `handoff` | la entrega entre dos capacidades | `esquemas/handoff.yaml` |
| `rubrica` | criterio de juicio con evidencia | `esquemas/rubrica.yaml` |
| `memoria` | una sección del corpus persistente de un equipo | `esquemas/memoria.yaml` |
| `escenario` | una prueba de conformidad ejecutable a mano o por script | `esquemas/escenario.yaml` |
| `pack` | la declaración de un pack | `esquemas/pack.yaml` |

## Tipos de campo

```text
texto        una cadena
lista        secuencia de valores del tipo declarado en `de`
objeto       mapa con sus propios campos
entero       número entero
booleano     true | false
enum         uno de los valores de `valores`
ref          identificador de otro artefacto canónico; se comprueba que existe
```

Restricciones disponibles: `patron` (expresión regular completa), `min`, `max`,
`valores`, `de`, `campos`, `obligatorios`.

## Vocabulario prohibido

`ads_lint` **rechaza** en cualquier fichero de `kernel/operativo/` y `packs/` las
expresiones que delegan el criterio sin escribirlo:

```text
si aplica · si procede · cuando corresponda · según el contexto · según convenga
el agente decidirá · a criterio del agente · a juicio del agente
se hará una revisión adecuada · revisión apropiada · lo que sea razonable
en la medida de lo posible · idealmente · preferiblemente
```

Cuando una variación es real, se escribe como **condición comprobable**:

```yaml
condicion_de_activacion: "el paquete declara afecta_contratos != []"
```

Un fichero cuyo objeto **es** hablar de estas expresiones —como éste— se exime con el
marcador HTML `<!-- ads-lint: permitir-vocabulario-prohibido -->` en sus primeras
líneas. El marcador es visible en el diff y su uso es excepcional.

## Identificadores

```text
capacidad          [A-Z]{3}                      DIS · PRD · ARQ
capacidad de pack  <pack>:[A-Z]{3}               wear:AMB
rol                <CAP>/<slug>                  DIS/direccion-artistica
método             <CAP>/<Slug>                  DIS/Fundacion
gate               gate:<algo>                   gate:excelencia-visual
otros              <tipo>:<slug>                 entrada:idea-inmadura
```

## Cómo se valida

```bash
python3 kernel/operativo/validadores/ads_lint.py        # todo
python3 kernel/operativo/validadores/ads_lint.py --json # salida para máquina
```

El validador comprueba: esquema de cada bloque · unicidad de identificadores ·
resolución de toda `ref` · resolución de todo enlace relativo de Markdown ·
vocabulario prohibido · reglas específicas declaradas en `validadores/reglas.yaml`.
