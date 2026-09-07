# `O31` · MATRIZ DE LOS CUATRO CONTROLES — 2026-09-07

> **Qué es.** El alcance CERRADO que `O31` autoriza. Exactamente cuatro identificadores:
> `V-G1`, `V-G2`, `M-04` y `C-L.7`. No se añade ninguno más, y `O31` §1 prohíbe
> expresamente convertir esto en otra auditoría general.
>
> **Qué NO es.** No es una certificación. `O31` §5 y §6 reservan el cierre de `M-04` y de
> `C-L.7` al verificador independiente, y `O31` §8 le reserva las seis declaraciones. Esta
> matriz declara el objetivo y el estado medido; no lo adjudica.
>
> **Los menores quedan fuera.** `V-M1`, `V-M2`, `V-M3`, `V-M4` y `CD-7` permanecen en
> [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md)
> §11 bis y §11 ter, **sin declararlos superados**, y no forman parte del delta.

## 1 · La matriz

### `V-G1` — el universo de instrumentos sale de un glob de un solo directorio

| campo | contenido |
|---|---|
| **identificador** | `V-G1` |
| **sede** | [`comprobar_evidencia.py`](../../kernel/operativo/validadores/comprobar_evidencia.py), comprobación 8 del bucle de `T158`; y el alcance de `T350` |
| **reproducción anterior** | medido el 2026-09-07 sobre `4d99a5e`: (a) retirar la fila `invariantes-criticos` —`dir: docs/evolucion/verificacion`— y su evidencia deja `comprobar_evidencia.py` en `2 superadas · 0 fallidas`, `rc=0`; (b) 13 de las 45 evidencias de validador están declaradas por CERO `ads:escenario`, incluidas las cinco que miden las condiciones de `O30`, frente a 23 escenarios de `contratos` y 17 de `admision`; (c) un `.py` nuevo en `docs/evolucion/verificacion` NO produce «el manifiesto no lo declara» —sólo se queja un censo de tamaño de corpus, con otro motivo—, mientras el mismo fichero en `validadores/` sí lo produce |
| **causa de clase** | la completitud se juzga contra un **glob de un directorio** (`kernel/operativo/validadores/*.py`) y el manifiesto reparte 56 filas en **cuatro** directorios. Lo que vive fuera del glob no existe para el control |
| **remedio de `O31`** | §3: el universo se deriva de **todas las filas vivas** que declaren instrumento ejecutable o `tipo: validador`, sea cual sea su directorio, contrastando identificador, ejecutable, directorio, argumentos, evidencia, condición de éxito, inclusión en el runner e inclusión en el guardián; y todo instrumento que sostenga una condición de certificación queda protegido por `T350` o guardián mecánicamente equivalente |
| **componentes** | `docs/evolucion/verificacion/comprobar-universo-de-instrumentos.py` (nuevo) · `comprobar_evidencia.py` (comprobación 8 y su nueva 8 bis) · `validadores.yaml` |
| **pruebas positivas** | `T601` el universo derivado no es vacío y cubre los cuatro directorios · `T602` toda fila viva tiene los ocho contrastes · `T603` todo instrumento de certificación tiene guardián |
| **ataques negativos** | `NU-01`…`NU-10` de §6 del encargo: instrumento fuera del directorio histórico · fila con `dir:` distinto · fila sin evidencia · evidencia sin fila · fila retirada con su evidencia · instrumento `K` retirado con huella y sello regenerados · instrumento movido de ruta · tipo nuevo reconocido por su declaración · manifiesto que omite una ruta · control sano |
| **evidencia** | `kernel/operativo/pruebas/evidencia/universo-instrumentos-salida.txt` |
| **propietario** | `PLT` implementa · `SIS` propietario |
| **estado inicial** | **ABIERTA · GRAVE** |
| **estado final** | *lo adjudica el verificador independiente de `O31` §7* |

### `V-G2` — la dispensa reflexiva se concede al script, no a la fila

| campo | contenido |
|---|---|
| **identificador** | `V-G2` |
| **sede** | [`comprobar_evidencia.py`](../../kernel/operativo/validadores/comprobar_evidencia.py), `_dispensa_reflexiva` y `_el_declarante_mide_de_verdad` |
| **reproducción anterior** | medido el 2026-09-07 sobre `4d99a5e`: una fila `coartada-v6` con el script legítimo y `args: ['--help']`, sustituyendo a `o26-impl`, **obtiene la dispensa** y deja `2 superadas · 0 fallidas`, `rc=0`; y una fila con el mismo script y `dir:` distinto **también la obtiene** |
| **causa de clase** | la condición empírica sondea el **SCRIPT** con argumentos FIJOS y **nunca mira los `args:` ni el `dir:` declarados de la FILA**. La dispensa se gana por parecerse al instrumento, no por ser el instrumento |
| **remedio de `O31`** | §4: la dispensa se liga a la **invocación declarada completa** —obligación, identificador de fila, ruta normalizada del script, cwd normalizado, argumentos normalizados, evidencia y condición de cierre— y pertenece a **una sola identidad exacta** |
| **componentes** | `comprobar_evidencia.py`: `identidad_de_invocacion()` y las condiciones 5, 5b, 6, 7 y 8 de la dispensa |
| **pruebas positivas** | `T604` la fila legítima conserva su dispensa y la identidad se publica · `T605` la dispensa es única |
| **ataques negativos** | `ND-11`…`ND-18` de §6: mismo script con `--help` · argumentos distintos · cwd distinto · obligación distinta · fila duplicada · ruta equivalente no idéntica · evidencia distinta · fila legítima exacta |
| **evidencia** | `kernel/operativo/pruebas/evidencia/evidencia-salida.txt` |
| **propietario** | `PLT` implementa · `SIS` propietario |
| **estado inicial** | **ABIERTA · GRAVE** |
| **estado final** | *lo adjudica el verificador independiente de `O31` §7* |

### `M-04` — el universo esperado depende del manifiesto cuya completitud se juzga

| campo | contenido |
|---|---|
| **identificador** | `M-04` |
| **sede** | [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) §3 · el aparato de validadores completo |
| **reproducción anterior** | el **duodécimo árbol**, reproducido entero el 2026-09-07 sobre `4d99a5e`: retirar del manifiesto la fila del instrumento de `K01`–`K24`, borrar su evidencia, regenerar huella y sello, y correr la batería → `comprobar_integridad rc=0` · `comprobar_evidencia rc=0` · `comprobar_contratos rc=0` · `comprobar_referencias rc=0` · `comprobar_recuentos rc=0` · `comprobar_fuentes rc=0` · `comprobar_arranque rc=0` · `ads_lint rc=0`. **Falso verde completo** |
| **causa de clase** | es la misma que `V-G1` vista desde la proposición de `M-04`: un árbol defectuoso pasa en verde porque **el universo esperado se lee del manifiesto que se está juzgando**. Quien edita el manifiesto edita a la vez el hecho y su medida |
| **remedio de `O31`** | §5: una **derivación independiente desde las sedes vivas del árbol**. El manifiesto CONTRASTA, no DEFINE. La ausencia del instrumento de `K01`–`K24` la detecta el universo independiente, no el manifiesto |
| **componentes** | los mismos que `V-G1`: comparten fuente mecánica por mandato de §5 del encargo |
| **pruebas positivas** | `T601`–`T603`, más la reejecución del duodécimo árbol como control |
| **ataques negativos** | `NU-06` es el duodécimo árbol literal, y su rojo tiene que venir **del universo independiente y por el motivo correcto** |
| **evidencia** | `kernel/operativo/pruebas/evidencia/universo-instrumentos-salida.txt` |
| **propietario** | `SIS` |
| **estado inicial** | **NO SUPERADA** |
| **estado final** | *`O31` §5 lo reserva expresamente al verificador independiente: no se cierra con una etiqueta* |

### `C-L.7` — el barrido comprueba por instancia y no por clase

| campo | contenido |
|---|---|
| **identificador** | `C-L.7` |
| **sede** | la regla 7 de `regla_de_reanclaje`, dentro de [`CHECKPOINT-ADS-NEXT.md`](../evolucion/CHECKPOINT-ADS-NEXT.md) |
| **reproducción anterior** | medido el 2026-09-07 sobre `4d99a5e`, con el barrido publicado y sobre un campo VIGENTE: minúsculas **CAZADO** · VERSALES **CAZADO** · cardinal separado de su sustantivo por un salto de línea **ESCAPA** · «los 24 invariantes críticos» **ESCAPA** · «las 58 obligaciones internas» **ESCAPA** · «los 57 sabotajes declarados» **ESCAPA**. Dos de seis. El árbol sano sale vacío y el barrido mira 55 campos reales, de modo que el verde no es tautológico |
| **causa de clase** | el barrido reconoce **una lista cerrada de sustantivos escrita a mano** y su alcance es **por línea**. Reconoce instancias del vocabulario que conoce, no la clase; y tres de los cuatro escapes son cardinales que este mismo expediente deriva |
| **remedio de `O31`** | §6: un control **estructural** que juzgue la clase —copia manual de estado, cardinal o conjunto variable dentro de una sede viva que debería derivarlo o remitir—, con excepciones **tipadas y justificadas** para fechas, versiones, identificadores normativos, SHA y digests, citas históricas rotuladas, límites contractuales realmente constantes, salidas generadas y comandos de derivación. Y, preferentemente, que las sedes vivas **retiren** el cardinal y remitan |
| **componentes** | `docs/evolucion/verificacion/comprobar-cardinales-manuales.py` (nuevo) · la regla 7 del `CHECKPOINT`, que pasa a remitir al instrumento |
| **pruebas positivas** | `T606` el control ve campos reales y el árbol sano sale limpio · `T607` cada excepción está tipada y justificada |
| **ataques negativos** | `NC-19`…`NC-30` de §6: dígitos · letras · mayúsculas · singular · sustantivo desconocido · puntuación alterada · cardinal posterior al detector · y los negativos fecha, versión, SHA, cita histórica y comando de derivación. Más las variantes que entrega el agente de crítica, **desconocidas para el implementador al diseñar** |
| **evidencia** | `kernel/operativo/pruebas/evidencia/cardinales-manuales-salida.txt` |
| **propietario** | `SIS` la especificación · `PLT` el instrumento |
| **estado inicial** | **NO CERRADA** |
| **estado final** | *`O31` §6 lo reserva al verificador independiente, y exige que lo demuestre con variantes que el implementador no usó* |

## 2 · Lo que esta matriz NO abarca

`O31` §1 cierra el alcance. Fuera quedan, y siguen registrados sin declararse superados:

| id | dónde vive | por qué queda fuera |
|---|---|---|
| `V-M1` | §11 ter de la sede de deuda | menor: suelo en la firma de cobertura adversarial |
| `V-M2` | ídem | menor: el emisor del sobre cita secciones inexistentes |
| `V-M3` | ídem | menor: confirma `CD-7` |
| `V-M4` | ídem | menor de observabilidad, estructuralmente irresoluble dentro de un ciclo |
| `CD-7` | §11 bis | menor: enlaces del índice a packs no embarcados, viene de la base |

No se corrigen cifras, enlaces ni redacciones menores salvo que sean materialmente
imprescindibles para cerrar uno de los cuatro. Si alguno lo fuera, se dirá aquí y se dirá
por qué.
