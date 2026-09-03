# T226–T239 y T249 — el paso 4 de `C4`: agentes, modelos y `execution_slots`

Conformidad del **cierre de completitud de `F6`** en el eje que el corte anterior dejó
declarado y no corregido: el **paso 4 de `C4`** —«ASIGNAR AGENTES: por cada rol, aplicar la
política de `C2`. Registrar modelo elegido, descartados y motivo»— y el corte por
`execution_slots`, cuya unidad es el **AGENTE** y no el rol.

Sus fuentes: [`../contratos/C4-MATERIALIZACION.md`](../contratos/C4-MATERIALIZACION.md)
—los siete pasos y las siete prohibiciones—,
[`../contratos/C2-AGENTES-Y-MODELOS.md`](../contratos/C2-AGENTES-Y-MODELOS.md) —los seis
pasos de la asignación, los siete ejes y los veintiún perfiles—,
[`../esquemas/perfil-agente.yaml`](../esquemas/perfil-agente.yaml) —de donde se DERIVAN los
ejes, sus escalas y el orden del esquema— y `b.11`, que calcula `execution_slots` «a partir
de agentes disponibles». Su contrato derivado:
[`../runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md`](../runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md).

**Dónde vive el catálogo de modelos.** En el `PROFILE.md` del **proyecto**, nunca en el
kernel: `C2` sitúa ahí el adaptador, y `K0.8` prohíbe que un proveedor o un modelo comercial
aparezcan en `kernel/` o en `packs/`. Los modelos que estas pruebas usan —`modelo:alfa`,
`modelo:beta`, `modelo:gamma`, `modelo:delta`, `modelo:epsilon`— son **neutros e
inventados**, y su forma es el **espejo del esquema `perfil-agente`**.

**Todo esto EJECUTA.** Control repos reales en directorios temporales, el corpus real del
kernel, procesos reales compitiendo por los mismos slots, y una copia real del árbol a la
que se le BORRA la regla para comprobar que la prueba se pone roja. Ningún mock hace de
pieza en ningún sitio.

**Dos ejecutables:**

```text
runtime/pruebas/test_agentes.py       T226..T239 y T249 — la política de C2, los pasos 1 y 4
                                      de C4, los slots por agente, y los ONCE sabotajes
                                      que ponen roja la prueba que cubre cada regla
runtime/pruebas/escenario_e2e_f6.py   T225 — el escenario de 24 pasos, cuyos pasos 05, 22,
                                      23 y 24 ejercen esta misma materia extremo a extremo
```

**Ninguna de ellas certifica nada.** `prueba-superada` significa que la prueba se ejecutó y
pasó. La CERTIFICACIÓN de `F6` la emite un juicio independiente y no quien construyó.

```yaml ads:escenario
id: T226
nombre: C4 paso 4 asigna agente y modelo a cada rol de una composición con varios roles
cubre: [C4, C2, C1]
dado:
  - "una composición real con cuatro roles obligatorios y tres perfiles distintos"
  - "un control repo real cuyo PROFILE.md declara el catálogo de modelos del proyecto"
cuando:
  - "se materializa el equipo por C4 con el catálogo del proyecto"
entonces:
  - "cada rol despachado lleva perfil, agente, modelo y slot, y ninguna pieza queda vacía"
  - "el perfil sale del contrato del rol y no del nombre del rol"
  - "el registro del paso 4 trae, por rol, el modelo elegido y los descartados con su motivo"
  - "la traza paquete, composición, rol, agente y modelo vive en el objeto durable"
falla_si:
  - "el eje agente se declara en prosa en vez de asignarse y registrarse"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T227
nombre: La selección de modelo es determinista y se repite byte a byte en otro proceso
cubre: [C2, C4]
dado:
  - "el mismo perfil, el mismo catálogo instalado y el mismo corpus"
cuando:
  - "se materializa y se selecciona repetidamente, y desde tres directorios distintos"
entonces:
  - "las cinco materializaciones son idénticas y el identificador del equipo no cambia"
  - "la elección suelta repetida cinco veces produce el mismo registro"
  - "otro proceso con otro cwd produce exactamente la misma salida"
falla_si:
  - "la elección depende de quién la calculó, de dónde se ejecutó o del orden de lectura"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T228
nombre: Un modelo que no cumple un eje se descarta con su motivo, y si es el único se bloquea
cubre: [C2, C4]
dado:
  - "un catálogo donde el modelo más barato no alcanza el nivel exigido en un eje"
cuando:
  - "se aplica el paso 2 de C2 sobre un perfil que exige ese eje al máximo"
entonces:
  - "el modelo queda descartado y el motivo nombra el eje, lo exigido y lo ofrecido"
  - "el modelo descartado nunca resulta elegido, por barato que sea"
  - "con ese modelo como único candidato el equipo queda bloqueado y nombra qué falta"
  - "el texto de degradacion_permitida viaja verbatim y no se interpreta"
falla_si:
  - "un modelo que no cumple el perfil ocupa el rol, o el rol se ocupa a medias"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T229
nombre: Un modelo sin la herramienta o sin el contexto declarados se descarta con su motivo
cubre: [C2, C4]
dado:
  - "un modelo que cumple los siete ejes y no ofrece una herramienta declarada"
  - "otro que cumple los siete ejes y cuyo contexto no llega al exigido"
cuando:
  - "se aplica el paso 3 de C2 sobre perfiles que exigen esa herramienta y ese contexto"
entonces:
  - "el primero se descarta nombrando la herramienta que falta"
  - "el segundo se descarta nombrando el contexto exigido y el ofrecido"
  - "con el primero como único candidato el rol queda bloqueado y nombra la herramienta"
falla_si:
  - "un agente ocupa un rol cuya herramienta o cuyo contexto no puede sostener"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T230
nombre: Agotar execution_slots deja esperando-capacidad y no reduce la composición
cubre: [C4, b.11]
dado:
  - "una composición real con cuatro roles y un par declarado combinable"
cuando:
  - "se materializa con noventa y nueve slots, con dos, con uno y con todos los intermedios"
entonces:
  - "con dos slots se despachan tres roles, porque el par combinable es un solo agente"
  - "lo que no cabe queda esperando-capacidad y conserva su agente asignado"
  - "la unión de despachados y esperando es siempre la composición entera"
  - "nunca hay más agentes despachados que slots, ni dos agentes en el mismo slot"
falla_si:
  - "el corte separa un par que la composición declara combinable, o recorta la composición"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T231
nombre: Dos roles declarados independientes nunca comparten agente, ni por encadenamiento
cubre: [C4, C2, G13]
dado:
  - "la composición real de DSP, donde supervision es independiente de enrutamiento"
  - "una copia real del corpus con una cadena de combinables A-B y B-C, con C independiente de A"
cuando:
  - "se materializan los dos equipos y se aplica el paso 5 de C4"
entonces:
  - "supervision y enrutamiento resuelven al mismo modelo y a agentes distintos"
  - "el cierre de las combinaciones no mete a dos independientes en un mismo agente"
  - "la combinación rechazada dice en su motivo que independientes manda sobre combinables"
  - "la combinación compatible sí se aplica, de modo que el rojo no vendría de no combinar nunca"
falla_si:
  - "un agente ocupa a la vez un rol productor y el rol que critica su producto"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T232
nombre: Cada candidato descartado lleva un motivo verificable uno a uno
cubre: [C2, C4]
dado:
  - "los veintiún perfiles del kernel y el catálogo del proyecto"
cuando:
  - "se recorre la selección de cada perfil y se recalcula el motivo de cada descarte"
entonces:
  - "un motivo por eje se comprueba contra la escala del esquema y contra el catálogo"
  - "un motivo por herramienta se comprueba contra lo exigido y lo ofrecido"
  - "un motivo por contexto se comprueba contra las dos escalas"
  - "los candidatos son exactamente la unión de descartados y ordenados, sin desapariciones"
falla_si:
  - "un descarte no tiene motivo, o su motivo no se sostiene contra el catálogo"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T233
nombre: Reanudar no reasigna en silencio, y el relevo de agente no cambia el rol
cubre: [C2, C4, g.13]
dado:
  - "un equipo materializado y publicado por el motor de estado durable"
cuando:
  - "se relee, se vuelve a escribir, se rematerializa y se cambia el catálogo del proyecto"
entonces:
  - "releer devuelve el mismo vínculo rol, agente y modelo que se escribió"
  - "escribirlo dos veces no mueve la revisión"
  - "rematerializar con la misma entrada produce el mismo identificador de equipo"
  - "con otro catálogo el modelo cambia, el rol no, y el equipo es otro objeto durable"
falla_si:
  - "una reasignación de agente pasa desapercibida dentro del mismo objeto durable"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T234
nombre: Varios procesos reales no producen doble ocupación de un execution_slot
cubre: [b.11, C4, g.12]
dado:
  - "un control repo real con su estado durable y su catálogo de modelos"
cuando:
  - "cuatro procesos reales, en tres carreras, materializan y publican el mismo equipo"
entonces:
  - "todos los procesos que terminan bien coinciden en el mismo identificador de equipo"
  - "el estado canónico contiene un solo objeto de equipo"
  - "cada slot está ocupado una sola vez y ningún rol aparece en dos agentes"
  - "nunca hay más agentes despachados que slots declarados"
falla_si:
  - "dos agentes ocupan el mismo slot, o un rol acaba en dos agentes"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T235
nombre: Borrar la regla en una copia del árbol pone la prueba roja de verdad
cubre: [C4, C2, b.11]
dado:
  - "una copia real del árbol del kernel operativo, con su runtime y su corpus"
cuando:
  - "se borra una a una la regla que cada prueba cubre y se ejecuta esa prueba en un proceso real"
entonces:
  - "la copia sin sabotear pasa en verde y ejecuta de verdad el caso, como control positivo"
  - "borrar el filtro por ejes, el filtro por herramientas o el orden de C2 pone rojo"
  - "devolver el corte de slots al corte por rol pone rojo"
  - "quitar la precedencia de independientes sobre el cierre de combinables pone rojo"
  - "ocupar el rol con un modelo por defecto cuando ninguno cumple pone rojo"
  - "restaurada la regla, la misma prueba vuelve al verde"
falla_si:
  - "una propiedad se puede borrar del producto sin que ninguna prueba parpadee"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

---

## Lo que añadió la AUDITORÍA INDEPENDIENTE · `T236`–`T239` y `T249`

**Estas cinco no estaban previstas: las pidió el auditor.** Cuatro de los cinco defectos que
cubren eran **propiedades que se podían borrar del producto sin que ninguna prueba
parpadeara** —el mismo modo de fallo que el corte anterior ya había sufrido—, y el quinto era
un paso de `C4` rotulado como ejecutado que era un passthrough. Las cinco entran en la tabla
de sabotaje de `T235`, que ahora tiene **once** entradas y comprueba una a una que la prueba
correspondiente se pone ROJA.

```yaml ads:escenario
id: T236
nombre: El paso 1 de C4 LEE el paquete de verdad y falla cerrado cuando no resuelve
cubre: [C4, C1]
dado:
  - "un paquete que declara capacidad responsable, método, objetivo, nivel de calidad y acoplamiento"
  - "el corpus real, con sus métodos por capacidad y su escala de novedad"
cuando:
  - "se materializa el equipo por C4 leyendo esas cinco materias contra sus sedes"
entonces:
  - "el modo se deriva de los pasos del método y no del nombre del método"
  - "el nivel de calidad aporta sus gates y sus estaciones al equipo escrito"
  - "el acoplamiento llega normalizado con sus siete campos"
  - "una materia no declarada consta como ausencia explícita y con su motivo"
  - "un método ajeno a la capacidad, un nivel fuera de la escala o una capacidad responsable distinta fallan cerrado"
  - "varios agentes sin integrador declarado, con integrador inexistente o sin fase divergente fallan cerrado"
falla_si:
  - "el paso 1 transporta dos cadenas y se rotula como ejecutado"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T237
nombre: El agente que ocupa varios roles cumple los perfiles de TODOS ellos
cubre: [C2, C4]
dado:
  - "dos perfiles del kernel con exigencias distintas en el eje vision"
  - "el catálogo real del proyecto"
cuando:
  - "se combina la exigencia de los dos roles que compartirán un agente"
entonces:
  - "la exigencia combinada es el máximo eje a eje, nunca el mínimo"
  - "las herramientas se unen y el contexto es el mayor de los dos"
  - "ningún agente combinado del equipo queda por debajo de ninguno de los perfiles que ocupa"
falla_si:
  - "un agente sin vision ocupa un rol que declara vision requerida por haberse combinado"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T238
nombre: El techo de coste de un agente combinado es el MENOR de los que comparte
cubre: [C2, C4]
dado:
  - "parejas de perfiles del kernel con techos de coste distintos"
cuando:
  - "se combina su exigencia para un agente que ocupará los dos roles"
entonces:
  - "el techo combinado es el menor de los dos, en las tres parejas medidas"
falla_si:
  - "combinar un rol barato con uno caro hace desaparecer el techo del barato"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T239
nombre: El eje dominante es el nivel maximo que C2 nombra, y vision nunca puede serlo
cubre: [C2]
dado:
  - "los veintiún perfiles del kernel y el orden de ejes del esquema perfil-agente"
cuando:
  - "se recalcula la regla de C2 paso 4 a sobre cada perfil, sin usar la implementación"
entonces:
  - "el eje dominante es el primero por orden del esquema declarado con nivel maximo"
  - "vision no es el eje dominante de ningún perfil, porque su escala no tiene ese nivel"
  - "el perfil que no declara ningún maximo publica su motivo marcado como DERIVADO"
falla_si:
  - "se publica como razón de la elección una regla que C2 no escribe"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```

```yaml ads:escenario
id: T249
nombre: El registro de combinaciones de C4 paso 7 no se autocontradice al romperse un grupo
cubre: [C4, C2]
dado:
  - "un catálogo hostil real con un modelo por perfil y ninguno que cumpla los dos"
  - "una composición cuyo par combinable no puede compartir agente con ese catálogo"
cuando:
  - "se materializa el equipo y la combinación se rompe"
entonces:
  - "ninguna combinación queda aplicada sobre un par que se rompió"
  - "comparte_agente_con coincide con el agente realmente asignado a cada rol"
  - "la comprobación de separación coincide con los agentes realmente asignados"
falla_si:
  - "el equipo escrito afirma a la vez que dos roles comparten agente y que no lo comparten"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_agentes.py
estado: prueba-superada
evidencia: evidencia/agentes-salida.txt
```
