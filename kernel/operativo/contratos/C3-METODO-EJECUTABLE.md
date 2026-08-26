# C3 — El método ejecutable


> Un método es lo que impide que cada agente invente su propia metodología. Si un método
> admite dos ejecuciones razonables con resultados distintos, no es un método: es un tema.

## Los diecisiete elementos del procedimiento

Todo método declara los diecinueve campos del esquema
[`esquemas/metodo.yaml`](../esquemas/metodo.yaml): los diecisiete de abajo más `id`,
`nombre` y `capacidad`, que son su identidad y no parte del procedimiento. La tabla lista
diecisiete porque incluye `modo`, que es subcampo de `pasos`, y no incluye los tres de
identidad. **La cifra la deriva y la comprueba T151**; aquí no se escribe a mano.

| # | elemento | qué responde |
|---|---|---|
| 1 | `disparador` | qué hace que este método empiece |
| 2 | `carga` | qué información se lee ANTES del primer paso |
| 3 | `preguntas_iniciales` | qué hay que responderse antes de trabajar |
| 4 | `pasos` | el procedimiento, numerado, con `termina_cuando` por paso |
| 5 | *(dentro de `pasos`)* `modo` | divergente · convergente · lineal · conversacional |
| 6 | `artefactos` | qué queda escrito, incluidos los intermedios |
| 7 | `puntos_owner` | dónde y por qué interviene el Owner |
| 8 | `consultas` | a qué otras capacidades se pregunta, y con qué pregunta |
| 9 | `checkpoints` | en qué momentos se persiste |
| 10 | `critica` | qué se pregunta el propio método sobre su resultado |
| 11 | `gate` | contra qué se cierra |
| 12 | `salida` | qué se entrega |
| 13 | `devolucion` | cuándo devuelve, a quién y con qué |
| 14 | `bloqueo` | qué lo detiene, y qué lo desbloquearía |
| 15 | `cancelacion` | cuándo deja de tener sentido continuar |
| 16 | `aprendizaje` | qué deja al sistema cuando termina |
| 17 | `prueba_de_reanudacion` | cómo se comprueba que un agente nuevo lo retoma |

## Reglas que hacen ejecutable un método

### 1 · Todo paso declara `termina_cuando`

```text
PROHIBIDO   «explorar direcciones visuales»
CORRECTO    hace: explorar direcciones visuales distintas entre sí
            termina_cuando: hay tres direcciones con su principio escrito, y ninguna
                            es variación de otra en tipografía, color y densidad a la vez
```

Sin `termina_cuando`, un paso dura lo que el agente decida, y dos ejecuciones del mismo
método producen profundidades distintas.

### 2 · Los pasos condicionales llevan condición comprobable

```text
PROHIBIDO   paso 4: consultar a Dominio si es necesario
CORRECTO    paso 4: consultar a Dominio
            condicion: el paquete declara afecta_contratos != [] o toca una tabla con
                       datos históricos
```

Todo `si` va seguido de algo que se puede mirar y responder sí o no **sin criterio**.

### 3 · Divergente y convergente son fases distintas y se declaran

```text
DIVERGENTE   se abren posibilidades. Prohibido descartar durante la fase.
             Termina con un número declarado de alternativas.
CONVERGENTE  se elige y se descarta. Prohibido añadir alternativas nuevas.
             Termina con una elección y el motivo de cada descarte escrito.
```

Mezclarlas produce el fallo más común de todo trabajo creativo: descartar la segunda idea
antes de tener la tercera, y acabar con la primera de siempre.

### 4 · Los puntos del Owner se declaran uno a uno

Cada punto declara **qué se le pregunta**, **por qué su autoridad lo exige** y **qué pasa
si no responde**. Un método que dice «se consulta al Owner» sin más es dependencia
excesiva disfrazada de prudencia.

### 5 · Toda consulta lleva pregunta cerrada

```text
PROHIBIDO   «consultar a Arquitectura»
CORRECTO    consultas:
              - "ARQ: ¿el radio de impacto medido de sustituir el componente de tabla
                 excede un módulo? Responde con la lista de ficheros afectados."
```

Una consulta sin pregunta devuelve una opinión general que nadie puede usar.

### 6 · El gate es una lista, y se recorre entera

El método **no** cierra porque el agente considere que terminó. Cierra porque recorrió las
comprobaciones del gate y anotó el resultado de cada una. Una comprobación no anotada es
una comprobación no hecha.

### 7 · La prueba de reanudación es obligatoria y concreta

```text
PROHIBIDO   «el método es reanudable por checkpoint»
CORRECTO    «se interrumpe tras el paso 3, se releva al agente, y el entrante produce el
            mismo artefacto que produciría una ejecución sin interrupción, sin preguntar
            al Owner nada ya contestado. Es la prueba T82.»
```

Un método sin prueba de reanudación **no es reanudable**: es reanudable en teoría, que es
otra cosa. El validador lo exige por la regla `R03`.

## Anatomía de un paso

```yaml
- n: 3
  nombre: COMPARAR
  modo: convergente
  hace: >
    Comparar las tres direcciones contra los principios de la memoria de diseño y contra
    las restricciones declaradas por el Owner, escribiendo por cada una qué gana y qué
    sacrifica.
  produce: "tabla de comparación con una fila por dirección"
  termina_cuando: >
    cada dirección tiene escrito qué gana, qué sacrifica y contra qué principio se evalúa
  checkpoint: true
```

`hace` describe el trabajo. `produce` nombra el artefacto. `termina_cuando` es la
condición de salida, comprobable por alguien que no ejecutó el paso.

## Cuándo un método puede saltarse un paso

**Nunca por decisión del agente.** Un paso se salta cuando:

```text
[ ] el paso declara una `condicion` y esa condición es falsa, comprobada y anotada, O
[ ] la composición del equipo no materializó el rol que ese paso requiere, y eso queda
    escrito en el checkpoint con el motivo de la composición elegida
```

En ambos casos **queda traza**, igual que la ruta deja traza de lo no activado (a.6).

## Método frente a criterio profesional

Un método no sustituye al juicio: lo **enfoca**. Los pasos dicen qué hacer y cuándo parar;
lo que se produce dentro de cada paso es trabajo profesional real.

```text
EL MÉTODO DICE       explora tres direcciones distintas entre sí, y prueba que lo son
EL MÉTODO NO DICE    cuáles. Eso es el trabajo, y por eso hace falta un buen agente.
```

Un método que intentara especificar el contenido produciría trabajo mecánico y
homogéneo — exactamente el resultado «correcto y sin alma» que el paso 3 de esta
iniciativa existe para impedir.
