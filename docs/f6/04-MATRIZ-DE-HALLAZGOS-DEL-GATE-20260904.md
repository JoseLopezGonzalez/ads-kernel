# `F6` · MATRIZ DE LOS HALLAZGOS DEL GATE DEL 2026-09-04, ANTES DE TOCAR NADA

**Qué es.** La clasificación completa de los VEINTIDÓS hallazgos que el gate publicado en
`review/f6-certificacion-final-insuficiente-20260904` dejó registrados y NO aplicados, más los
dos externos que arrastra el expediente. **Se escribe ANTES de editar una sola línea de
código**, que es lo que el encargo ordena, y su función es que la disposición de cada uno sea
una decisión declarada y no un residuo de lo que se acabó tocando.

**De dónde sale.** De la ADJUDICACIÓN ÍNTEGRA —§5 de
[`03-GATE-DE-CERTIFICACION-FINAL-20260904.md`](03-GATE-DE-CERTIFICACION-FINAL-20260904.md)—,
leída entera, y no del informe resumido. Donde el adjudicador matizó o agravó a un revisor,
manda el adjudicador.

**Reglas que esta matriz aplica, y ninguna es negociable.** Se reproduce cada hallazgo antes
de corregirlo · no se corrige lo que no reproduzca · lo que resulte falso se explica y se
rechaza · **ningún interno se convierte en externo** · no se edita ningún documento histórico
de gate · `ADJ-O1` y `ADJ-O2` quedan resueltos NORMATIVAMENTE por `O27`, no reescribiendo
`O23`–`O26` · `E-17` permanece EXTERNA · `E-18` permanece LIMITACIÓN DE ANFITRIÓN.

---

## 1 · Los tres BLOQUEANTES

| id | severidad | sede | hecho reproducido por el adjudicador | alcance real | remedio adjudicado | propietario · fase | clase | acción autorizada | prueba capaz de fallar |
|---|---|---|---|---|---|---|---|---|---|
| **`ADJ-B1`** | BLOQUEANTE | `runtime/estado/migracion.py:178` contra `estado/motor.py:558` | de las CINCO llamadas a `_publicar_revision` del árbol, una no pasa el `testigo` que `E-08` hizo obligatorio. Sobre un almacén heredado GENUINO —sin `FORMATO.json`, sin diario, sin `REVISION.json`—: `TypeError` NO tipado, traza con SIETE rutas del anfitrión, `EXIT=1`, stdout vacío; 2ª y 3ª llamada → `ESTADO_CORRUPTO` | **mayor que la línea**: con el diario ya fundado y sin `REVISION.json` la rama no se vuelve a entrar, y el almacén queda inmigrable **incluso con el `testigo` puesto**. La única prueba fabrica el heredado con `os.remove(FORMATO.json)` sobre uno ya inicializado, y **nunca entra en la rama rota** | la línea, **el fixture** y **un camino de recuperación** para los almacenes ya rotos | autoría de `F6`, eje de estado durable · `F6` | **INTERNO** | CORREGIR ENTERO | migración heredada REAL, caída antes y después del testigo, testigo ausente y corrupto, repetición, formato futuro, recuperación, CLI, y sabotaje que vuelva a omitir el argumento |
| **`ADJ-B2`** | BLOQUEANTE | `kernel/operativo/raiz-externa/` ENTERO · alcance de `T306` en `test_integridad_y_evidencia.py:49` | `PYTHONPATH` envenenado → `verificador.py capacidades` publica `{}` con **código 0**; `instalar.py` escribe manifiesto de **3 bytes** (sano: 6 734) e instala 41 ficheros con **código 0**; aguas abajo `KeyError: 'ficheros'` con cuatro rutas del anfitrión. `grep` de purga sobre todo el paquete: **CERO líneas** | es el MISMO defecto que el árbol declara cerrado para los cinco `ads_*.py`, vivo en la única pieza que `O26` §1 juzga. `T306` cubre cinco ejecutables y ninguno más | llevar el prólogo `E-10` completo a `verificador.py` e `instalar.py`, **y ampliar `EJECUTABLES` de `T306`**, que es lo que impide que vuelva | autoría de `F6`, eje de raíz externa · `F6` | **INTERNO** | CORREGIR ENTERO, por INVENTARIO MECÁNICO y no por lista | sano, `PYTHONPATH` envenenado, módulo homónimo, repo A desde repo B, `--repo` ausente, instalación parcial, y sabotaje de la purga |
| **`ADJ-B3`** | BLOQUEANTE | `runtime/admision/perimetro.py:394` · `04-CONTRATOS` §6 · `03-GOBIERNO` §2 | `actual.startswith(anterior)` contra el commit de NACIMIENTO: prefijo de **14 395 de 42 181 bytes = 34,1 %**. `O17`, `O18` y `O19` protegidas; `O20`…`O26` FUERA. Mutar la condición 5 de `O26` y confirmar → `hallazgos=0`. **Borrar `O20`–`O26` enteras y sustituirlas por «F6 QUEDA CERTIFICADA SIN CONDICIONES» → `hallazgos=0`**, con la sede perdiendo el 66 % de su contenido | **el acto que da competencia a este gate se puede reescribir para que diga lo contrario, y el verificador calla.** Nada más lo caza: la huella cubre `kernel/`, `packs/` y `tooling/`, **no `docs/`**. Ninguna prueba del corpus muta contenido POSTERIOR al nacimiento | igualdad sobre el prefijo común **y sólo-adición sobre el resto**, con prueba que mute una entrada posterior al nacimiento y exija ROJO. **`O27` §3 lo eleva a NORMA** | `PLT` implementa · `SIS` propietario · `F6` | **INTERNO** | CORREGIR ENTERO, por ENTRADA CERRADA | los siete controles de `O27` §3 más el ataque de borrado `O20`–`O27` |

## 2 · Los tres GRAVES

| id | severidad | sede | hecho reproducido | alcance real | remedio adjudicado | propietario · fase | clase | acción autorizada |
|---|---|---|---|---|---|---|---|---|
| **`ADJ-G1`** | GRAVE | `derivar-universo-obligatorio.py`, modo `--obligaciones` | TRES vías con `exit 0`: cambiar la fase de `F-07` (58→57, el id desaparece), retirar la fila `F-10`, retirar el bloque `CONTRATO 2` (guarda `< 4` con CINCO reales = una unidad de holgura) | `F-nn` no tiene suelo y el cliquet existente es SÓLO del universo de FUENTES. `O26` §5 convierte estas restas en criterio de certificación | cliquet propio para obligaciones; publicar lo que se cae de CADA componente; derivar el suelo de §19 en vez de escribirlo | `PLT` · `F6` | **INTERNO** | CORREGIR LA CLASE, no las tres instancias |
| **`ADJ-G2`** | GRAVE | bloques `ads:escenario` · `validadores/registro_pruebas.py:57,76` | ningún validador contrasta el `estado:` declarado contra la evidencia. **Divergencia VIVA hoy**: `T273` publicado `PRUEBA FALLIDA` mientras su evidencia dice `SUPERADA` y su prosa «queda en VERDE», con 34/34 validadores verdes | `REGISTRO.md` escribe «ninguna prueba sube de estado por argumento»: esa regla NO está mecanizada | derivar el `estado` de la evidencia, o contrastar el declarado contra la salida del validador que la prueba nombra | `PLT` implementa · `SIS` propietario · `F6` | **INTERNO** | CORREGIR ENTERO |
| **`ADJ-G3`** | GRAVE | `04-CONTRATOS-TECNICOS.md` §5.3 L326-329 · §5.4 L336-337 · §6 L343 y L382 · §4 L274 | el documento que se declara **la ÚNICA SEDE** afirma en cuatro secciones que no existen los adaptadores, el verificador de admisión, la raíz externa y el sellado, **y su propia §1.1 los declara CONSTRUIDOS**. `06-DEUDA` §6 L197 y `05-PLAN` L6 lo repiten | tercera recurrencia del mismo defecto en el mismo documento | que §5.3, §5.4, §6 y §4 **REMITAN a §1** en vez de declarar estado | `SIS` · `F6` | **INTERNO** | BARRIDO DE CLASE sobre todo el documento y las demás sedes vivas |

## 3 · Los once MEDIOS

| id | sede | hecho reproducido | remedio | propietario | clase | acción |
|---|---|---|---|---|---|---|
| **`ADJ-M1`** | `ads_admision.py:388` | `censo-formulas` sobre el propio candidato: `segundas definiciones: 7 · ok: no · EXIT=1`, mientras su prueba está verde porque censa OTRO conjunto | alinear el conjunto censado por la orden con el que la prueba mide, o declarar la diferencia | autoría `F6` | INTERNO | CORREGIR |
| **`ADJ-M2`** | los cinco `ads_*.py` | los cinco llevan el comentario «`E-10` · la PROCEDENCIA se PUBLICA» y **sólo `ads_admision.py` tiene una orden que la publique**, medido en las cinco tablas `ORDENES` | publicarla en los cinco, o retirar el comentario de los cuatro que no la publican | autoría `F6` | INTERNO | CORREGIR |
| **`ADJ-M3`** | `CONTRATO-ESTADO-DURABLE.md` §3 L106-107 | afirma que las tres E2E «ya no pueden seguir verdes sobre un almacén irrecuperable», y **ninguna de las tres inyecta `entre-el-paso-8-y-el-9`**, que es el único punto que produce ese estado | o lo inyectan, o el contrato deja de afirmarlo | autoría `F6` | INTERNO | CORREGIR |
| **`ADJ-M4`** | `derivar-universo-obligatorio.py`, `ROTULOS_DE_RESTA` | `A=0` no demuestra `O26` §5.1 y `B=0` no demuestra §5.2. Contraejemplo vivo: `V6-12` con `B=0` y la propiedad de `ADJ-B3` sin ningún sabotaje que la ponga roja | que los rótulos digan lo que miden, y que el gate no los lea como lo que no son | `PLT` | INTERNO | CORREGIR |
| **`ADJ-M5`** | `comprobar_recuentos.py:239`, `AMBITO_VIVO` | seis prefijos de INCLUSIÓN **sin motivo escrito para lo que dejan fuera**, mientras `FUERA_DEL_AMBITO` motiva sus seis y `T151` comprueba los motivos. `docs/rediseno/`, `docs/owner/`, `docs/evolucion/` y `tooling/` quedan fuera EN SILENCIO | motivar cada exclusión, y comprobarlo como se comprueba la otra mitad | `PLT` | INTERNO | CORREGIR |
| **`ADJ-M6`** | `docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md` L168 | conserva «no hay decisión del Owner que tomar», premisa que `01-MATRIZ` L113 declara medida FALSA: «hay al menos tres resultados conformes, no uno» | alinear con la medición | `SIS` | INTERNO | CORREGIR |
| **`ADJ-M7`** | `docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md` L190 y L192 | afirma EN PRESENTE «`T151` está en ROJO» y «`T152` está en ROJO», y la evidencia dice `SUPERADA` las dos | reescribir en pasado o derivar | `SIS` | INTERNO | CORREGIR |
| **`ADJ-M8`** | `06-DEUDA` §13, comando 5 (L475) | publica un comando cuya salida vacía significa, por su propia anotación, «`A14` sigue abierto», mientras §4 del mismo documento declara `A14` **CERRADA POR `F6`** | corregir el comando o su anotación | `SIS` | INTERNO | CORREGIR |
| **`ADJ-M9`** | `06-DEUDA` §2, filas `C-L.10` y `C-L.13` | declaran «cero líneas de código escritas» y «NO implementado» cuando el CHECKPOINT identifica `C-L.10` con `CONTRATO 1+2+3` y el componente vivo de `C-L.13` con `J-11 ≡ CONTRATO 3`, **los cuatro construidos y probados** | poner al día las dos celdas | `SIS` | INTERNO | CORREGIR |
| **`ADJ-M10`** | `derivar-universo-obligatorio.py` | el criterio de pertenencia no es UNO: FASE para el componente `deuda`, SECCIÓN para `C-L`. El resultado es correcto y la frontera no está trazada por la propiedad que dice trazarla | criterio homogéneo, o frontera declarada como lo que es | `PLT` | INTERNO | CORREGIR |
| **`ADJ-M11`** | `arboles/versiones.py:22-25` y `CONTRATO-ARBOLES-ADVERSARIALES.md` §2 L75 contra `admision/censo.py:378` | las dos primeras afirman que `arboles/` «no está entre» los paquetes del censo; el código dice que SÍ está | alinear las dos afirmaciones con el código | autoría `F6` | INTERNO | CORREGIR |

## 4 · Los dos DEL OWNER — resueltos por `O27`, NO reescribiendo `O23`–`O26`

| id | sede | qué es | disposición |
|---|---|---|---|
| **`ADJ-O1`** | entradas `O23`–`O26` | la sede declara obligatorios seis campos por entrada; `O17`–`O22` llevan `## Texto` y `O23`–`O26` no. `FD-2` registra el defecto sólo para `O23` y `O24` | **RESUELTO NORMATIVAMENTE por `O27` §2**: los campos son exigibles PROSPECTIVAMENTE y **no se insertan retroactivamente**, porque romperían la literalidad, el append-only y el digest del acto. **Su ausencia no invalida esas resoluciones.** Acción autorizada: **NINGUNA edición de `O23`–`O26`**; sólo poner al día el registro de `FD-2`, que hoy nombra dos de cuatro |
| **`ADJ-O2`** | entrada `O26` | la omisión de «FIN LITERAL DE `O26`.» fue un acto de interpretación del coordinador | **RESUELTO NORMATIVAMENTE por `O27` §1**: la línea era un delimitador externo del encargo, **su omisión fue CORRECTA y no debe repararse añadiéndola ahora**. Acción autorizada: **NINGUNA edición de `O26`** |

## 5 · Los cinco DEL APARATO DEL GATE — no del candidato

| id | sede | qué es | remedio | acción |
|---|---|---|---|---|
| **`ADJ-GT1`** | commit `26d6c54` · `00-INDICE.md` · el derivador | sobre la rama del gate, `comprobar_evidencia` da `T158 FALLIDA EXIT=1` y el derivador FALLA CERRADO con `EXIT=2`; sobre la candidata, los dos en 0. **El acto de convocar el gate cambió el corpus que dos instrumentos del gate miden** | separar FÍSICAMENTE checkout de la candidata y rama del gate. **`O27` §4 lo eleva a NORMA** | CORREGIR EL MÉTODO del gate siguiente |
| **`ADJ-GT2`** | `docs/evolucion/00-INDICE.md` | el manifiesto se enlaza sólo desde su fila del registro de pasadas y no desde la LISTA que la regla del propio índice exige. **Sexta recurrencia** de la misma clase | enlazarlo donde la regla lo exige | CORREGIR |
| **`ADJ-GT3`** | el reparto | `ASIGNADO − LEÍDO ≠ ∅` en el lote del revisor 2: 50 de 84 ficheros, 60,9 %. Por §4 del manifiesto, el gate es NO VÁLIDO | cobertura BLOQUEANTE y mecánica, no declarativa. **`O27` §5 lo eleva a NORMA** | CORREGIR EL MÉTODO |
| **`ADJ-GT4`** | el manifiesto §1 | la referencia de la candidata «no existe» localmente; existe como `refs/remotes/origin/…` y apunta bien | precisar la comprobación: `git ls-remote` contra el remoto | CORREGIR EL MÉTODO |
| **`ADJ-GT5`** | el manifiesto §5 y §6 | «N líneas … **más** los rangos» cuando la cifra YA los incluye. Simétrico, sin efecto | redactar la cifra sin ambigüedad | CORREGIR EL MÉTODO |

## 6 · Los dos que NO cambian de clase

| id | clase | disposición |
|---|---|---|
| **`E-17`** | **DEUDA EXTERNA** | la custodia productiva de claves permanece EXTERNA. Se registra propietario, mecanismo previsto, condición de cierre y que **una clave efímera NO la satisface**. No bloquea la certificación técnica; **bloquea toda afirmación de custodia productiva** |
| **`E-18`** | **LIMITACIÓN DE ANFITRIÓN** | `cgroup v2` presente y **no ejercitable** aquí; identidad diferenciada **ejercida** en contenedor; backend fuerte probado; el débil **no** contiene `setsid`; sin backend fuerte, fallo cerrado. **Ninguna afirmación universal** |

## 7 · Recuento

```text
BLOQUEANTES              3   ADJ-B1 · ADJ-B2 · ADJ-B3          todos INTERNOS, todos se corrigen
GRAVES                   3   ADJ-G1 · ADJ-G2 · ADJ-G3          todos INTERNOS, todos se corrigen
MEDIOS                  11   ADJ-M1 … ADJ-M11                  todos INTERNOS, todos se corrigen
DEL OWNER                2   ADJ-O1 · ADJ-O2                   resueltos por `O27`, sin editar O23-O26
DEL APARATO DEL GATE     5   ADJ-GT1 … ADJ-GT5                 se corrige el MÉTODO del gate
EXTERNO                  1   E-17                              permanece EXTERNA
LÍMITE DE ANFITRIÓN      1   E-18                              permanece limitación

TOTAL                   26
NINGUNO cambia de INTERNO a EXTERNO. Ninguno se cierra por búsqueda textual.
```
