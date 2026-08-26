# Revisión adversarial del kernel operativo


Revisión del conjunto contra los doce defectos que el encargo pide buscar. **No es un
informe de que todo está bien**: lo que encontró está corregido y, donde se pudo, convertido
en prueba permanente para que no vuelva en silencio.

## Cómo se hizo, y su limitación honesta

```text
PREVISTO      un agente independiente, sin acceso a esta conversación, atacando el material
OCURRIÓ       ese agente se lanzó y TERMINÓ SIN COMPLETARSE por un límite de gasto de la
              cuenta, no por un fallo del material
HECHO         la revisión la ejecutó el mismo agente que escribió el corpus, apoyándose en
              barridos automáticos sobre el árbol completo y en la prueba del agente frío
```

> **Esta es la limitación más importante de esta entrega.** La revisión por un lector que no
> escribió el material sigue pendiente, y es exactamente la clase de independencia que el
> propio kernel exige en `DIS/critica-visual`, `VER/dosier` y `ENC/critica-de-encuadre`. Un
> sistema que exige independencia y no la aplica a sí mismo tiene una deuda declarada, y
> ésta lo es.

## Los doce defectos buscados

| | defecto | resultado |
|---|---|---|
| 1 | ambigüedad | `ads_lint` prohíbe el vocabulario que delega el criterio; 0 apariciones fuera de las tres exenciones declaradas |
| 2 | ceremonia inútil | **encontrada y corregida**: ver hallazgo H3 |
| 3 | dependencia excesiva del Owner | tabla de confirmación de `entrada/04` derivada de a.8, con regla de cierre que impide el «sí» por prudencia |
| 4 | autoridad silenciosa | **encontrada y corregida**: ver hallazgo H1 |
| 5 | equipos genéricos | cada capacidad tiene conocimientos, preguntas, artefactos y antipatrones propios; ninguna comparte método |
| 6 | métodos interpretables | T91 comprueba que **todo paso** de **todo método** declara `termina_cuando`. 35 métodos, 0 fallos |
| 7 | pasos imposibles de reanudar | T89 comprueba que toda `prueba_de_reanudacion` cita un escenario existente |
| 8 | calidad visual reducida a usabilidad | dos gates independientes, y T99 exige demostrar que una interfaz usable puede ser rechazada |
| 9 | documentos sin uso operativo | **encontrado y corregido**: ver hallazgo H2, ahora prueba permanente T134 |
| 10 | duplicación kernel/pack | `packs/00-QUE-ES-UN-PACK` fija qué no puede tocar un pack; T132 lo comprueba |
| 11 | diseño orientado a un único proyecto | T92 comprueba que ningún contrato nombra una marca; los packs no mencionan gym-wear |
| 12 | autorreferencia sin producto | freno de racha SIS, justificación de producto obligatoria, y H2 |

## Hallazgos

### H1 · Una composición se contradecía a sí misma *(grave)*

`composicion:inv-con-experimento` declaraba `INV/investigacion` y `CON/experimental`
**combinables bajo condición** y **independientes** a la vez. C4 dice que ante conflicto
manda `independientes`, con lo que la condición era letra muerta: había una combinación
declarada que nunca podía ejecutarse, y quien la leyera creería que sí.

```text
CÓMO SE ENCONTRÓ   T87, al hacerse exacta. Antes la independencia era prosa y el
                   validador no podía comprobarla.
QUÉ SE HIZO        el esquema de composición pasó de prosa a dato: `independientes`
                   declara ahora rol, de-quién y motivo. Se partió la composición en dos,
                   con condiciones excluyentes: experimento corto reversible (combinable)
                   y experimento que sostiene una decisión irreversible (separado).
PRUEBA             T87, y además T135, que comprueba la dirección contraria: que ninguna
                   composición rebaje lo que un contrato exige.
```

### H2 · Siete documentos que existían para nadie *(media)*

`circuitos/00-CIRCUITOS.md`, `plantillas/CHECKPOINT.md`, `plantillas/DEVOLUCION.md`, las
tres especializaciones de Diseño de los packs y el propio checkpoint de la iniciativa **no
tenían ningún enlace entrante ni ningún bloque citado desde fuera**. Un agente no podía
llegar a ellos.

```text
QUÉ SE HIZO   índice maestro reescrito con las quince capacidades, las plantillas y los
              packs enlazados uno a uno; los PACK.md enlazan sus ficheros concretos en vez
              de sus directorios; el README de rediseño enlaza el checkpoint.
PRUEBA        T134, permanente: ningún documento del corpus puede quedarse sin entrada.
```

### H3 · El README del repositorio no llevaba a ninguna parte *(grave)*

La portada del repositorio no mencionaba `kernel/operativo/`. Un agente que llegara por
primera vez —el caso que este trabajo existe para servir— no encontraba nada de lo
construido.

```text
QUÉ SE HIZO   la portada abre con dónde está cada cosa y con el camino explícito de cuatro
              saltos: índice → capacidad → rol → prompt. Y con el estado honesto: el runtime
              no existe, y la mayoría de las pruebas son contratos definidos.
```

### H4 · El prompt del interlocutor no sabía partir una frase en dos *(media)*

La regla de que una expresión con dos cosas dentro **se parte en dos expresiones** vivía
sólo en el catálogo de formas. El prompt —que es lo único que un agente carga— no la tenía,
y ese agente habría atendido la mitad más fácil.

```text
CÓMO SE ENCONTRÓ   la prueba del agente frío, con la frase «el buscador va lentísimo y
                   encima no se entiende el resultado»
QUÉ SE HIZO        la regla entra en el prompt y en el paso 2 de ENC/Escucha; y el índice
                   declara que los prompts REPITEN operativamente lo que necesitan, porque
                   se cargan solos, y que eso no es duplicación de fuente
```

### H5 · Cuatro roles que juzgan sin exigir independencia en su contrato *(menor, no es defecto)*

`PLT/maquinaria`, `PRD/criterio-de-exito`, `ARQ/diagnostico` y `DIS/sistema-de-diseno`
juzgan o comprueban trabajo y declaran `requiere_independencia: false`. Al revisarlo, los
cuatro tienen motivo escrito y sus composiciones sí los separan donde importa.

```text
NO ERA UN DEFECTO, pero faltaba la regla explícita: el CONTRATO fija el mínimo y la
COMPOSICIÓN puede exigir más, nunca menos. Ahora está escrita en C1 y comprobada por T135.
```

## Lo que esta revisión NO puede afirmar

```text
NO PUEDE AFIRMAR   que el material funcione: sólo que es coherente consigo mismo
NO PUEDE AFIRMAR   que un agente nuevo lo use bien: eso lo dirá el primer proyecto real
NO PUEDE AFIRMAR   que no haya contradicción entre la prosa y su bloque canónico en algún
                   fichero: ningún validador lo comprueba, y es la clase de defecto que
                   sólo encuentra un lector independiente
NO PUEDE AFIRMAR   nada sobre las 50 pruebas en estado «contrato definido»
```

La primera prueba real de todo esto es el piloto de gym-wear, y su punto de partida está en
[`CHECKPOINT-OPERATIVO.md`](CHECKPOINT-OPERATIVO.md).
