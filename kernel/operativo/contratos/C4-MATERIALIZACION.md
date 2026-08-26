# C4 — Materialización, ampliación y retirada de equipos


> **No se crean equipos permanentes sin trabajo real.** a.4 fija el criterio; C4 lo hace
> ejecutable: qué roles necesita un paquete concreto, cuántos agentes, cuáles se combinan,
> cuáles no pueden combinarse nunca, y cuándo el equipo se deshace.

## El algoritmo de materialización

Determinista: mismo paquete y misma composición instalada producen el mismo equipo, y
queda escrito por qué.

```text
1 LEER EL PAQUETE     capacidad responsable · modo · objetivo · nivel de calidad exigido
                      · declaración de acoplamiento

2 ELEGIR COMPOSICIÓN  recorrer los bloques ads:composicion de esa capacidad EN EL ORDEN
                      EN QUE ESTÁN ESCRITOS y quedarse con el PRIMERO cuya `condicion`
                      sea verdadera. El orden es parte del contrato, no casual.
                      Si ninguna condición se cumple → la capacidad no tiene composición
                      para este trabajo: es un defecto del catálogo y se escala a SIS.

3 EXPANDIR ROLES      los roles con `obligatorio: true` entran siempre.
                      Los que declaran `condicion` entran si su condición es verdadera.

4 ASIGNAR AGENTES     por cada rol, aplicar la política de C2. Registrar modelo elegido,
                      descartados y motivo.

5 APLICAR COMBINACIÓN dos roles comparten agente SÓLO si la composición los declara
                      `combinables` Y ninguno aparece en `independientes`.
                      Ante conflicto entre ambas listas, MANDA `independientes`.

6 COMPROBAR LÍMITES   execution_slots del equipo (b.11). Lo que no cabe queda
                      `esperando-capacidad`. NO se reduce la composición para que quepa.

7 ESCRIBIR EL EQUIPO  qué roles, qué agentes, qué composición, qué condición la eligió y
                      qué roles quedaron fuera y por qué
```

> El paso 7 es lo que convierte la materialización en auditable. Un equipo sin registro de
> composición es indistinguible de un equipo improvisado.

## Cuántos agentes por rol

```text
1 AGENTE            por defecto, siempre
VARIOS AGENTES      cuando se cumple alguna, y la composición lo declara:
                      [ ] el trabajo se reparte por artefacto o superficie sin solapamiento
                      [ ] el método declara una fase divergente con exploración en paralelo
                      [ ] el volumen excede lo que un contexto puede sostener
                    En los tres casos se declara QUIÉN INTEGRA el resultado.
COMPETENCIA         dos agentes con el mismo rol y el mismo objetivo, produciendo por
                    separado para comparar después. Sólo si el método lo declara, y con
                    criterio de comparación escrito ANTES de empezar.
```

**Varios agentes sin integrador declarado está prohibido.** Produce tres propuestas y
ninguna decisión, que es ceremonia con apariencia de profundidad.

## Ampliación y reducción durante el trabajo

```text
SE AMPLÍA    cuando la condición de otra composición pasa a ser verdadera durante el
             trabajo. El equipo NO se rehace: se AÑADE el rol que falta, y el trabajo en
             curso conserva su custodia y su checkpoint.

SE REDUCE    cuando un rol termina su artefacto y su `retirada` se cumple. El rol sale;
             el equipo sigue.

NO SE REDUCE por presupuesto, por prisa ni por tamaño aparente del trabajo. Reducir la
             composición para ir más rápido es la forma operativa del sesgo barato que
             a.7 derogó al sustituir K0.9.
```

**Un rol independiente nunca se retira para ahorrar una lectura.** Si su condición de
activación se cumplió, su dictamen forma parte del gate, aunque después la incertidumbre
haya bajado.

## Retirada del equipo

```text
ROL       se retira cuando cumple su `retirada`. Su memoria persiste.
EQUIPO    se desmaterializa cuando su tablero queda sin cola.
          Regla de retirada de G52: sin movimiento durante dos auditorías → candidato.
MEMORIA   NUNCA se retira. Las memorias no mueren; los equipos sí (a.4).
```

Al desmaterializar se escribe: qué equipo, qué composición tenía, y dónde queda su memoria.
Rematerializarlo después es cargar esa memoria, no empezar de cero.

## Tres cosas distintas que no deben confundirse

> Confundirlas produce el defecto que a.4 y T12 existen para impedir: equipos que hay que
> mantener ocupados, y trabajo fabricado para justificarlos.

```text
CAPACIDAD DISPONIBLE      está en el catálogo instalado. No consume nada: sin tablero, sin
                          cola, sin agentes. Las QUINCE lo están siempre.

EQUIPO MATERIALIZADO      tiene tablero, cola, memoria viva y agentes ocupando roles,
                          PORQUE hay trabajo real que lo necesita. Se materializa por la
                          señal de a.4 y se retira por la regla de retirada de G52.

EQUIPO PERMANENTEMENTE    se materializa al instalar y no se retira nunca. Son DOS.
ACTIVO
```

### Los dos equipos permanentemente activos

```text
DSP   sin despacho no hay orden ni ruta
SIS   sin ingeniería del sistema nadie mantiene la fábrica
```

**`ENC` NO es uno de ellos.** La enmienda [E1.2](../../../docs/rediseno/a-ENMIENDA-E1-ENC.md)
lo fija expresamente: `ENC` es capacidad disponible siempre y equipo materializado **bajo
demanda**, y se retira por la regla general. Que no esté materializada no cierra la puerta de
entrada: la primera expresión del Owner es la señal de materialización de a.4, igual que
para cualquier otra capacidad. Su memoria persiste y es lo que evita que el Owner repita
contexto al rematerializarla.

## Prohibiciones de materialización

```text
PROHIBIDO   materializar una capacidad «por si acaso», sin paquete que la necesite  (T12)
PROHIBIDO   materializar un rol sin asignarle agente: un rol vacío no es un rol
PROHIBIDO   asignar un agente que no cumple el perfil, sin aplicar `degradacion_permitida`
PROHIBIDO   combinar dos roles que la composición declara independientes
PROHIBIDO   un agente ocupando un rol productor y su crítico en el mismo paquete
PROHIBIDO   reducir la composición declarada para que el trabajo quepa en los slots
PROHIBIDO   materializar un equipo cuya capacidad no está en el catálogo instalado
```

## Ejemplo completo de materialización

```text
PAQUETE           FEA-014/02 · capacidad DIS · modo trabajo propio
                  objetivo: dirección visual del producto
                  nivel de calidad exigido: primera dirección, área diferencial

PASO 2  se recorren las composiciones de DIS EN EL ORDEN EN QUE ESTÁN ESCRITAS en
        capacidades/DIS/composicion.md, y se toma la primera cuya condición es verdadera:
        composicion:dis-bug-visual            falsa (no hay patrón vigente que se incumpla)
        composicion:dis-extension-de-patron   falsa (no hay patrón que extender)
        composicion:dis-gap-de-diseno         falsa (no hay dirección aprobada)
        composicion:dis-caso-nuevo            falsa (no hay sistema aún)
        composicion:dis-nueva-interaccion     falsa
        composicion:dis-animacion             falsa
        composicion:dis-revision-implementacion  falsa (no hay nada construido)
        composicion:dis-feature-visual        falsa (no hay dirección vigente)
        composicion:dis-reconstruccion        falsa (no hay producto construido)
        composicion:dis-proyecto-nuevo        VERDADERA  → elegida

PASO 3  roles obligatorios: direccion-artistica · investigacion-visual · diseno-visual ·
        critica-visual · sistema-de-diseno
        roles condicionales: movimiento (condición: la dirección incluye transiciones
        o microinteracciones) → verdadera · prototipado → verdadera

PASO 4  cada rol recibe agente según su perfil; los descartes quedan registrados

PASO 5  combinables: diseno-visual + prototipado en un agente
        independientes: critica-visual de TODOS los demás  → no se combina

PASO 6  execution_slots de DIS: auto → 4 efectivos.
        Se despachan cuatro roles; investigacion-visual queda `esperando-capacidad`.
        NO se elimina de la composición: espera.

PASO 7  se escribe el equipo, la composición elegida, la condición que la eligió y que
        investigacion-visual está esperando capacidad, no retirado.
```
