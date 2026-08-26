# MAPA — la directiva del Owner contra el ADS que existe

Trabajo **23.2** de la [directiva](ADS-NEXT-OWNER-BRIEF.md). Un veredicto por apartado,
contra el estado comprobado en [`01-BASELINE-ADS.md`](01-BASELINE-ADS.md).

## Los seis veredictos

```text
CUBIERTO        existe contrato Y algo que lo sostiene. No implica uso real: la columna
                de uso real está vacía para todo el sistema, y eso se dice una vez aquí.
PARCIAL         existe la mitad: el contrato sin portador, o el portador sin contrato.
AUSENTE         ni contrato, ni implementación, ni prueba.
CONTRADICHO     la directiva pide algo que choca con material normativo APROBADO.
                No se resuelve por escritura: se resuelve por el proceso de autoridad.
EVIDENCIA       la respuesta correcta depende de la minería. Cerrarla antes sería inventar.
OWNER           la decisión pertenece al Owner, no al sistema.
```

## Mapa por apartado

| § | qué pide | veredicto | dónde está hoy, o por qué no |
|---|---|---|---|
| 2 | intención del Owner → trabajo persistente y recuperable | **PARCIAL** | `ENC` convierte la frase en item; lo persistente no tiene dónde persistir |
| 3.1 | el Owner no es scheduler de agentes | **PARCIAL** | `a.8` fija sus tres niveles de intervención con criterio escrito; sin runtime, el scheduler sigue siendo él |
| 3.2 | la organización no depende del agente concreto | **CUBIERTO** | `C1` separa rol de agente · `C2` perfiles de modelo · portabilidad comprobada por `T92` |
| 3.3 | productor y crítico independientes | **CUBIERTO** | `G13` como estructura por defecto · `C4` paso 5 · `T87`: la independencia gana a la combinación |
| 3.4 | evidencia antes que afirmación | **CUBIERTO** | los cuatro estados de [`REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md) · `T158` comprueba que la evidencia respalde el informe |
| 3.5 | fuente única de verdad | **CUBIERTO** | regla de fuente única del [índice operativo](../../kernel/operativo/00-INDICE.md) · `T147` · `T151` |
| 3.6 | persistencia y recuperación tras cerrar el chat | **PARCIAL** | contrato completo —`a.10` checkpoint, `b.14` `Continúa`— y **ningún portador**: no existe un solo fichero de estado |
| 3.7 | el sistema no crece sin control | **PARCIAL** | `a.4` retirada de capacidades · `G52` aplicada a lo materializado; falta la señal de uso que dispare una retirada |
| 4.1 | reglas universales | **CUBIERTO** | es exactamente `kernel/operativo/` |
| 4.2 | conocimiento por clase de proyecto | **CUBIERTO** | tres packs con [composición computable](../../packs/COMPOSICION.md) |
| 4.3 | conocimiento reutilizable **nuestro**, ni universal ni de un proyecto | **AUSENTE · EVIDENCIA · OWNER** | no hay capa donde ponerlo. Choca con `K-1`, que declara **tres** capas — ver contradicción **X1** |
| 4.4 | conocimiento específico del proyecto | **PARCIAL** | `PROFILE` existe como plantilla; roles, métodos y herramientas locales no tienen contrato de creación |
| 5 | minería de proyectos reales → ADS | **AUSENTE** | `APR/Promocion` promueve lo aprendido **dentro** de un proyecto gobernado por ADS. La minería entra en proyectos que ADS nunca ha gobernado: es otro circuito |
| 6 | adopción de un proyecto con historia | **PARCIAL** | «Ruta B» de [`START_HERE.md`](../../START_HERE.md) es copiar directorios y pegar un prompt. No reconstruye la realidad del proyecto ni preserva procedencia |
| 7 | proyecto nuevo instalable y reproducible | **PARCIAL** | `new-project.sh`, ejecutado por `T148`. No existe definición verificable de «ADS está instalado correctamente» más allá de que el lint salga verde |
| 8 | gobierno Git del proyecto real | **PARCIAL** | *corregido en F2.* `G29` y `G30` cubren rama protegida, aislamiento, commits y push autónomos, PR, CI como autoridad, cuatro niveles de autoridad de merge, `merge ≠ release`, tags, rollback y contención. **Ninguna capacidad de la línea 2.0 los ha recogido**, y el 8.3 —Git como memoria operativa— falta entero. Ver [`06-CONTRASTE`](06-CONTRASTE.md) **P-04** |
| 9 | neutralidad de proveedor con adaptadores | **PARCIAL** | la neutralidad conceptual es real y está comprobada (`K0.8`, `T92`). Es neutralidad **por ausencia**: no hay adaptador que traduzca nada a ningún entorno |
| 10 | skills y agentes especializados como piezas de primera clase | **AUSENTE** | `skill` y `herramienta` **no son tipos canónicos**: no están entre los esquemas. `a.4` sí prevé extender el catálogo, así que es extensión, no choque |
| 11 | base tecnológica y defaults probados | **AUSENTE · EVIDENCIA** | misma capa que 4.3. Qué defaults son nuestros de verdad lo dice la minería, no una preferencia escrita hoy |
| 12 | aprendizaje proyecto → ADS | **PARCIAL** | `APR` y `docs/UPSTREAM.md` existen; los destinos que el 12 enumera —blueprint, adaptador, tooling— no existen como destino posible |
| 13 | documentación estructurada de lo aprendido | **AUSENTE** | hay changelog e historia de auditoría; no hay corpus consultable de «qué aprendimos, con qué evidencia, qué se retiró» |
| 14 | actualización ADS → proyectos instalados | **AUSENTE** | `kernel-status.sh` detecta que la copia divergió. No hay comparación de versiones, ni impacto, ni migración, ni rollback |
| 15 | ADS instalable como sistema, con interfaz clara | **PARCIAL** | un script de creación. Ni `adopt`, ni `update`, ni `status` del sistema instalado |
| 16 | runtime real | **AUSENTE · CONTRADICHO** | `a.9` y `(b)` son su especificación de requisitos. Choca con `G03` — ver contradicción **X2** |
| 17 | circuito formal para crear PROFILE y especialización | **AUSENTE** | hoy es una plantilla y una conversación que nadie garantiza |
| 18 | ADS se evoluciona usando ADS | **PARCIAL** | `SIS` existe con sus dos roles y métodos, y **nunca se ha usado para esto**. Esta iniciativa es su primer intento |
| 19 | no depender de un chat | **PARCIAL** | igual que 3.6: contrato sin portador |
| 20 | estado ejecutivo para el Owner | **PARCIAL** | `G08` ya está ajustado a «vista derivada, no informe redactado». No hay estado del que derivarla |
| 21 | criterios de realidad | **CUBIERTO** | es la disciplina central del repositorio, y la que hace posible este mapa |
| 22 | compatibilidad y migración entre versiones de ADS | **AUSENTE** | [`VERSIONES.md`](../../kernel/VERSIONES.md) fija qué se versiona; nada dice cómo se migra |
| 23 | trabajo previo antes de cerrar arquitectura | **EN CURSO** | este documento es su punto 2 |

## Las contradicciones que no se resuelven escribiendo

Se registran. **No se tocan (a) ni (b) desde aquí**, igual que hizo la iteración anterior.

### X1 · Una cuarta capa contra `K-1`

**Qué pide la directiva.** El 4.3 describe conocimiento que no es universal para la
industria pero sí válido para muchos de nuestros proyectos, y pide estudiar si necesita
capa propia. El 11 lo concreta en stacks, librerías y patrones de UI.

**Qué choca.** `K-1` declara **tres** capas, y `K0.10` define el test de contaminación
como una pregunta binaria: *¿sería igual de cierta en un proyecto de otra clase? → KERNEL.
¿En otro de la misma clase? → PACK. ¿Sólo aquí? → PROFILE.* Ese test **no tiene casilla**
para «cierta en nuestros proyectos, no en los de otro». Hoy ese conocimiento sólo puede
contaminar el kernel o repetirse en cada PROFILE, que es exactamente lo que el 4.3 quiere
evitar.

**Por qué no se decide aquí.** Añadir una capa cambia el test de contaminación, la regla de
precedencia entre packs, qué copia `new-project.sh` y qué compara `kernel-status.sh`. Y la
directiva dice, con todas las letras, que el nombre y la implementación de esa capa **no
están decididos**. La forma correcta la fija la evidencia de la minería: si dos proyectos
del Owner comparten decisiones que ningún pack explica, la capa está justificada; si no,
sobra.

**Estado:** abierta. Es la primera pregunta que la minería debe poder responder.

### X2 · Runtime contra `G03`

**Qué pide la directiva.** El 16 exige un runtime que materialice la organización:
persistencia, colas, checkpoints, handoffs, concurrencia, recuperación tras fallo.

**Qué choca.** `G03` de 1.3.0 dice que la autonomía temporal no es requisito inicial y que
no debe introducirse esa complejidad. El [mapa del rediseño](../rediseno/00-MAPA.md) ya
había separado las dos cosas: `Continúa` —reanudar al abrir un chat— **no** es autonomía
temporal y ya era requisito; la ejecución desatendida sí cae bajo `G03`.

**Lectura:** la mayor parte del 16 es la primera cosa, no la segunda. Persistencia, estado,
handoffs y recuperación no son autonomía temporal. Lo que sí lo es —ejecución desatendida,
concurrencia real de varios agentes trabajando solos— sigue bajo `G03` y necesita decisión
explícita del Owner para levantarse.

**Estado:** parcialmente resuelta por lectura; la parte desatendida es **OWNER**.

### X3 · «El kernel es neutral» frente a «existen adaptadores»

**Qué pide la directiva.** El 9.2 pide una capa de adaptadores que traduzca roles, skills,
herramientas, memoria y permisos a Claude Code, Codex, Cursor y Gemini.

**Qué choca — y qué no.** `K0.8` y `T92` garantizan que ningún contrato exige una marca.
Un adaptador **no** rompe eso: lo cumple, porque saca lo específico del proveedor fuera de
los contratos. Lo que sí falta es dónde vive un adaptador. No es kernel —es específico de
una marca—, no es pack —no depende de la clase de proyecto— y no es PROFILE —no es de un
solo proyecto—. **Es el mismo hueco de X1, encontrado por otro camino.**

**Estado:** no es contradicción; es la segunda prueba de que falta una capa.

### X4 · La minería entra en proyectos que ADS no gobierna

**Qué pide la directiva.** El 5 ordena estudiar proyectos reales como fuente de
conocimiento para `ads-kernel`, y el 5.1 insiste en que no es adopción.

**Qué choca.** Todo el aprendizaje de ADS —`APR`, `G52`, `docs/UPSTREAM.md`— presupone un
proyecto **ya gobernado por ADS** que produce evidencia dentro del sistema. La minería
carece de esa premisa: no hay items, ni paquetes, ni evidencia ADS de la que promover.

**Lectura:** es un proceso nuevo, no una variante de `APR`. Cuál de los diez procesos
canónicos de `b.16` lo representa —o si hace falta uno más— es materia de la síntesis, no
de este mapa.

**Estado:** abierta, y es una de las preguntas del [plan](04-PLAN-DE-INVESTIGACION.md).

### X5 · Un documento en voz del Owner no tenía sitio

Encontrado por los validadores al entrar esta directiva, y documentado en el
[baseline](01-BASELINE-ADS.md). Resuelto con el mecanismo de exención acotada que el kernel
ya tenía, pero deja una pregunta abierta: **la directiva del Owner es material normativo de
primer orden y hoy no tiene tipo canónico**. Un `PROFILE` tampoco lo tiene. Se registra
para la síntesis.

## Lo que este mapa NO decide

```text
qué arquitectura resuelve los AUSENTES           depende de la minería (23.3) y la síntesis
si la cuarta capa existe, y cómo se llama        X1 · evidencia + Owner
si se levanta G03 para ejecución desatendida     X2 · Owner
qué proceso representa la minería                X4 · síntesis
qué es una skill en ADS                          §10 · síntesis
```
