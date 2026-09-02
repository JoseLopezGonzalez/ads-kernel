# `F5` · ÍNDICE DEL ÁREA DE TRABAJO

**Esto es el área de trabajo de `F5`, la fase de ENMIENDA NORMATIVA.** Aquí viven la matriz
de obligaciones, el paquete de decisiones del Owner y los borradores. **Nada de aquí es
norma.**

> **QUÉ ES ESTA ZONA, y su clasificación es comprobable.** El registro de sedes canónicas la
> clasifica en dos: [`docs/f5/`](.) es **DERIVADA** —la matriz y el paquete salen de sus
> sedes superiores y no crean autoridad— y [`docs/f5/borradores/`](borradores/) es
> **NO APLICABLE A IMPLEMENTACIÓN** —son borradores NO APROBADOS que no autorizan a
> implementar nada—. La clasificación la ejecuta
> [`validar-fuentes-canonicas.py`](../canonico/validar-fuentes-canonicas.py), y un fichero
> plantado aquí sin zona que lo clasifique es ROJO.
>
> **QUÉ NO ES.** No es corpus canónico, no es un gate, no es una certificación y **no
> contiene ni una sola decisión del Owner**. El estado de las fases **no se copia aquí**:
> su única sede es
> [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6.

**La entrada del sistema sigue siendo**
[`docs/canonico/00-EMPEZAR-AQUI.md`](../canonico/00-EMPEZAR-AQUI.md). Este índice es el
área de trabajo, no la puerta.

---

## 1 · Los documentos, en orden de lectura

| # | documento | qué contiene |
|---|---|---|
| — | [`01-ACTO-DE-INICIO-DE-F5.md`](01-ACTO-DE-INICIO-DE-F5.md) | el registro literal del acto del Owner que inició `F5`, y qué autoriza y qué no |
| 1 | [`10-MATRIZ-CANONICA-DE-F5.md`](10-MATRIZ-CANONICA-DE-F5.md) | la matriz completa, legible: una fila por obligación, con su estado |
| 2 | [`20-PAQUETE-DE-DECISIONES-DEL-OWNER.md`](20-PAQUETE-DE-DECISIONES-DEL-OWNER.md) | **el único paquete de decisiones.** Diez elecciones y cuatro actos de aprobación |
| 3 | [`30-TRAZABILIDAD-Y-ORDEN-DE-APLICACION.md`](30-TRAZABILIDAD-Y-ORDEN-DE-APLICACION.md) | de la presión a la prueba, y el orden exacto de aplicación posterior |
| — | [`MATRIZ-F5.yml`](MATRIZ-F5.yml) | la matriz en forma de datos, que es lo que el control lee |
| — | [`validar-f5.py`](validar-f5.py) | los controles pequeños sobre la matriz y los borradores |

## 2 · Los borradores · TODOS NO APROBADOS

**Cada uno lleva la marca `ESTADO-DEL-BORRADOR: NO_APROBADO` en su cabecera, y el control
`F10` de [`validar-f5.py`](validar-f5.py) exige que la lleve.** El control `F11` exige
además que **ningún** fichero de esta zona lleve la marca contraria: este árbol no contiene
ninguna aprobación del Owner, y eso es comprobable en vez de prometido.

| borrador | entregable | decisión de la que depende |
|---|---|---|
| [`B-01-SECCION-G.md`](borradores/B-01-SECCION-G.md) | `F5-B` · `F5-C` | `D-01` |
| [`B-02-RAIZ-EXTERNA.md`](borradores/B-02-RAIZ-EXTERNA.md) | `F5-D` | `D-02` |
| [`B-03-REGLAS-CONSTITUCIONALES.md`](borradores/B-03-REGLAS-CONSTITUCIONALES.md) | `F5-G` | `D-04` |
| [`B-04-VIA-DEL-TRABAJO-RECURRENTE.md`](borradores/B-04-VIA-DEL-TRABAJO-RECURRENTE.md) | `F5-A` | `D-05` |
| [`B-05-RATIFICACIONES-DE-LECTURA.md`](borradores/B-05-RATIFICACIONES-DE-LECTURA.md) | `F5-A` | `R-01` · `D-10` |
| [`B-06-RUTAS-DE-b16.md`](borradores/B-06-RUTAS-DE-b16.md) | `F5-A` | `D-06` · `D-07` · `D-09` |
| [`B-07-RECONCILIACION-PENDIENTE.md`](borradores/B-07-RECONCILIACION-PENDIENTE.md) | `F5-A` | `D-03` |
| [`B-08-GRAFIA-CANONICA.md`](borradores/B-08-GRAFIA-CANONICA.md) | `F5-E` · `F5-A` | `D-08` |
| [`B-09-CHECKLIST-EDITORIAL.md`](borradores/B-09-CHECKLIST-EDITORIAL.md) | `F5-E` | `R-02` |
| [`B-10-NOTA-DE-VIGENCIA.md`](borradores/B-10-NOTA-DE-VIGENCIA.md) | `F5-F` | `R-03` |

## 3 · Cómo se comprueba que esto es cierto

```bash
# los controles de la matriz y de los borradores
python3 docs/f5/validar-f5.py

# el censo VIGENTE de presiones, derivado de su sede única — la matriz tiene que cubrirlo
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'

# que ningún borrador se presente como aprobado
grep -rn 'ESTADO-DEL-BORRADOR' docs/f5/ | grep -c 'NO_APROBADO'

# la clasificación de zona de este directorio
python3 docs/canonico/validar-fuentes-canonicas.py
```

## 4 · Qué NO hay aquí

```text
NO HAY   ninguna respuesta del Owner. Ni una
NO HAY   ninguna enmienda aplicada sobre material aprobado
NO HAY   ninguna resolución escrita en voz del Owner
NO HAY   nada de F6: ni runtime, ni verificador, ni raíz externa, ni contrato construido
NO HAY   ningún hallazgo declarado superado, ni ninguna deuda cerrada
NO HAY   ningún gate nuevo, ni ninguna certificación
```
