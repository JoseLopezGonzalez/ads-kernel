# `F6` · GATE DE CERTIFICACIÓN FINAL · 2026-09-05

```text
EL GATE ES VÁLIDO                     ← por PRIMERA VEZ en el expediente
F6 NO ESTÁ COMPLETAMENTE IMPLEMENTADA
F6 NO QUEDA CERTIFICADA
F6 SIGUE ABIERTA · PesquerApp SIGUE BLOQUEADA
```

## Qué se juzgó

| | |
|---|---|
| **candidata** | `c2437214c9353185d6b90b8fe86178302d4cf349` · tree `bb5b674` |
| **rama** | `review/f6-candidate-g01-g08-20260905` |
| **base** | `769a8b6dfd2dd71aab69f35893da46bf35356168` |
| **árbol juzgado** | checkout SEPARADO y CONGELADO en ese SHA, limpio antes y después |
| **agentes** | `REV-1`, `REV-2`, `REV-3` en paralelo y sin verse · `ADJUDICADOR` creado **sólo después** de que los tres cerraran. Nunca más de tres a la vez |

## El gate ES VÁLIDO, y esto es lo que cambia respecto de los dos anteriores

Los gates del 2026-09-03, del 2026-09-04 y del 2026-09-05 (primero) se declararon **NO
VÁLIDOS por cobertura**, y los tres por defecto **del coordinador**: un manifiesto con un
rango imposible, un tramo sin asignar, un universo declarado en vez de derivado. Éste no.

```text
COBERTURA DEL GATE · COMPLETA
  REV-1   87 fichas ·  55 204 líneas · sin abrir 0 · con huecos 0 · SIN LEER 0 · cerrado sí
  REV-2   86 fichas ·  55 203 líneas · sin abrir 0 · con huecos 0 · SIN LEER 0 · cerrado sí
  REV-3   86 fichas ·  55 208 líneas · sin abrir 0 · con huecos 0 · SIN LEER 0 · cerrado sí

  OBLIGATORIO − ASIGNADO                     ∅
  ASIGNADO − LEÍDO                           ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS           ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS      ∅

  209 fuentes · 165 615 líneas · los tres lotes difieren en el 0,01 %
```

**El universo es la UNIÓN**: las 94 fuentes obligatorias que el derivador publica **más** las
119 que `git diff -M -C -z` deriva entre la base y la candidata. El adjudicador no se quedó
en la salida del instrumento —cuya cuarta resta es amañable declarando `modificadas` de
menos— y comprobó a mano que el campo del manifiesto **es exactamente** el conjunto
derivado, sin una ruta de diferencia: *«la puerta existe y no está usada aquí»*.

**El PREFLIGHT encontró DOS defectos del manifiesto ANTES de abrir el gate**, y por eso el
gate no cayó por ellos: el primero declaraba cero fuentes modificadas mientras el árbol
derivaba 119, y el segundo partía once ficheros modificados por rangos entre revisores
distintos —un fichero que la candidata cambió y que tres personas leen a trozos no lo ha
leído nadie entero—. Los dos se corrigieron antes de confirmar nada, y la cerrabilidad se
comprobó en los dos sentidos: con lectura honesta y completa, las cuatro restas vacías; con
**una sola línea** sin leer, el instrumento lo dice y la nombra.

## La adjudicación

> **`F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — NO.** `G-04` se declara CERRADO y su invariante
> cae en **dos transiciones por el canal oficial**; `V6-12` no juzga el contenido en disco de
> la sede del Owner donde el mismo verificador sí juzga las otras 29 zonas; la comprobación 3
> de `comprobar_integridad.py` está declarada y **no existe**; y `M-04` figura **NO SUPERADA ·
> fase `F6`** en la sede canónica.
>
> **`F6 QUEDA CERTIFICADA` — NO.** De las cinco condiciones de `O26` §5, **§5.1 y §5.2 no las
> demuestra nada** —lo publica el propio instrumento pegado a sus ceros—, §5.4 no la ejerció
> nadie (`E-18`) y §5.5 falla con `M-04` y `C-L.7` vivas.

**27 hallazgos verificados · 23 defectos distintos · 0 rechazados por entero · 4
sub-afirmaciones rechazadas · 5 cifras corregidas.** El adjudicador rechazó, entre otras, la
afirmación de `REV-2` de que la matriz de cierre no tenía fila de manifiesto —está asignada a
`REV-1` y leída entera— y una atenuante de `REV-1` que **iba a favor** de la candidata: los
fallos de la batería del expediente anterior no son por falta de `.git`, son seis y son
sustantivos.

Los tres revisores llegaron a `NO` y `NO` **por caminos independientes**, y `REV-1` lo dejó
dicho de las dos proposiciones: *si el hallazgo grave 1 se cerrara, la segunda seguiría siendo
NO; si `O26` §5.1/§5.2 estuvieran acreditadas por otra vía, la primera seguiría siendo NO*.

## Lo que consta A FAVOR, porque una adjudicación no es un pliego de cargos

- **La línea base es enteramente verdadera**, sus siete líneas, reproducida por los tres
  revisores y por el adjudicador: `38/38` validadores · `170/0` infracciones · `582/0/0`
  bloques · `314·254·0·0` escenarios · 58 obligaciones `A=0·B=0·C=0` · 58 puntos ejecutables
  y 58 con guarda · huella `854dfa1b99be3824` estable e igual a la almacenada.
- La suite completa sobre copia pristina deja `git status` **vacío** y la evidencia **SIN
  DIFERENCIAS** contra el congelado: lo publicado es byte a byte lo que el código produce hoy.
- **`G-01`, `G-02` y `G-07` están cerrados de verdad**, ejercitados por el adjudicador,
  incluidas las dos puertas traseras que el auditor independiente había abierto.
- El manifiesto es **el más limpio del expediente** y el gate **no cae por cobertura**.
- La honestidad de los rótulos del derivador —decir qué **NO** demuestran sus ceros— la
  adjudicación la registra como **mérito, no como defecto**.

## Defectos del COORDINADOR, dichos y no redondeados

1. **No se emitió sobre de ancla** para este gate: nada externo ancla el congelado ni el
   manifiesto.
2. La cuarta resta de `comprobar-cobertura-de-gate.py` es **burlable por construcción**
   declarando `modificadas` de menos. Aquí no se usó —comprobado ruta a ruta— pero la puerta
   sigue abierta.

## Las piezas, íntegras y con su digest

Ningún dictamen se resume, se recorta ni se edita. Se registran enteros.

| pieza | líneas | sha256 |
|---|---|---|
| [`DICTAMEN-REV-1.md`](DICTAMEN-REV-1.md) | 667 | `ce845a8d218bc73da852c7342ac18572268b48c9f7872282b313f7278bfd10d1` |
| [`DICTAMEN-REV-2.md`](DICTAMEN-REV-2.md) | 507 | `47c57fef014e1c4087832c479f9f2846af340fe7c894e93ccfeda283c6b96399` |
| [`DICTAMEN-REV-3.md`](DICTAMEN-REV-3.md) | 551 | `d8199316635003f58d464e098d38fc52e2e7af787961af240fed945a37e0b53d` |
| [`ADJUDICACION.md`](ADJUDICACION.md) | 589 | `16e5f8fe4b3494850a629676a5e7debee6b4b436fec770ac92d71847f69513b4` |
| [`MANIFIESTO.json`](MANIFIESTO.json) | — | `bc1a4b6ff725b5e777cd65751efe51304684997fb9a85e2b95781da78201f11a` |
| [`LECTURA-REV-1.json`](LECTURA-REV-1.json) | — | `24d236d35d391f8702861b079b65002321071895573baa2a6b79835b998ca5e8` |
| [`LECTURA-REV-2.json`](LECTURA-REV-2.json) | — | `7d1886cd9d172c0d777feeadd71dda8c0457ae2775ab7f29247cbe23d1d03a37` |
| [`LECTURA-REV-3.json`](LECTURA-REV-3.json) | — | `d698658d07e6c66683f08745a9225bb743e8708d84dd8bcc8ffae9288a42623b` |
| [`INFORME-COBERTURA.json`](INFORME-COBERTURA.json) | — | lo que el instrumento midió |
| [`ENCARGO-REVISOR.md`](ENCARGO-REVISOR.md) · [`ENCARGO-ADJUDICADOR.md`](ENCARGO-ADJUDICADOR.md) | — | lo que se les pidió, para que se pueda juzgar si se les pidió bien |

## Y lo que este gate NO hace

**No se corrige ni un hallazgo.** El encargo lo prohíbe después del gate, y no se ha tocado
una línea de la candidata desde que se congeló: el árbol juzgado sigue en `c2437214…`, tree
`bb5b674`, con `git status` vacío.

`O26` §8 no se mueve: la aceptación arquitectónica permanece, **`F6` sigue ABIERTA** y
**PesquerApp sigue BLOQUEADA**. Un veredicto que no certifica no cierra nada.
