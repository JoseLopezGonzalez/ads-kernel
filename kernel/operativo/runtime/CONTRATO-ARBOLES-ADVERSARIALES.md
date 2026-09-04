# CONTRATO DERIVADO · ÁRBOLES ADVERSARIALES · `V6-15`

**Qué instancia.** La fila `V6-15` de §20.1 de
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` y, sobre todo, **§20.5**, que
fija de dónde sale el conjunto y por qué **no se enumera a mano**. Es contrato DERIVADO: no
reformula §20 ni la sección `(g)`; las instancia en forma ejecutable.

**Qué NO es.** No es una certificación. `V6-15` en verde no cierra `F6`, no cierra `M-04` y
no desbloquea PesquerApp: los tres los gobiernan sus sedes, y ninguna es ésta.

**Reparto, conservado de §20.5.** Especificar el conjunto es de **`SIS`**, fase **`F4c`**.
CONSTRUIR la suite es de **`F6`**, y eso es lo que hay aquí.

**Contratos hermanos de este corte.**
[`CONTRATO-CONTENCION.md`](CONTRATO-CONTENCION.md) ·
[`CONTRATO-RAIZ-EXTERNA.md`](CONTRATO-RAIZ-EXTERNA.md) ·
[`CONTRATO-ADMISION.md`](CONTRATO-ADMISION.md), cuya implementación mide esta suite.

---

## 1 · El conjunto se DERIVA, y su cardinal no se escribe

§20.5 designa como sede la CABECERA que cada gate publica en su documento inmutable:

```bash
grep -nE '^## [0-9]+ · EL [A-ZÁÉÍÓÚ]+ ÁRBOL' docs/evolucion/[0-9][0-9]-*.md
```

`arboles/derivador.py` implementa **esa** derivación analizando los ficheros, y no llamando a
`grep`. Cada árbol se identifica por su **cabecera** y por el **documento** que la contiene,
y trae el **identificador del hallazgo que lo cerró**, derivado del mismo documento.

```text
NO SE ESCRIBE          el conjunto, su cardinal, ni una lista de árboles. Es la regla de
                       `J-07` que §20.5 aplica a esta fila, y alcanza al código, a este
                       contrato y a la salida del instrumento. Una prueba lo comprueba
SON ÁRBOLES            y no identificadores de hallazgo. §20.5 registra por qué: el remedio
                       anterior devolvía setenta y cinco identificadores «que no tienen rojo
                       que dar», y un cierre medido sobre el objeto equivocado es
                       insatisfacible
CRECE SOLO             si un gate futuro publica otro árbol con la misma cabecera, entra en
                       el conjunto sin editar una línea, y la resta `entrada − suite` deja
                       de ser vacía hasta que se le añada su fixture
```

## 2 · Decisiones técnicas, con sus alternativas descartadas

```text
ANALIZAR EL FICHERO    frente a invocar `grep`. Un derivador que delega en una orden externa
Y NO INVOCAR `grep`    depende de la localización, del `grep` instalado y del `cwd`, y las
                       tres cosas cambian el resultado sin que cambie el corpus

EL HALLAZGO SE DERIVA  frente a (a) una tabla escrita a mano —caduca en cuanto un gate
POR REGLA MECÁNICA     publique otro árbol, que es lo que §20.5 prohíbe—, (b) recoger todos
                       los identificadores del documento —devuelve su censo entero, que es
                       el error de OBJETO que §20.5 corrige—, (c) recoger los de la sección
                       del árbol —la sección de resumen no los nombra—.
                       La regla elegida: líneas del MISMO documento que nombran ese árbol por
                       su ORDINAL y son cabecera de sección o fila de matriz cuya PRIMERA
                       CELDA es un identificador; y de ahí, sólo los que el propio documento
                       DECLARA como hallazgos suyos. Sin ese último filtro, la cabecera «MI
                       ATAQUE A `M-04` — ¿HAY UN OCTAVO ÁRBOL?» aportaba `M-04`, que es la
                       proposición ATACADA y no el hallazgo que la cerró

REPRODUCIR LA REGLA    frente a editar el script del gate. `comprobar-correccion-gate-de-
Y NO EL SCRIPT         cierre.py` es evidencia de proceso, INMUTABLE y clasificado
                       `EVIDENCIA` por el registro canónico. Lo que se compara son REGLAS,
                       no versiones de un fichero. Es el criterio que `test_admision.py` ya
                       adoptó para la regla que `S1-02` derribó

LAS VERSIONES          frente a pasar por `gobierno/git.py`. Ese canal fija
VULNERABLES NO USAN    `core.quotePath=false` y prohíbe leer listas sin `-z`: una versión
EL CANAL ÚNICO         histórica que pasara por ahí **no podría reproducir su propio
                       defecto**, y `S1-01` existe justamente porque la lectura no iba por
                       ahí. Y `arboles/` **SÍ entra en el censo** de `admision/censo.py`
                       —en los dos: el de LECTURAS, que deriva sus paquetes del disco, y
                       el de FÓRMULAS, cuyo `PAQUETES_DEL_VERIFICADOR` lo nombra—: lo que
                       queda exento es la VÍA HISTÓRICA, acotada por `(paquete, módulo)` en
                       `SEDES_DE_REPRODUCCION_HISTORICA` y publicada con su motivo.
                       Cualquier lectura insegura NUEVA en este paquete da ROJO. Dejarlo
                       fuera entero habría sido no enumerar una superficie, que es el modo
                       de fallo de `S1-01`

UN REPOSITORIO POR     frente a mutar un solo árbol tres veces. El SANO, el ATACADO y el del
PAPEL                  CONTROL POSITIVO tienen que existir A LA VEZ: el control del ataque
                       compara el sano contra el atacado byte a byte, y compararlos exige
                       que los dos estén
```

## 3 · La matriz, con sus CUATRO columnas y su quinta comprobación

```text
1 · ÁRBOL SANO             la implementación VIGENTE le da VERDE. Sin esta columna, un
                           verificador que dijera ROJO a todo pasaría la suite entera
2 · EL ATAQUE EXISTE       el árbol atacado DIFIERE del sano EN LO QUE EL ATAQUE DICE
                           cambiar. Sin ella, un fixture roto se lee como un remedio
3 · LA VULNERABLE ACEPTA   la implementación histórica le da VERDE. Sin ella, no consta que
                           el ataque fuera real contra nada
4 · LA VIGENTE RECHAZA     y la aserción NOMBRA la propiedad. Un ROJO por otra causa es un
    POR SU PROPIEDAD       aprobado por accidente

CONTROL DEL CONTROL        retirado el INGREDIENTE del ataque —el sufijo, el commit, el
                           carácter no ASCII, el cuerpo ilegible, el borrado confirmado—, la
                           MISMA versión histórica da ROJO. Sin esto, una versión vulnerable
                           que devolviera VERDE siempre pasaría por reproducción histórica
```

## 4 · Vocabulario cerrado

```text
ÁRBOL                el objeto de `V6-15`. Un árbol adversarial publicado por un gate con
                     cabecera propia en su documento inmutable
ORDINAL              el que le puso el gate que lo encontró. Es su identidad estable
FIXTURE              la materialización de un árbol en un repositorio Git real
VERSIÓN VULNERABLE   la implementación histórica con UNA propiedad debilitada, con su
                     procedencia documental y su literal
INGREDIENTE          lo único que separa el verde del rojo en la versión vulnerable
CONTROL DEL ATAQUE   la comprobación de que el atacado difiere del sano en lo que se dice
CONTROL POSITIVO     el mismo ataque SIN su ingrediente
ENTRADA − SUITE      árboles derivados que la suite no reproduce. Tiene que ser ∅
SUITE − ENTRADA      fixtures sin árbol adjudicado. Tiene que ser ∅
```

Errores tipados: `SEDE_AUSENTE` · `ARBOL_DUPLICADO` · `ARBOL_NO_CUBIERTO` ·
`FIXTURE_SIN_ARBOL` · `ATAQUE_INERTE` · `REPRODUCCION_INVALIDA`.

## 5 · Qué demuestra, y dónde

`T210`–`T213` en [`pruebas/test_arboles.py`](pruebas/test_arboles.py), sobre repositorios Git
**reales** y sobre la sede documental del propio repositorio. Punto ejecutable:
[`ads_arboles.py`](ads_arboles.py), con `conjunto`, `cruce` y `suite`, salida JSON de claves
ordenadas y **bytes idénticos desde cualquier `cwd`**.

## 6 · Lo que este contrato NO alcanza

```text
LOS ÁRBOLES ANTERIORES    §20.5, literal: «Ninguna sede los publica con cabecera propia, y
AL OCTAVO                 por eso el comando no los devuelve. No se les inventa aquí un
                          identificador ni una fase». Entrarían solos si un gate los
                          publicara con la misma cabecera

LA SUITE NO ES UNA        `V6-15` cerrado no cierra `V6-18` —que mide la suite ENTERA—, ni
CERTIFICACIÓN             `M-04`, ni `F6`. Y `V6-15` no se puede citar como «cubre los once
                          árboles»: cubre los que su ENTRADA entrega, que es otra cosa

EL VEREDICTO VIGENTE      la matriz mide que la implementación de `admision/` rechaza cada
SE MIDE, NO SE AMPLÍA     árbol por su propiedad. NO añade guardas nuevas al verificador:
                          si un árbol futuro no lo rechazara, la fila saldría en rojo y ése
                          sería el hallazgo, no un parche escrito aquí
```
