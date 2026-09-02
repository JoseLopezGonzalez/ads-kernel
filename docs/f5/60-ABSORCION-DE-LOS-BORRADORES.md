# 60 · QUÉ ARTEFACTO DEFINITIVO ABSORBIÓ CADA BORRADOR

**Los diez borradores se conservan.** No se borran, no se editan y **NO se marcan como
aprobados**. Este documento dice qué artefacto definitivo absorbió cada uno, y **qué parte
de cada uno NO fue absorbida y por qué**.

> **POR QUÉ LOS BORRADORES SIGUEN DICIENDO `NO_APROBADO`, y no es un descuido.**
> Un borrador **nunca** se convierte en material aprobado: lo aprobado es la **enmienda**, la
> **sección** o la **resolución** que recogió su contenido. La marca `NO_APROBADO` de la zona
> de borradores es lo que impide que un texto preparatorio se cite como norma, y el control
> `F11` de [`validar-f5.py`](validar-f5.py) **pone rojo cualquier fichero de esta zona que se
> declare aprobado**. La aprobación se registra **aquí y en la matriz**, nunca dentro del
> borrador.

---

## 1 · La correspondencia

| borrador | absorbido por | ¿íntegro? |
|---|---|---|
| [`B-01`](borradores/B-01-SECCION-G.md) | la sección [`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) entera | **NO — parcial.** Ver §2 |
| [`B-02`](borradores/B-02-RAIZ-EXTERNA.md) | `(g)` `g.15` + `O23` §3 | **NO — parcial.** Ver §2 |
| [`B-03`](borradores/B-03-REGLAS-CONSTITUCIONALES.md) | [`E3`](../rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md) `E3.1` | **NO — parcial.** Ver §2 |
| [`B-04`](borradores/B-04-VIA-DEL-TRABAJO-RECURRENTE.md) | `E3` `E3.2` y `E3.3` | **NO — con una sede corregida.** Ver §2 |
| [`B-05`](borradores/B-05-RATIFICACIONES-DE-LECTURA.md) | `O23` §10 lo aprueba **por su nombre** · su texto de reanudación, en [`E6`](../rediseno/a-ENMIENDA-E6-REANUDACION.md) | **SÍ, íntegro** |
| [`B-06`](borradores/B-06-RUTAS-DE-b16.md) | [`E4`](../rediseno/a-ENMIENDA-E4-COMPOSICION-DE-RUTAS.md) | **SÍ**, con las condiciones de activación que el borrador dejaba abiertas |
| [`B-07`](borradores/B-07-RECONCILIACION-PENDIENTE.md) | `O23` §4 + `(g)` `g.9` | **NO — parcial.** Ver §2 |
| [`B-08`](borradores/B-08-GRAFIA-CANONICA.md) | `O23` §8 | **SÍ, íntegro** |
| [`B-09`](borradores/B-09-CHECKLIST-EDITORIAL.md) | `O23` §10 lo aprueba **por su nombre** · su texto, en [`E5`](../rediseno/a-ENMIENDA-E5-CORRECCIONES-EDITORIALES.md) | **SÍ**, con dos sedes corregidas |
| [`B-10`](borradores/B-10-NOTA-DE-VIGENCIA.md) | `O23` §10 lo aprueba **por su nombre** · su texto, en las cuatro sedes del documento del Owner | **SÍ, íntegro** |

## 2 · Lo que NO se absorbió, y por qué — dicho contra el propio interés

**Un borrador puede contener arquitectura que la resolución del Owner no cubre. Esa parte NO
se aplica**, y decir cuál es más honesto que dejarla pasar en el mismo movimiento.

```text
B-01 · LA REGLA DE FRONTERA que el borrador proponía
       NO se aplicó. El Owner NO la confirmó: dio LA SUYA, que es una enumeración cerrada
       de materias más cinco condiciones de evolución. Manda la del Owner, y es la que (g)
       g.0 recoge

B-01 · LA ELECCIÓN DE FORMA del estado durable, y el descarte de las otras tres
       NO se aplicó. O23 fija COMPONENTES e INVARIANTES; NO elige forma. Elegirla aquí
       habría sido norma sin acto

B-01 · LA PROHIBICIÓN DE UN TERCER ARTEFACTO durable
       NO se aplicó, Y HABRÍA SIDO UN ERROR APLICARLA: O23 §4 crea precisamente un tercer
       artefacto durable —el registro auxiliar—. El borrador se escribió antes de la
       decisión y la contradice

B-01 · «LO QUE (g) DEJA EXPRESAMENTE ABIERTO»
       NO se aplicó. O23 §2 dice que el perímetro se incluye ÍNTEGRAMENTE. Dejar materia
       abierta habría necesitado un acto propio

B-02 · EL TITULAR de la identidad, la RUTA de la evidencia y el CUSTODIO de las claves
       NO se aplicaron como norma. O23 §3 los manda EXPRESAMENTE al contrato de F6. La
       norma fija que existan y qué propiedades tienen; el detalle es de F6

B-02 · LA CLAVE DE FIRMA del Owner
       SIGUE SIN CONSTAR en ninguna resolución. NO se inventa: se registra como deuda FD-1

B-03 · «LA CORRESPONDENCIA ENTREGABLE A ENTREGABLE es parte de la enmienda»
       se aplicó COMO TRABAJO DE F6 y no como parte de la enmienda. Salía de una columna
       de inconvenientes del paquete, no de una sede normativa

B-04 · «AMPLÍA LA TAXONOMÍA DE ENTRADA»
       SEDE CORREGIDA. La taxonomía de entrada es DERIVADA y su alineación es de F6. La
       sede de F5 es b.15.1, y es la que E3 enmienda

B-07 · «NO EXIGE ABRIR TRANSACCIÓN»
       NO se aplicó como norma: O23 §4 no lo dice. Lo que (g) g.9 sí fija es que el
       registro NO modifica el estado canónico, que es la garantía que O23 SÍ da

B-07 · «NO DEPENDE DE LA SECCIÓN (g) NI LA BLOQUEA»
       SUPERADO por O23: la reconciliación es hoy materia de (g), y vive en g.9

B-08 · «con las citas históricas marcadas como tales»
       es diseño del barrido, y por tanto de F6
```

## 3 · Cómo se comprueba que esto es cierto

```bash
# los diez borradores siguen marcados NO_APROBADO
grep -lr 'ESTADO-DEL-BORRADOR: NO_APROBADO' docs/f5/borradores/ | wc -l
# y NINGUNO se declara aprobado
python3 docs/f5/validar-f5.py        # control F11
```
