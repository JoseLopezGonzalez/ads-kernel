# C1 — Capacidad, equipo, rol, agente, método, herramientas y autoridad


> Amplía el contrato de capacidad de a.1 **sin contradecirlo**. Lo que (a) define no se
> repite aquí: se enlaza.

## Los siete conceptos, y qué se rompe al confundirlos

```text
CAPACIDAD     qué SABE HACER el sistema. Vive en el catálogo. Permanente, no consume nada.
              Confundirla con equipo → equipos materializados sin cola (T12).

EQUIPO        organización TEMPORAL materializada para trabajo real: capacidad + tablero
              + cola + memoria viva + agentes ocupando roles.
              Confundirlo con capacidad → «el equipo de Diseño» como entidad permanente
              que hay que mantener ocupada, y trabajo fabricado para justificarla.

ROL           responsabilidad CONCRETA dentro del equipo, con autoridad delimitada.
              Confundirlo con agente → al cambiar de modelo se pierde la memoria y la
              autoridad, y hay que reexplicar todo.

AGENTE        INSTANCIA de IA que ocupa uno o varios roles: modelo + instrucciones +
              herramientas + contexto + presupuesto.
              Confundirlo con rol → un agente que critica lo que él mismo construyó.

MÉTODO        PROCEDIMIENTO que el rol debe seguir, con pasos, checkpoints y gate.
              Confundirlo con rol → dos roles distintos ejecutando el mismo procedimiento
              genérico, que es la definición de equipo genérico.

HERRAMIENTAS  recursos que el rol PUEDE utilizar. Declaradas, no supuestas.
              Sin declararlas → un rol bloqueado a mitad de método por no tener acceso.

AUTORIDAD     qué puede DECIDIR, PROPONER, VETAR o ESCALAR.
              Sin declararla → autoridad silenciosa: alguien decide sin poder hacerlo.
```

## Contrato común de rol — veintinueve campos

Todo rol, del kernel o de un pack, declara los veintinueve campos del esquema
[`esquemas/rol.yaml`](../esquemas/rol.yaml). **Un rol que declare menos no es
materializable y el instalador DEBE rechazarlo.**

| campo | qué responde | error que evita |
|---|---|---|
| `id` | `<CAP>/<slug>` | dos roles con el mismo nombre en capacidades distintas |
| `nombre` | cómo se le llama en una conversación | hablarle al Owner en identificadores |
| `capacidad` | de qué equipo forma parte | roles huérfanos sin tablero ni memoria |
| `mision` | qué falta si este rol no existe | roles decorativos |
| `resultado` | qué artefacto produce | un rol que «participa» sin entregar nada |
| `responsabilidades` | qué hace, en concreto | responsabilidad difusa entre dos roles |
| `limites` | qué **no** hace | invasión de la materia de otro |
| `autoridad` | decide · propone · veta · escala | **autoridad silenciosa** |
| `entradas` | qué necesita para empezar | empezar sin material y rellenar con supuestos |
| `metodo` | qué procedimientos ejecuta | improvisar metodología propia |
| `herramientas` | qué recursos usa | bloqueo a mitad por falta de acceso |
| `conocimientos` | qué debe saber | asignar el rol a quien no puede ejercerlo |
| `perfil_agente` | qué capacidades de modelo exige | ocupar el rol con un modelo incapaz |
| `memoria_consulta` | qué lee antes de trabajar | repetir una decisión ya tomada |
| `memoria_actualiza` | qué deja escrito | aprendizaje que muere con la sesión |
| `interaccion_owner` | nivel · cuándo · formato | molestar al Owner sin autoridad que lo exija |
| `interaccion_roles` | con quién y cómo | coordinación por conversación informal |
| `independencia` | de quién debe ser independiente y por qué | crítico que revisa su propio trabajo |
| `checkpoint` | cuándo persiste | trabajo perdido al cortarse la sesión |
| `salida` | qué entrega | capa depositada sin artefacto localizable |
| `gate` | contra qué se cierra | cierre por criterio propio |
| `devolucion` | cuándo devuelve y a quién | construir sobre una capa que se sabe mala |
| `bloqueo` | qué le impide avanzar | bloqueos sin desbloqueador nombrado |
| `veto` | sobre qué materia, o vacío | veto improvisado sin contrato |
| `criterios_calidad` | cómo se sabe que su trabajo es bueno | calidad como opinión |
| `antipatrones` | qué hace mal característicamente | repetir el mismo error en cada proyecto |
| `activacion` | cuándo entra | equipos materializados por si acaso |
| `retirada` | cuándo sale | equipos permanentes sin trabajo |
| `prompt` | dónde está su instrucción operativa | rol no materializable |

### `autoridad` — los cuatro verbos, sin quinto

```yaml
autoridad:
  decide:  # lo ejecuta y queda hecho. No pide permiso ni avisa antes.
  propone: # lo prepara y lo entrega a quien tiene autoridad. No lo ejecuta.
  veta:    # puede DETENER algo en su materia. Exige contrato de veto de a.5.
  escala:  # ni decide ni propone: entrega la decisión a otro, con las opciones escritas.
```

**Regla dura:** lo que no está en `decide` **no se decide**. Un rol que actúa fuera de su
lista de decisión comete autoridad silenciosa, que es un defecto de conformidad aunque el
resultado sea bueno.

**Vacío es una respuesta legítima y explícita.** `veta: []` significa «este rol no veta
nada», y hay que escribirlo. El validador exige que el campo esté declarado, no que tenga
contenido.

### `independencia` — cuándo es obligatoria

```text
requiere_independencia: true  OBLIGATORIO si se cumple cualquiera:
  [ ] el rol juzga un artefacto que otro rol produjo
  [ ] el rol tiene veto sobre una materia en la que otro rol produce
  [ ] el rol verifica evidencia que sostiene un gate
  [ ] el rol emite un dictamen que puede detener el avance

En esos casos, `de_quien` enumera los roles concretos, y `motivo` dice qué se rompe si se
comparte agente. «Buenas prácticas» no es un motivo válido: el motivo describe el fallo.
```

> **El contrato fija el MÍNIMO; la composición puede exigir MÁS.** Una composición puede
> separar dos roles que sus contratos no obligan a separar —porque en ese trabajo concreto
> el sesgo importa—, y eso es correcto. Lo que **NO PUEDE** hacer ninguna composición es
> combinar dos roles que un contrato declara independientes: ahí el contrato manda, y la
> prueba T135 lo comprueba sobre todo el corpus.

## Autoridad del rol frente a autoridad de la capacidad

```text
La capacidad declara su autoridad en a.1 campo AUTORIDAD.
El rol declara la suya en su contrato.

REGLA:  la autoridad de un rol es SIEMPRE un subconjunto de la de su capacidad.
        Un rol NO PUEDE decidir lo que su capacidad escala.
        Un rol NO PUEDE vetar lo que su capacidad no veta.
        La suma de los roles PUEDE ser menor que la capacidad: hay autoridad que sólo se
        ejerce cuando la composición materializa el rol correspondiente.
```

Si un rol necesitase más autoridad que su capacidad, el defecto está en el catálogo, no en
el rol: se corrige la ficha de capacidad, con la traza que exige a.4.

## Un rol, varios agentes; un agente, varios roles

Las combinaciones permitidas y prohibidas están en
[`C2-AGENTES-Y-MODELOS.md`](C2-AGENTES-Y-MODELOS.md). Lo que C1 fija es **dónde se
declara**: en el bloque `ads:composicion` de la capacidad, campos `combinables` e
`independientes`. Nunca en la conversación, nunca por decisión del agente que está
trabajando.

## Qué NO puede declarar un rol

```text
PROHIBIDO   autoridad sobre una materia ya vetada por otra capacidad del kernel
            → salvo override declarado en el PROFILE (K0.7)
PROHIBIDO   ser propietario global de un tipo de proceso del kernel
            → eso lo fija b.16, no el rol
PROHIBIDO   un método propio no declarado en `metodo`
            → improvisar metodología es el fallo que este contrato existe para impedir
PROHIBIDO   herramientas no declaradas en `herramientas`
PROHIBIDO   escribir en una memoria no declarada en `memoria_actualiza`
PROHIBIDO   hablar con el Owner si `interaccion_owner.nivel` es `ninguna`
```

## Cómo se lee un contrato de rol para ocuparlo

```text
1  perfil_agente   ¿puede este modelo ocupar el rol? Si no, se degrada según el perfil
                   o se bloquea nombrando qué capacidad falta. NO se ocupa a medias.
2  prompt          se carga como instrucción del agente
3  metodo          se ejecuta paso a paso; no hay pasos opcionales sin condición escrita
4  memoria_consulta  se lee ANTES de empezar, no cuando surge la duda
5  gate            se comprueba al cerrar, comprobación por comprobación
6  checkpoint      se escribe cuando el contrato lo exige, no cuando apetece
7  memoria_actualiza  se escribe ANTES de soltar la custodia
```
