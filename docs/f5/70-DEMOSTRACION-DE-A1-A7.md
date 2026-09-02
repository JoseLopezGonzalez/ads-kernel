# 70 · DEMOSTRACIÓN DE `A1`…`A7`, UNO POR UNO

**Los siete criterios de aceptación de `F5`, con la evidencia que los demuestra y el comando
que la reproduce.** Ninguno se declara satisfecho por argumento.

> **QUÉ NO DEMUESTRA ESTE DOCUMENTO.** No demuestra que `F5` esté cerrada — **no lo está**, y
> su cierre exige un acto posterior y expreso del Owner. Demuestra que las **cuatro
> condiciones** que `O23` §11 pone antes de ese acto están cumplidas.

---

## `A1` · cada presión vigente tiene enmienda aprobada o retirada motivada

**SATISFECHO.** Las diecisiete presiones vigentes tienen **acto** y **artefacto**, y ninguna
queda «pendiente».

```bash
# el censo VIGENTE, de su sede única
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'
# las filas del acta de disposición, que debe cubrirlo entero
grep -cE '^\| `PN-[0-9]+` \|' docs/f5/40-DISPOSICION-DE-LAS-PRESIONES.md
# y el control que lo exige, derivando el censo del árbol
python3 docs/f5/validar-f5.py          # control F16
```

**Acta completa:** [`40-DISPOSICION-DE-LAS-PRESIONES.md`](40-DISPOSICION-DE-LAS-PRESIONES.md),
una fila por presión con su disposición, su acto y su prueba. **Ninguna queda RETIRADA: las
diecisiete quedan RESUELTAS.** Y la presión retirada en su día **no se reinstaura**, que es
un acto y no un silencio.

## `A2` · ninguna enmienda sin aprobación expresa, ninguna silenciosa

**SATISFECHO.**

```text
EL ACTO       `O23`, inscrita LITERALMENTE en la sede canónica del Owner por él mismo
              —opción `B` de `R-04`—, con sus doce apartados
APPEND-ONLY   comprobado contra el COMMIT DE NACIMIENTO, no contra el estado actual:
              el fichero de hoy EMPIEZA por el contenido de la versión que lo creó
INTEGRIDAD    `O17`–`O22` conservan su texto BYTE A BYTE. Lo único añadido tras `O22` es
              el separador estructural que la sede ya usa entre resoluciones
NADA SILENCIOSO  las cinco enmiendas citan `O23` en su campo `origen`, y ninguna reescribe
              su fuente: la fuente conserva su texto y recibe MARCAS DE REMISIÓN
```

```bash
grep -c 'O23' docs/rediseno/a-ENMIENDA-E[3-6]-*.md docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
python3 docs/f5/validar-f5.py          # controles F14 y F15
```

## `A3` · `(g)` existe, está aprobada y cubre las materias que su fuente le reservó

**SATISFECHO, y es comprobable por barrido y no por lectura.**

```text
EXISTE        docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
APROBADA      por `O23` §2, §3 y §4
PERÍMETRO     `O23` §2 lo CIERRA por remisión: «incluye íntegramente las materias que las
              fuentes vigentes reservaron a (g) y que F5 ha reconstruido en B-01»
COBERTURA     el Anexo de `(g)` publica la correspondencia materia → apartado, fila a fila
```

```bash
# los apartados g.0 … g.18 existen todos
for n in $(seq 0 18); do grep -q "^## \`g\.$n\`" docs/rediseno/g-ESTADO-DURABLE-APROBADA.md \
  || echo "falta g.$n"; done
# y el Anexo cubre las materias reservadas
awk '/^## Anexo/,0' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md | grep -cE '^\| [0-9]+ \|'
```

**Y la materia que su fuente declaraba PENDIENTE queda resuelta:** la regla de diario que
`a.11` dejaba «hasta diseñar memoria, eventos y recuperación en la sección `(g)`» pasa a
estar **RESUELTA POR `(g)` `g.7`**, por `E3` `E3.3 bis`.

## `A4` · la norma existe y el contrato deja de estar bloqueado por dependencia

**SATISFECHO.**

```bash
grep -oE '^\| `V6-[0-9]+`.*\| (`CONTRATO_[A-Z_]+`)' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE 'CONTRATO_[A-Z_]+' | sort | uniq -c
```

**Reparto: los diecinueve CONSTRUIBLES, cero bloqueados.** La condición exacta de desbloqueo
exigía que `F5` aprobara una sede; la sede es `(g)` `g.15`, y la sección que declaraba la
dependencia **la declara SATISFECHA sin borrar su historia**.

> **Y lo que esto NO significa, dicho porque confundirlo es la deuda mayor del expediente:**
> **CONSTRUIBLE NO ES CONSTRUIDO.** Ninguno de los diecinueve está implementado, ejecutado ni
> certificado. `F6` no ha empezado.

## `A5` · la checklist editorial aplicada entera, con su prueba posterior

**SATISFECHO.**

| fila | aplicada en | prueba posterior | resultado |
|---|---|---|---|
| cita a un predicado | `E5` `E5.1` | que toda cita case con el predicado que ese número define | **verde** |
| lista mal numerada | `E5` `E5.2` | que la secuencia sea estrictamente creciente | **verde: 1 2 3 4 5** |
| recuento de marcas | `E5` `E5.3` | que el número **se derive** y no se escriba | **verde** |
| inventario de enmiendas | `E5` `E5.4` | que las sedes coincidan y que se derive | **verde** |

**La cuarta fila de la checklist de origen —la grafía— NO está aquí, y es correcto:** era una
elección real del Owner, la resolvió `O23` §8 a favor de la fuente aprobada, y por esa vía
**no se enmienda `(b)`**: se alinea el derivado, y eso es `F6`.

```bash
grep -c 'deja al item en `en espera` (P9)' docs/rediseno/b-RECORRIDO-APROBADA.md
grep -c '\[E1[ :→]' docs/rediseno/a-CAPACIDADES-APROBADA.md
ls -1 docs/rediseno/a-ENMIENDA-E*.md | wc -l
```

## `A6` · NINGÚN hallazgo vivo se declara SUPERADO

**SATISFECHO, y es el criterio que más se ha cuidado.**

```bash
awk '/^## 1 · LOS/,/^## 2 /' docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md \
  | grep -oE '^\| \*\*`[A-Z]{2}-[0-9]+`\*\*' | grep -oE '[A-Z]{2}-[0-9]+' | sort -u | wc -l
```

**El censo NO encoge: los diez siguen publicados como vivos, y su sede no se ha tocado.**

> **Y la razón por la que no encoge, dicha sin adornarla.** `F5` CUMPLIÓ la condición de
> cierre de tres de ellos, y **no los cerró**: cumplir una condición no es cerrarla, y el
> cierre lo adjudica su sede. Los otros cuatro ni siquiera cumplen la condición entera —su
> instrumento es de `F6`, o su cierre es de un gate independiente—. Detalle fila a fila en
> [`10-MATRIZ`](10-MATRIZ-CANONICA-DE-F5.md) §3.3.

```text
SIGUEN VIVOS        los diez hallazgos · la clase de recuentos copiados, NO CERRADA ·
                    la deuda que bloquea la adopción, NO SUPERADA · la guarda de entorno ·
                    las seis entradas de deuda del corpus · las cuatro observaciones
Y SE AÑADEN DOS     `FD-1` la clave de firma que ninguna resolución cubre · `FD-2` los dos
                    campos que `O23` no lleva. **Registrar deuda nueva es lo contrario de
                    declarar superada la vieja**
```

## `A7` · la batería en verde y la huella del kernel sin cambio

**SATISFECHO.**

```text
BATERÍA         13/13 validadores en verde por el runner canónico
NEGATIVOS       67 infracciones detectadas · 0 NO detectadas
HUELLA          3e90ac3726a3ce94 · LIMPIO, coincide con el release
INTÉRPRETE      Python 3.12.14 con PyYAML — se registra, porque con un intérprete antiguo
                varias comprobaciones fallan POR EL ENTORNO y no por el producto, y la
                guarda que lo impediría es contrato de `F6` y no código
```

**Y la huella NO cambia**, sin excepción que declarar: ninguna enmienda de `F5` ordena tocar
`kernel/`, `packs/` ni `tooling/`. Toda alineación de derivado es trabajo de `F6`.

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
./tooling/kernel-status.sh
git status --porcelain kernel/ packs/ tooling/ | grep -v 'pruebas/evidencia/'
# debe salir vacío: la evidencia DERIVADA sí cambia, y el runner la republica
```

---

## Las cuatro condiciones que `O23` §11 pone antes del acto de cierre

| condición | estado |
|---|---|
| `F5-A`–`F5-G` completos | **SÍ** — ver [`10-MATRIZ`](10-MATRIZ-CANONICA-DE-F5.md) §3.2 |
| `A1`–`A7` satisfechos | **SÍ** — este documento, uno por uno |
| ningún borrador presentado como aprobado sin estarlo | **SÍ** — los diez siguen `NO_APROBADO`, y el control `F11` lo exige |
| validación final satisfactoria | **SÍ** — batería, negativos, huella y los 21 controles de `F5` |

**Con las cuatro cumplidas, lo único que falta es el acto del Owner.** El ESTADO de la fase
**no se declara aquí**: su única sede es
[`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6, y este documento
lo enlaza en vez de copiarlo.
