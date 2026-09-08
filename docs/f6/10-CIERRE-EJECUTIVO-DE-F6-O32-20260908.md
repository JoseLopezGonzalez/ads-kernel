# `O32` · CIERRE EJECUTIVO DE `F6` POR ACEPTACIÓN EXPRESA DEL OWNER — 2026-09-08

> **Qué es este documento.** El cierre del expediente de construcción y certificación de
> `F6`. Registra qué se cerró, con qué autoridad, sobre qué hechos, con qué riesgo aceptado
> y qué queda vivo.
>
> **Qué NO es.** **No es una certificación técnica, y no la sustituye.** La verificación por
> composición de `O31` **NO CERTIFICÓ**, y este documento no reinterpreta ese resultado ni
> lo rebaja: lo cita literal. `F6` se cierra por un acto **expreso y competente del Owner**
> que acepta el riesgo residual, no porque el aparato haya demostrado lo que no demostró.
>
> **Autoridad.** `O32`, en la [sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md).
> El estado vigente vive en su única sede,
> [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6; este documento
> **remite y no lo duplica**.

## 1 · Las dos frases, que son ciertas a la vez

```text
F6 CERRADA POR ACEPTACIÓN EXPRESA DEL OWNER
CERTIFICACIÓN TÉCNICA O31 NO OBTENIDA
```

Separarlas sería mentir en cualquiera de los dos sentidos. `F6` está cerrada y está
implementada; y el verificador independiente de `O31` no la certificó. `O32` §6 lo dice con
esa forma exacta y este expediente la conserva en todas sus sedes:

`F6 CERRADA · IMPLEMENTADA · ACEPTADA POR EL OWNER · CERTIFICACIÓN TÉCNICA O31 NO OBTENIDA · RIESGO RESIDUAL DECLARADO`

## 2 · Objeto y referencias

```text
candidata juzgada por O31   697eab9c8078b467b3741151e36fb5af792046e3
tree                        92f7e0dfb9dc36f78d2bc13665bb5419af3614c0
                            CONGELADA · publicada en
                            review/f6-o31-four-controls-candidate-20260907
                            y NO modificada por este encargo

base de este encargo        c52e5a980f8aea56f92bf3b5d82864f989dcf466
                            = review/f6-o31-final-insufficient-20260907
resultado                   review/f6-closed-by-owner-o32-20260908
```

**Registros que este documento no reemplaza y de los que depende:**

- la verificación que **no certificó**, íntegra, en
  [`09-VERIFICACION-POR-COMPOSICION-O31-20260907.md`](09-VERIFICACION-POR-COMPOSICION-O31-20260907.md);
- la verificación anterior, también no certificada, en
  [`07-VERIFICACION-FINAL-O30-20260907.md`](07-VERIFICACION-FINAL-O30-20260907.md);
- la matriz del alcance cerrado de `O31`, en
  [`08-MATRIZ-DE-LOS-CUATRO-CONTROLES-O31.md`](08-MATRIZ-DE-LOS-CUATRO-CONTROLES-O31.md).

Son **material protegido**. Ninguno se ha tocado.

## 3 · Los hechos técnicos que el Owner acepta como demostrados

`O32` §1. Todos reproducidos por el verificador independiente de `O31` sobre la candidata,
no aceptados por declaración de quien implementó:

| hecho | lo medido |
|---|---|
| `K01`–`K24` satisfechas | 24 medidos · 24 satisfechos · 0 incumplidos · 57 sabotajes ejercidos · 0 sin detectar |
| obligaciones internas completas | 58 medidas · 0 sin implementar · 0 faltantes individuales |
| la resta de obligaciones está vacía | pendientes de `O26-IMPL`: ∅ |
| las ocho condiciones de `O26` | 8 de 8 satisfechas · 0 no ejercibles · 0 no satisfechas |
| las baterías se ejecutan | funcionales, adversariales, concurrencia, recuperación, aislamiento, firma, integridad, instalación y extremo a extremo |
| cobertura integral del verificador | `MODIFICADO − LEÍDO ÍNTEGRO = ∅`, demostrada mecánicamente. **La primera del expediente** |
| ninguna regresión | ni del runtime ni de los mecanismos del producto |
| PesquerApp no iniciada | ningún fichero, ningún directorio, ningún acto de inicio |

**Estos hechos no se vuelven a someter a otro gate** —`O32` §1—.

## 4 · El resultado de `O31`, conservado sin reinterpretarlo

`O32` §2 lo reconoce **sin modificarlo**:

```text
V-G1 NO CERRADA
V-G2 NO CERRADA
M-04 NO SUPERADA
C-L.7 NO CERRADA
F6 NO CERTIFICADA
F6 ABIERTA
```

No se reconstruye ese resultado y no se declara que aquellas condiciones hayan sido
superadas. Fallaron cuatro de las nueve condiciones de `O31` §7, y el verificador lo razonó
una por una en su dictamen, que está transcrito íntegro y sin edición.

## 5 · El riesgo aceptado, y qué significa aceptarlo

`O32` §3 y §5. Los defectos afectan a la capacidad del aparato para garantizar **por sí
solo** que sus instrumentos futuros no puedan ser retirados, excluidos, transferidos o
eludidos:

- la completitud del universo de instrumentos admite una exclusión controlada por material
  **interno al propio árbol**;
- la dispensa reflexiva puede transferirse manipulando la invocación declarada;
- `M-04`: el aparato puede perder un instrumento **y su evidencia** si además se altera la
  declaración que define su pertenencia;
- `C-L.7` detecta instancias lingüísticas y no toda la clase semántica;
- quedan límites menores de vigencia, referencias, instalación y observabilidad.

**Aceptar no es cerrar.** `O32` §5 lo enumera y este documento lo repite porque es la parte
que más fácilmente se malinterpreta: la aceptación **no elimina** los hallazgos, **no** los
declara superados, **no** cambia su reproducción, **no** modifica el dictamen del
verificador, **no** convierte un rojo histórico en verde, **no** afirma que la certificación
técnica de `O31` se obtuviera, **no** autoriza a ocultar fallos futuros y **no** impide
corregir después el sistema genérico.

**Por qué se acepta en vez de seguir.** `O32` §4: ningún repositorio puede demostrar
únicamente desde su propio contenido que todas las reglas capaces de juzgarlo sean
imposibles de modificar por un commit autorizado a modificar ese mismo repositorio. Exigirlo
produce una recursión sin punto final —un control necesita otro control, que necesita un
guardián, que necesita una sede de pertenencia, que necesita otro control que garantice que
no será modificada—. La raíz final de confianza descansa **fuera del árbol**: revisión
humana, protección externa del repositorio, permisos, reglas de rama, firmas, revisión
independiente y responsabilidad explícita del Owner. No se exigirá al kernel resolver
enteramente desde dentro una propiedad que depende de autoridad externa.

Y el hecho que hace la aceptación defendible, dicho por el propio verificador: los defectos
**no falsifican la evidencia de la candidata juzgada ni demuestran un fallo del runtime
implementado**.

## 6 · Dónde va el riesgo: `ADS-HARDENING`

`O32` §9 abre **una sola** familia de deuda, no bloqueante, con ocho entradas:

| id | materia |
|---|---|
| `ADS-HARDENING-01` | universo externo o firmado de instrumentos |
| `ADS-HARDENING-02` | identidad completa y efectiva de invocaciones y dispensas |
| `ADS-HARDENING-03` | cierre futuro de `M-04` mediante raíz externa |
| `ADS-HARDENING-04` | sustituir el detector lingüístico de `C-L.7` por un modelo estructural |
| `ADS-HARDENING-05` | enlaces del producto instalado |
| `ADS-HARDENING-06` | vigencia y observabilidad de evidencias |
| `ADS-HARDENING-07` | custodia productiva de claves |
| `ADS-HARDENING-08` | capacidades de contención dependientes del anfitrión |

Cada una publica origen, hallazgos relacionados, riesgo real, alcance, propietario,
mecanismo de cierre futuro y **el criterio exacto que la haría bloqueante para una operación
concreta**. Su sede, con la trazabilidad a los identificadores anteriores:

```bash
$ sed -n '/^## 11 quinquies /,/^## 12 /p' docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md
```

**Los identificadores anteriores siguen vivos y ninguno se declara superado:** `V-G1`,
`V-G2`, `M-04`, `C-L.7`, `V-M1`, `V-M2`, `V-M3`, `V-M4`, `CD-7`, `CD-8`, `B-01`, `B-02`,
`B-03`, `G-01`, `G-02` y los menores de `O31`.

Esta deuda **no bloquea** la creación ni el uso del repositorio ADS de PesquerApp. Sólo
bloqueará una operación concreta cuando esa operación **dependa materialmente** del
mecanismo pendiente.

## 7 · Qué pasa ahora con PesquerApp

`O32` §7. Al quedar `F6` cerrada por aceptación expresa, desaparece el bloqueo previo, **y
eso es todo lo que desaparece**:

```text
PESQUERAPP AUTORIZADA PARA CREAR SU REPOSITORIO ADS DEFINITIVO
REPOSITORIO ADS DE PESQUERAPP TODAVÍA NO CREADO
PESQUERAPP TODAVÍA NO INICIADA BAJO ADS
```

**`O32` §7 no ordena crear el repositorio, y este encargo no lo ha creado.** La creación se
hará mediante una orden posterior y separada, y ése es el siguiente encargo.

**El modelo, cuando se ejecute** —`O32` §8—: repositorio global ADS **definitivo y
directo**; sin copia piloto, sin repositorio temporal y sin adopción paralela desechable;
independiente de los repositorios reales de frontend, backend, aplicación móvil e
infraestructura; exclusivamente para **gobernar y orquestar el equipo**; con el ADS genérico
como fuente y **sin convertirse en un fork divergente**.

**Si aparece un defecto estructural importante**, el orden es: corregir en el **genérico**,
publicar nueva versión del genérico, **preservar** la información propia y no regenerable de
PesquerApp, y sólo entonces eliminar y recrear la instancia desde el genérico. Los
repositorios reales del producto **no se eliminan ni pierden autoridad**, y el código o los
datos reales **no dependen** del repositorio de orquestación.

## 8 · Qué queda prohibido

`O32` §10 cierra el expediente. No se autoriza otro gate de `F6`; ni otra resolución
destinada a certificar retrospectivamente la misma candidata; ni otra clasificación de
cláusulas; ni otro universo de invariantes; ni otra tanda automática; ni otra corrección
previa a la adopción; ni iniciar PesquerApp dentro del encargo que cerró `F6`.

## 9 · Lo que este cierre no compra, dicho sin adorno

Tres verificaciones independientes juzgaron `F6` y ninguna la certificó. La última alcanzó
**cobertura integral** —la primera del expediente— y encontró tres bloqueantes y dos graves
en el aparato que se había construido precisamente para cerrar los anteriores. El cierre no
los borra: los traslada a `ADS-HARDENING` con su reproducción intacta.

Lo que se cierra es la **recursión**, no el problema. `O32` §4 explica por qué esa recursión
no tenía punto final dentro del árbol, y dónde tiene que descansar la confianza en su lugar.
Quien lea esto dentro de un año debe poder saber, sin recorrer los gates, que `F6` se usa
con un riesgo **conocido, medido, escrito y asumido por su Owner** —y no con uno ignorado.
