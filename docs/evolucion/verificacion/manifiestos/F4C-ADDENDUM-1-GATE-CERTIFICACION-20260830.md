# ADDENDUM 1 AL MANIFIESTO PREVIO DE ASIGNACIÓN — GATE DE CERTIFICACIÓN DE F4c

> **EL MANIFIESTO ANTERIOR NO SE EDITA.** `C-L.5` · `1bis` lo declara inmutable una vez
> repartido: «si hace falta reasignar, se publica un manifiesto nuevo con su motivo, no se
> edita el anterior». Esto es ese manifiesto nuevo. El de `44d2e74` queda como está, con su
> error dentro, que es como debe quedar.

## 1 · El motivo, dicho sin suavizar

El manifiesto de `44d2e74` declaró **33 fuentes AGOTADAS** por lectura íntegra certificada en
un gate anterior. Su propia **regla 1** dice:

```text
un gate anterior tiene que declarar LEÍDO ÍNTEGRO DE ESA RUTA, y se cita con documento
y línea. La fila del manifiesto de ASIGNACIÓN transcrita en un dictamen NO es una
lectura: confundirlas es el defecto que P-08 describió, y el derivador las separa
```

**Veintiuna de esas treinta y tres no cumplen esa regla, y el manifiesto no lo vio.** Lo
encontró el relevo `Q3` de este mismo gate, leyendo el documento 20 íntegro, ANTES de que
hubiera ninguna adjudicación. Es su hallazgo `Q3-02`, y es correcto:

```text
QUÉ SE CITÓ        documento 20, L368 · L372 · adjudicado en L638

QUÉ DICE L368      «Leído íntegro, sin excepción: las cuatro fuentes del bloque común y las
                   diecisiete entradas de mi lote propio, incluidas las quince fichas de
                   capacidad completas» — una declaración de CONJUNTO

QUÉ NO DICE        NI UNA SOLA RUTA. Ni L368, ni L372, ni L638 nombran ninguno de los
                   veintiún ficheros. El único sitio del documento 20 donde esas rutas
                   aparecen es la tabla del COORDINADOR, §2 L74-L85 — que es un manifiesto
                   de ASIGNACIÓN, exactamente lo que la regla 1 prohíbe tomar por lectura

Y ADEMÁS           trece líneas después de L638, el adjudicador `O` escribe en L651
                   «REGLA DE CIERRE · NO CERTIFICABLE POR MÍ (`O-04`)» y en L656
                   «`C-L.5` queda ABIERTA en forma». Apoyar un agotamiento en un gate que
                   declaró NO CERTIFICABLE su propia regla de cierre no se sostiene
```

**El manifiesto anterior aplicó su regla 1 a las doce fuentes que cita del documento 21 —que
sí tienen fila propia con `LEÍDO ÍNTEGRO`, ruta y SHA-256— y NO se la aplicó a las veintiuna
que cita del documento 20.** Es el mismo defecto de `P-08` un nivel más abajo: una regla
escrita bien y aplicada sólo donde era cómoda.

## 2 · Qué se reasigna

Las **veintiuna** dejan de estar AGOTADAS y vuelven al reparto de **LECTURA ÍNTEGRA** en este
mismo gate. Son **3 575 líneas**: el coste de cerrarlo bien es pequeño, y la alternativa
—defender un agotamiento que un revisor del propio gate ya ha refutado por escrito— no es
una alternativa.

| # | ruta | líneas | SHA-256 | `1bis` | reasignada a |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` |ii+iv| **Q · relevo Q5** |
| 2 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` |ii| **Q · relevo Q5** |
| 3 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` |ii| **Q · relevo Q5** |
| 4 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` |ii| **Q · relevo Q5** |
| 5 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` |ii| **Q · relevo Q5** |
| 6 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` |ii| **Q · relevo Q5** |
| 7 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` |ii| **Q · relevo Q5** |
| 8 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` |ii| **Q · relevo Q5** |
| 9 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` |ii| **Q · relevo Q5** |
| 10 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` |ii| **Q · relevo Q5** |
| 11 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` |ii| **Q · relevo Q5** |
| 12 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` |ii| **Q · relevo Q5** |
| 13 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` |ii| **Q · relevo Q5** |
| 14 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` |ii| **Q · relevo Q5** |
| 15 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` |ii| **Q · relevo Q5** |
| 16 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` |ii| **Q · relevo Q5** |
| 17 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` |ii| **Q · relevo Q5** |
| 18 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` |ii| **Q · relevo Q5** |
| 19 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` |ii| **Q · relevo Q5** |
| 20 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` |ii| **Q · relevo Q5** |
| 21 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` |ii| **Q · relevo Q5** |

**Las DOCE restantes siguen AGOTADAS y no se tocan**: cada una tiene en el documento 21 una
fila propia de manifiesto de LECTURA con `LEÍDO ÍNTEGRO`, su ruta, sus líneas y su SHA-256, y
sus bytes son idénticos a los del árbol que la leyó. Cumplen la regla 1 y la regla 2.

## 3 · A quién se entrega, y cuándo

```text
RELEVO Q5     nuevo, contexto limpio, creado DESPUÉS de commitear este addendum y no antes.
              No ha visto ningún dictamen, ninguna nota de otro relevo y ningún hallazgo.
              Lee las veintiuna ÍNTEGRAS y publica su manifiesto de lectura con SHA-256
              recalculado, primera y última sección sustantiva y dos anclas por fuente

ORDEN         este documento se commitea SOLO y ANTES de que `Q5` exista, igual que el
              manifiesto al que enmienda. La comprobación es `git log`
```

## 4 · Las dos restas, actualizadas

```text
FUENTES OBLIGATORIAS        59     sin cambio: el universo lo deriva el mismo comando y da
                                   el mismo resultado. Este addendum NO toca el universo,
                                   toca el REPARTO

ASIGNADAS A LECTURA         47     26 del manifiesto + 21 de este addendum · 30 779 líneas
ASIGNADAS COMO AGOTADAS     12     10 395 líneas, todas con fila propia en el documento 21

OBLIGATORIO menos ASIGNADO   0     cero fuentes sin asignar, y ahora con una regla de
                                   agotamiento aplicada por igual a todas
ASIGNADO menos LEÍDO         —     la calcula el adjudicador `R`, cruzando el manifiesto,
                                   ESTE addendum y los manifiestos de lectura
```

## 5 · Lo que este addendum NO hace

```text
NO EDITA el manifiesto anterior. Sigue en `44d2e74`, con su error dentro y legible
NO CAMBIA el universo obligatorio ni el comando que lo deriva
NO CORRIGE el hallazgo `Q3-02`: lo REGISTRA. El hallazgo entra en el dictamen de `Q` y lo
   adjudica `R` como cualquier otro, incluido su juicio sobre si el coordinador de este gate
   —que es quien escribió el manifiesto defectuoso— ha reaccionado bien o ha tapado
NO EXIME de nada: si `Q5` no lee una de las veintiuna, esa fuente queda asignada y no leída,
   y la suficiencia queda excluida por la regla de cierre
```
