# `F6` · GATE ÚNICO E INDEPENDIENTE DE CERTIFICACIÓN FINAL · 2026-09-03

**Qué es este documento.** El REGISTRO del gate de certificación de `F6`: su objeto congelado,
su manifiesto, los dos dictámenes independientes, la adjudicación y las cuatro declaraciones.
Es **DERIVADO**: no crea autoridad, no aprueba nada y **no certifica nada** —precisamente
porque el veredicto fue que no se puede certificar—.

**Qué NO es.** No es una tanda de corrección. **Durante este gate no se corrigió ni un byte de
código, de pruebas ni de documentación sustantiva**, y los hallazgos quedan REGISTRADOS y NO
APLICADOS, que es lo que el encargo mandaba. No es la sede del estado de las fases: ésa es
[`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6, **que este gate no
modifica porque su veredicto no la mueve**: `F6` sigue `INICIADA · EN CURSO` y PesquerApp sigue
`BLOQUEADA`.

---

## 1 · Objeto congelado

```text
SHA auditado     5cc3cb7b5417a461057d5045187b2fff4f2fdc8c
TREE             b5519230b586b70ff508339ea59bef2e933dfae7
referencia       review/f6-complete-before-certification-20260903
rama del gate    gate/f6-certificacion-final-20260903, creada DESDE ese SHA
fd633383…        NO es ancestro (verificado)
intérprete       Python 3.12.14 · PyYAML 6.0.2
```

**Precondiciones estructurales, todas verificadas antes de crear ningún agente:** árbol limpio ·
historia lineal · sin upstream · sin operaciones Git pendientes · `F4c` CERRADA · `F5` CERRADA ·
`F6` INICIADA·EN CURSO · PesquerApp BLOQUEADA.

**Línea base reproducida por el coordinador y, por separado, por los TRES agentes**, el segundo
y el tercero en rutas de checkout distintas:

```text
31/31 validadores en verde · 31 evidencias publicadas · 0 problemas
535 casos de F6 en 15 baterías (592 totales − 57 de workspace)
escenarios 15/15 · 25/25 · 24/24
84 negativos detectados · 0 NO detectados
huella 54256290d7cbf26a
git status --porcelain vacío ANTES y DESPUÉS de la corrida
cero skips ejecutados en las 31 evidencias
```

> **La línea base de la candidata es EXACTA**, y la evidencia es reproducible byte a byte fuera
> de su checkout. Los tres agentes lo confirmaron por separado. Se dice aquí con la misma
> claridad que lo negativo, porque un gate que sólo publica lo que falla miente por omisión.

## 2 · Los tres agentes, y su separación

| marca | papel | eje | vio los dictámenes ajenos |
|---|---|---|---|
| **SONDA** | revisor 1 | ejecución y resistencia | **no** |
| **PLOMADA** | revisor 2 | contratos y completitud | **no** |
| **ESCUADRA** | adjudicador | juicio propio | **sólo después de que los dos cerraran** |

Los tres son nuevos: ninguno participó en ninguna implementación ni en ningún gate anterior de
este expediente. **Ninguno escribió un byte en el repositorio**: `HEAD`, `TREE`,
`git status --porcelain` y `git reflog` se comprobaron al abrir y al cerrar cada trabajo, y
salieron idénticos las tres veces. Todos los ataques se hicieron sobre clones desechables.

## 3 · Cobertura, y por qué el gate cae por ella

**PLOMADA:** `ASIGNADO − LEÍDO = ∅`. Quince fuentes íntegras con SHA-256, primera y última
sección sustantiva y dos anclas separadas; rangos exactos declarados para `11-ARQ` §19 y §20
—las dos íntegras—, `CHECKPOINT-ADS-NEXT`, y `O18`, `O20`, `O24` y `O25`.

**SONDA:** `ASIGNADO − LEÍDO ≠ ∅`, **declarado por ella misma**. Sin abrir:

```text
CONTRATO-CICLO-Y-MACROCIRCUITOS.md   338 líneas   sólo grep
CONTRATO-ADAPTADOR.md                112          sólo grep
CONTRATO-RAIZ-EXTERNA.md             172          sólo grep · uno de los TRES de g.17
11-ARQ §8.1-§8.4 (6560-7378)                      no leída
11-ARQ §9.6 ENTERA (7378-8075)                    rango asignado EXPRESAMENTE
b-RECORRIDO b.16 (835-1144)                       fuente de la derivación de rutas
CONTRATO-CONTENCION.md 1-94                       no leída
```

El adjudicador la juzgó **real, material y no subsanable**, con tres razones: alcanza a
componentes sustantivos modificados en los tres cortes de `F6` —para los que el manifiesto
prohíbe la cobertura histórica delegada—; **tuvo consecuencia demostrable**, porque
`CONTRATO-RAIZ-EXTERNA.md` contiene la cláusula «*el commit y su `tree` … la atestación queda
atada a los DOS*», que es exactamente la obligación cuya cobertura de prueba resultó defectuosa
(`E-07`), y entró por el otro eje por reparto y no por diseño; y porque §9.6 —sede de las filas
`X-S` de la `FASE 0` que `F6-F` debe demostrar— no entró ni por lectura ni por derivación.

La regla del manifiesto §8 se aplica sin atenuarla: **el gate continúa técnicamente y se declara
NO VÁLIDO para certificar `F6`**.

## 4 · Las tres restas, derivadas por el adjudicador

**`A` · obligaciones internas SIN implementación — NO VACÍA (7)**

```text
A1  C4 «Cuántos agentes por rol» · cardinalidad y semántica no derivadas de la composición
A2  11-ARQ §19 CONTRATO 1    · AFIRMACIONES sigue siendo lista literal
A3  11-ARQ §19 CONTRATO 1bis · el censo de perfiles no se publica
A4  11-ARQ §19 CONTRATO 2    · T152 no barre toda sede que publique versión
A5  11-ARQ §19 D104          · cero instancias de <CAP>:revision, cero validadores
A6  b.12 paso 5   · criterios (b) grado de salida y (c) antigüedad de espera
A7  b.12 inanición · tiempo_listo, postergaciones, adelantado_por
```

**`B` · implementaciones SIN prueba capaz de fallar — NO VACÍA (6)**

```text
B1  el ORDEN de los pasos 8 y 9 de estado/motor.py          verde bajo inversión fiel
B2  exigir_vinculo · mitad TREE                             38/38 verde
B3  exigir_vinculo · mitad COMMIT                           38/38 verde
B4  V6-12 · degradación con commit_de_nacimiento=None       58/58 verde
B5  procedencia del sys.path en el camino productivo --repo 38/38 verde
B6  C4 · la declaración prohibida de varios agentes         15/15 y 30/31, sólo la huella roja
    + el instrumento: firma_de_exito 'OK' no distingue 'OK (skipped=N)'
```

**`C` · obligaciones SIN trazabilidad hasta evidencia — NO VACÍA (4)**

```text
C1  criterio B3 del plan · «la acepta el Owner» · no consta acto · no existe O26
C2  §19 CONTRATO 1, 1bis, 2 y D104 ausentes del universo de la resta y del inventario F6-H
C3  04-CONTRATOS-TECNICOS.md · la ÚNICA SEDE del estado de construcción es falsa en los dos
    sentidos y se contradice consigo misma; docs/f6/00-ESTADO se declara DERIVADO de ella
C4  la matriz registra en F6-B un «límite de anfitrión» donde lo que falta es un acto del Owner
```

## 5 · «Cuántos agentes por rol» — la cuestión que el encargo marcó como crítica

El corte anterior la rotuló «DEUDA POSTERIOR, parcialmente cerrada por el paso 1». El gate la
resolvió con sus cinco puntos, y **la rechaza**:

1. **Obligación exacta:** `C4-MATERIALIZACION.md`, «Cuántos agentes por rol»: «*VARIOS AGENTES
   cuando se cumple alguna, **y la composición lo declara** … En los tres casos se declara QUIÉN
   INTEGRA el resultado*» y «***Varios agentes sin integrador declarado está prohibido***».
2. **Es INTERNA a `F6`:** `C4` es contrato transversal, `equipos.materializar()` implementa sus
   siete pasos, y su sede es `kernel/operativo/`, que sólo `F6` edita.
3. **Medida por ejecución sobre el corpus real**, en las TRES composiciones que declaran varios
   agentes —`dis-proyecto-nuevo` con `DIS/diseno-visual` «2 o 3, uno por dirección explorada» y
   `DIS/investigacion-visual` «1 o 2 repartidos por territorio», y `dis-feature-visual` con
   `DIS/diseno-visual` «1 o 2 en competencia declarada»—: se materializa **UN** agente,
   `reparto_de_agentes: []`, sin error, sin aviso y sin `esperando-capacidad`. El registro
   durable queda **internamente contradictorio**: publica «2 o 3» junto a un agente único, y
   `C4` paso 7 dice que ese registro «es lo que convierte la materialización en auditable».
4. **«Deuda posterior» RECHAZADA:** el adjudicador barrió el corpus entero y **no existe ninguna
   fase posterior a `F6`**. `03-GOBIERNO` §6 conoce `F4c`, `F5`, `F6` y luego PesquerApp; §7 fija
   la cadena `F6 → certificación → adopción` y añade «no admite atajos». **No hay a quién
   diferirlo.**
5. **La excusa, desmontada por medición:** el campo `agentes` tiene **99 valores en 22 formas**, y
   **exactamente tres** declaran más de uno. No es texto libre: es un vocabulario cerrado. Y el
   integrador **ya está declarado** en las tres composiciones —`DIS/direccion-artistica`—; el
   runtime no lo lee.

**Y el sabotaje que lo cierra:** poner `agentes: "7 repartidos por artefacto, sin integrador"`
—literalmente lo que `C4` llama prohibido— deja la batería `agentes` en **15/15 OK** y la suite
en 30/31, **y el único rojo es la huella**, que sólo dice que el kernel cambió y saltaría igual
con cualquier edición legítima. **Ninguna propiedad semántica lo detecta.**

## 6 · Hallazgos ACEPTADOS

| id | hecho | clase | severidad |
|---|---|---|---|
| `E-01` | `C4` «cuántos agentes por rol»: cardinalidad y semántica no derivadas de la composición; declaración prohibida indetectable | defecto INTERNO | **BLOQUEANTE** |
| `E-02` | §19 `CONTRATO 1` no cerrado, con su condición de cierre escrita e incumplida | defecto INTERNO | **BLOQUEANTE** |
| `E-03` | §19 `CONTRATO 2` no cerrado | defecto INTERNO | **BLOQUEANTE** |
| `E-04` | §19 `D104` no materializado: cero instancias, cero validadores | defecto INTERNO | **BLOQUEANTE** |
| `E-05` | §19 `CONTRATO 1bis` no cerrado | defecto INTERNO | **BLOQUEANTE (menor)** |
| `E-06` | `b.12`: dos de cuatro criterios de orden y uno de cuatro campos de inanición, sin declarar y sin prueba | defecto INTERNO | **BLOQUEANTE** |
| `E-07` | `exigir_vinculo`: ninguna de las dos mitades tiene cobertura individual | defecto INTERNO | ALTA · resta `B` |
| `E-08` | el orden de los pasos 8/9 de `motor.py` sin prueba: invertirlo deja el almacén irrecuperable con las tres baterías en verde | defecto INTERNO | ALTA · resta `B` |
| `E-09` | `V6-12` degrada en silencio con `commit_de_nacimiento=None` | defecto INTERNO | ALTA · resta `B` |
| `E-10` | procedencia del `sys.path` no probada en el camino productivo `--repo` | defecto INTERNO | MEDIA · resta `B` |
| `E-11` | criterio `B3` del plan sin satisfacer: no consta acto del Owner aceptando la raíz externa | **EXTERNO**, con propietario y condición expresos (`O18`) | **BLOQUEA LA CERTIFICACIÓN** |
| `E-12` | `04-CONTRATOS-TECNICOS.md`, única sede designada del estado de construcción, desmentida por el árbol y contradictoria consigo misma | defecto INTERNO | **BLOQUEANTE** |
| `E-13` | `F6-H` declarado completo sobre un universo que omite cuatro obligaciones `FASE F6` de su propia sede | defecto INTERNO | **BLOQUEANTE** |
| `E-14` | `firma_de_exito: 'OK'` casa con `'OK (skipped=N)'`; 17 `skipTest` sin contar ni publicar | defecto INTERNO del instrumento | MEDIA |
| `E-15` | `adaptadores.CapacidadNoSoportada` escapa de `main()` como traza cruda con rutas absolutas | defecto INTERNO | BAJA |
| `E-16` | ningún punto ejecutable puede activar la contención construida | defecto de completitud funcional, INTERNO | MEDIA, no bloqueante |
| `E-17` | custodia productiva de claves | **DEUDA EXTERNA** declarada (`O25` §5) | no bloqueante hoy |
| `E-18` | `cgroup-v2` no ejercitable; identidad de sistema no disponible; falso rojo latente | **LIMITACIÓN DE ANFITRIÓN** | informativa |

## 7 · Hallazgos RECHAZADOS o CORREGIDOS — el adjudicador no copió a nadie

```text
SONDA · S11b, el relato        PARCIALMENTE FALSO en el método. Dos de las tres inversiones
                               SÍ se ponen rojas. Sólo la que respeta el significado de cada
                               punto de fallo pasa en verde. El hallazgo sobrevive; el relato
                               exageraba la ceguera del aparato
SONDA · «recuperar rc=1»       FALSO: es rc=0. Corregido en la dirección DESFAVORABLE: un
                               guion con && leería «recuperado»
SONDA · S-02, la jerarquía     IMPRECISA: hay DOS clases homónimas `CapacidadNoSoportada`; la
                               del runtime SÍ se captura. La conclusión se salva por la del
                               adaptador
SONDA · FD-5 como deuda        RECLASIFICADO: las obligaciones escritas de FD-5 y del
externa                        CONTRATO-CONTENCION §5 están CUMPLIDAS. Lo que queda es un
                               defecto interno de completitud funcional
PLOMADA · «dis-superficie-     FALSO: la tercera composición es `dis-feature-visual`.
premium»                       El hecho —tres filas— es correcto
PLOMADA · «101 valores, 98     CARDINALES FALSOS: son 99 valores y 22 formas. El dato
de forma 1, 3 plurales»        operativo —exactamente tres— es exacto
PLOMADA · «21 skipTest»        Son 17 en las baterías del runtime
```

> **Y la nota de método del adjudicador, que se conserva porque vale más que el veredicto:**
> «*Los dos revisores se equivocaron en cosas distintas y ninguno merece ser copiado sin
> verificación.*» El gate no resolvió por mayoría: reprodujo personalmente cada razón capaz de
> mover el veredicto.

## 8 · Lo que este gate SÍ puede afirmar

Se dice porque un registro que sólo publica lo que falla no describe el objeto:

```text
· la suite da 31/31 con 0 problemas, 592 casos y CERO skips ejecutados, y la evidencia es
  reproducible byte a byte en otro checkout, con porcelain=0 antes y después
· el motor de estado durable resiste corte REAL en las ventanas del protocolo, con revisión
  1-o-2 y NUNCA intermedia, y bloqueo entre escritores reales: 40 carreras, cero dobles éxitos
· la serialización multimáquina NO descansa en el flock, demostrado por NEUTRALIZACIÓN con
  control positivo: 50 carreras, cero dobles confirmaciones
· los diecinueve V6-* tienen correspondencia ejecutada e inequívoca, incluidos los tres que la
  candidata declara no citados por nombre
· V6-15 deriva su conjunto de la sede y CRECE SOLO al publicar un árbol nuevo en una copia
· V6-18 da falsos_verdes = 0 y falsos_rojos = 0 sobre 24 controles
· los SEIS bloqueantes de la auditoría anterior están cerrados con prueba capaz de ponerse roja
· la contención fuerte, CUANDO SE LE DA POLÍTICA, alcanza 0 supervivientes sobre tres
  generaciones reales con setsid, y el backend débil deja escapar 2 de 3, que es el control que
  impide presentar el débil como fuerte
· las once entradas de la tabla de sabotaje son reales y alcanzan su propiedad, y el propio
  mecanismo resiste dos meta-ataques
```

## 9 · Lo que este gate NO puede afirmar

```text
· que F6-H esté completo: su universo omite cuatro obligaciones FASE F6 de su propia sede
· que C4 esté implementado en su sección de cardinalidad
· que las propiedades de la resta B estén PROBADAS: están implementadas y sin prueba capaz de fallar
· que el estado de construcción de F6 esté publicado con verdad en NINGUNA sede canónica
· que el criterio B3 del plan esté satisfecho
· que «los 24 pasos del e2e pasan» signifique gran cosa: los TRES escenarios quedaron VERDES
  bajo la inversión de los pasos 8 y 9 que deja el almacén irrecuperable. NO son red de seguridad
· que la evidencia publicada distinga un anfitrión que ejerció las propiedades de uno que las saltó
```

## 10 · LAS CUATRO DECLARACIONES

```text
A · VALIDEZ         EL GATE NO ES VÁLIDO
                    Motivo: ASIGNADO − LEÍDO ≠ ∅ para el revisor 1, con seis fuentes o
                    rangos sin abrir, entre ellos CONTRATO-RAIZ-EXTERNA.md —uno de los tres
                    de g.17 y elemento expreso de su lote—, CONTRATO-CICLO-Y-MACROCIRCUITOS.md
                    —la familia donde el tercer corte concentró el cambio— y 11-ARQ §9.6
                    entera, rango asignado explícitamente

B · COMPLETITUD     F6 NO ESTÁ COMPLETAMENTE IMPLEMENTADA
                    Pendientes internos: A1–A7 de la resta A, más E-12 y E-13

C · CERTIFICACIÓN   F6 NO CERTIFICADA
                    Razones finitas: (1) el gate no es válido · (2) la resta A no está vacía
                    · (3) la resta B no está vacía · (4) la resta C no está vacía · (5) hay
                    bloqueantes internos vivos, y no puede certificarse F6 con una parte
                    interna de C4 parcialmente cerrada · (6) el criterio B3 no está satisfecho

D · PesquerApp      PESQUERAPP SIGUE BLOQUEADA
                    Derivado, no presupuesto: O20 §8 · O24 §4 · 03-GOBIERNO §6 L174 y §7
                    · 11-ARQ §18 nodo 9 → 8 · O25 §6. La precondición es la CERTIFICACIÓN, y
                    no se emite aquí. No queda siquiera «técnicamente desbloqueable»: ese
                    estado exigiría que sólo faltara un acto formal sobre un objeto completo,
                    y faltan siete obligaciones internas de implementación
```

## 11 · El acto del Owner, nombrado y NO ejecutado

Aun cerrados los pendientes internos y emitido un gate válido, la certificación seguiría siendo
insuficiente sin un acto que **sólo el Owner** puede emitir, porque `O18` lo reserva y el
criterio `B3` de `05-PLAN` §2.2 lo exige:

> Una **resolución nueva del Owner** —que por la numeración append-only de la sede sería `O26`—
> inscrita en [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md), que
> **ACEPTE O RECHACE expresamente la RAÍZ EXTERNA DE CONFIANZA de `F6`**, en ejercicio de la
> autoridad que `O18` le reserva —«*el Owner conserva la autoridad de aceptar o rechazar la raíz
> externa*»— y que `F6-B` declara **INDELEGABLE**, para satisfacer el segundo conyunto del
> criterio `B3` —«*la raíz externa existe, **la acepta el Owner**, y su ejecutor NO comparte
> identidad de escritura con el runtime*»—, que `O25` §6 dejó expresamente sin emitir.

**Este gate no lo inventa, no lo redacta y no lo ejecuta. Lo nombra.**

## 12 · Lo que este gate NO hizo

```text
NO CORRIGIÓ    ni un byte de código, de pruebas ni de documentación sustantiva. Los dieciocho
               hallazgos quedan REGISTRADOS y NO APLICADOS
NO CERTIFICÓ   nada
NO CERRÓ       F6, que sigue INICIADA · EN CURSO en su sede canónica
NO MOVIÓ       ninguna resolución del Owner, ningún documento histórico, ningún estado de fase
NO ABRIÓ       ningún ciclo posterior, ningún segundo gate, ni PesquerApp
```
