# CONTRASTE — los 29 candidatos contra el corpus de ADS

Fase **F2** del [plan](04-PLAN-DE-INVESTIGACION.md). Cada candidato de
[`05-CANDIDATOS.md`](05-CANDIDATOS.md) se lee contra el artefacto de ADS que gobierna su
materia, **por identificador**, no por recuerdo del corpus.

**Qué NO hace esta fase.** No propone arquitectura, no crea capas, no enmienda material
aprobado y no incorpora nada al kernel. Produce dos cosas: un veredicto por candidato, y
una lista de **problemas arquitectónicos** registrados con evidencia y deliberadamente sin
resolver.

## Los siete veredictos

```text
YA CUBIERTO          ADS ya lo resuelve, y en varios casos mejor. El candidato vale como
                     confirmación empírica de una regla, no como cambio.
PARCIAL              ADS cubre una parte identificable y deja otra fuera.
MEJORA KERNEL        material para una regla universal que hoy falta.
MEJORA PACK          material para el saber hacer de una clase de proyecto.
ADAPTADOR·TOOLING·RUNTIME   pertenece a la maquinaria, no al contenido normativo.
ESPECÍFICO           es de ese proyecto y no sube.
CARENCIA CONCEPTUAL  no cabe limpiamente en ninguna categoría actual. Se registra como
                     problema, con evidencia, y NO se resuelve aquí.
```

## Estado de Q1 y de la contradicción X1 — instrucción del Owner

El Owner ha retirado `gym-wear` de la minería el 2026-08-26, con su motivo:

> Gym Wear no es una fuente independiente útil para esta minería: nació a partir de una
> versión primitiva de ADS y apenas tuvo desarrollo organizativo propio. Analizarlo
> introduciría evidencia contaminada y de poco valor.

Consecuencias, que son normativas para el resto de esta iniciativa:

```text
Q1   NO RESPONDIDA, ni en positivo ni en negativo. No existe hoy evidencia independiente
     suficiente para demostrar si hace falta una capa adicional entre PACK y PROFILE.
     PesquerApp es la única fuente externa madura de esta fase, y sus dos repositorios
     son un solo producto: su repetición interna demuestra copia, no reutilización.

X1   ABIERTA Y DEFERIDA. No es una tarea pendiente de ejecutar: es una pregunta que la
     evidencia disponible NO PUEDE responder. Se reabre cuando exista un proyecto
     independiente y maduro, no antes.

PROHIBIDO   diseñar la cuarta capa por intuición, y forzar los candidatos de PesquerApp
            para justificarla. Registrado como problema P-05, sin propuesta.
```

## Correcciones que este contraste ha producido sobre F0 y F1

Leer el corpus por identificador ha desmentido tres afirmaciones anteriores. Se corrigen en
su documento y se listan aquí, porque cambian conclusiones.

| | qué se afirmó | qué dice el corpus | dónde se corrige |
|---|---|---|---|
| C-1 | el apartado 8 —gobierno Git— está **AUSENTE**, con «sólo `G29` en prosa» | `G29` gobierna rama principal, unidad aislada, commit y push autónomos, PR, CI como autoridad, **cuatro niveles de autoridad de merge**, `merge ≠ release`, tags y rollback. `G30` añade contención y recuperación. El veredicto correcto es **PARCIAL**, y el hallazgo real es otro: **ninguna capacidad de la línea 2.0 lo ha recogido** | [`02-MAPA`](02-MAPA-DIRECTIVA.md) · [`01-BASELINE`](01-BASELINE-ADS.md) |
| C-2 | «`ORG_LEARNINGS` y `PROJECT_LEARNINGS` de ADS son plantillas sin campos» | tienen juego completo de campos —observación, evidencia, **confianza `anécdota` / `patrón` / `medido`**, implicación, afecta a, estado—, techo de entradas vigentes y curación obligatoria al superarlo | CAND-017, abajo |
| C-3 | el artefacto con tres zonas de escritura contradice «aparentemente» a `I5` | `a.9` ya resuelve exactamente eso para el tablero: dos zonas con autoridad distinta, canal de órdenes, CAS sobre el hash de contenido y evento antes de mutar. No es una contradicción aparente: es un mecanismo que ya existe y no se ha aplicado al paquete | CAND-004, abajo |

## Resumen

| veredicto | candidatos |
|---|---|
| YA CUBIERTO | CAND-002 · 003 · 005 · 016 · 020 · 028 |
| PARCIAL | CAND-004 · 007 · 013 · 015 · 017 · 018 · 019 · 021 · 025 |
| MEJORA KERNEL | CAND-008 · 011 · 012 · 014 |
| MEJORA PACK | CAND-022 · 024 |
| ADAPTADOR · TOOLING · RUNTIME | CAND-001 · 009 · 010 · 023 · 027 |
| ESPECÍFICO | CAND-006 |
| CARENCIA CONCEPTUAL | CAND-029 |
| evidencia sin destino propio | CAND-026 |

**Seis de veintinueve ya estaban resueltos en ADS, y en cuatro de esos seis ADS es más
estricto que el proyecto.** Es el resultado más útil de esta fase: mide cuánto del corpus
resiste el contacto con un proyecto real que nunca lo leyó.

---

## Contraste por candidato

### Estado, memoria y sesión

**CAND-001 · Estructura persistente de sesión** → **RUNTIME**, con una reserva importante
`contra` `a.9` delega la disposición física · `a.10` fija el checkpoint · `b.2` los estados
`qué cubre ADS` el checkpoint de `a.10` cubre lo que `active_task.md` y `context_stack.md`
hacen, y con más campos: `based_on` con versión, `freshness`, `last_meaningful_event`,
`resuelto` con lo descartado y su motivo
`qué NO cubre` la disposición física. No existe un solo fichero de estado
`la reserva` **su unidad de organización es la SESIÓN**, y la sesión es exactamente aquello
de lo que ADS está diseñado para no depender —apartado 19 de la directiva—. Adoptar la
carpeta por sesión sería una regresión. Lo reutilizable es su **subestructura**
—trabajo · análisis · plan · ejecución · registro · entregables— colgando de la unidad de
custodia de ADS, que es el paquete
`veredicto` material para el runtime · **la unidad no se copia**

**CAND-002 · Tres capas de memoria** → **YA CUBIERTO**, con otro vocabulario
`contra` `a.10` checkpoint · `b.3` capas y su vigencia · `esquemas/memoria.yaml` · `G52`
`qué cubre ADS` los tres horizontes existen y tienen portador distinto: el **checkpoint**
es la memoria de trabajo, la **capa depositada en el paquete** es la que evoluciona durante
la tarea, y la **memoria de capacidad más los dos ledgers** es la permanente. `memoria.yaml`
exige además `caducidad`, `se_actualiza_cuando`, `se_consulta_en` y `vacio_significa`
`qué añade el candidato` nombrar los tres horizontes juntos en un sitio. ADS nunca lo hace
`veredicto` **no cambia nada normativo**. Mejora de redacción, si acaso

**CAND-003 · Decisión crítica frente a automática** → **YA CUBIERTO**, y ADS es más preciso
`contra` `a.8` tres niveles de intervención con criterio escrito · campo `autoridad` de cada
capacidad, con `decide_sola`, `escala` y `veta` · `b.2` estado `esperando-owner`
`por qué ADS es más preciso` PesquerApp tiene **una** lista global de lo automático y lo
crítico. ADS lo declara **por capacidad y por rol**, de modo que la misma decisión puede ser
automática para una y escalable para otra. Una lista global no puede expresar eso
`veredicto` confirmación empírica. Sin cambio

**CAND-017 · Ledger con confianza** → **PARCIAL**, y mucho menos nuevo de lo que F1 dijo
`contra` `kernel/templates/ORG_LEARNINGS.md` y `PROJECT_LEARNINGS.md` · `gate:aprendizaje-fundado`
`corrección C-2` los dos ledgers **ya tienen** observación, evidencia, **confianza en tres
grados —`anécdota`, `patrón`, `medido`—**, implicación, a qué afecta y estado. Y techo de
entradas vigentes con curación obligatoria al superarlo. El grado de ADS es además mejor que
un recuento: `medido` no es «apareció tres veces», es «se midió»
`el umbral también está` `gate:aprendizaje-fundado` comprueba `dos-veces-o-incidente` antes
de dejar escribir la entrada
`qué NO cubre ADS` **la lista vinculante de quién debe leer el ledger antes de trabajar**.
PesquerApp la escribe en la cabecera del fichero y nombra trece agentes. ADS pide consultarlo
antes de un ADR o una decisión significativa, y no ata la lectura a ningún rol ni método
`veredicto` **MEJORA KERNEL, sólo en la lista de lectores obligatorios.** Todo lo demás ya está

**CAND-018 · Escritor único declarado en el fichero** → **PARCIAL**
`contra` `I1` y `I2` de `a.9` · campo `autoridad` de `memoria.yaml`
`qué cubre ADS` la propiedad y el ejecutor de mutación son invariantes aprobados, y cada
sección de memoria declara su autoridad en su bloque canónico
`qué añade` que el propio fichero lo diga **en su primera línea**, donde lo lee quien va a
escribirlo. La declaración de ADS vive en el esquema, no en el artefacto
`veredicto` mejora menor de redacción de plantilla. No es contrato nuevo

### El circuito GAP

**CAND-004 · Artefacto único con zonas por rol** → **PARCIAL**
`contra` `a.9` el tablero y su ciclo de consumo de órdenes · `plantillas/DICTAMEN.md`
`corrección C-3` `a.9` **ya tiene** el mecanismo completo: dos zonas con autoridad distinta
en un fichero, órdenes que nunca se sobrescriben, elevación de toda diferencia antes de
regenerar, evento persistido antes de mutar, idempotencia por id y compare-and-swap sobre el
hash de contenido con tope de reintentos. No hay contradicción con `I5`, ni aparente
`qué NO cubre ADS` ese mecanismo se aplica **sólo al tablero**. El paquete no tiene zonas: el
contrato, la capa depositada y el dictamen viven en artefactos distintos
`qué se rechaza del candidato` su veredicto de auditoría admite **«APROBADO CON
OBSERVACIONES»**. `plantillas/DICTAMEN.md` regla 4 prohíbe expresamente el término medio:
*«los términos medios son cómo se cuela la aprobación complaciente»*. Adoptarlo sería una
regresión
`veredicto` material para aplicar el mecanismo de zonas al paquete · **el término medio no**

**CAND-005 · Descubrimiento → implementación → auditoría** → **YA CUBIERTO**
`contra` `G13` como estructura por defecto · `C4` paso 5 · `T87`
`valor` 115 ciclos completos en producción. Es la **primera evidencia de proyecto real** de
que la separación productor/crítico se sostiene, y `01-BASELINE` decía que esa columna estaba
vacía. Sigue vacía para ADS: lo que se sostuvo fue la idea, no la implementación de ADS
`veredicto` confirmación empírica de una regla vigente. Sin cambio

**CAND-006 · Checklist con las prohibiciones del proyecto** → **ESPECÍFICO**
`contra` `esquemas/gate.yaml` · la regla de infracción deliberada por prueba
`veredicto` el contenido no sube. La forma —comprobaciones nacidas de errores ya cometidos—
ya es doctrina de ADS

**CAND-007 · Estado como directorio** → **PARCIAL**, y el candidato es inferior
`contra` `b.2`, que declara **doce** estados de paquete, y `aparcado` como estado global del
item proyectado sobre todos sus paquetes
`por qué es inferior` tres directorios no expresan doce estados sin doce directorios, y no
pueden representar `aparcado`, que no es un estado de paquete sino una proyección que
conserva intacto el estado real de cada uno
`qué se conserva` una sola idea: el estado debe verse sin herramienta, que es `I4`
`veredicto` no se adopta la disposición · se retiene el requisito de legibilidad

**CAND-008 · Registro derivado y regenerable** → **MEJORA KERNEL**
`contra` `I4` vistas completas derivadas · `I5` lo derivado no es editable
`qué cubre ADS` los dos invariantes lo exigen, y `registro_pruebas.py` y
`comprobar_recuentos.py --generar` lo implementan **para el propio corpus**
`qué NO cubre` ninguna vista derivada del **estado de trabajo**, porque no hay estado
`veredicto` el patrón está probado en los dos lados; lo que falta es el material sobre el que
aplicarlo

### Neutralidad de proveedor

**CAND-009 · Núcleo neutral con adaptadores** → **ADAPTADOR**, y descubre **P-01**
`contra` `K0.8` portabilidad · `C2` regla de portabilidad · `T92`
`qué cubre ADS` la prohibición: ningún fichero de kernel ni de packs nombra un proveedor. Y
`C2` dice literalmente que *«los nombres de marca sólo aparecen en el adaptador del
proyecto»*
`qué NO cubre` **el adaptador.** Está nombrado en una regla y no existe en ninguna otra
parte: no es uno de los dieciocho tipos canónicos, ninguna capacidad lo posee, ningún gate lo
comprueba, ninguna ruta lo produce y `new-project.sh` no crea ninguno
`veredicto` la arquitectura del apartado 9 existe, construida a mano y en producción. Su
hueco en ADS es de contrato, no de idea → **P-01**

**CAND-010 · Mapa de qué consume cada herramienta** → **ADAPTADOR** · contenido de P-01
`contra` nada. No hay artefacto de ADS que declare qué lee un entorno agentic
`veredicto` es la ficha del adaptador que P-01 dice que falta

**CAND-011 · Entrada mínima para la herramienta sin adaptador** → **MEJORA KERNEL**
`contra` el apartado 9.3 de la directiva —degradación explícita— que el
[mapa](02-MAPA-DIRECTIVA.md) marca como parte de un PARCIAL
`qué cubre ADS` nada en el kernel. La palabra degradación aparece en un pack, referida a
permisos de dispositivo, no a capacidades del entorno agentic
`veredicto` sin esto, «neutral» significa «no funciona en lo que no previmos». Es regla
universal y hoy no existe

**CAND-012 · Prueba de humo del adaptador en sesión nueva** → **MEJORA KERNEL + TOOLING**
`contra` `T148` comprueba que `new-project.sh` instala · `kernel-status.sh` comprueba
integridad · `comprobar_arranque.py`
`qué cubre ADS` que **los ficheros están y son íntegros**
`qué NO cubre` que **el agente pueda arrancar el sistema**, que es el noveno requisito del
apartado 15.2 de la directiva. Nada lo comprueba, y no puede comprobarse leyendo ficheros:
exige abrir una sesión nueva y mirar
`veredicto` es la definición operativa que falta para «ADS está instalado correctamente»

**CAND-013 · Mapa de comandos** → **PARCIAL**
`contra` `b.13` órdenes en lenguaje natural, con umbral de anclaje y margen de ambigüedad
`qué cubre ADS` la interpretación de una frase del Owner, que es más general que una tabla
`qué NO cubre` la superficie por herramienta: qué escribe el Owner y qué activa en ese entorno
`veredicto` la tabla pertenece al adaptador, no al kernel

**CAND-014 · Frontera de escritura entre adaptadores** → **MEJORA KERNEL**
`contra` `I2` propiedad de escritura **por zona** en artefactos compartidos
`qué cubre ADS` zonas dentro de un artefacto, con un ejecutor por zona
`qué NO cubre` zonas **del repositorio** entre dos ejecutores distintos, que es el caso real
cuando dos entornos agentic trabajan sobre el mismo proyecto. PesquerApp lo resuelve
declarando un árbol de sólo lectura con tres excepciones nombradas una a una, cada una con su
motivo — y la de memoria dice el suyo: *«to avoid re-introducing the same drift»*
`veredicto` extensión natural de `I2`, y la concurrencia entre proveedores la exige

**CAND-015 · Precedencia entre genérico y proyecto** → **PARCIAL**, y descubre **P-02**
`contra` `P1`–`P4` de [`packs/COMPOSICION.md`](../../packs/COMPOSICION.md)
`qué cubre ADS` la precedencia entre **kernel, pack y PROFILE**, computable: lo más
restrictivo gana cuando la propiedad es medible y comparable, el pack de la superficie gana
cuando no lo es, el kernel gana en contrato universal, y si ninguna aplica hay conflicto y lo
arbitra el PROFILE
`qué NO cubre` **conocimiento traído de fuera de la organización.** La skill de `shadcn/ui`
no es kernel, ni pack, ni PROFILE: es de un tercero. `P1`–`P4` no tienen casilla para ella
`veredicto` la regla del proyecto —lo del proyecto gana a lo genérico— resuelve el caso
concreto y no el hueco → **P-02**

### Calidad y evolución

**CAND-019 · Puntuación antes y después** → **PARCIAL**, y con un choque explícito
`contra` `esquemas/rubrica.yaml` · `b.9` `avance_material`
`el choque` el esquema de rúbrica de ADS se describe a sí mismo como *«criterio de juicio
profesional con niveles descritos y evidencia exigida; **no reduce el juicio a una nota**»*, y
exige por eje un umbral de rechazo, uno de suficiencia y uno de excelencia, con su evidencia.
Un número de 1 a 10 es justo lo que ese esquema existe para impedir. **La escala no se adopta**
`qué sí es valioso, y ADS no tiene` la puntuación no se aplica a un item: se aplica a un
**bloque funcional del producto**, y se compara consigo misma a lo largo del tiempo. ADS mide
avance dentro de un item —`b.9` define siete formas de avance material— y **no tiene ninguna
noción de nivel de calidad persistente por área del producto**
`veredicto` se rechaza la nota · se retiene la pregunta → **P-03**

**CAND-020 · El déficit declarado con su siguiente acción** → **YA CUBIERTO**
`contra` `b.3` obligación satisfecha, retirada y huérfana · `plantillas/CIERRE.md` · `b.16` `GAP`
`por qué está cubierto` un objetivo de calidad no alcanzado no es una obligación incumplida:
es un hueco, y ADS ya tiene un proceso canónico para un hueco, que es `GAP`. El informe de
cierre además impide el error que el candidato podría inducir: sumar lo satisfecho y lo
retirado y llamarlo entregado
`veredicto` sin cambio. La forma de PesquerApp —una nota dentro del log— es más débil que
crear el item

**CAND-021 · Log de evolución con formato fijo** → **PARCIAL**
`contra` `G52` los dos ledgers · `G26` el journal · el registro de decisiones
`qué cubre ADS` **qué se aprendió** (ledgers), **qué pasó** (journal) y **qué se decidió**
(decisiones). Los tres con dueño y frontera escrita
`qué NO cubre` **qué cambió en un área del producto y cómo estaba antes**. No es ninguno de
los tres: es historia por área, con estado de calidad. Mismo hueco que CAND-019
`veredicto` → **P-03**

### Herramientas y automatismo

**CAND-022 · Captura de pares esqueleto/cargado** → **MEJORA PACK · `web-app`**
`contra` `diseno/05-FIDELIDAD.md` y `DIS/RevisionDeFidelidad`
`qué cubre ADS` el artefacto de comparación está **completamente especificado**: capturas por
entorno de la matriz del pack, a tamaño real y con zoom en las juntas, los cinco estados
obligatorios en ambas columnas, grabaciones con duración medida frente a la especificada,
extracción de valores realmente usados y evidencia en dispositivo real
`qué NO cubre` **con qué se captura.** Seis pasos de método sin una sola herramienta
`por qué encaja exactamente` la herramienta retiene las respuestas de API hasta capturar el
esqueleto y luego las libera, de modo que las dos imágenes salen de la misma navegación. Eso
es lo que hace comparable la estructura, y es la condición que el método da por supuesta
`veredicto` primera evidencia de que la revisión de fidelidad de ADS es ejecutable

**CAND-023 · Permisos del agente en el repositorio** → **ADAPTADOR** · contenido de P-01
**CAND-024 · Gancho de git con degradación declarada** → **MEJORA PACK · `web-app`**
`contra` `G29` CI como autoridad automática. ADS exige la comprobación y no dice qué pasa
cuando el entorno no puede ejecutarla. El gancho lo resuelve declarándolo y avisando
**CAND-027 · Skill de terceros con procedencia y hash** → **TOOLING**, y refuerza **P-02**
`contra` `K0.11` vendorizado y `huella.py`, que hacen esto **con el propio kernel**. ADS
controla la integridad de lo suyo y no tiene forma de vendorizar conocimiento ajeno

### Git

**CAND-025 · Rama por trabajo de agente, integración por PR** → **PARCIAL**, y descubre **P-04**
`contra` `G29` y `G30` de `kernel/KERNEL.md`
`corrección C-1` `G29` es sustancial: rama principal protegida, unidad de trabajo aislada
—rama, worktree o sandbox—, commit y push autónomos dentro del trabajo autorizado, PR como
punto de convergencia, CI como autoridad automática, **cuatro niveles de autoridad de merge**
graduados por riesgo, `merge ≠ release`, tags y rollback, y la regla de que el Owner no es
operador de Git. `G30` añade contención, diagnóstico y recuperación
`el hallazgo real` **ninguna capacidad de la línea 2.0 lo ha recogido.** Un barrido de
`kernel/operativo/` y `packs/` encuentra git sólo de pasada, en `ENT`, `CON` y `DIS`. Ninguna
ficha de capacidad lo declara en su autoridad, ningún gate lo comprueba, ningún método lo
ejecuta y ningún handoff lo transporta
`qué aporta el candidato` poco por sí mismo: prefijo de rama por proveedor. Su valor es la
escala —67 PR, 48 ramas fusionadas— que demuestra que el modelo de `G29` funciona
`veredicto` → **P-04**

**CAND-026 · Diez ramas abandonadas** → evidencia sin destino propio
`contra` el apartado 8.3 de la directiva: *«¿qué trabajo quedó abandonado sin integrar?»*
`qué cubre ADS` nada. `G29` gobierna cómo se integra y no lleva cuenta de lo que no se integró
`veredicto` medida concreta de P-04, no candidato

### Evidencia negativa

**CAND-016 · La memoria espejada divergió** → **YA CUBIERTO** como regla · **TOOLING** como
comprobación
`contra` la regla de fuente única del índice operativo · `T147`
`qué cubre ADS` la regla, y un validador que la hace cumplir **dentro del corpus del kernel**
`qué NO cubre` la misma regla **dentro de un proyecto instalado**, entre un núcleo neutral y
sus adaptadores. Nada la comprueba allí
`veredicto` → **P-06**

**CAND-028 · Las skills duplicadas también divergieron** → **YA CUBIERTO** como regla
`el dato` cuatro skills con el mismo nombre en dos carpetas de adaptador. **Las cuatro
difieren.** Y la skill de auditoría de GAP sigue remitiendo a la memoria que CAND-016 declaró
puntero hace casi dos meses
`lo que demuestra` la deriva entre adaptadores no es un descuido: es el comportamiento por
defecto cuando nada la mira. Ocurrió dos veces, en material distinto, en el mismo proyecto,
después de haberla detectado y documentado una vez
`veredicto` → **P-06**

### El indicio de la capa

**CAND-029 · Sistema de trabajo propio copiado entre repositorios** → **CARENCIA CONCEPTUAL**
`contra` `K-1` tres capas · `K0.10` test de contaminación
`el hueco` el test de contaminación pregunta si algo sería igual de cierto en un proyecto de
otra clase, o en otro de la misma clase, o sólo aquí. **No tiene casilla** para «cierto en
nuestros proyectos y no necesariamente en los de otro»
`la evidencia disponible` cinco ficheros copiados a dos repositorios de clase técnica
distinta, divergidos entre copias, con el índice del repositorio de frontend todavía titulado
como el del backend
`por qué NO basta` los dos repositorios son un producto. La copia demuestra que se copió
`veredicto` **registrado como P-05 y no resuelto.** Ninguna capa se diseña con esto

---

## Problemas arquitectónicos registrados

Se registran con evidencia y **no se resuelven**. Ninguno autoriza a crear una capa, un tipo
canónico ni una capacidad. Entran en F3 como preguntas, no como decisiones.

### P-01 · El adaptador está nombrado en una regla y no tiene contrato

```text
DÓNDE APARECE   C2 regla de portabilidad: «los nombres de marca sólo aparecen en el
                adaptador del proyecto». K0.8 y T92 lo comprueban por su AUSENCIA en el
                kernel — nunca por su PRESENCIA en ninguna parte.

QUÉ FALTA       no es uno de los dieciocho tipos canónicos · ninguna capacidad lo posee ·
                ningún gate lo comprueba · ninguna ruta lo produce · new-project.sh no
                crea ninguno · ninguna prueba lo cubre.

EVIDENCIA       CAND-009 · 010 · 011 · 013 · 023. PesquerApp construyó uno completo a mano,
                con núcleo neutral, cuatro adaptadores, degradación explícita y prueba de
                humo, sin haber leído ADS.

POR QUÉ NO SE RESUELVE AQUÍ   decidir dónde vive un adaptador toca K-1, y K-1 está bajo
                              la misma pregunta que P-05.
```

### P-02 · ADS no tiene posición para el conocimiento que viene de fuera

```text
QUÉ FALTA       P1–P4 ordenan kernel, pack y PROFILE. Una skill de terceros, una librería
                con su propia doctrina o un preset de componentes no son ninguna de las
                tres, y no tienen posición en la precedencia.

QUÉ SÍ EXISTE   K0.11 y huella.py gobiernan el vendorizado DEL KERNEL, con hash de
                referencia y detección de fork. La figura existe; se aplica sólo a lo propio.

EVIDENCIA       CAND-015 · CAND-027. skills-lock.json vendoriza la skill de shadcn/ui con
                su origen y su hash: es K0.11 aplicado a conocimiento ajeno.

RELACIÓN        parece cercano a P-05 y NO es lo mismo. P-05 pregunta por conocimiento
                NUESTRO reutilizable. P-02 pregunta por conocimiento AJENO incorporado.
                Confundirlos sería la forma más fácil de justificar mal una capa nueva.
```

### P-03 · No hay estado de calidad persistente por área del producto

```text
QUÉ MIDE ADS    avance dentro de un item: b.9 define siete formas de avance material, y
                un freno a las tres recomposiciones sin ninguna.

QUÉ NO MIDE     el nivel en que está un área del producto, ni cómo ha cambiado. Los tres
                registros existentes tienen otro sujeto: los ledgers registran qué se
                aprendió, el journal qué pasó, las decisiones qué se decidió.

EVIDENCIA       CAND-019 · CAND-021. 47 entradas de log con puntuación antes y después por
                bloque funcional, sostenidas durante meses, y una tabla de bloques con su
                nivel vigente.

LO QUE NO SE ADOPTA   la nota de 1 a 10. esquemas/rubrica.yaml existe expresamente para
                      impedir que el juicio se reduzca a un número.

LA PREGUNTA ABIERTA   si el sujeto «área del producto» debe existir en ADS, qué lo posee,
                      y si su nivel es estado o es aprendizaje.
```

### P-04 · `G29` gobierna Git en la línea 1.3.0 y la línea 2.0 no lo ha recogido

```text
QUÉ HAY         G29 y G30 cubren buena parte del apartado 8 de la directiva: rama
                principal, aislamiento, commits, push, PR, CI, cuatro niveles de autoridad
                de merge, merge ≠ release, tags, rollback y contención.

QUÉ FALTA       propiedad. El apartado 8.2 exige una respuesta inequívoca por operación:
                quién la solicita, quién la ejecuta, quién puede bloquearla, quién verifica
                y qué evidencia queda. Hoy ninguna capacidad de la línea 2.0 declara Git en
                su autoridad, y las menciones que hay son de pasada.

Y FALTA ENTERO  el apartado 8.3: Git como memoria operativa. Qué commits ejecutaron un
                item, qué paquetes tienen rama sin integrar, qué versión contiene una
                decisión, qué commit está desplegado. CAND-026 lo mide: diez ramas sin
                fusionar y nada que las mire.

RIESGO          es el candidato más fácil de resolver mal, escribiendo una capacidad nueva
                de Git. La directiva avisa en su 8.2 de que el reparto ambiguo entre PLT,
                ENT, DSP y CON es precisamente el problema.
```

### P-05 · Sin evidencia independiente no puede demostrarse si falta una capa entre PACK y PROFILE

```text
ESTADO          ABIERTO Y DEFERIDO por decisión del Owner del 2026-08-26. No es una tarea
                pendiente: es una pregunta que la evidencia disponible no puede responder.

POR QUÉ         PesquerApp es la única fuente externa madura de esta fase, y sus dos
                repositorios son un solo producto. gym-wear queda excluido por contaminado:
                nació de una versión primitiva de ADS.

QUÉ SE PROHÍBE  diseñar la capa por intuición, y forzar los candidatos de PesquerApp para
                justificarla.

QUÉ SE REGISTRA el indicio, tal cual: CAND-029, cinco ficheros copiados entre dos
                repositorios de clase distinta, divergidos entre copias.

CUÁNDO SE REABRE  cuando exista un proyecto independiente y maduro que minar. No antes.
```

### P-06 · La deriva entre un núcleo neutral y sus adaptadores no la ve nadie

```text
LA REGLA        una verdad vive en un fichero; los demás la enlazan. Repetirla es un
                defecto de conformidad. T147 la hace cumplir DENTRO del corpus del kernel.

EL HUECO        en un proyecto instalado, un núcleo neutral consumido por varios
                adaptadores reproduce exactamente el problema, y ningún validador de ADS
                mira ahí.

EVIDENCIA       dos ocurrencias independientes en el mismo proyecto: la memoria espejada
                divergió 23 contra 32 entradas, y cuatro skills duplicadas divergieron las
                cuatro. La segunda ocurrió DESPUÉS de detectar y documentar la primera.

QUÉ SUGIERE     que la regla no basta sin comprobación, que es la misma lección que el
                repositorio ya aprendió con T147 y con las infracciones deliberadas.
```

---

## Qué entra en F3, y qué no

```text
ENTRA     los seis problemas, como preguntas con evidencia
          los cuatro candidatos de MEJORA KERNEL, para decidir su forma
          los dos de MEJORA PACK, que son los más simples y los más cerrados
          las cinco piezas de adaptador, tooling y runtime, para decidir dónde viven

NO ENTRA  ninguna capa nueva. P-05 lo prohíbe hasta que haya evidencia independiente.
          ninguna enmienda a (a), (b) o E1. Se registra la presión; no se resuelve.
          la nota de 1 a 10 y el veredicto «aprobado con observaciones»: ADS los rechaza
          por diseño, y el contraste confirma por qué.
```

**Ninguna decisión de este documento es irreversible.** Ningún fichero de
`kernel/operativo/`, `packs/` ni `docs/rediseno/` ha cambiado en F2.
