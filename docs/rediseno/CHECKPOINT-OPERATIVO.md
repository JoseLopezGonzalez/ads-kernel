# CHECKPOINT — construcción del kernel operativo

> Registro persistente de esta iniciativa. **Se actualiza antes de cada commit**, no al
> final. Basta decir «Continúa» en un chat nuevo: la siguiente acción exacta está abajo.

```text
iniciativa   contenido operativo del kernel 2.0 — pasos 1 a 6
rama         claude/kernel-operativo-equipos-roles-s4dzfq
base         (a) y (b) APROBADAS · no se modifican
alcance      contratos, esquemas, plantillas, roles, prompts, métodos, circuitos,
             criterios, checkpoints, gates, validadores, pruebas y packs
fuera        runtime · dispatcher · gym-wear · pack ERP · secciones (c)-(i) abstractas
```

## Bloque actual

```text
LOS SEIS PASOS ESTÁN IMPLEMENTADOS. La iniciativa está TERMINADA.

BLOQUE 0   esquemas, validadores e índice          TERMINADO
BLOQUE 1   circuito Owner → item (paso 1)          TERMINADO
BLOQUE 2   contrato equipo/rol/agente/método       TERMINADO
BLOQUE 3   sistema de excelencia de Diseño         TERMINADO
BLOQUE 4   equipo de Diseño materializado          TERMINADO
BLOQUE 5   demás capacidades                       TERMINADO
BLOQUE 6   packs web-app · mobile-app · wear-os    TERMINADO
REVISIÓN   adversarial del conjunto                TERMINADA, con limitación declarada

FUERA DE ALCANCE, por instrucción del Owner y sin empezar:
runtime · dispatcher · gym-wear · pack ERP · secciones (c) a (i) en abstracto
```

## Terminado

- Lenguaje canónico y sus diecisiete esquemas — `kernel/operativo/esquemas/`
- Validador estructural `ads_lint.py` y sus reglas — **ejecutado, en verde**
- Generador determinista del registro de pruebas — `registro_pruebas.py`
- Índice y regla de fuente única — `kernel/operativo/00-INDICE.md`
- Registro honesto de estado de pruebas — `kernel/operativo/pruebas/REGISTRO.md`
- Decisiones, decisiones del Owner y contradicciones — `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`
- Packs 1.3.0 retirados a `packs/legacy-1.3.0/` con su carta de retirada

**Bloque 1 — paso 1 completo**

- Taxonomía de nueve clases de entrada — `entrada/01-TAXONOMIA.md`
- Circuito de catorce estaciones con sus caminos de vuelta — `entrada/02-CIRCUITO.md`
- Catorce formas de conversación, con árbol de decisión ordenado — `entrada/03-FORMAS.md`
- Escala de incertidumbre, tabla de confirmación, umbral y margen de anclaje
- Seis escenarios completos, incluido el de referencia — `entrada/05-ESCENARIOS.md`
- Capacidad `ENC` con tres roles, seis métodos, tres prompts y tres composiciones
- Política de agentes y modelos, neutral de proveedor, con 21 perfiles — `contratos/C2`
- Plantilla de encuadre rellenable — `plantillas/ENCUADRE.md`
- T75–T85 definidas

**Bloque 2 — paso 2 completo**

- C1 los siete conceptos y los 28 campos del contrato de rol
- C2 agentes, perfiles y modelos (escrito en el bloque 1)
- C3 el método ejecutable: 17 elementos y 7 reglas
- C4 materialización: algoritmo de 7 pasos, ampliación y retirada
- C5 handoff y devolución, con la distinción rechazo/devolución
- Plantillas CHECKPOINT, DEVOLUCION, DICTAMEN
- `comprobar_contratos.py`: T86–T92 **EJECUTADAS Y SUPERADAS**, con salida registrada

**Bloque 3 — sistema de excelencia de Diseño**

- Dos gates independientes: `gate:usabilidad` y `gate:excelencia-visual`
- Dos rúbricas: seis ejes de usabilidad, nueve de excelencia, con evidencia por eje
- Memoria de diseño: doce secciones con autoridad, actualización y qué significa vacía
- Escala de novedad N0–N4, con exploración mínima y estaciones por nivel
- Ciclo de calidad de trece estaciones con nueve retornos declarados
- Fidelidad: ocho cosas que no se simplifican, tres veredictos, camino de imposibilidad

**Bloque 4 — equipo de Diseño materializado**

- Capacidad DIS con doce campos y contrato de veto de seis campos
- Once roles con los 28 campos del contrato común
- Seis métodos ejecutables: Fundacion, Reconstruccion, Evolucion, CriticaVisual,
  RevisionDeFidelidad, ValidacionDeUso
- Once prompts operativos
- Diez matrices de composición, con independencia declarada de forma comprobable
- T93–T99 definidas

**Bloque 5 — las trece capacidades restantes**

- PRD ARQ DOM CON VER ENT USO INV SEG PLT APR DSP SIS, cada una con ficha de doce
  campos, gate propio, roles con los 28 campos, métodos ejecutables, prompts y
  composiciones
- Contratos de veto de seis campos en DOM, SEG, VER y DIS
- Circuitos concretos para las diez rutas de b.16, más los dos que el trabajo real
  produce y (b) no numera
- Diecisiete handoffs declarados con qué se comprueba al recibir y qué evidencia
  acompaña a cada devolución
- T100–T121 definidas

**Bloque 6 — los tres packs**

- `packs/00-QUE-ES-UN-PACK.md`: qué puede y qué NO puede hacer un pack
- `web-app`, `mobile-app` y `wear-os`, cada uno con su bloque `ads:pack`, sus
  restricciones, dos roles especializados, tres gates adicionales, matriz de
  entornos, antipatrones, especialización de Diseño y ejemplos de composición
- `packs/COMPOSICION.md`: cuatro reglas de precedencia, cinco tipos de conflicto
  detectables y las tres combinaciones previstas en concreto
- `comprobar_packs.py`: T131 y T132 **EJECUTADAS Y SUPERADAS**
- T122–T133 definidas

## En revisión

Nada en revisión. La revisión adversarial del conjunto está hecha y sus cinco hallazgos
corregidos: [`REVISION-ADVERSARIAL.md`](REVISION-ADVERSARIAL.md).

**Deuda declarada:** el agente revisor independiente terminó sin completarse por un límite
de gasto de la cuenta, y la revisión la ejecutó finalmente quien escribió el material. Una
lectura verdaderamente independiente sigue pendiente, y es la limitación más importante de
esta entrega.

## Decisiones pendientes del Owner

Agrupadas en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` §2 — **ninguna bloquea**.
La única con contenido normativo es **C1** (¿`ENC` es capacidad propia o función de `DSP`?).

## Pruebas

```text
T01-T74   contrato-definido, salvo tres parciales en validador-implementado
T75-T85   contrato-definido (11)
T86-T92   PRUEBA SUPERADA (7), con evidencia en pruebas/evidencia/
T93-T99   contrato-definido (7)
T100-T121 contrato-definido (22)
T122-T133 contrato-definido (10) + PRUEBA SUPERADA (2)
ads_lint  EJECUTADO y en verde sobre 298 bloques canónicos
comprobar_contratos  EJECUTADO, 7/7 superadas
comprobar_packs      EJECUTADO, 2/2 superadas
TOTAL     59 escenarios: 50 contrato-definido, 9 PRUEBA SUPERADA
```

## Siguiente acción exacta

> **La iniciativa está terminada.** La siguiente acción NO es de esta iniciativa: es el
> piloto de gym-wear, y su punto de partida exacto está más abajo.
>
> Si el Owner quiere continuar aquí, las dos únicas cosas pendientes son:
> 1. una revisión adversarial por un lector independiente que no escribió el material
> 2. las decisiones agrupadas en `DECISIONES-Y-CONTRADICCIONES.md` §2, ninguna bloqueante


---

## Punto exacto desde el que empieza el piloto de gym-wear

```text
1  INSTALAR       ./tooling/new-project.sh gym-wear wear-os,mobile-app
                  copia kernel/ con su directorio operativo, y los dos packs con su
                  fichero de composición

2  PROFILE        rellenar PROFILE.md, y AÑADIR lo que la composición de packs exige:
                    · matriz de relojes y de dispositivos reales
                    · el arbitraje de todo conflicto de materia entre wear-os y mobile-app
                    · los valores que la precedencia P1 resolvió, con cuál ganó
                    · la decisión de independencia: ¿el reloj es autónomo, acompañante o mixto?

3  PRIMER ITEM    NO empezar por una pantalla. Empezar por una frase del Owner, entrando
                  por ENC con el prompt de ENC/interlocutor cargado tal cual

4  PRIMER ANCLAJE ENC/anclaje sobre un repositorio vacío devolverá
                  `no_existe_y_se_creia: no existe memoria de diseño`. Eso es correcto y
                  significa nivel de novedad N4 → DIS/Fundacion, sin techo de sesiones

5  LO QUE HAY     el escenario A de entrada/05-ESCENARIOS.md es exactamente ese recorrido,
   QUE VIGILAR    con dos items enlazados. Si el sistema produce en su lugar una tarea de
                  estilos, el kernel operativo ha fallado en su primer uso real y hay que
                  registrarlo como aprendizaje, no corregirlo a mano

6  QUÉ SE APRENDE la primera ejecución convertirá varias pruebas de «contrato definido» a
                  «prueba ejecutada». Ese cambio de estado, con su evidencia, es el
                  resultado más valioso del piloto — más que la aplicación
```

**No se empieza el runtime.** El piloto se ejecuta con agentes siguiendo los métodos a mano;
lo que el runtime tendrá que automatizar se descubre haciéndolo, y ése es el material del
que nacerán los items `SIS` de la siguiente iteración.
